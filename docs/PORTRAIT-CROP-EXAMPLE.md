# How to compare a landscape video with its vertical crop

[Play the wide shot and portrait render](https://valmera.io/tools/auto-reframe?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=portrait_crop#portrait-example). The wide player outlines two possible 9:16 frames over the same lecture footage. The solid lines mark the crop measured in the Valmera render. The dashed lines mark the same shape centered on the source. Both previews are public and silent. You can compare them before uploading footage or connecting an assistant.

## What happened in the render?

The speaker stands to the left of the screen. Watch the side of his face nearest the edge and the laptop in front of him. Moving the frame right leaves less room on the speaker’s left and shows more of the laptop. The two framing choices deliver the same aspect ratio while telling the viewer where to look.

The [selected landscape excerpt](https://valmera.io/showcase/raw-thiel-hook-list.mp4) measures 640 × 360. The [portrait render](https://valmera.io/showcase/demo-thiel-stage-reframed.mp4) measures 540 × 960. Both have 276 frames and run about 9.21 seconds. The source cuts were already selected before the portrait pass. The later caption, graphics and color passes appear in the [complete editing walkthrough](https://valmera.io/blog/ai-video-editing-complete-guide#real-edit).

A full-height 9:16 window in the wide preview is 202.5 pixels across. Centering it places its left edge at 218.75 pixels. Across all 276 decoded frame pairs, the best image match placed the left edge at **153 pixels**, about 66 pixels farther left. The published excerpt shows a steady off-center composition. For evidence of moving-subject tracking, test another passage where the subject actually crosses the shot.

## Reproduce the frame comparison

Download the two MP4s above and [the comparison script](evaluation/measure_portrait_crop.py). With Python and OpenCV installed, run the command from the folder containing your downloads.

```sh
python3 measure_portrait_crop.py raw-thiel-hook-list.mp4 demo-thiel-stage-reframed.mp4
```

The script decodes both clips in order, scales each portrait frame to a 202 × 360 grayscale template, and slides it horizontally across the corresponding wide frame. The best normalized correlation ranged from 0.9893 to 0.9976 in this run. The left edge is an estimate in preview pixels. Different scale, letterboxing, overlays, repeated textures or unmatched source cuts can make the same procedure unreliable on other files.

## Try it on your own recording

> Make a 9:16 preview of the passage where the speaker demonstrates the product. Keep the face and the gesture visible together. Preserve the original timing and sound. If a slide or second subject would be lost, show me a full-width fit for that passage.

Review the beginning of the gesture, its widest point and the first frame after the next cut. If the face fits but the product leaves the frame, ask for the correction using the preview timestamp and the object you need to see. The [crop and fit planner](https://valmera.io/tools/auto-reframe#planner) lets you compare geometries and prepare your own brief. Creating a new AI edit in Studio requires an editing subscription.

Footage from [The End of the Future with Peter Thiel](https://www.youtube.com/watch?v=ibR_ULHYirs), Stanford Classical Liberalism Initiative. The [published operation record](https://valmera.io/showcase/demo-replay-thiel.json) identifies the two preview stages.
