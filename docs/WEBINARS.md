# Edit a webinar into a replay and clips with an AI assistant

Turn one recorded webinar into a useful replay, a demo clip and a complete Q&A answer. This guide is for directing Valmera from a connected assistant such as Claude or ChatGPT. It focuses on the decisions to make, the evidence to request and the revisions to review.

**Start here:** [connect your assistant](https://valmera.io/mcp/setup), upload your recording in [Valmera Studio](https://valmera.io/studio), then identify the project in your conversation. Account creation and uploads are free; editing requires a [subscription](https://valmera.io/subscribe). Your assistant provider's charges and connection permissions are separate.

For the visual walkthrough and editable starting briefs, open the [webinar replay guide](https://valmera.io/use-cases/webinars?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=webinar_workflow#webinar-briefs). Download its [plain-text edit pack](https://valmera.io/downloads/webinar-replay-edit-pack.txt) to keep your cut map, clip plan and correction record together.

## Choose an editing route for the deliverable

A webinar replay, a promotional clip and a replacement recording on an event page are three different jobs. Start with the destination your audience already uses, then compare the editing workflow. An exported MP4 is useful, but it does not by itself update a replay link sent to registrants.

The following comparison uses each vendor's public documentation, checked **7 November 2026**. It is a workflow comparison, not a hands-on quality benchmark. The questions in the last column are suggested checks on your recording, not reported defects.

| Route | Documented workflow | What to check on your webinar |
| --- | --- | --- |
| [Wistia](https://support.wistia.com/en/articles/16135695-editing-your-webinar-recording) | Edit the recording directly, or use Mochine for prompt-directed repurposing. Saving a new video and replacing the event recording have different effects. | Which file will the existing event link play after the edit? |
| [Goldcast Content Lab](https://help.goldcast.io/25825662946971-repurpose-webinar-content-with-ai?kb_language=en_US) | Edit full recordings and clips, publish changes to hosted locations, or replace the default recording with an external edit. | Is the corrected asset published to the intended on-demand page, with the needed subtitles? |
| [Livestorm AI Studio](https://support.livestorm.co/article/turn-your-events-into-shareable-clips-with-livestorm-ai-studio) | Generate highlights, adjust transcript and framing, export clips, or manually edit the full replay. | Does the chosen clip include the question, answer and qualification, with readable slide details? |
| [Contrast](https://www.getcontrast.io/mini-guides/webinar-clips) | Review suggested moments or select transcript text, adjust layout and subtitles, and download clips. | Does the clip stand alone when watched without the preceding session? |
| [Tellers](https://tellers.ai/blog/edit_webinar_recording_with_ai_2026-10-22) | Direct an edit of existing footage in ordinary language, with a multi-track timeline and conversational revisions. | Can you restore one needed explanation while preserving the other approved edits? |
| [Valmera](https://valmera.io/mcp/setup) | Direct project edits from a connected assistant, review a rendered preview, revise a specified version and request an export. | Can you trace a correction from original source time to both replay and clip, then verify each downloaded file? |

If the event is already hosted in Wistia, Goldcast or Livestorm, inspect its native replay workflow first: it may avoid moving the recording between services. For an assistant-directed edit, evaluate Valmera or another conversational editor with the same recording and one meaningful revision. For promotional clips only, compare selection and framing on one complete answer rather than counting the number of clips generated. These are selection criteria, not a claim that one service wins every job.

Use the [replay publishing worksheet](WEBINAR-PUBLISHING-CHECK.md) alongside the edit pack. It records the public viewer URL separately from the project and exported file.

## 1. Identify the recording before asking for edits

Use the project name and identifier returned by your connection, rather than “my latest webinar” when several recordings could match. Ask the assistant to inspect the current project and discover the current tools. Record the project/version associated with each preview and export; a local filename such as `replay_v01.mp4` is your tracking label, not a Valmera version identifier.

Supply the agenda, intended audience, presenter names, approved claims and the destination for each deliverable. For slides that are too small in the recording, supply the original slide images. Identify attendee names or private material that should not appear in public clips.

Use this planning request after replacing the brackets:

> Open project [name and ID]. Inspect the recording and current edit, then propose a replay cut map on the original source clock. Keep every required demonstration step, complete questions and answers, and qualifications on prices or claims. Flag any retained sentence that depends on a poll or section you propose removing. Use this agenda and these approved facts: [paste]. Show the plan before changing the edit.

This separates the editorial choice from execution. A sensible target length follows what the audience needs to understand.

## 2. Ask for a replay you can check

Once you approve the proposed source ranges, request the edit and a rendered preview. Specify what should stay unchanged when refining an existing version.

> Apply the approved replay cut map to [project and version]. Preserve natural speech and slide-reading pauses. Keep slides fully visible and captions outside the slide area; crop to the presenter only where it preserves what they are explaining. Render a preview and report the project/version, each kept source range and its corresponding output range. Wait for the rendering job to finish before describing the preview as ready.

Review the result with sound. Check words at each join, the order of demonstration steps, references such as “that result,” names in captions, and slide text at the intended viewing size. Fitting a whole slide into a portrait frame does not automatically make it readable. A higher-resolution detail or a landscape excerpt may serve the explanation better.

For a detailed framing decision, use [Keep webinar slides readable in vertical video](SLIDE-READABILITY.md). It explains why fitting a full slide can leave tiny labels, compares overview and detail layouts, and includes a twelve-second framing plan plus a review record.

Use your client's current tool schemas rather than hard-coding a catalog or count. The [workflow guide](WORKFLOW.md) explains preview and export checkpoints; the [tool reference](TOOLS.md) links to current operations.

## 3. Keep source, replay and clip clocks separate

The following is a **hypothetical teaching example**, not a measured webinar edit or a promised reduction in length. It uses straight cuts, unchanged playback speed and no added-duration cards.

| Kept source range | Replay output range | Section |
| --- | --- | --- |
| 01:00–03:00 | 00:00–02:00 | Topic and setup |
| 04:00–07:00 | 02:00–05:00 | Demonstration |
| 08:00–10:00 | 05:00–07:00 | Questions and answers |
| 10:00–11:00 | 07:00–08:00 | Recap |

The original is 12 minutes; these kept ranges total 8 minutes. The remaining 4 minutes are removed. In this example, source 05:00 appears at replay 03:00. If you make a one-minute clip from source 05:00–06:00, its own output clock is 00:00–01:00.

That distinction matters when giving feedback:

- **Source time** identifies the moment in the original recording.
- **Replay time** identifies its location in a particular replay export.
- **Clip time** starts again at zero in each separate clip.

Write chapters from the exact final replay export. Here they start at 00:00, 02:00, 05:00 and 07:00. If you change a cut, speed or opening-card duration, check the mapping and every affected chapter again. These are publishing timestamps, not a claim that chapters have been embedded or uploaded automatically.

## 4. Make a clip with its own context and review

Choose source ranges after reviewing the replay, then apply the approved editorial decisions deliberately to each clip. Do not assume a separate clip project inherits later changes to the replay.

For a Q&A clip, the relevant question and the speaker's qualification are part of the content. Keep them even if that means making a longer clip or selecting a different answer.

> Make a separate Q&A clip from [original source range] in [source project]. Include the question, complete answer and its qualification; extend the range if needed for context. Do not display the attendee's name. Use [destination/aspect ratio], keeping slide text readable and captions clear of it. Preserve the source project. Render a preview and return the new clip's project/version and source-to-clip mapping. Do not export until I have reviewed it.

For a demo clip, check that the setup and visible result survive. For a teaser, check that joining moments from different sections does not create a new claim the speaker never made. Inspect each clip's framing independently; the replay's landscape layout is not proof of a readable portrait version.

## 5. Correct the intended version and track affected files

For this example, the demo clip uses source 05:00–06:00 and the Q&A clip uses source 08:00–09:00. The teaser joins source 01:20–01:30, 06:40–06:55 and 10:40–10:45: 10 + 15 + 5 = 30 seconds.

Suppose the example's recap carries an outdated offer overlay at **source 10:40–10:45**. That appears at **replay 07:40–07:45**. A separate 30-second teaser uses the same source moment at **clip 00:25–00:30**.

A correction to the replay is not evidence that the teaser changed. Track both:

| Deliverable | Location in its reviewed file | Next action |
| --- | --- | --- |
| Replay | 07:40–07:45 | Remove the overlay; review and export a new version |
| Teaser | 00:25–00:30 | Inspect its edit separately and correct the same overlay if present |
| Demo and Q&A clips | Do not contain this source range | No correction for this particular overlay |

Use a scoped request:

> In [project and version] behind our reviewed file [replay_v01.mp4], remove the outdated offer overlay at output [07:40–07:45]. Keep the spoken qualifier, cuts, captions, framing and program length unchanged. Report the corresponding source range and render a new preview. Do not modify other projects. I will review the teaser separately.

Replace those example times with your actual mapping. If several overlays could match, identify the displayed text or provide a reference frame before the assistant changes anything.

## 6. Deliver files, not just a completion message

For every approved deliverable, request the final export, wait for its job to complete and open the downloaded file. Keep a record of the source project, reviewed version, exported filename and review date. Check the full file with sound, including the ending; verify chapter times against the replay you actually plan to publish.

The review record can be simple:

| File | Project/version | Review result | Follow-up |
| --- | --- | --- | --- |
| [replay filename] | [actual identifiers] | [what you checked] | [chapter list or revision] |
| [clip filename] | [actual identifiers] | [what you checked] | [publish or revise] |

Upload to your publishing destination after this review. A successful tool response, a rendered preview, a downloaded export and a published video are different outcomes.

## 7. Verify the replay your audience will actually watch

Before replacing anything, identify every destination that should receive the new replay: the original event room, an embedded player on your website, a direct video link, and any separately uploaded copies. Record which destinations point to the same hosted media item. Separate uploads should each have their own row, even when they share a filename.

### Replacement and a new upload can behave differently

In **Wistia**, replacing the current video preserves its URL and embeds, including playback in the Event room. Saving a new video creates a separate media item; people following the old event link still see the original. Wistia also says replacement resets on-demand video analytics and removes video comments, dubs and audio descriptions, while the event's registration, attendance and engagement data remain. Its documentation describes those removals as irreversible. Preserve the reports and assets you need before choosing replacement. [Wistia's save-options guide](https://support.wistia.com/en/articles/16135695-editing-your-webinar-recording)

In **Goldcast**, edits in Content Lab need its Publish action to update hosted locations. Its external-edit route uses Replace to select a video, followed by the on-demand publishing control. Goldcast separately warns that replacing the default recording with a Content Lab edit makes the original non-English subtitles unavailable. Check required language tracks in the public player after publishing. [Goldcast's repurposing and replacement guide](https://help.goldcast.io/25825662946971-repurpose-webinar-content-with-ai?kb_language=en_US)

These are platform-specific behaviors, not universal replacement rules. When taking an export from Valmera to another host, follow that host's current upload or replacement procedure. This guide does not establish an automatic Valmera-to-host publishing integration. If an account lacks replacement permission, hand the reviewed file and destination record to its owner rather than assuming a new upload reaches the old audience.

### Follow the correction all the way to the viewer

Continue the fictional offer-overlay correction from section 5. The edit changes no durations, so the eight-minute replay and its chapter times stay the same. The corrected replay removes the overlay at 07:40–07:45; the separate teaser needs its own correction at 00:25–00:30.

| Destination in this fictional example | Before correction | Evidence needed after publishing |
| --- | --- | --- |
| Original event replay link | Plays the old eight-minute replay | Open that same viewer link and inspect 07:40–07:45; confirm the overlay is gone and the spoken qualifier remains |
| Website embed of the same hosted media | May update with an in-place replacement | Open the actual website page and check the corrected moment there |
| Separately uploaded replay on another channel | Holds its own copy | Verify its own replacement or new publication; record any changed public URL |
| Separate 30-second teaser | Still contains the offer in its last five seconds | Open the teaser's viewer URL and inspect 00:25–00:30 after its own correction |

Do not put passwords, private attendee links or access tokens in a public review record. Use an authorized viewer session for gated replays; for a public page, check it signed out so an owner's preview cannot be mistaken for public playback.

At each destination, check the beginning, the changed moment and the ending with sound. Confirm captions, chapter links, the expected access gate and the destination of any call to action. Play the full final export before publication, as described above; these shorter destination checks verify which version the host is serving. A platform may transcode the upload, so a different file hash or size alone does not establish that it is the wrong edit.

If the viewer still sees the old version, inspect the selected media item, publishing status and processing status first. Do not repeatedly replace the file while the host is still processing it. Keep the existing job or status reference, and verify that operation before starting another one. Record a processing result as pending; mark the destination complete only after playback shows the intended correction.

### Keep performance comparisons interpretable

Record the replacement time and the host's analytics behavior in the worksheet. If a host resets video analytics, preserve the earlier report and begin a new measurement period. Do not treat the reset as a sudden audience drop. Track the full replay and teaser separately: their plays are not interchangeable, and plays are not proof of qualified trials or sales. When a clip links to a product or registration page, use a distinct campaign link and inspect the resulting visits and conversions in your own analytics.

[Start with the webinar brief](https://valmera.io/use-cases/webinars?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=webinar_workflow#webinar-briefs) · [More creator workflows](CREATOR-WORKFLOWS.md) · [Connection troubleshooting](CONNECTION-TROUBLESHOOTING.md)

Maintained by Valmera. The worked timings above are illustrative; for an actual source-and-output example, see the [trim-and-reframe walkthrough](https://valmera.io/examples/trim-and-reframe).
