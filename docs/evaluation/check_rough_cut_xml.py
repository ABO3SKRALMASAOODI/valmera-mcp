"""Check the picture edit in a Final Cut Pro 7 XML export of Valmera's 30 fps trial."""
import argparse
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

CUTS = {
    "first": ((90, 210), (360, 480), (570, 690)),
    "revised": ((90, 210), (360, 420), (570, 690)),
}


def check_rate(rate):
    if rate is None or rate.findtext("timebase") != "30" or rate.findtext("ntsc", "FALSE").upper() == "TRUE":
        raise ValueError("The fixture requires a 30 fps non-drop sequence and source.")


def inspect(path, version):
    root = ET.parse(path).getroot()
    sequences = root.findall(".//sequence")
    if root.tag != "xmeml" or len(sequences) != 1:
        raise ValueError("Export one sequence in Final Cut Pro 7 XML format.")
    sequence = sequences[0]
    check_rate(sequence.find("rate"))
    tracks = sequence.findall("media/video/track")
    if len(tracks) != 1:
        raise ValueError("Supply one picture track for this cuts-only exercise.")
    track = tracks[0]
    if track.findtext("enabled", "TRUE").upper() == "FALSE" or track.find("transitionitem") is not None:
        raise ValueError("A disabled track or transition cannot be checked as a straight cut.")

    if track.find("generatoritem") is not None:
        raise ValueError("Generated track items require review in the destination editor.")

    files = {f.get("id"): f for f in root.iter("file") if f.get("id") and f.findtext("pathurl")}
    expected = [i for start, end in CUTS[version] for i in range(start, end)]
    position = 0
    for clip in track.findall("clipitem"):
        if clip.find("filter") is not None or clip.find("sequence") is not None or clip.findtext("enabled", "TRUE").upper() == "FALSE":
            raise ValueError("Use enabled source clips without filters, retiming or nested sequences.")
        media = clip.find("file")
        if media is None:
            raise ValueError("A clip is missing its source file.")
        if not media.findtext("pathurl"):
            media = files.get(media.get("id"))
        if media is None or not media.findtext("pathurl"):
            raise ValueError("A source reference could not be resolved inside the XML.")
        name = Path(unquote(urlsplit(media.findtext("pathurl")).path).replace("\\", "/")).name
        if name != "original-source.mp4":
            raise ValueError("The trial uses original-source.mp4. Keep the supplied source filename.")
        for rate in (clip.find("rate"), media.find("rate")):
            if rate is not None:
                check_rate(rate)
        start, end, source_in, source_out = (int(clip.findtext(tag, "")) for tag in ("start", "end", "in", "out"))
        if start != position or end <= start or end - start != source_out - source_in:
            return f"First unsupported gap, overlap or duration change at output frame {position}."
        for out in range(start, end):
            if out >= len(expected):
                return f"Extra footage begins at output frame {out}. Expected {len(expected)} frames."
            actual = source_in + out - start
            if actual != expected[out]:
                return f"Output frame {out} uses source frame {actual}. Expected {expected[out]}."
        position = end
    if position != len(expected) or int(sequence.findtext("duration", "")) != position:
        return f"Picture track has {position} frames. Expected {len(expected)} and a matching sequence duration."
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("xml", type=Path)
    parser.add_argument("--cut", choices=CUTS, default="revised")
    args = parser.parse_args()
    try:
        mismatch = inspect(args.xml, args.cut)
    except (OSError, ValueError, ET.ParseError) as error:
        print(f"Could not verify this file: {error}", file=sys.stderr)
        return 2
    if mismatch:
        print(mismatch)
        return 1
    frames = sum(end - start for start, end in CUTS[args.cut])
    print(f"Matched all {frames} picture frame references for the {args.cut} cut at 30 fps.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
