# Edit YouTube videos with an AI assistant and Valmera

Use Valmera to turn a channel brief into a video you can review: establish the story, refine picture and sound, and make standalone Shorts from the recording. This guide is maintained by Valmera for creators working through an authorized MCP client.

[Start a YouTube editing project](https://valmera.io/use-cases/youtubers?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=youtube_workflow) · [Connect your assistant](https://valmera.io/mcp/setup) · [Current plans](https://valmera.io/subscribe)

Creating an account and uploading are free; AI editing requires a subscription. An assistant's own subscription and integration availability are separate.

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
