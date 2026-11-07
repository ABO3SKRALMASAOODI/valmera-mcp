# Edit YouTube videos with an AI assistant and Valmera

Use Valmera to turn a channel brief into a video you can review: establish the story, refine picture and sound, and make standalone Shorts from the recording. This guide is maintained by Valmera for creators working through an authorized MCP client.

[Start a YouTube editing project](https://valmera.io/use-cases/youtubers?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=youtube_workflow) · [Connect your assistant](https://valmera.io/mcp/setup) · [Current plans](https://valmera.io/subscribe)

Creating an account and uploading are free; AI editing requires a subscription. An assistant's own subscription and integration availability are separate.

## Choose an editor for the episode you want to publish

Write the deliverable before choosing the tool. A cleaned presenter recording, a complete tutorial, three Shorts and a generated scene are different outputs. A useful shortlist starts with the footage you have and the remaining work you want the editor to do.

| Your starting point | Route to inspect | What to request in a trial |
| --- | --- | --- |
| A presenter recording with repeated attempts | [Gling](https://www.gling.ai/) describes bad-take, silence and filler removal, captions and reframing. | A continuous episode with the intended takes retained. Inspect removed material, joins and the path to your finishing editor if you need one. |
| A speech-led episode you want to revise through text | [Descript Underlord](https://www.descript.com/underlord) combines an assistant with transcript-based editing and production tools. | Move an explanation, restore one deleted sentence and check the corresponding picture and sound. |
| Recorded material requiring story assembly and visual finishing | [Invideo Editor](https://invideo.io/make/ai-video-editor/) describes conversational editing, timeline controls, footage search and timeline export. | One complete episode, followed by a focused revision. If another editor must finish it, open the exported project there. |
| A long recording you primarily want to repurpose | [OpusClip's clipping route](https://www.opus.pro/ai-video-editor) describes clipping, captioning, reframing and publishing workflows, separately from AI Producer. | Distinct, complete Shorts with enough context. Choose the appropriate route if you also need an edited episode. |
| One person speaking to camera, with a conversational finishing workflow | [OpusClip AI Producer](https://producer.opus.pro/) describes editing raw talking-head footage through Claude or ChatGPT and continuing revisions in the same project. | Test the full episode and a restoration request. Its current page excludes multicamera footage and screen recordings; check that your tutorial fits before uploading. |
| Dialogue-led assembly with direct control over the desktop timeline | [Premiere Text-Based Editing](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/overview-of-text-based-editing.html) links transcript changes to timeline edits; [Paper Edit](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/create-a-sequence-with-paper-edit.html) assembles selected speech into a sequence. | Restore a source passage, refine its joins and export the episode. Measure your manual finishing time separately; these transcript controls do not by themselves demonstrate autonomous editing. |
| Missing shots to generate for an existing project | [YouTube Create's AI guidance](https://support.google.com/youtube/answer/16631240?hl=en) describes experimental generated clips with limited availability. | The required supporting shot, then a separate check of how it fits the episode. Confirm access on your account before planning around it. |
| Your recording, directed through conversation in Studio or an MCP client | [Valmera's editing workflow](WORKFLOW.md) covers inspection, edits, previews, revisions and export. | A story cut from your source, a specific correction and the downloaded final file. Use the current tools available to your authorized account. |

These are workflow descriptions checked against the linked first-party pages on November 7, 2026, not a hands-on ranking. Several tools span more than one route. Compare the requested deliverable and the work left after export, rather than treating the route labels as permanent product limits.

## Test the whole episode, then one precise correction

A polished thirty-second sample can help you assess captions or framing. It cannot show whether an editor sustains a six-minute explanation, remembers a required limitation, or delivers the promised conclusion. Use a small complete recording when comparing episode editing; keep a separate short sample for visual treatment experiments.

Here is a fictional trial brief you can adapt. The timestamps and duration target are placeholders, not measured Valmera results:

> I have a 12-minute recording demonstrating [task]. Make a 6–8 minute YouTube episode for someone doing this for the first time. Open with the actual result, then retain the required setup, the working method and the final verification. Keep the warning that [specific limitation] applies. Remove abandoned attempts only when the successful attempt supplies the same necessary explanation. Use my supplied recording and approved assets. Show a story preview before adding decorative graphics. Deliver a 16:9 video; propose two distinct Shorts separately after I approve the episode.

The target duration is a preference. If the necessary explanation cannot fit, ask for the tradeoff instead of silently dropping a step. A compelling opening still needs to represent what the method actually achieves.

Review the first cut in viewing order:

| Moment | Question to answer from the rendered video |
| --- | --- |
| Opening | Is the promised result visible, and is its context accurate? |
| Setup | Can the intended viewer identify the prerequisites and starting state? |
| Demonstration | Does every required action lead to a visible, understandable result? |
| Qualification | Is the limitation still attached to the claim it qualifies? |
| Payoff | Does the ending actually verify what the opening promised? |

Then request one controlled revision:

> In the preview version I just reviewed, restore the omitted explanation about [required setting] between [preceding action] and [following action]. Identify its original source passage. Keep the other approved story decisions, caption style and music choices unchanged. Render the revised passage and tell me which later chapter or caption timings need updating.

This tests an everyday creator need: recovering important context without rebuilding the whole video. Review the new join, the restored instruction and the surrounding approved material. A message saying the sentence was restored is not the result; the new preview must contain it.

Keep one [episode trial record](YOUTUBE-EDITOR-TRIAL.md) per candidate. Record account plan, footage duration, elapsed processing time, active correction time, allowance used, unresolved work and the downloaded file. Do not call a timeline handoff a finished video, or a set of Shorts a delivered episode. For a final file, check the required format, resolution, branding and complete playback. The [export checklist](FREE-EXPORT-CHECK.md) helps separate free access from the file you can actually download.

## Connect the project to the brief

Connect at `https://valmera.io/mcp/server`, sign in, and let your client discover the current tool schemas. Choose the intended project and preview version. Use the [upload guide](https://valmera.io/docs/file-uploads) when the recording is not in Valmera yet.

Start with a request like this, replacing the brackets before sending:

> Open [project]. I am making a YouTube video for [viewer]. The title promises [specific result], and the viewer should leave understanding [takeaway]. Aim for [length], preserving [required steps, qualifications and sponsor wording]. Use [approved assets] and propose any additional visuals or sound before extending the treatment. Show a story cut first, then we will refine the picture and audio.

Ask the assistant to identify the project and the requested deliverables. If it cannot access the project, resolve that before starting an edit. Do not paste account tokens into the brief.

## Review three different outcomes

| Pass | Ask the assistant to produce | What you review |
| --- | --- | --- |
| Story | An opening, the necessary explanation, evidence and payoff | Does the cut deliver the title's promise while preserving meaning? |
| Presentation | Captions, illustrative visuals, readable demonstrations and a balanced mix | Can the intended viewer follow the action and understand the words? |
| Delivery | The approved long-form version and any separately reviewed Shorts | Are these the right versions, aspect ratios and caption treatments? |

A job identifier means work has started. Continue checking that job's reported status until it reaches a terminal state; a timeout is not evidence that the work failed. Review the resulting preview before calling the edit finished. Follow the current tool responses and schemas rather than guessing arguments from an old tutorial.

## Four focused revision briefs

### Make the opening deliver the promise

> Find a short passage that genuinely demonstrates the result promised by my title. Propose it as the opening, followed by the problem and necessary constraints. Identify the source passage and show a preview. Preserve the speaker's meaning and required warnings. Keep the rest of the approved structure unchanged.

Source time and preview time can differ after cuts or rearrangement. Name the version when referring to a timestamp. A result from later in the recording should not imply that a different method produced it.

### Make a tutorial reproducible

> Review the demonstration from a first-time viewer's perspective. Keep every required setting and step. Shorten loading waits and repeated attempts, make the relevant controls readable, and preserve the final check that proves the task worked. Show a representative passage before applying the treatment to the rest.

For a step map, a worked 76-to-58-second cut and a revision that updates later timestamps, use the [screen-recording tutorial guide](SCREEN-RECORDING-TUTORIALS.md).

### Refine sound without reopening the story

> Keep the approved picture edit. Make the narration easy to understand, use music only where it supports the sequence, and add a few purposeful sound effects. Identify supplied, sourced or newly created audio. Show the mixed passage so I can compare speech clarity and timing before export.

The [sound-effects guide](https://valmera.io/tools/add-sound-effects) includes an accent-alignment example and revision prompts.

### Make Shorts that stand on their own

> Propose three distinct moments from this recording for [audience]. Each should contain enough setup to understand the point and a complete payoff. Explain the selection, then show vertical previews with readable captions. Preserve qualifications, check crops throughout, and avoid repeating the same argument in all three clips.

Choose the length for the story and its destination. YouTube's current [three-minute Shorts guide](https://support.google.com/youtube/answer/15424877) explains aspect-ratio and upload-date eligibility. It also explains why Shorts longer than one minute with active Content ID claims can be blocked. A shorter duration does not establish permission to use music.

## Make YouTube chapters from the finished edit

Chapter timestamps belong to the video viewers will watch. A transcript of the original recording is useful for finding topics, but its times become wrong when you remove a false start, move a result to the opening or shorten a demonstration. Write the chapter list against the approved output, then verify it against the downloaded file.

YouTube's [manual chapter instructions](https://support.google.com/youtube/answer/9884579?hl=en) require an initial `00:00` entry, at least three timestamps in increasing order, and chapters lasting at least ten seconds. Put the titles and times in the video's description. Manual chapters replace automatic chapters; automatic chapters are not available on every video. If chapter access is missing, consult the linked Advanced features guidance. These requirements were checked November 7, 2026.

### Worked example: a nine-minute recording becomes five minutes

This is a fictional editing plan, not a recorded Valmera run. It assumes ordinary-speed cuts with no overlapping transitions, inserted introductions or additional ending. Intervals include their start and exclude their end. Check the actual export if the treatment adds time.

Imagine a tutorial that shows how to set up a project and verify the result. Keep the following passages in this order:

| Source recording | Why keep it? | Duration | Output version 1 |
| --- | --- | --- | --- |
| 00:30–01:00 | Promise and finished-result preview | 30 seconds | 00:00–00:30 |
| 01:20–02:10 | Required setup | 50 seconds | 00:30–01:20 |
| 03:00–05:00 | Main demonstration | 120 seconds | 01:20–03:20 |
| 06:10–07:20 | Verify the result | 70 seconds | 03:20–04:30 |
| 08:10–08:40 | Recap and next action | 30 seconds | 04:30–05:00 |

The retained passages total 300 seconds. The source starts for these topics are `00:30`, `01:20`, `03:00`, `06:10` and `08:10`; none is the correct chapter start for this cut. The output version 1 description would contain:

```text
00:00 What you will make
00:30 Set up the project
01:20 Build the first version
03:20 Check the result
04:30 Recap and next step
```

Use titles that name the viewer's next task. A chapter called “Check the result” should land where that check begins, with enough context to follow it. Do not promise a fix, comparison or result that the retained passage does not show.

### A twenty-second revision changes later chapters

Suppose the loading wait at source `04:10–04:30` is unnecessary. It lies inside the main demonstration, at output version 1 `02:30–02:50`. Removing it produces a 280-second cut, or `04:40`.

| Chapter | Output version 1 | Revised output version 2 |
| --- | --- | --- |
| What you will make | 00:00 | 00:00 |
| Set up the project | 00:30 | 00:30 |
| Build the first version | 01:20 | 01:20 |
| Check the result | 03:20 | 03:00 |
| Recap and next step | 04:30 | 04:10 |

The first three chapters keep their starts. Only starts after the removed passage move twenty seconds earlier. Subtracting twenty seconds from every timestamp would break the opening and setup. The last chapter still lasts thirty seconds, from `04:10` to `04:40`.

Give the assistant a bounded revision request:

> In the approved tutorial version 1, remove only the loading wait at source 04:10–04:30, corresponding to output 02:30–02:50. Preserve the action before it and the visible result after it. Show the revised join. Recalculate chapters and caption timing for version 2, identify which entries changed, and verify them against the new preview. Keep the other story decisions unchanged.

Those times apply only to this fictional example. For your recording, identify the correct source and preview version before using a revision prompt.

## Keep the video, chapters and captions together

Record a small handoff table when approving a version:

| Deliverable | Version to identify | Check before publishing |
| --- | --- | --- |
| Downloaded video | Project, approved edit version and filename | Play the whole file, including the ending; note its measured duration |
| Description chapters | The same exported edit | Seek to every timestamp and confirm the title matches what begins there |
| Switchable captions | Language and matching edit version | Listen at the opening, every revised join and the final spoken sentence; then review the entire track |
| Short extracted from the video | Its own approved version | Start its timing from its own beginning; review crop, setup and payoff separately |

An added intro moves later times; an appended end card changes the ending; a speed change requires a new mapping within that passage. Inspect the delivered file instead of assuming that the planned five-minute program and downloaded duration are identical. The [recorded MCP example](MCP-RECORDED-EDIT.md) shows why this matters: its ten-second program was delivered in a fifteen-second file with a five-second end card.

Burned-in captions and a switchable caption track are separate deliverables. YouTube supports [caption-file uploads with or without timing and transcript synchronization](https://support.google.com/youtube/answer/2734796?hl=en). Use the words and timing of the finished edit. A transcript containing deleted speech can no longer describe that edit accurately. Review names, numbers, speaker changes and meaningful sounds, then check the processed upload with captions enabled. YouTube also documents [editing caption text and timestamps](https://support.google.com/youtube/answer/2734705?hl=en); for a cue crossing a removed passage, see the [caption revision examples](CAPTION-REVISIONS.md).

## Review the export and the processed upload

Play the exported file, including its ending. Check sentence joins, names and numbers, demonstration details, crops, audio and the version that was rendered. Then inspect the processed upload in YouTube Studio before publishing.

Use YouTube's [encoding recommendations](https://support.google.com/youtube/answer/1722171) for the destination. Distinguish on-screen captions from a switchable subtitle track; YouTube documents [subtitle upload and editing](https://support.google.com/youtube/answer/2734796) separately. For realistic generated media or meaningful AI alterations, review its [disclosure guidance](https://support.google.com/youtube/answer/14328491).

After publishing, use the [retention report](https://support.google.com/youtube/answer/9314415) to investigate a specific passage. A spike can reflect interest or confusion; a dip can reflect skipping or leaving. Use that evidence to propose the next editing change. This workflow does not guarantee retention, recommendations or monetization.

Primary YouTube references reviewed November 6, 2026. The prompts are editorial examples, not a measured editing benchmark. For the wider workflow, see [how to edit YouTube videos with AI](https://valmera.io/blog/edit-youtube-videos-with-ai).
