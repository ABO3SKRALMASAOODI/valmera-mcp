# AI B-roll editors for your own footage when a shot is missing

Use supplied footage where it shows the exact product, screen or action the speaker describes. When none of the clips fits a claim, leave the presenter on screen or record the missing shot. A visually similar clip can mislead viewers about the steps they need to follow. Test this before you buy an editor that automatically fills gaps.

[Try the approved-footage exercise](examples/b-roll-missing-shot/review-shot-choices.html) · [Brief an edit in Valmera](https://valmera.io/tools/add-b-roll?utm_source=github.com&utm_medium=referral&utm_campaign=broll_missing_shot)

## Compare how each editor handles a gap

| Editor | What the vendor documents | What to check on your footage |
| --- | --- | --- |
| AgentReel B-roll Cut | Builds from a script or voice recording and uploaded footage. It marks fallback shots when a phrase has no match and offers an editable timeline export. [AgentReel B-roll Cut](https://agentreel.ai/broll-cut) | Inspect the marked fallback on the unsupported sentence. See whether you can remove it or replace it with a presenter shot in your intended workflow. |
| Eddie AI | Its vlog guide describes an instruction to use only your footage and options for adding B-roll when coverage is incomplete. [Eddie AI vlog guide](https://www.heyeddie.ai/how-to/edit-vlogs) | Supply a main recording and one current supporting shot. Ask for footage-only editing and confirm the uncovered claim stays on camera in the preview and export. |
| Kapwing Kai | Its editing walkthrough shows placing uploaded screen recordings above narration and muting the inserts. [Kapwing’s AI editing walkthrough](https://www.kapwing.com/resources/ai-video-editing-tutorial-9-workflows-tested/) | Ask it to insert a clip only on named words and keep the speaker visible on the next sentence. Review the actual timeline and downloaded MP4. |
| Valmera | The B-roll guide documents specifying uploaded clips only, naming exact words for coverage, and keeping source narration in a silent overlay. [Valmera’s B-roll editor](https://valmera.io/tools/add-b-roll) | Name the current capture and cue. State where the presenter must stay visible. Check the exported frames and narration, including the join back to the presenter. |

Valmera publishes this comparison. The table describes documented workflows. The example below is a planning exercise, and the linked Valmera export tests exact timing and narration separately.

## Give each editor a current capture and a look-alike

Use a short passage from an upcoming product walkthrough. Add one approved insert and a similar-looking clip that shows a different result. Leave one line without a supporting clip. In the [downloadable practice exercise](examples/b-roll-missing-shot/review-shot-choices.html), the current capture shows **Export MP4** and the previous version shows **Export CSV**. The narration later mentions a reviewer opening an email, for which no capture was supplied. The same two control labels are visible at 00:04 in the [current practice MP4](examples/training-line-pickup/approved.mp4) and the [previous practice MP4](examples/training-line-pickup/original.mp4).

| Spoken cue | Required picture | Review decision |
| --- | --- | --- |
| “Choose Export MP4.” | The current control and the export result | Cut to the current approved capture. Check the words on the button and that playback reaches the result. |
| “Your reviewer opens the email.” | Presenter, pending an approved email capture | Return to the presenter for the complete sentence. The export screen is unrelated to the email claim. |
| “I’ll show the review next.” | Presenter | Inspect the end of the prior cutaway and keep the transition in the same place across revisions. |

On GitHub, use **Download raw file** on the HTML exercise and open it in your browser. It runs offline and gives feedback on both shot decisions. Use your actual files in the editor you are evaluating.

## Run the purchase test

> Use only the files I uploaded. Keep the base recording and original narration. Show the approved current-release export capture while I say “Choose Export MP4.” Start at the visible control and let the export confirmation play. Leave the presenter visible for the complete sentence about opening the email. Send an MP4 and tell me which source file you used for the cutaway.

1. **Review the first export.** Check the label and result in the cutaway, then skim the complete sentence with no approved insert. At both joins, listen for uninterrupted narration.
2. **Send one correction.** If the result is hard to see, ask for a longer visible portion of the same approved capture while keeping the next sentence with the presenter. Compare the revised MP4 and log how much manual adjustment it required.
3. **Compare the approved delivery.** Record the asset name, final in and out times, and any manual replacement. Use [Valmera’s recorded cutaway example](OWN-FOOTAGE-B-ROLL-CUTAWAY-TEST.md) to see how the picture boundaries and narration were checked frame by frame.

[Try the B-roll workflow on your own footage](https://valmera.io/tools/add-b-roll?utm_source=github.com&utm_medium=referral&utm_campaign=broll_missing_shot). AI editing requires a subscription. For regular client uploads, [request a done-for-you editing pilot](https://valmera.io/subscribe?inquiry=product-demo-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=broll_missing_shot#enterprise) with one example, your footage rules and the number of videos per month.
