---
name: edit-video-with-valmera
description: Edit a real video with the Valmera connector. Use when the user wants footage cleaned up or polished, for example removing silences, pauses or filler words, cutting retakes, adding captions or subtitles, reframing to vertical 9:16, adding b-roll, music, sound effects, zooms or titles, color grading, blurring something, or exporting the finished MP4.
---

# Edit a video with Valmera

Valmera is a hosted AI video editor. Its connector gives you editing tools that work on footage the user uploaded to Valmera. Every edit writes a new version of a non-destructive edit decision list (EDL). The original file is never changed, and any cut can be restored.

## Workflow

1. **Find the project.** Call `list_projects`. If the user names a video, open that project with `open_project`. If there are no projects, ask the user to upload the file at https://valmera.io or, if your client can send files, use `upload_start` and `upload_finish`. A file path in the chat doesn't upload anything.
2. **Wait for analysis.** Call `index_status` until it reports done. Transcript, shots and silences aren't available before that.
3. **Read before you cut.** Use `get_transcript` or `get_words` for what was said, `find_silences` for pauses, `get_shots` for camera changes, and `look_at` to see frames at exact times. Summarize what you found when the brief is vague.
4. **Edit in focused steps.** For example:
   - Dead air and filler: `cut_silences`, `remove_filler_words`, then check `get_kept_transcript` so no sentence lost a word.
   - Retakes or tangents: `search_transcript`, then `cut_range` or `keep_segments`. `restore_range` undoes a cut.
   - Captions: `add_captions`, `set_caption_style` (size, color, position, active-word highlight), `set_caption_fixes` for names, then `audit_captions`.
   - Vertical video: `auto_reframe` to 9:16, then `look_at` with `output_times` to confirm the subject is in frame.
   - B-roll and graphics: `research_broll`, `search_stock`, `add_stock_media`, `insert_media`, `add_title_card`, `add_text`.
   - Audio: `find_song` or the user's file, then `add_music` (it ducks under speech), `search_sfx` and `add_sfx`, `set_master_loudness`.
   - Emphasis: `suggest_emphasis`, `punch_in_on_emphasis`, `add_zoom`.
5. **Render and check your own work.** Call `render_preview` with `complete=true`. Slow tools return a job id: call `wait_for_job` until it's done, and never report a job id as a finished result. Then `watch_video` or `look_at` with `rendered=true` and fix anything wrong before you report.
6. **Report clearly.** List what changed, with output times, and anything you couldn't do.
7. **Export when asked.** When the user approves the preview and asks for the file, call `export_final` with the project id and the reviewed `edl_version`. Then call `wait_for_job`, then `download_url` with `kind="final"`, and share the link.

## Good defaults

- Keep natural pauses between ideas. Remove dead air, not breathing room.
- Captions: two lines at most, readable size, placed clear of faces and on-screen text.
- Music under speech should be quiet. Let it rise only where nobody is talking.
- Make one change at a time when the user is reviewing, and always say which version you edited.

## Limits to tell the user about

- Valmera edits footage the user provides. It doesn't generate whole videos from text.
- Captions are burned in. There's no SRT/VTT import or export.
- No direct posting to YouTube or TikTok. Share the download link.
- No audio denoise or AI music generation.
- Editing requires a Valmera subscription (https://valmera.io/subscribe). Uploading and creating an account are free.
- If Studio has the same project open for editing, MCP editing is refused until Studio finishes.
