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

### Refine sound without reopening the story

> Keep the approved picture edit. Make the narration easy to understand, use music only where it supports the sequence, and add a few purposeful sound effects. Identify supplied, sourced or newly created audio. Show the mixed passage so I can compare speech clarity and timing before export.

The [sound-effects guide](https://valmera.io/tools/add-sound-effects) includes an accent-alignment example and revision prompts.

### Make Shorts that stand on their own

> Propose three distinct moments from this recording for [audience]. Each should contain enough setup to understand the point and a complete payoff. Explain the selection, then show vertical previews with readable captions. Preserve qualifications, check crops throughout, and avoid repeating the same argument in all three clips.

Choose the length for the story and its destination. YouTube's current [three-minute Shorts guide](https://support.google.com/youtube/answer/15424877) explains aspect-ratio and upload-date eligibility. It also explains why Shorts longer than one minute with active Content ID claims can be blocked. A shorter duration does not establish permission to use music.

## Review the export and the processed upload

Play the exported file, including its ending. Check sentence joins, names and numbers, demonstration details, crops, audio and the version that was rendered. Then inspect the processed upload in YouTube Studio before publishing.

Use YouTube's [encoding recommendations](https://support.google.com/youtube/answer/1722171) for the destination. Distinguish on-screen captions from a switchable subtitle track; YouTube documents [subtitle upload and editing](https://support.google.com/youtube/answer/2734796) separately. For realistic generated media or meaningful AI alterations, review its [disclosure guidance](https://support.google.com/youtube/answer/14328491).

After publishing, use the [retention report](https://support.google.com/youtube/answer/9314415) to investigate a specific passage. A spike can reflect interest or confusion; a dip can reflect skipping or leaving. Use that evidence to propose the next editing change. This workflow does not guarantee retention, recommendations or monetization.

Primary YouTube references reviewed November 6, 2026. The prompts are editorial examples, not a measured editing benchmark. For the wider workflow, see [how to edit YouTube videos with AI](https://valmera.io/blog/edit-youtube-videos-with-ai).
