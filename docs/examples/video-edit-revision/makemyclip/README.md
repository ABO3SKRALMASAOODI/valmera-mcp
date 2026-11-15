# Reproduce the local and hosted MP4 revision check

[Download the complete revision test (ZIP)](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/examples/video-edit-revision/revision-test.zip) and extract it into one folder. The archive includes the source footage, all four MP4 exports, frame labels, the MCP call record, a scoring script and an executed Jupyter notebook.

From that folder, run `python3 score.py` with FFmpeg on your path to score all four exports. To inspect the exact frames before and after the join, open `check-revision.ipynb` in Jupyter with Pillow, FFmpeg and ffprobe installed. The bundled notebook reads the files offline. You can also [run the visual check in Colab](https://colab.research.google.com/github/ABO3SKRALMASAOODI/valmera-mcp/blob/main/docs/examples/video-edit-revision/check-revision.ipynb) or [get the original Valmera fixtures on Kaggle](https://www.kaggle.com/datasets/valmera/ai-video-editing-revision-test).

To re-render the local example, put `original-source.mp4` in an empty media folder, set `MAKEMYCLIP_WORKSPACE` to its absolute path and connect an MCP client using command `npx` and arguments `-y @makemyclip/editor@0.4.2 mcp`. Use the [publisher’s installation instructions](https://github.com/MakeMyClip/editor/blob/7b12e942d171d9e8a7a7101eba3ead4d3378e9d8/README.md) to configure FFmpeg. Send the tool names and arguments in the recorded order. MakeMyClip exported both versions from one composition. The second edit explicitly moves the closing clip after trimming the middle one. The [hosted edit record](../../../MCP-RECORDED-EDIT.md) links to Valmera’s original workflow and renders.

## What the counts measure

The first cut keeps source seconds 3–7, 12–16 and 19–23. The revision keeps 3–7, 12–14 and 19–23. During output seconds 6–10, the two schedules predict different source frames. At 30 fps this gives 120 comparisons. The script crops each picture to its central square and downsamples to 96 × 96 gray pixels, so a landscape and a square render can be checked against the same source area. For each output frame, the lower mean absolute pixel difference wins. Equal differences count as ties.

The clips are silent. This check measures shot timing. It does not assess sound, framing preference, storytelling, model choice or the branded ending after program time. Valmera published the test on November 16, 2026 using its own synthetic footage.
