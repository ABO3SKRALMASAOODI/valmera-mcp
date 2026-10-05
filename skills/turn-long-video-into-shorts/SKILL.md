---
name: turn-long-video-into-shorts
description: Turn a long video, podcast, interview, webinar or livestream into vertical shorts for TikTok, Instagram Reels and YouTube Shorts with the Valmera connector. Use when the user asks for clips, shorts, highlights, viral moments or a highlight reel from a longer recording.
---

# Turn a long video into shorts with Valmera

Valmera can split one long recording into several short projects. Each one is a complete, self-contained story with its own reframing and captions, and each can be refined and exported separately.

## Workflow

1. **Set up the source.** For a podcast or long interview, create a shorts project with `create_project` and `kind="shorts"`, then upload into it. For an existing project, open it with `open_project`. Wait for `index_status` to report done.
2. **Read the whole conversation first.** Use `get_transcript`, which has speaker labels, plus `get_editorial_map` and `find_visual_moments` for visual beats. Pick stories that:
   - start with a hook that makes sense without context in the first two seconds,
   - finish their thought; never cut mid-argument,
   - fit the length the user asked for (often 30–60 seconds).
3. **Propose before you cut** when the user hasn't chosen moments. List each candidate with its source start and end time, a working title, and one line on why it works.
4. **Create the shorts.** Call `make_shorts` with your chosen story arcs. Track progress with `shorts_status`, and open each short with `open_short`.
5. **Polish each short.** Reframe to 9:16 so the speaker stays in frame (`auto_reframe`, with `compose_panels` when two people matter). Add captions with an active-word highlight, a title card or hook text, and punch-ins on key lines. `apply_short_edit_batches` applies the same kinds of edits to up to 30 shorts in one call.
6. **Review.** Render a preview of each short (`render_preview`, `wait_for_job`) and check its opening frame, captions and framing with `look_at` and `rendered=true`.
7. **Export when asked.** For each approved short, call `export_final`, then `wait_for_job`, then `download_url` with `kind="final"`.

## Be honest about virality

No tool can guarantee a clip goes viral. Say that you picked complete, hook-first stories from the transcript and visuals, and suggest the user test several.

## Limits

- Each short is exported separately. There's no direct posting to social platforms.
- Reframing picks crop positions section by section, so check fast camera moves in the preview.
- Editing requires a Valmera subscription (https://valmera.io/subscribe).
