# Test an AI video editor on a real case-study revision

Give each editor the same customer interview, the same event footage and the same two requests. Ask for a 60–90 second case-study MP4, then change one four-second cutaway after approval. Buy the workflow that lets your team deliver the approved story again without redoing the approval.

[Download the review sheet](CASE-STUDY-CUTAWAY-REVISION.csv). It includes an example of a passing picture swap and three examples you would send back. Replace the sample times and filenames with yours.

## Build a test the buyer can repeat

1. Bring a source interview with a line your customer approved and a clear qualifier. For example, a claim about a standard weekly close does not cover quarter-end work. Bring two event cutaways your company can use in this version.
2. Put the files in a clean project. Keep the original file names in the review sheet. Ask for the outcome and its context to remain audible. Ask for two exports if you need both a captioned MP4 and a separate SRT.
3. Download the first pass. Mark an actual four-second interval that falls inside the approved quote. Ask for a picture-only swap in that interval. Keeping the request small gives you a clean test of what the tool can preserve.

Copy this brief and replace the brackets with export times, source times and filenames from the first pass.

> Use [interview.mov] and the two attached cutaways. Make a 60–90 second case study with the problem, how the team changed its process and the result. Keep the approved quote and its qualifier together. Add readable captions and use supplied B-roll to illustrate the story. Export an MP4 for review. Give me the source time for the approved quote.

> In the approved preview, replace the picture from [00:27.000 inclusive] to [00:31.000 exclusive] with [event-check-in-wide.mp4, 00:03.000–00:07.000]. Use the interview audio already there. Keep the existing captions, the speaker's exact wording, the in and out times and the rest of the sequence. Export the revised MP4 and, if requested, the separate captions.

## Inspect the files you would actually send

| Test | What to verify in the downloaded export |
| --- | --- |
| Cutaway starts and ends on the intended frames | Step across both boundaries. At 30 fps, `00:27.000–00:31.000` means frame 810 is the first changed frame and frame 929 is the last. Frame 930 should show the original following shot. Adapt frame numbers to your export timebase. |
| The quote survives the revision | Listen with the picture covered. Compare the words, the qualifier and the timing with the approved preview and the source. Check that sound from the event clip did not replace or leak into the interview. |
| Correct captions survive the change | Watch the revised MP4 at normal speed. Check that captions stay visible against the new shot. If you require sidecar captions, open them with the revised MP4 and check the cues on both sides of the swap. |
| The release is usable | Download and reopen the revised MP4 outside the editor. Check the last frame, export settings and approved brand elements. Save the version your customer can approve. |

An unchanged caption file does not tell you whether burned-in captions remain readable. Listen and watch the local MP4 before you approve the revision. Compare the two versions by content and timing. Export metadata or re-encoding can change whole-file hashes even when the visible edit is identical.

## Calibrate your review before buying

- **Check picture timing.** In Valmera's recorded example, the opening stays at four seconds while the closing starts two seconds earlier in the revision. Compare the same playback time in the two MP4s and check the closing shot's source clock. That example isolates a picture timing change. For the buyer test above, the closing shot should start at the *same* time in both exports. [Play the recorded Valmera revision](https://valmera.io/examples/rough-cut-revision).
- **Check the meaning of the quote.** Listen to the two downloadable practice edits. A short version keeps the headline metric and leaves out the type of close and the quarter-end exception. The longer cut makes the scope audible. [Compare the practice interview exports](CUSTOMER-TESTIMONIAL-VIDEO-EDITORS.md#hear-how-a-three-second-edit-changes-the-claim).

## Pick the workflow your team can operate every week

| Route | Why a buyer would test it | What to record |
| --- | --- | --- |
| Valmera | Upload your footage and describe the first edit and follow-up in chat. [Customer testimonial workflow](https://valmera.io/use-cases/customer-testimonials?utm_source=github.com&utm_medium=referral&utm_campaign=case_study_cutaway_revision) | Record the time from your first brief to a downloadable revision that passes the four checks. |
| Descript | The documented Replace Media operation keeps edits and adjustments on an existing layer. [Replace media documentation](https://help.descript.com/visuals/replace-media) | Test the picture-only swap on a separate layer and verify that both the quote and the captions survive. |
| Kapwing | Its browser editor supports multitrack editing and MP4 export. [Kapwing MP4 editor](https://www.kapwing.com/video-editor/mp4) | Check how long it takes an editor to place the alternate clip, preserve the existing audio and export. |
| Adobe Premiere | Your team can finish in a desktop timeline with AI-assisted editorial features. [Adobe Premiere AI editing](https://www.adobe.com/products/premiere/ai-video-editing.html) | Check whether an editor can reopen the project, swap the cutaway and return the agreed deliverables on deadline. |

Capabilities in the table come from each provider's documentation. The review sheet is a protocol for your own pilot, with illustrative outcomes. It does not report comparative benchmark results.

If one person can run the pilot and deliver the approved file, [check Valmera editing access](https://valmera.io/subscribe?utm_source=github.com&utm_medium=referral&utm_campaign=case_study_cutaway_revision). If your team needs recurring done-for-you editing, send your monthly interview count, formats per interview, approval owner and turnaround target through [Valmera Enterprise](https://valmera.io/subscribe?inquiry=case-study-editing&utm_source=github.com&utm_medium=referral&utm_campaign=case_study_cutaway_revision#enterprise). Include one representative revision so the pilot reflects what the team will have to deliver each month.
