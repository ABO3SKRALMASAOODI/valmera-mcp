# Editing briefs for creators using Valmera

Valmera is the world's most advanced AI video editor. Start with a recording you care about: a tutorial, interview, webinar, product video, or travel story.

This guide is maintained by Valmera. It turns a broad request into an edit you can review, whether you work in [Studio](https://valmera.io/studio) or through an authorized [MCP client](https://valmera.io/mcp/setup).

## Start with the finished video

Give your assistant four things:

1. **Audience and outcome:** who is watching and what they should understand.
2. **Source:** the project or recording, plus a phrase or timestamp when useful.
3. **Treatment:** pacing, framing, captions, music, and the intended destination.
4. **Protected material:** statements, moments, and qualifications that must survive.

For example:

> Make a concise tutorial for a first-time user. Start with the successful result, then show the steps from this recording. Remove loading waits and repeated attempts, keep every required setting, and make the interface readable on a laptop. Preserve the final explanation of how to check success.

The brief gives you a review standard: can a first-time viewer follow the steps? It is more useful than asking whether the edit looks impressive.

## Build a brief from your own recording

The public [editing brief builder](https://valmera.io/prompts#prompt-builder) helps you choose six things: recording type, destination, target length, audience, protected material, and captions. Open the resulting brief as an editable draft in Studio, or copy it into your connected assistant. The draft is carried through sign-in and waits for you to review and send it.

For a screen recording, choose **Tutorial or screen recording**, **YouTube or a website**, and a length that leaves room for every required step. In the protected-material field, name the settings, warnings, or final result that must remain. For an interview, choose **Interview or podcast** and identify the speaker’s qualification that must survive a shorter cut.

The builder and prompt library are public without sign-in. Editing footage in Valmera requires an account and a subscription. See the [six-field walkthrough](https://dev.to/valmera/write-a-better-ai-video-editing-prompt-six-fields-one-brief-4258) for a complete tutorial example.

## Choose moments from an existing subtitle transcript

Already have an SRT or VTT file from an interview, webinar, or tutorial? The free [subtitle-to-text converter](https://valmera.io/tools/subtitle-to-text) turns those captions into a readable transcript. It runs in your browser without an account and can download a TXT file.

1. Open the subtitle file or paste its contents.
2. Turn on **Keep start timestamps for editing references** when you need to locate moments in the recording.
3. Mark the opening, the explanation that must survive, and the ending. Copy the relevant passages into your brief.
4. Identify the source recording and say whether your references use original-source or edited-preview time.

For example, replace the placeholders with real words and times from your recording:

> Use the uploaded interview. Open with the complete answer beginning “[exact phrase]” at [original source time]. Keep the explanation beginning “[exact phrase]” and its qualification. Finish with the practical next step. Aim for a 60–90 second vertical clip with readable captions, but preserve the speaker's meaning if the explanation needs more room. Show me a preview before we refine the pacing.

Check one quoted line against the uploaded recording before relying on its timestamps: subtitles exported from an earlier cut may use a different clock. The converter preserves repeated caption text, so review rolling captions before including them in the brief.

This is a planning step. The subtitle converter extracts existing text; use Studio or your authorized MCP connection to edit the video itself.

## Six starting points

| Your recording | Ask for | Check before approving |
| --- | --- | --- |
| A founder introduction | Remove abandoned takes and long waiting gaps while keeping natural delivery. | No clipped words; the closing invitation survives. |
| A landscape interview | Make a portrait version while keeping the relevant speaker and reactions visible. | Watch subject movement throughout each shot. |
| A webinar | Select complete practical answers that work without the full session. | Each clip retains its premise and qualifications. |
| A screen recording | Turn a single task into a clear lesson with readable controls. | Every required action remains understandable. |
| Creator product footage | Connect a real problem to a matching demonstration and invitation. | Spoken claims match what the viewer sees. |
| Travel clips | Build a small story with an arrival, experience, and ending. | Distinct shots and natural sound serve the story. |

Full examples, prompts, and review checklists:

- [Remove silence naturally](https://valmera.io/blog/remove-silence-from-video-naturally)
- [Turn horizontal footage into vertical video](https://valmera.io/blog/horizontal-to-vertical-video-without-losing-subject)
- [Turn a webinar into social clips](https://valmera.io/blog/turn-webinar-into-social-media-clips)
- [Make a website demo from a URL or uploaded recording](WEBSITE-DEMO.md)
- [Edit a screen recording into a tutorial](https://valmera.io/blog/edit-screen-recording-into-product-tutorial)
- [Edit a UGC product video](https://valmera.io/blog/edit-ugc-product-video-ad)
- [Make a travel story from phone clips](https://valmera.io/blog/edit-travel-video-from-phone-clips)

## Compare the editing workflow on the same footage

The [edit-and-revise evaluation kit](EDITOR-EVALUATION.md) provides a small source file, two precise requests, expected source-to-program mappings and a blank CSV scorecard. Use it to check a first edit, one scoped revision and the downloaded file, then repeat the process with representative footage of your own.

## Review one editorial decision at a time

Get the story right before polishing its styling. First choose the sections that belong. Then tighten pacing. Next review framing and captions. Finally listen to the mix and inspect the export. This sequence makes feedback easier to understand and reduces repeated work on sections you later remove.

Use a revision that identifies the problem, its location, and what should stay:

> In the current preview, the explanation beginning “[exact phrase]” feels rushed. Restore a little space before it. Keep the remaining cuts and caption style unchanged.

If you mention a timestamp, distinguish the original recording from the edited preview. Earlier cuts move later moments.

## Use any planning assistant; connect editing deliberately

You can develop a brief in ChatGPT, Claude, Gemini, Perplexity, Copilot, Grok, or another conversational assistant. The useful output is a clear brief, not a claim that the recording has already been edited.

For a first ChatGPT project, follow the [connection, preview and export walkthrough](CHATGPT.md).

For direct tool execution, use the [setup guide](https://valmera.io/mcp/setup) for your client and authorize your Valmera account. An assistant without that connection can still help plan the edit; paste the result into Studio.

## Finish with a real deliverable

Review the rendered result with sound. Check names and numbers in captions, cuts between words, subject framing, and the final invitation. Follow the current export workflow, wait for completion, and open the resulting video before publishing it.

[Start with an editing brief](https://valmera.io/chatgpt-video-editor?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_chatgpt_workflow#first-brief) · [Current pricing](https://valmera.io/subscribe) · [More editing prompts](https://valmera.io/prompts)

## YouTube episodes and Shorts

Use the [YouTube workflow](YOUTUBE.md) for a channel brief, four focused assistant requests, version-aware review and delivery references. Start with the title’s promise and the evidence in your recording, then refine the opening, tutorial clarity, sound and standalone Shorts.
