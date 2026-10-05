# Valmera MCP tool catalog

These are the tools listed by the live server card at https://valmera.io/.well-known/mcp/server-card.json on October 6, 2026: **143 tools**, made up of 129 editing tools in 9 groups and 14 session tools.

The catalog can change between deployments, and a tool whose backing service isn't configured is hidden from `tools/list`. Your client's own `tools/list` response is the source of truth for names and argument schemas. Human-readable descriptions are at https://valmera.io/mcp/tools.

## Reading the footage (20)

Read the transcript, words, shots, silences, audio analysis, burned-in text and frames before deciding anything.

`find_burned_text`, `find_footage`, `find_silences`, `find_song`, `find_visual_moments`, `get_audio_analysis`, `get_editorial_map`, `get_edl`, `get_kept_transcript`, `get_shots`, `get_transcript`, `get_video_info`, `get_words`, `list_assets`, `look_at`, `look_at_asset`, `read_skill`, `search_sfx`, `search_stock`, `search_transcript`

## Cutting (6)

Remove dead air, filler words and chosen passages; keep or restore ranges against the source or the edited output.

`cut_output_range`, `cut_range`, `cut_silences`, `keep_segments`, `remove_filler_words`, `restore_range`

## Captions and on-screen text (12)

Word-timed captions, styles, fixes and mutes, titles, kinetic text and text behind the subject.

`add_captions`, `add_kinetic_text`, `add_text`, `add_text_behind`, `add_title_card`, `audit_captions`, `erase_burned_text`, `remove_text`, `set_caption_fixes`, `set_caption_mutes`, `set_caption_style`, `set_text_motion`

## Framing and motion (17)

Reframe to any aspect ratio, punch-in zooms and zoom paths, speed changes, freeze frames, screen frames and cursor enhancement.

`add_aspect_shift`, `add_freeze_frame`, `add_screen_takeover`, `add_zoom`, `add_zoom_path`, `auto_reframe`, `enhance_cursor`, `remove_aspect_shift`, `remove_cursor_enhance`, `remove_screen_frame`, `remove_screen_takeover`, `remove_speed`, `remove_zoom`, `remove_zoom_path`, `set_frame`, `set_screen_frame`, `set_speed`

## Audio (20)

Music selection, fit and beat alignment, sound effects, voiceover, gain, loudness and stem separation.

`add_music`, `add_sfx`, `add_voiceover`, `add_web_sfx`, `audit_audio_mix`, `audition_sfx_candidates`, `beat_align_cuts`, `extract_audio`, `fetch_sfx`, `move_sfx`, `remove_music`, `remove_sfx`, `remove_voiceover`, `review_audio`, `separate_music`, `set_audio_gain`, `set_master_loudness`, `set_music_fit`, `set_volume`, `swap_music`

## Colour and finishing (8)

Color grades and looks, stylize, enhancement, fades and transitions.

`add_stylize`, `apply_look`, `enhance_video`, `remove_stylize`, `set_color_grade`, `set_fades`, `set_grade_custom`, `set_transitions`

## Media, generation and screen capture (13)

Insert clips, overlays and stock media, fetch URLs, and record or showcase a website demo.

`add_overlay`, `add_stock_media`, `fetch_url`, `insert_media`, `move_insert`, `move_overlay`, `record_website`, `record_website_demo`, `remove_insert`, `remove_overlay`, `set_insert_window`, `set_overlay_motion`, `showcase_demo`

## Repair and censoring (6)

Blur or erase regions and cover problem frames.

`add_color_screen`, `add_corrupt_screen`, `blur_region`, `erase_region`, `remove_blur`, `remove_erase`

## Editing (27)

Batch edits, shorts, b-roll research, emphasis, editorial graphics, typography scenes, panels and previews.

`add_custom_filter`, `add_vector_graphic`, `apply_edit_batch`, `ask_user`, `bind_motion_motif`, `compare_uploaded_media`, `compose_panels`, `expand_toolset`, `justify_verification_findings`, `make_shorts`, `open_visual_page`, `punch_in_on_emphasis`, `remove_custom_filter`, `remove_editorial_graphic`, `remove_picture_card`, `remove_stem_mix`, `remove_typography_scene`, `remove_vector_graphic`, `render_preview`, `research_broll`, `reset_edit`, `set_editorial_graphic`, `set_picture_card`, `set_typography_scene`, `set_vector_graphic`, `start_media_sequence`, `suggest_emphasis`

## Session tools (14)

Projects, uploads, indexing status, jobs, shorts, previews, final export and download links: the parts of Studio a headless caller needs.

`apply_short_edit_batches`, `create_project`, `download_url`, `export_final`, `index_status`, `list_projects`, `open_project`, `open_short`, `project_state`, `shorts_status`, `upload_finish`, `upload_start`, `wait_for_job`, `watch_video`

## Not supported

The server card lists these explicitly:

- delegating edits to Valmera's in-house agent
- text-to-video generation of a whole video
- SRT/VTT import or export (captions are burned in)
- team seats or collaboration
- direct publishing to YouTube or TikTok
- custom font uploads
- true crossfade/dissolve transitions
- motion-tracked overlays or stickers
- denoise / studio sound
- AI music generation
