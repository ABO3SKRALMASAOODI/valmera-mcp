---
name: edit-video-with-valmera
description: Edit uploaded footage through Valmera's authenticated MCP connector, review a rendered preview, and deliver an MP4. Use for conversational cuts, captions, framing, sound and visual treatments on a chosen video project.
license: MIT
---

# Edit a video with Valmera

Valmera is a hosted AI video editor. The connected assistant calls editing tools directly; it does not delegate the edit to Valmera's in-house agent. Changes create versioned editing state and preserve the original upload.

## Connection and cost

Connect to `https://valmera.io/mcp/server` and authenticate using the [client setup guide](https://valmera.io/mcp/setup). Discover the current tools and input schemas in the connected session; the names below describe a workflow, not a permanent catalog.

Account creation and uploads are free; editing requires a paid [Valmera plan](https://valmera.io/subscribe). Before billable work, explain the intended scope and use any cost estimate exposed by the account. If an exact quote is unavailable, say so and obtain approval for a bounded preview before proceeding. Reuse an existing explicit scope and budget approval; ask again if the work would exceed it. Do not buy credits or upgrade a plan without authorization. Review a preview before an approved final export.

## Workflow

1. **Choose the project and result.** Use `list_projects` and `open_project` to identify the intended recording. Reuse the user's brief; clarify only missing decisions that materially change the edit. State the destination, aspect ratio, target duration and delivery files. For new media, use Studio or the `upload_start` → file transfer → `upload_finish` protocol. A path mentioned in chat does not upload a file.
2. **Wait for source readiness.** Follow `index_status` until analysis is ready. Read the transcript and available visual evidence before selecting cuts. `get_transcript`, `get_words`, `get_shots`, `find_silences` and `look_at` can inform the plan when available.
3. **Apply focused changes.** Select tools from the current session for the requested treatment. For example, `cut_silences` or `keep_segments` shapes the cut; `add_captions` and `set_caption_style` handle caption appearance; `auto_reframe` changes framing; audio and visual tools add supporting material. Use each returned schema instead of guessing arguments. Check that cuts preserve the speaker's meaning.
4. **Review a representative preview.** Call `render_preview`; follow its existing job with `wait_for_job`. Inspect the rendered result with `look_at` or `watch_video` as supported by the client. Check cut boundaries, readable text, framing and sound. Fix a small sample before repeating a treatment across a long recording.
5. **Report the version and clock.** Identify the project and reviewed edit version. Distinguish source timestamps from output timestamps in revision notes; a time in a shortened or reordered preview may refer to a different source moment. Describe what was verified and any unresolved requirement.
6. **Deliver the approved version.** When final export is authorized, call `export_final` with the intended `project_id` and reviewed `edl_version`, then `wait_for_job`, then `download_url` with `kind="final"`. A job ID is a receipt, not a finished video. Return the actual final link and identify the version. Verify the downloaded file when the client can inspect it; otherwise state what still needs checking.

## Requirements that change the plan

- Identify approved source files and any supporting material to supply, source or create. Use the [creative-media brief](https://valmera.io/docs/ai-generation) for new visual requirements.
- Specify caption language, names, appearance and whether delivery needs burned-in text, a subtitle file or both. Confirm the required output against current project options and the [caption guide](https://valmera.io/docs/captions).
- Name the dialogue source, music treatment and passages needing attention. Compare a sound change with the source before extending it.
- For multiple deliverables, review each aspect ratio and export version. Use the [delivery guide](https://valmera.io/docs/publishing) for destination requirements.
- Let an active Studio or MCP edit finish before editing the same project from another client. On a queued or running job, continue with its existing job ID; inspect a terminal failure before retrying.

For a worked result, see the [original motion-graphic trim-and-reframe example](https://valmera.io/examples/trim-and-reframe). It documents an actual cuts-and-crop export; it does not demonstrate every treatment above. For multiple stories from one recording, use the `turn-long-video-into-shorts` skill when installed.
