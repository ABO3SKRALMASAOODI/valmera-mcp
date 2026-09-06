# Valmera MCP server — AI video editing for your own footage

Valmera is a hosted AI video editor for footage you have already recorded. Its Model Context Protocol (MCP) server lets an authorized AI assistant inspect a recording, cut pauses and filler words, add captions, mix music, reframe the picture, and render a review preview. You can revise the same project through conversation. **The user starts the final MP4 export in Valmera Studio; MCP cannot create final exports.**

This repository contains public documentation and directory manifests. It does not contain a self-hostable edition of the Valmera service.

## Connection details

| Field | Value |
| --- | --- |
| Remote endpoint | `https://entrepreneur-bot-backend.onrender.com/mcp` |
| Transport | Streamable HTTP |
| Authentication | OAuth with dynamic client registration and PKCE (S256), or a Valmera MCP bearer token |
| Account | A Valmera account authorized to use MCP; editing requires an active subscription |
| Setup guide | [Connect an MCP client](https://valmera.io/mcp/setup) |
| Tool reference | [Valmera MCP tools](https://valmera.io/mcp/tools) |
| Public capability discovery | [Live server card](https://entrepreneur-bot-backend.onrender.com/.well-known/mcp/server-card.json) |

The live server card reported **134 tools on September 5, 2026: 122 editing tools and 12 session tools**. This is a dated observation, not a fixed product limit. The enabled catalog changes with deployment configuration. Read your connection's `tools/list` response for available names, arguments and constraints.

## What can an agent edit?

| Editing task | Representative tools |
| --- | --- |
| Read the footage and current project | `project_state`, `get_video_info`, `get_transcript`, `get_words`, `look_at` |
| Cut pauses, filler words or selected passages | `cut_silences`, `remove_filler_words`, `cut_range`, `cut_output_range`, `keep_segments` |
| Restore a removed passage | `restore_range` |
| Add and correct burned-in captions | `add_captions`, `set_caption_style`, `set_caption_fixes`, `set_caption_mutes` |
| Reframe for vertical or square delivery | `auto_reframe`, `set_frame` |
| Add on-screen text, logos and other media | `add_text`, `add_title_card`, `add_overlay`, `insert_media` |
| Add music and adjust the mix | `add_music`, `set_volume`, `set_audio_gain`, `set_master_loudness` |
| Grade the picture and add motion | `set_color_grade`, `set_grade_custom`, `add_zoom`, `set_speed` |
| Render and inspect a review preview | `render_preview`, `wait_for_job`, `watch_video`, `look_at` |

These are examples, not the entire tool catalog. A tool's presence does not guarantee that every source file, requested effect or connected client will work. Follow its returned schema and errors, then review the rendered result.

## Quickstart

### Connect your client

Use an MCP client that supports remote Streamable HTTP and Valmera's authentication flow. Add the endpoint above as a remote connector, complete Valmera's sign-in and consent flow, and ask the assistant to list your Valmera projects. An empty project list is a valid first connection result.

For Claude Code:

```sh
claude mcp add --transport http valmera https://entrepreneur-bot-backend.onrender.com/mcp
```

Use `/mcp` in Claude Code to authenticate. See the [Claude setup guide](https://valmera.io/mcp/claude) for the current walkthrough. Other clients have their own account, connector and action-approval requirements. Protocol compatibility alone does not establish end-to-end compatibility with every client.

If your client supports bearer authentication instead, create a token through [Valmera's MCP page](https://valmera.io/mcp) and configure the `Authorization: Bearer <your-token>` header using the client's credential settings. Keep real tokens out of public configuration examples, repositories and chat transcripts.

### Open footage

The simplest upload path is to upload your file in [Valmera Studio](https://valmera.io), let indexing finish, and ask your connected assistant to list and open that project. The web upload limit is 14 GB or three hours, with MP4, MOV, MKV and WebM supported. Consult [file upload documentation](https://valmera.io/docs/file-uploads) for current limits.

Clients that can transfer files can also use `upload_start` and `upload_finish`. Media bytes move through the returned upload mechanism, not inside an MCP JSON argument. Follow the live tool's upload instructions; a chat-only client may need you to perform the upload in Studio. Use `index_status` to check that analysis has completed before requesting edits against transcript timestamps.

### Request a first edit

An example request for a talking-head recording:

> Open my uploaded interview project. Read the transcript and inspect representative frames. Remove obvious dead air and filler words while keeping natural pauses and complete sentences. Keep the meaning and order of the answers. Add readable captions, correct names only when I provide the spelling, and render a review preview. Report which changes completed and anything that needs my review.

After watching the preview, request a focused revision:

> Restore the pause before the final answer. Keep the rest of the edit. Make the captions smaller and render another review preview.

These are example instructions, not a measured case study or a promise of a particular runtime reduction. The agent should report actual tool results. It should inspect output frames and use available audio review tools before describing work as verified.

### Review and export

Watch the preview for cut boundaries, caption spelling, framing and music levels. Previews use a faster proxy, so they are not the final quality reference. Slow jobs return a job identifier; wait for a terminal result instead of assuming that submission means completion.

When the edit is ready, open the project in Studio and start the final export yourself. Valmera renders the final H.264 MP4 from the original upload. Paid exports have no watermark over your footage, but **every export ends with a brief Valmera end card, approximately 2.5 seconds long**. See [export documentation](https://valmera.io/docs/publishing).

For a more detailed walkthrough, see [the agent editing workflow](docs/WORKFLOW.md).

## How the workflow works

The assistant reads project information, transcript timings and selected frames, then calls editing tools. Those tools update a versioned edit decision list. The renderer turns those decisions into a preview; the original upload remains unchanged. Cuts can be restored.

The MCP catalog reuses the editor's tool definitions, adds project/session operations, hides unconfigured capabilities and excludes operations that are not allowed over MCP. Final-export creation and delegation to Valmera's in-house editing agent are excluded. It is not an identical copy of the Studio agent's complete surface.

Editing the same project from Studio and MCP simultaneously is refused. Finish the current editing operation before switching control between them.

## Pricing and access

Account creation and uploads are free. **AI editing requires a subscription.** There is no current offer of 50 signup credits or a three-day editing trial.

Monthly plans verified on September 5, 2026:

| Plan | Monthly price in USD | Credits per month |
| --- | ---: | ---: |
| Creator | $15 | 1,000 |
| Pro | $30 | 2,000 |
| Frontier | $50 | 5,000 |

Editing work consumes credits. Refer to the [live Plans page](https://valmera.io/subscribe) for current billing terms, included credits and annual options. A separate MCP client may have its own subscription or usage charges.

## Limits to consider before choosing Valmera

Valmera fits workflows where you have source footage, want an assistant to carry out edits, and can review the result before final delivery. It supports work on recordings such as interviews, podcasts, tutorials and product demonstrations.

The current server card explicitly lists these limitations:

- MCP cannot start final exports or delegate work to Valmera's in-house agent.
- Captions are burned into the picture; SRT/VTT import and export are not supported.
- Team seats, collaboration and direct publishing to YouTube or TikTok are not supported.
- True crossfade/dissolve transitions, motion-tracked overlays and custom font uploads are not supported.
- Audio denoise or “studio sound” and AI music generation are not supported.
- Generating a whole video from a text prompt is outside this workflow.

English is the best-tested transcription path. Review names, specialist terms, accents and noisy passages. For the current enabled surface and additional restrictions, consult the [server card](https://entrepreneur-bot-backend.onrender.com/.well-known/mcp/server-card.json), [tool reference](https://valmera.io/mcp/tools) and the tool schemas returned to your client.

## Common questions

**Can Claude edit my recorded video with Valmera?**

A connected, authorized Claude client can use Valmera's editing tools to work on uploaded footage and render review previews. Final delivery is a user action in Studio. The [Claude guide](https://valmera.io/mcp/claude) explains setup.

**Can I use it with ChatGPT or another assistant?**

The client must expose remote MCP connections and support the required authentication and actions. Client availability and account policies vary. See [ChatGPT connection guidance](https://valmera.io/mcp/chatgpt) and [other client setup instructions](https://valmera.io/mcp/setup). Do not assume that a client can upload local files or inspect returned media merely because it can list tools.

**Does the assistant see the footage?**

Tools can return transcript text, analysis and requested video frames to the connected assistant. What the assistant can inspect depends on the tools it calls and the client's support for returned content. Review the [privacy policy](https://valmera.io/legal#privacy) and your MCP client's data practices before connecting sensitive footage.

**Is Valmera free to edit with?**

Account creation and uploads are free; editing requires a subscription. The current entry monthly plan is Creator at $15. Check [current pricing](https://valmera.io/subscribe) before subscribing.

**Is this an open-source video editor?**

This repository's documentation is MIT licensed. The hosted commercial service is governed by [Valmera's legal terms](https://valmera.io/legal); the video editor is not distributed here for self-hosting.

## Links

- [Valmera product](https://valmera.io)
- [Getting started in Studio](https://valmera.io/docs/getting-started)
- [MCP setup](https://valmera.io/mcp/setup)
- [MCP tool reference](https://valmera.io/mcp/tools)
- [Machine-readable product summary](https://valmera.io/llms.txt)
- [Maintaining directory listings](docs/PUBLISHING.md)

Report documentation errors and tool issues in this repository's issue tracker.

## License

Note: this license covers the documentation and manifests in this repository.
The Valmera service itself is a hosted commercial product governed by the terms
at https://valmera.io/legal.
