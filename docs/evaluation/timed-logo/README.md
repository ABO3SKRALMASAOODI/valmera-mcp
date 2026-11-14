# Check a timed PNG overlay in the exported video

Show a transparent logo over the top-right corner of a 25-second recording from 3 seconds until 22 seconds. At 30 frames per second the logo should first appear on frame 90, remain visible on frame 659, and disappear on frame 660. Count from frame zero.

[Play the two exports and inspect the boundary frames](https://valmera.io/open-source-agentic-video-editors#hyperframes). For a local run, [download the project ZIP](https://valmera.io/examples/hyperframes-logo-test/project.zip) and open the extracted `timed-logo` directory. It contains the HTML and verifier published here, the original frame-counter MP4 and the transparent PNG.

## Render and measure

With Node.js 22+, FFmpeg and ffprobe on your path, run the pinned CLI. The frame check also needs Python 3 and NumPy.

```sh
npx --yes hyperframes@0.9.48 lint
npx --yes hyperframes@0.9.48 render --workers 1 --fps 30 --no-best-effort --output hyperframes-logo.mp4
python3 verify-overlay.py original-source.mp4 hyperframes-logo.mp4
```

The [HTML composition](index.html) places the logo at 20% of frame width. The center of the image is 86% across the frame and 10% down. In the original test, HyperFrames exported 750 frames. The archived Valmera renderer exported 749. Both showed the logo on exactly frames 90–659 under the published pixel-difference threshold. [Inspect the reference measurements](measurement.json).

To test a revision, change the logo’s duration from 19 seconds to 17. At 30 fps the revised last active frame should be 599. The verifier reports the detected range. Its `onlyExpectedFramesActive` field refers to the original brief, so it should now be false.

## Export a revision in your browser

Open the [free timed watermark editor](https://valmera.io/tools/add-logo-to-video) to try this fixture without installing the renderer. The sample starts with the logo visible from 3 to 22 seconds. Change **Hide at** to **20**, export the MP4 and run the verifier on your download. Expect the first logo frame at 90 and the last at 599. You can also choose your own clip and transparent logo, change the corner, width or opacity, and carry those instructions into Studio.

For a reference run using the original 3–22 second interval, download the [browser export](https://valmera.io/examples/timed-watermark/browser-export.mp4) and [frame measurements](https://valmera.io/examples/timed-watermark/frame-check.json). This browser export retains all 750 source frames. The logo detector found the mark on exactly the 570 requested frames.

## Try the same brief through an assistant

Upload the clip and logo to a Valmera project with AI editing access. Give your connected assistant the timing and size above. Review the preview, request the two-second revision and export the revised video. Check the downloaded file against the source. [Valmera overlay instructions](https://valmera.io/docs/text-and-overlays).

The original two renderer files came from authored renderer instructions, an HTML composition in HyperFrames and a supplied edit decision list in Valmera. An assistant run on your project exercises a separate part of the workflow. [Original Valmera render record](https://valmera.io/examples/logo-overlay/evidence.json).
