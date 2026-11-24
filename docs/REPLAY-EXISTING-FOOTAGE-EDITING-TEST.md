# Replay two AI editing tests on the same uploaded recording

One editing request removes a sentence from picture and audio. The other places an uploaded B-roll shot at an exact time and keeps the complete original narration. Give an editor both requests on separate projects to see whether it understands which part of the recording can change.

[Download the original recording, silent B-roll, both requests and a blank scorecard](https://valmera.io/downloads/edit-by-chat-buyer-test.zip). The four-second narration is synthetic and the original picture is a waveform.

## Verify the supplied reference files

Clone the public repository or download its ZIP. From the repository root, with Python 3 and FFmpeg on your path, run:

```sh
python3 docs/evaluation/replay_existing_footage_evidence.py
```

The command downloads four fixed reference files from valmera.io, verifies their SHA-256 digests and decodes them locally. It prints the evidence as JSON and cleans up its temporary downloads. Reviewers can play the [original recording](https://valmera.io/examples/filler-word-cut/original.mp4), [sentence removal](https://valmera.io/examples/filler-word-cut/first-sentence-removed.mp4) and [finished cutaway](https://valmera.io/examples/b-roll-cutaway/final.mp4) in a browser.

| Request | What the replay measures |
| --- | --- |
| Remove source 0.20–1.45 s from picture and audio | The output has 69 video frames at 25 fps and 2.75 s of decoded mono audio. The audio correlates at 0.999949 with the same two retained source spans joined together. |
| Add the swatch shot over 2.56–3.68 s, keeping narration | Frames 63 and 93 show the dark waveform. Frames 64 and 92 show the lighter swatches. The final’s first four seconds of decoded narration correlate at 0.999987 with the original. The final has an end card outside the measured region. |

Values shown came from FFmpeg 7.1.1. Luminance distinguishes the known swatch and waveform shots in this example. The waveform comparison checks continuity in the exported audio and allows small codec differences. For your own project, listen across the join, check that the intended words remain, and inspect the actual picture at each boundary.

## Use it to compare potential purchases

Ask each editor for both changes and keep the same source and target ranges. Record whether each request produced an export, which manual steps it took, and whether a follow-up correction affected anything outside the requested range. [Read and try the exact briefs](https://valmera.io/edit-video-by-chatting-with-ai?utm_source=github&utm_medium=referral&utm_campaign=existing_footage_evidence). Valmera editing requires an eligible subscription.

If your team needs the same checks for recurring interview or tutorial edits, [contact Valmera Enterprise](https://valmera.io/subscribe?inquiry=video-editing-service&utm_source=github&utm_medium=referral&utm_campaign=existing_footage_evidence#enterprise). Include one representative source, your monthly volume, and a correction you want to see in the first paid pilot.
