# How to replace one spoken instruction in a training video

Record the corrected sentence as a pickup, meaning a short replacement take of the affected line. Use the same speaker, mic and room when possible. Match the sentence to the approved control on screen, then update its caption and every published version that uses it. If the screen changed, capture the affected step again and join it to the existing cut.

[Scope a training video revision with Valmera Enterprise](https://valmera.io/subscribe?inquiry=training-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=training_line_pickup#enterprise)

## See how an audio-only correction can leave the wrong instruction visible

In this synthetic ten-second lesson, the export format changes from CSV to MP4. Play the clip with sound, then open the accompanying SRT and check cue 2. The next instruction begins at 00:07.250 in each version.

| File pair | What you hear from 00:02.750 | What the viewer sees at the same step |
| --- | --- | --- |
| [Original MP4](examples/training-line-pickup/original.mp4) and [original SRT](examples/training-line-pickup/original.srt) | Choose Export CSV. | The control and caption both say Export CSV. |
| [Audio-only revision MP4](examples/training-line-pickup/audio-only.mp4) and [its SRT](examples/training-line-pickup/audio-only.srt) | Choose Export MP4. | The control and caption still say Export CSV. A learner gets different directions depending on how they watch. |
| [Complete revision MP4](examples/training-line-pickup/approved.mp4) and [its SRT](examples/training-line-pickup/approved.srt) | Choose Export MP4. | The control and caption both say Export MP4. |

The sample uses a mock interface and synthetic narration. The audio-only and complete revisions share identical decoded audio. The original and audio-only revisions share identical decoded picture. The fixture shows what a reviewer should check on their own exports. [See the measurements](examples/training-line-pickup/measurements.json).

## Send a brief that an editor can quote

Give the editor the approved script, the original edit or best available export, and the exact lesson version that the audience sees. Mark the words before and after the changed line. Record those surrounding words along with the pickup so the editor has room to match cadence and make clean joins. If a presenter’s mouth appears through the edited line, offer a new on-camera take or a relevant clean cutaway where the picture can follow the corrected instruction. [Avid’s ADR overview](https://www.avid.com/resource-center/adr-in-film) explains using the original dialogue as a guide.

| Send with the brief | Example |
| --- | --- |
| Current lesson, version and changed line | Review lesson v3, 00:02.750. Change “Choose Export CSV from the Download menu” to “Choose Export MP4 from the Download menu.” |
| Pickup WAV and updated capture | Record the revised sentence with the words on either side. Capture the menu opening, the correct control and the result. |
| Where the old line appears | Full lesson, 30-second onboarding excerpt, its captions and transcript. List each destination. |
| Files to return and date | Revised MP4 for each affected version, matching captions, and a changelog that identifies the new time of the corrected line. Name the reviewer and first delivery date. |

Ask the editor whether they can reopen the original project. When all you have is the final file, request a short pilot first to check whether they can cover the obsolete control, remove burned-in text where needed and match the surrounding voice. Define who owns the caption and transcript updates. [W3C explains what synchronized captions need to convey](https://www.w3.org/WAI/media/av/captions/).

## Approve one corrected lesson before committing the batch

1. **Play the exported MP4 with sound.** Check the exact instruction and listen to both joins. Have the reviewer follow the task once.
2. **Play it muted with the delivered captions.** Check that the updated label is visible and the revised cue appears with the right line. Repeat in the intended learning platform, where captions can cover controls.
3. **Open a second affected version.** Check the excerpt or localized cut independently. If its timeline differs, use its own cue times.
4. **Update the delivery log.** Record each replaced file, its reviewer, the approval date and the production destination. Keep an archive of the superseded cut and captions.

For a single lesson, try the [recorded course editing workflow](https://valmera.io/use-cases/course-creators?utm_source=github.com&utm_medium=referral&utm_campaign=training_line_pickup). For a recurring queue, send Valmera the number of lessons and additional versions you update each month, a representative revision and your first deadline. [Open the Enterprise inquiry](https://valmera.io/subscribe?inquiry=training-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=training_line_pickup#enterprise).
