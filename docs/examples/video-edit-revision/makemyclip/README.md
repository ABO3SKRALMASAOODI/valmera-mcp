# Reproduce the local and hosted MP4 revision check

[Download the public dataset](https://www.kaggle.com/datasets/valmera/ai-video-editing-revision-test) and put its seven files in one directory. Download the [local first cut](first-cut.mp4), [local revision](shorter-cut.mp4), [measurement script](score.py) and [run record](comparison.json) to that directory. With Python 3 and FFmpeg on your path, run `python3 score.py` there. The script decodes the source and four exports and calculates the reported counts.

To re-render the local example, put `original-source.mp4` in an empty media folder, set `MAKEMYCLIP_WORKSPACE` to its absolute path and connect an MCP client using command `npx` and arguments `-y @makemyclip/editor@0.4.2 mcp`. Use the [publisher’s installation instructions](https://github.com/MakeMyClip/editor/blob/7b12e942d171d9e8a7a7101eba3ead4d3378e9d8/README.md) to configure FFmpeg. Send the tool names and arguments in the recorded order. MakeMyClip exported both versions from one composition. The second edit explicitly moves the closing clip after trimming the middle one. The [hosted edit record](../../../MCP-RECORDED-EDIT.md) links to Valmera’s original workflow and renders.

## What the counts measure

The first cut keeps source seconds 3–7, 12–16 and 19–23. The revision keeps 3–7, 12–14 and 19–23. During output seconds 6–10, the two schedules predict different source frames. At 30 fps this gives 120 comparisons. The script crops each picture to its central square and downsamples to 96 × 96 gray pixels, so a landscape and a square render can be checked against the same source area. For each output frame, the lower mean absolute pixel difference wins. Equal differences count as ties.

The clips are silent. This check measures shot timing. It does not assess sound, framing preference, storytelling, model choice or the branded ending after program time. Valmera published the test on November 16, 2026 using its own synthetic footage.
