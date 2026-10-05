# Valmera video editing

You have the Valmera MCP server, a hosted AI video editor for footage the user uploads to https://valmera.io.

- Start with `list_projects`. Upload with `upload_start`/`upload_finish` or ask the user to upload in Studio, then wait for `index_status` to report done.
- Read before you edit: `get_transcript`, `get_words`, `find_silences`, `get_shots`, `look_at`.
- Edit with focused tools (`cut_silences`, `remove_filler_words`, `add_captions`, `auto_reframe`, `add_music`, `make_shorts`, ...). Every edit is a new, restorable version.
- `render_preview`, then `wait_for_job`, then `watch_video` or `look_at` with `rendered=true`. Verify the result before you report.
- When the user approves and asks for the file: `export_final`, then `wait_for_job`, then `download_url` with `kind="final"`.
- Valmera edits existing footage. It doesn't generate whole videos from text, and captions are burned in (no SRT). Editing requires a subscription.

Full workflow: https://github.com/ABO3SKRALMASAOODI/valmera-mcp/blob/main/skills/edit-video-with-valmera/SKILL.md
