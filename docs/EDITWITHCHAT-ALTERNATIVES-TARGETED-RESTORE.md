# EditWithChat alternatives for precise revisions to footage you already recorded

Give every editor a second instruction before deciding which one to pay for. Ask it to restore one removed sentence while keeping a separate filler-word cut. Undoing the whole edit can bring both back. A targeted revision keeps the other decision.

## Choose a desktop, browser or transcript workflow

| Option | What the public workflow offers | What to check on your project |
| --- | --- | --- |
| [EditWithChat](https://editwithchat.com/) | A desktop editor for supported Mac and Windows computers. It edits footage with written requests and uses your own Claude access. | Confirm the current OS and license requirements, how Claude access is billed, and what data each tool sends to the model provider. Preserve a review version before the follow-up. |
| [ChatCut](https://chatcut.io/features/ai-video-editor) | Edits supplied footage by chat and offers desktop downloads and connections for several assistants. | Request one restored sentence and inspect the MP4 for the revision. Try the connection you actually intend to use. |
| [Descript](https://www.descript.com/video-editing) | A transcript-first editor for reviewing and cutting recorded speech. | Try restoring just the relevant spoken passage, then check the cut and captions in the export. |
| [Valmera](https://valmera.io/ai-video-editor?utm_source=github.com&utm_medium=referral&utm_campaign=editwithchat_targeted_restore) | Edit uploaded footage from a written brief in Studio or with a supported connected assistant. AI editing requires an eligible subscription. | Give the assistant both instructions, review the source range that changed, and check the approved MP4. [See a real recorded revision](MCP-RECORDED-EDIT.md). |

Valmera publishes this guide. The comparison describes each provider's published workflow. The two short downloads below are reference edits made locally from the same synthetic voice source. Use them to hear what a narrow restoration should do.

## Listen to the first cut and the targeted restoration

The [original four-second recording](https://valmera.io/examples/filler-word-cut/original.mp4) says “I like the blue label. Um, use the green one for print.” Suppose the first edit removes the opening sentence and the hesitation. After reviewing it, you decide the opening explains the contrast between the two labels. Keep the filler removed.

| Version | What to listen for | Measured video duration |
| --- | --- | --- |
| [Original](https://valmera.io/examples/filler-word-cut/original.mp4) | Both sentences and the hesitation | 4.00 s |
| [Over-cut reference](examples/targeted-sentence-restore/over-cut.mp4) | The final sentence alone, without the filler | 2.40 s, 60 frames at 25 fps |
| [Targeted-restore reference](examples/targeted-sentence-restore/targeted-restore.mp4) | The opening sentence followed by the instruction to use green, with the filler still removed | 3.68 s, 92 frames at 25 fps |

The restoration adds 32 frames and retains source intervals **0.00–1.56** and **1.88–4.00 seconds**. The two reference files both contain the same measured portion of the final sentence. The restored opening and retained tail each correlated above 0.999 with the corresponding source audio over the sampled window. Correlation checks alignment in this sample. Listen around the join to judge how it sounds. [Source ranges, measurements and hashes](examples/targeted-sentence-restore/measurements.json)

## Give each editor the same two-pass request

**First pass**

> From the supplied original recording, remove “I like the blue label” and the hesitation immediately before “use the green one for print.” Keep the remaining sentence intact. Show the preview and record which source intervals remain.

**Revision**

> Restore “I like the blue label.” Keep the earlier cut of the “um” before “use the green one for print,” and preserve the last sentence and the rest of the approved edit. Show the revised preview and export that version as an MP4.

With your own footage, choose one spoken qualification and an unrelated cut that must stay. If the editor removed visual or caption material during the first pass, check whether those layers also need restoration. Compare the two MP4s at the join. Confirm the intended words, the sound and the total duration. For a separate subtitle file, play it beside the final cut and check that the restored words have the new times.

[Try a written revision in Valmera](https://valmera.io/ai-video-editor?utm_source=github.com&utm_medium=referral&utm_campaign=editwithchat_targeted_restore) or [request a recurring interview editing pilot](https://valmera.io/subscribe?inquiry=testimonial-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=editwithchat_targeted_restore#enterprise). Include the number of recordings, target formats and who signs off on changes to quoted speech.
