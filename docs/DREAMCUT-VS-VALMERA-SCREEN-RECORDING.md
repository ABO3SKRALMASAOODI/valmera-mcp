# DreamCut vs Valmera for editing a recorded product walkthrough

DreamCut documents a Mac application with a local MCP connection to the open project. Valmera lets you work on an uploaded recording in browser Studio or connect a supported assistant to its hosted MCP server. Try the same revision in both if your decision depends on whether the editor can restore one missed action in a demo you already recorded.

| Decision | DreamCut | Valmera |
| --- | --- | --- |
| Where you edit | Mac application with a timeline and in-app Sakura chat. The local MCP helper gives tools such as Codex, Claude Code and Cursor access to the open project. [DreamCut MCP and CLI](https://dreamcut.ai/docs/mcp-and-cli) | Browser Studio or the hosted OAuth connector from a supported assistant. The hosted agent works with video in a Valmera project. [Valmera Studio setup](https://valmera.io/docs/getting-started) · [MCP setup](https://valmera.io/mcp) |
| Where the capture comes from | The Mac recorder can capture a local app or screen. DreamCut documents macOS 15 or later for its CLI and MCP recording. [DreamCut quickstart](https://dreamcut.ai/docs/quickstart) · [Agent requirements](https://dreamcut.ai/docs/mcp-and-cli#before-you-start) | Upload a screen recording you already have. For a public site you can also evaluate Valmera's separate website recorder. [Website recorder and sample](https://valmera.io/tools/record-website-demo) |
| What to inspect after a revision | DreamCut documents the edits appearing in its timeline and undoing an edit in the app. Choose a separate filename on export so you can compare both versions. [DreamCut editing and export](https://dreamcut.ai/docs/mcp-and-cli#ask-for-your-first-edit) · [Export settings](https://dreamcut.ai/docs/export-settings) | Check the preview and downloaded MP4 after the requested revision. A public three-shot example includes both versions, the edit request and export receipt. [Recorded revision](https://valmera.io/examples/rough-cut-revision) |
| What access to confirm | DreamCut's guide calls for its Pro trial or plan when setting up local MCP. [DreamCut requirements](https://dreamcut.ai/docs/mcp-and-cli#before-you-start) | Valmera's AI editing requires eligible paid access. The sample files below are public. [Valmera access](https://valmera.io/subscribe) |

Valmera publishes this comparison. The DreamCut column describes its documentation. The files below are a Valmera walkthrough and reference edits. A completed side-by-side product run would require using both editors and recording both results.

## Download one clip and ask for one revision

Use the 10.83-second [source recording](https://valmera.io/examples/website-capture/public-docs-walkthrough.mp4) of Valmera's public documentation. At about 3.57 seconds, the pointer clicks **Captions** in the sidebar. The heading of the new page appears next. The file is silent, which makes the sequence easy to evaluate from just the picture.

> Make a six-second landscape walkthrough of how to reach the Captions guide. Show the starting page, the pointer reaching Captions, the click and the new Captions heading. Shorten the waits and scrolling. Keep the text and controls readable. Export the previewed cut as a separate MP4.

Now request a revision in the same project. If the first pass already kept the click, use a copy where the beginning of that action has been trimmed away.

> Restore the pointer reaching Captions and the click. Keep the opening and result as they were. To hold the same length, take time out of the wait after the heading is readable. Show the revised preview and export it under a new filename.

Pause the original and revised files around the click and compare three things. The pointer should be visible before it reaches the link. The click should explain how the new page opened. The heading should remain readable long enough to confirm the result. Record where each happens in both exported files, along with any edits to the opening and ending.

## Check the landscape master and the portrait version

The [six-second landscape reference](https://valmera.io/examples/tutorial-click/restored-click.mp4) keeps the action and the resulting heading in the full interface. At 1.30 seconds in the [portrait reference](https://valmera.io/examples/weekly-demo-pilot/portrait.mp4), the sidebar and page are stacked, so a phone viewer can see the click and the result together. Both reference files are six seconds and 180 frames. The [crop and measurement record](https://valmera.io/examples/weekly-demo-pilot/measurements.json) describes how the portrait reference was made from the landscape file.

| Check on the file you download | What to record |
| --- | --- |
| Click is present and understandable | Timestamp, visible control name and the first frame of the result |
| Approved opening and ending are preserved | What you compared and any changed text, picture or timing |
| Export is readable in the intended player | Landscape on desktop. Portrait full-screen on a phone if a vertical cut is part of the job. |
| Revision is practical at your volume | Review time, the number of correction passes and which steps a person had to do |

Buyers testing their own recordings can [start in the Valmera AI video editor](https://valmera.io/ai-video-editor?utm_source=github.com&utm_medium=repository&utm_campaign=dreamcut_demo_revision). For a recurring batch, [see the Valmera Enterprise walkthrough pilot](https://valmera.io/product-demo-video-editing-service?utm_source=github.com&utm_medium=repository&utm_campaign=dreamcut_demo_revision#weekly-demo-pilot) or [email Enterprise from the pilot inquiry page](https://valmera.io/subscribe?inquiry=product-demo-video-editing-service&utm_source=github.com&utm_medium=repository&utm_campaign=dreamcut_demo_revision#enterprise). Include expected weekly volume, landscape and portrait delivery counts, and a review deadline.
