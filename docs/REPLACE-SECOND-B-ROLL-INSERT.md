# Replace one B-roll insert and keep the other in place

When you give an AI video editor two clips from your own footage, try a revision that touches only one of them. Keep both exported versions. Compare the approved insert at the same program time in each and listen through the full revised video. This is a useful test before committing to weekly tutorial editing.

## Try the same brief in each editor

| Route | How to start the test |
| --- | --- |
| [Kapwing Kai](https://www.kapwing.com/resources/ai-video-editing-tutorial-9-workflows-tested/) | Its tutorial shows prompting with uploaded screen recordings, muted cutaways and an instruction to preserve the talking-head audio. Verify the exact frame boundaries and check the revised MP4 in Studio. |
| [AgentReel](https://agentreel.ai/docs/ai-broll-editor) | Its B-roll editor can place supplied clips over the sound from a main talking clip. Try a per-shot replacement and confirm the other approved shot still starts on the same words. |
| [FluidCut](https://fluidcut.app/features/ai-video-editor) | Its documentation describes changes by chat, separate layers and replacing B-roll with your own media. Check which of your two inserts it changes and whether you need to fix the layer by hand. |
| [Valmera](https://valmera.io/tools/add-b-roll?utm_source=github.com&utm_medium=referral&utm_campaign=two_b_roll_inserts) | Supply the main recording and both named clip files. Ask for a timed edit, check the preview, then name the second insert and what must stay fixed. Hosted AI editing requires an eligible subscription. |

The descriptions come from each provider’s public documentation. Valmera publishes this guide and made the small practice files below locally.

## Play two exports of the same edit

In both four-second MP4s the swatch clip plays from **0.64 to 1.44 seconds**. At **2.56 seconds**, the first cut shows a slideshow screen capture and the revised cut shows a synthetic **Export ready** screen. Playback returns to the main picture at **3.56 seconds**.

| First cut | Second insert revised |
| --- | --- |
| [Play or download the first MP4](examples/two-b-roll-inserts/first-cut.mp4) | [Play or download the revised MP4](examples/two-b-roll-inserts/second-insert-revised.mp4) |
| The second shot shows the slideshow. | The second shot shows the export result. |

We decoded both files at 25 frames per second. Only frames **64–88** changed, counting from zero. The other 75 decoded frames matched, including every frame of the first insert. Both decoded audio tracks matched each other and the original narration byte for byte. Our fixture kept the original audio track when rendering and checked the downloaded files. [Hashes and measurements](examples/two-b-roll-inserts/measurements.json) · [Original narrated recording](https://valmera.io/examples/filler-word-cut/original.mp4) · [First supplied cutaway](https://valmera.io/examples/b-roll-cutaway/print-swatches.mp4)

## Give the editor an approved time range

> Add `feature-overview.mp4` over 00:18.00–00:24.00 and `report-demo.mp4` over 00:42.00–00:48.00. Keep the original voice at its current level and mute both inserts. Use the supplied shots. Return a preview and one MP4.

After approving the first cut, send a second request:

> Replace only the picture over 00:42.00–00:48.00 with `export-confirmation.mp4`. Keep the first insert, main narration, captions and total duration. Send the revised MP4.

Check the revised file at both edges of each insert. Start with the first insert, which you already approved. Then check the changed picture, the voice across both joins, any captions that overlap the cuts and the total runtime. A fresh encode can change pixel values without moving a cut. When hashes differ, use the actual frames and sound to determine what changed.

[Open the B-roll workflow](https://valmera.io/tools/add-b-roll?utm_source=github.com&utm_medium=referral&utm_campaign=two_b_roll_inserts). For recurring tutorials, [scope a done-for-you pilot with Valmera Enterprise](https://valmera.io/subscribe?inquiry=product-demo-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=two_b_roll_inserts#enterprise). Include one tutorial, the number of weekly edits and what must stay fixed when an insert changes.
