# Add your own B-roll over an exact phrase and keep the original audio

Use a picture-only overlay when the audience needs to see the product while hearing the speaker finish the sentence. Put the supporting shot on top, mute its audio, and review the exported frames at both ends of the cutaway. For a buyer comparing editors, test one move to a later phrase too. The picture should move with the brief while the narration and program length stay in place.

## Choose how to place your own clip

| Workflow | Where you control the cutaway |
| --- | --- |
| Valmera | Name the approved file and spoken cue in the edit request, ask for a silent overlay, and review the resulting MP4. Hosted AI editing requires a subscription. [Valmera B-roll guide](https://valmera.io/tools/add-b-roll) |
| Descript | Place a visual layer in the composition and inspect its range. Its help guide documents replacing B-roll in an existing layer while retaining adjustments. [Descript media replacement](https://help.descript.com/visuals/replace-media) |
| Adobe Premiere | Use the transcript to locate the phrase and the timeline to set the picture boundaries precisely. Adobe documents switching to the editing tools after the text-based rough cut. [Premiere editing guide](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/edit-sequences-using-text-based-editing.html) |
| CapCut | Import your clip, trim it and place it above the main footage on the timeline. [CapCut B-roll guide](https://www.capcut.com/resource/what-is-a-b-roll) |

Valmera publishes this guide. The third-party workflow descriptions come from the vendors' public documentation. The measurements below apply to the linked Valmera sample.

## Check the preview and export frame by frame

In this sample, the source is four seconds of narration with a waveform as the main picture. The supplied print-swatch overlay was requested from **2.56 to 3.68 seconds**. Decoding the preview and export at 25 fps showed the swatches from **frame 64 through frame 92**, counting from zero. The waveform returned on **frame 93 at 3.72 seconds**. Use the frame you can see when evaluating the timing in the final file.

| Frame | Program timestamp | Visible picture in the preview and export |
| --- | --- | --- |
| 63 | 2.52 s | Source waveform |
| 64 | 2.56 s | First swatch frame |
| 92 | 3.68 s | Last swatch frame |
| 93 | 3.72 s | Source waveform |

The preview still runs four seconds. The nine-second archival final includes a five-second end card. Decoded mono audio from 2.625 to 3.55 seconds correlated above 0.999 with the original in both outputs. This measurement checks the narration during the cutaway.

[Original recording](https://valmera.io/examples/filler-word-cut/original.mp4) · [Approved swatch shot](https://valmera.io/examples/b-roll-cutaway/print-swatches.mp4) · [Preview](https://valmera.io/examples/b-roll-cutaway/preview.mp4) · [Export](https://valmera.io/examples/b-roll-cutaway/final.mp4) · [Original measurement record](https://valmera.io/examples/b-roll-cutaway/measurements.json)

## Run the same revision using your own footage

1. Pick a short passage containing two distinct spoken phrases and an approved clip. Write down the filename, first and last words, and whether text or captions must remain visible.
2. Request the cutaway over phrase one. Specify that only your named clip may be used. Keep source narration at its existing level and keep the original program duration.
3. Move the cutaway to phrase two. Export. Compare the first and last visible frames with the approved cue, listen for both complete phrases, and check that surrounding footage stays in place. Record the manual steps and minutes needed to get the MP4 you would publish.

[Brief your own B-roll edit in Valmera](https://valmera.io/tools/add-b-roll?utm_source=github.com&utm_medium=referral&utm_campaign=exact_b_roll_cutaway). For recurring product or talking-head edits, [contact Valmera Enterprise through the subscription page](https://valmera.io/subscribe?utm_source=github.com&utm_medium=referral&utm_campaign=exact_b_roll_cutaway#enterprise) with your footage mix, weekly volume and approval deadline.
