# Add B-roll to a narrated product demo and verify the MP4

Upload the screen recording and the supporting shot as separate files. Place the supporting picture over the selected range, mute its sound and keep the original narration running. Review the preview at the entry and return before exporting.

[Watch Valmera's narrated product demo](https://valmera.io/tools/record-website-demo?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=narrated_demo_b_roll#narrated-demo-b-roll). The example includes the source, separate supporting clip, complete approval preview and exported MP4. It uses synthetic narration and Valmera's public Captions documentation.

## Use the same brief in each editor

1. Download the [narrated screen recording](https://valmera.io/examples/narrated-tutorial/source.mp4) and [supporting close-up](https://valmera.io/examples/narrated-demo-b-roll/captions-guide-close-up.mp4). The close-up contains an audible 697 Hz test tone. A silent input would hide a failure to mute it.
2. Keep the original playback speed and use program time starting at zero. Place the close-up over the picture from 4.50 to 6.30 seconds. Keep the click at about 3.57 seconds, and preserve the original voice and its level. Leave the supporting audio out.
3. Check that the close-up shows the Captions heading while the voice says “The Captions guide opens on the right.” At 6.55 seconds, the wide view should be back. Export the approved version and replay the MP4 across both joins.

In the recorded Valmera run, the connected assistant placed a full-frame cover through MCP, rendered a complete preview and exported the approved version. A gentle push-in ends the otherwise static screen, and this export has a branded ending. [Read the first-party edit record and file hashes](https://valmera.io/examples/narrated-demo-b-roll/evidence.json).

## Verify the reference files or your own candidate

With Python 3 and FFmpeg on your path, run from the root of this repository.

```sh
python3 docs/evaluation/replay_narrated_demo_b_roll.py
```

This downloads four public files, verifies their SHA-256 hashes and prints a JSON report for both the preview and final MP4. The command cleans up its temporary downloads. Valmera editing requires an eligible subscription. Replaying the existing evidence uses only the public files and your local decoder.

To check an export from any editor using the same two inputs and brief, pass the path to its downloaded MP4.

```sh
python3 docs/evaluation/replay_narrated_demo_b_roll.py --candidate /path/to/your-export.mp4
```

Your candidate file stays on your device. The command exits with status 1 if an expected picture is missing, the voice changes materially, or the test tone carries into the export. It checks the known fixture at the specified timestamps. Use the JSON and a playback review when evaluating a different project.

| Check | What the command measures |
| --- | --- |
| The original picture and the cutaway both appear | It compares the decoded picture with the two input clips at 3.57, 4.25, 5.10 and 6.55 s. The expected picture must be the closer match, with a mean luminance error of at most 9 on a 0–255 scale. |
| The original voice keeps playing | From 4.65 to 6.15 s, each decoded stereo channel must correlate at 0.98 or higher with the source narration, with a fitted gain within 6 dB of the source. |
| The close-up's sound stays out | After subtracting the matched narration, the 697 Hz component must be at least 25 dB below the tone measured in the supplied close-up. The published source, preview and final files were also checked with their hashes. |

The public footage turned up in the expected frames before, during and after the cutaway. In the original measurement the supplied tone was −21.1 dBFS, and the estimated residual in the final export was −102 dBFS. Decoders can vary slightly. Use `--candidate` with an unshifted export of the same brief, check the pictures, and listen through each join before delivery.
