# Valmera documentation: find the workflow for your recording

Start with the edit you want to make. These public guides cover connecting an assistant, writing a brief, reviewing a result and correcting it. Valmera edits footage you provide through its browser Studio or hosted MCP service. Account creation and uploads are free; AI editing requires an eligible subscription. Check [current plans](https://valmera.io/subscribe).

## Start an edit or connect your assistant

| What you want to do | Start here |
| --- | --- |
| Go from an uploaded recording to a reviewed export | [Complete editing workflow](WORKFLOW.md) |
| Connect Claude, ChatGPT or another compatible client | [Client setup and hosted-service responsibilities](CLIENTS.md) |
| Choose between your own assistant and Valmera AI | [Plans, allowances and editing routes](CLIENTS.md#choose-the-plan-for-your-editing-route) |
| Make a first edit through ChatGPT | [ChatGPT walkthrough](CHATGPT.md) |
| Use the Claude plugin | [Claude plugin setup](CLAUDE-PLUGIN.md) |
| Choose a Gemini video-editing route or connect Gemini CLI | [Gemini video workflow](GEMINI-VIDEO-EDITING.md) |
| Prepare a brief with Grok and choose an execution route | [Grok workflow](GROK.md) |
| Resolve sign-in, authorization or missing tools | [Connection troubleshooting](CONNECTION-TROUBLESHOOTING.md) |
| Find the operation that matches the edit | [MCP tool guide](TOOLS.md) |
| Write a specific request | [Prompt examples](PROMPTS.md) and [creator briefs](CREATOR-WORKFLOWS.md) |

Use the current tool schemas returned by your authorized connection. A successful connection check establishes access, not a completed edit. For client-neutral installation instructions, see [the agent setup guide](../llms-install.md).

## Choose the guide that matches your footage

| Recording or task | Guide and practical artifact |
| --- | --- |
| Interview | [Editor workflow comparison and traceable paper edit](INTERVIEW-PAPER-EDIT.md), with a [trial and review worksheet](INTERVIEW-REVIEW-WORKSHEET.md) |
| Podcast clips | [Compare ten clipping workflows and select a complementary clip set](PODCAST-CLIPS.md), with a [blank selection and delivery worksheet](PODCAST-CLIP-WORKSHEET.md) |
| Screen recording or software tutorial | [Preserve the starting state, action and result](SCREEN-RECORDING-TUTORIALS.md) |
| Website demonstration | [Plan and make a website demo](WEBSITE-DEMO.md) |
| Webinar replay and clips | [Webinar workflow](WEBINARS.md) and [vertical slide readability](SLIDE-READABILITY.md) |
| YouTube video | [Editing workflow, chapter timing map and caption handoff](YOUTUBE.md) |
| Property walkthrough | [Real-estate shot map and revision plan](REAL-ESTATE-SHOT-MAP.md) |
| Several recordings with one style | [Batch editing: pilot, source-specific notes and delivery tracking](BATCH-VIDEO-EDITING.md) |
| Unwanted pauses or filler words | [Speech cleanup: compare controls, review joins and restore a pause](SPEECH-CLEANUP.md), with a [trial and repair worksheet](SPEECH-CLEANUP-WORKSHEET.md) |
| Fan noise, hiss or distracting sound behind speech | [Compare noise-removal routes and review the exported audio](VIDEO-AUDIO-NOISE-REMOVAL.md), with a [listening and delivery worksheet](AUDIO-NOISE-REVIEW-WORKSHEET.md) |
| Translate subtitles while keeping the original voice | [Compare translation routes and review a bilingual sample](SUBTITLE-TRANSLATION.md), with a [trial and delivery worksheet](SUBTITLE-TRANSLATION-WORKSHEET.md) |
| Incorrect captions after an edit | [Fix wording, offset, drift and cues crossing a cut](CAPTION-REVISIONS.md) |
| Remove or replace a video background | [Compare ten routes and verify the exported foreground](VIDEO-BACKGROUND-REMOVAL.md), with a [trial and delivery worksheet](BACKGROUND-REMOVAL-WORKSHEET.md) |

The examples and sample prompts are editing guidance. Where a guide labels a timing map as fictional, use it to understand the method and replace its timestamps with verified times from your own recording. Do not treat a worked example as proof that your requested edit succeeded.

## Inspect evidence before choosing a workflow

| Question | Public material | What it establishes |
| --- | --- | --- |
| Can I compare two real caption treatments on spoken footage? | [Recorded caption-style revision](CAPTION-STYLE-EXAMPLE.md) | Downloadable previews and full-resolution export, identical decoded audio between previews, observed branding and disclosed limitations. |
| Can I see translated captions with the original recording preserved? | [Recorded Spanish-caption example](SUBTITLE-TRANSLATION-EXAMPLE.md) | Supplied Spanish text, rendered artifacts, matching comparison-preview audio and an explicit export revision. |
| Can I inspect an actual MCP edit and focused revision? | [Recorded MCP run](MCP-RECORDED-EDIT.md) | Downloadable source, previews and final MP4; measured durations and inspected cut boundaries from one silent sample. |
| Can I inspect a browser-generated freeze frame? | [Freeze-frame before-and-after](FREEZE-FRAME-EXAMPLE.md) | Original source, unchanged WebM, file measurements and sampled frames from a manual browser edit. |
| Does a browser color preset reach the downloaded file? | [Color-grade before-and-after](COLOR-GRADE-EXAMPLE.md) | B&W settings, original MP4, unchanged WebM, sampled images and the observed frame-count difference. |
| How should I compare editors on the same task? | [Edit-and-revise evaluation kit](EDITOR-EVALUATION.md) | A repeatable brief and blank scorecard, rather than a completed competitive benchmark. |
| How can I compare caption revisions on the same spoken recording? | [Shared speech trial and blank results worksheet](SPEECH-EDITOR-TRIAL.md) | One licensed source, three reusable briefs and separate checks for captions, audio preservation and exported delivery. |
| Which AI editor fits footage I already recorded? | [Video editing agent guide](VIDEO-EDITING-AGENTS.md) | Workflow choices, primary-source product comparisons and a shortlist method to test on your footage. |

The cut, freeze and color examples use a silent motion graphic. The caption example uses a licensed animated-film dialogue excerpt and checks audio identity between two previews. None establishes general speech-cleanup accuracy or creative quality. The browser freeze and color examples do not test AI editing. Review the source, method and limits with each artifact, then repeat the relevant task on representative footage.

When approving your own edit, identify the project, preview version and downloaded file. Check the actual result at normal playback speed; a finished render or an assistant's summary does not establish that every requested change was delivered.

## For maintainers

[Directory publishing](PUBLISHING.md) covers maintaining Valmera's MCP listings. For the hosted service endpoint, project overview and public examples, return to the [main README](../README.md).
