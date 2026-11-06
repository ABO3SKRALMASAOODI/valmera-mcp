# Valmera MCP tools: find the right operation for your video edit

Use Valmera's tools to work on footage you already recorded: inspect the source, shape the edit, review a rendered version and export the approved result. The assistant chooses operations from the tools available to its connection.

**Start here:** [connect your assistant](https://valmera.io/mcp/setup) · [live tool reference](https://valmera.io/mcp/tools) · [public server card](https://valmera.io/.well-known/mcp/server-card.json)

The public card was checked on **November 7, 2026**. It described 217 tools: 203 editing tools across nine groups and 14 session tools. This is a dated observation, not a permanent catalog or proof that every operation succeeds for every account.

## Discover tools before planning the edit

Your authenticated client's `tools/list` response is authoritative for the tools and input schemas available to that connection. The public server card helps you discover the published catalog without sharing credentials. Project state, media, permissions and configured services still matter.

Refresh discovery after reconnecting or when an expected tool is missing. Read the current argument schema before constructing a call. Do not invent arguments from a tool name or treat this guide's examples as a complete inventory.

For example, the current public schema for `export_final` requires both `project_id` and `edl_version`: a project selected for navigation is not a substitute for an explicit export target. Record the reviewed version before requesting the final file.

## Choose tools by the result you want

These are representative names present in the checked card. Follow their current descriptions and schemas for behavior and supported settings.

| Editing job | Useful starting points | What to establish before applying changes |
| --- | --- | --- |
| Find the right spoken passage | `get_transcript`, `get_words`, `search_transcript`, `get_kept_transcript` | Identify the passage in the source and distinguish it from the currently kept edit |
| Understand the footage visually | `get_video_info`, `get_shots`, `find_visual_moments`, `look_at` | Inspect the relevant frames and what must remain visible |
| Cut a passage or tighten pacing | `cut_range`, `cut_output_range`, `keep_segments`, `cut_silences`, `remove_filler_words`, `restore_range` | Name the timing basis and preserve complete meaning, speech and necessary pauses |
| Add or revise captions | `add_captions`, `set_caption_style`, `set_caption_fixes`, `audit_captions` | Separate spelling corrections, caption appearance and changes to the spoken recording |
| Reframe for a new format | `auto_reframe`, `set_frame`, `add_aspect_shift`, `deliver_aspects` | Specify the output format, subject and text or demonstrations that must stay readable |
| Shape music and sound | `list_music_library`, `add_library_music`, `add_music`, `add_sfx`, `set_master_loudness`, `audit_audio_mix` | Identify the intended assets and balance them against speech in the preview |
| Add supporting visuals or a demo | `research_broll`, `source_broll`, `insert_media`, `add_overlay`, `record_website_demo` | State the source material, placement and visible outcome; inspect captured actions |
| Build typography and motion | `add_typeset`, `add_motion_graphic`, `compose_panels`, `import_font`, `audit_motion` | Define the visual treatment and test a representative passage before expanding it |
| Adjust color or a region | `set_color_grade`, `match_grade`, `set_grade_window`, `blur_region`, `erase_region` | Identify the affected shot or region and what should remain unchanged |
| Create short versions | `make_shorts`, `shorts_status`, `open_short`, `apply_short_edit_batches` | Track each child project's identity and version separately |
| Review and deliver | `render_preview`, `wait_for_job`, `watch_video`, `export_final`, `download_url` | Distinguish an edit saved, a preview rendered and a downloadable final file |

The broader creative workflow is covered in [creative media and generated visuals](https://valmera.io/docs/ai-generation). Ask for the required result and let the current catalog determine the available route; the presence or absence of a name in this short table does not establish a product-wide capability limit.

## From a connected account to a reviewed file

1. **Identify the project.** Use `list_projects` and inspect the intended project with `open_project` or `project_state`. Keep its explicit identifier with subsequent requests. An empty project list is different from a failed connection.
2. **Prepare the media.** Upload through Studio, or follow `upload_start` and `upload_finish` from a client that can send the file. Use `index_status` to check when the source analysis is ready. See [file uploads](https://valmera.io/docs/file-uploads).
3. **Agree on the edit.** Read the transcript and relevant frames. Name the desired output, required content, source ranges and parts that should stay unchanged. Use the available tools to make a versioned edit.
4. **Review the preview.** Request a representative rendered preview, follow any job identifier until a terminal result, and inspect the actual output. Listen to speech and joins; check captions, framing and visible claims.
5. **Export the reviewed version.** Supply the project and version required by the current export schema. A queued or running response is pending work. After completion, obtain the download link and open the resulting file.

The live card describes versioned edit decisions that preserve the uploaded original. It also states that simultaneous Studio and MCP editing of the same project is refused. Respect that project lock and resolve which editor is active before continuing.

## Three briefs to adapt

For a worked timing map and caption corrections after a cut, see [Fix AI captions after cuts](CAPTION-REVISIONS.md). It covers one-word revisions, cues that cross removed footage, and matching subtitle files to the final export.

Replace the bracketed fields with the project and version returned by your connection. These are requests for an assistant to interpret, not literal API payloads.

**Transcript-led rough cut**

> In project [project ID], inspect version [version] and the source transcript. Propose a shorter explanation of [topic]. Keep the complete claim, its qualifications and the visible demonstration. List proposed source ranges before applying them. After approval, render a preview and report the new version and any unresolved review issues.

**A caption correction without a new cut**

> In project [project ID], version [version], correct the caption spelling of [name] in the passage beginning [quoted words]. Keep the spoken recording, cuts, framing and duration unchanged. Discover the available caption-correction tool, apply the scoped change, then show a preview where I can check it.

**A focused visual revision**

> In project [project ID], version [version], improve the readability of [specific title or demonstration] during [identified passage]. Keep the story and spoken audio unchanged. Explain the proposed visual treatment, test it on that passage and show the rendered preview before extending it.

## Missing tools, pending jobs and explicit exclusions

A missing tool does not by itself prove that Valmera cannot perform the underlying task. Check current discovery and account requirements; the public card states that tools with unconfigured backing services are hidden. Use the [connection troubleshooting guide](CONNECTION-TROUBLESHOOTING.md) for sign-in, missing-tool and transport checks.

Conversely, a listed name is not proof of a completed edit. Inspect the result and report unresolved work accurately. If a job remains running, continue observing that job instead of repeating the mutation merely because a wait returned.

On November 7, the public card's only explicit `notSupported` entry was **delegating edits to Valmera's in-house agent**. Connected assistants use the direct editing tools. Older documentation's broader exclusion list is not the current card. Removal of an old exclusion is not a promise that every conceivable request is supported; consult current schemas and verify the requested output.

## Continue with your footage

- [Creator workflow briefs](CREATOR-WORKFLOWS.md): choose a practical first edit.
- [Webinar replay and clips](WEBINARS.md): preserve source, replay and clip timing.
- [Website demos](WEBSITE-DEMO.md): inspect capture actions and the final result.
- [Edit-and-revise evaluation kit](EDITOR-EVALUATION.md): compare tools with the same footage and evidence.
- [Current plans](https://valmera.io/subscribe): account creation and upload are free; editing requires a subscription. Your assistant provider's billing is separate.
