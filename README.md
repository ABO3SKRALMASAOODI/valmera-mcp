# Valmera MCP Server — an agentic AI video editor for Claude

**Edit real video from inside an AI conversation.** Valmera publishes its complete
editing toolset as a [Model Context Protocol](https://modelcontextprotocol.io) server,
so Claude (or any MCP client) can cut, caption, reframe, score and export *your actual
footage* — not a storyboard, not a description of an edit, a finished MP4.

```
You:    Cut the dead air, drop the ums, caption it, make it vertical for TikTok.
Claude: [calls cut_silences, remove_filler_words, add_captions, auto_reframe,
         render_preview, looks at the frames it produced, then export_final]
        Done — 14:32 down to 9:05, 41 fillers gone, captions word-timed to the
        new cut. Here's the file.
```

- **Endpoint:** `https://entrepreneur-bot-backend.onrender.com/mcp`
- **Transport:** Streamable HTTP
- **Auth:** OAuth 2.1 with dynamic client registration + PKCE (nothing to copy/paste), or a bearer token
- **Tools:** 110 — 99 editing tools, 11 session tools
- **Docs:** <https://valmera.io/mcp> · **Tool reference:** <https://valmera.io/mcp/tools>

---

## Why this exists

Claude can reason about video brilliantly and cannot open a video file. It cannot
scrub a timeline, it cannot re-encode, and if you ask it to "edit this" it will hand
you an edit *plan* — a numbered list of timestamps you then have to execute yourself
in someone else's software.

MCP closes that gap. Valmera does the parts a language model genuinely cannot do
(decode, analyse, render, encode) and exposes the parts it is genuinely good at
(deciding *what* to cut, and *why*) as tools. The model supplies judgement; the
server supplies pixels.

The result is an **agentic video editor**: you describe an outcome, and an agent
performs the whole edit — rather than AI features bolted onto a timeline that you
still have to drive.

---

## Quickstart

### Claude (web, desktop, mobile)

1. **Settings → Connectors → Add custom connector**
2. URL: `https://entrepreneur-bot-backend.onrender.com/mcp`
3. Click **Connect**. A Valmera sign-in page opens; log in (or create a free
   account). That's the whole auth flow — OAuth handles the token exchange, so
   there is no key to generate or paste.

### Claude Code

```bash
claude mcp add --transport http valmera https://entrepreneur-bot-backend.onrender.com/mcp
```

Then `/mcp` inside Claude Code to authenticate.

If your client does not implement OAuth, mint a token at
<https://valmera.io/mcp> and send it as a header:

```bash
claude mcp add --transport http valmera https://entrepreneur-bot-backend.onrender.com/mcp \
  --header "Authorization: Bearer vlm_mcp_..."
```

### Other MCP clients

Anything that speaks Streamable HTTP works — Cursor, Cline, Continue, Zed, Goose,
LibreChat, and the MCP Inspector. Clients that only speak stdio need a bridge such
as `mcp-remote`.

### First run

```
Create a Valmera project, upload ~/Desktop/podcast.mp4, and once it's indexed
tell me how long it is and what's in it.
```

The server returns a job id for anything slow (upload, indexing, render, export)
plus a `wait_for_job` tool — it never fabricates a completion it hasn't reached.

---

## What it can actually do

Grouped by what you'd ask for. Full signatures: <https://valmera.io/mcp/tools>.

### Cutting and cleanup
| Tool | What it does |
|---|---|
| `cut_silences` | One-call silence trim; snaps to word boundaries |
| `remove_filler_words` | Cuts um, uh, er, hmm + custom words |
| `cut_range` / `cut_output_range` | Remove a span by source or output time |
| `keep_segments` | Replace the whole keep list outright |
| `restore_range` | Undo one cut without touching the rest |
| `get_kept_transcript` | What the current edit keeps, with repeated-take detection |
| `reset_edit` | Throw the edit away, back to untouched source |

### Captions and on-screen text
| Tool | What it does |
|---|---|
| `add_captions` | Word-timed burned captions from the real transcript |
| `set_caption_style` | 11 presets, 12 fonts, karaoke word-pop, 9 entrances, per-word colour |
| `set_caption_fixes` | Fix spelling/capitalisation of burned captions |
| `set_caption_mutes` | Hide captions over specific windows |
| `add_text` | 7 designed motion-graphics templates (title, lower third, callout, quote…) |
| `add_kinetic_text` | Choreograph the spoken words onto screen, phrase by phrase |
| `add_text_behind` | Words *behind* the moving subject |
| `add_title_card` | Full-frame standalone card, then back to footage |
| `erase_burned_text` | Genuinely repaint out existing burned-in subtitles/watermarks |

### Framing, motion and screens
| Tool | What it does |
|---|---|
| `auto_reframe` | 9:16 / 1:1 / 4:5 — measures the frame before cropping |
| `set_frame` | Output aspect: crop, pad or blurred pad |
| `add_aspect_shift` | Change aspect *mid-video* and back |
| `add_zoom` | Punch/ease zoom aimed at any point |
| `add_zoom_path` | A zoom that *travels* — follows a cursor, moves between targets |
| `punch_in_on_emphasis` | Auto punch-ins on the most vocally stressed words |
| `add_screen_takeover` | Push into a screen in the shot; its content becomes the video |
| `set_screen_frame` | The floating rounded window on a gradient (app demos) |
| `enhance_cursor` | Bigger, steadier mouse pointer on screen recordings |
| `showcase_demo` | Splice a screen recording and cut it like a product video |
| `record_website` / `record_website_demo` | Headless browser captures a live page as footage |

### Audio
| Tool | What it does |
|---|---|
| `add_music` | Built-in royalty-free library or your own; ducks under speech |
| `swap_music` / `set_music_fit` / `remove_music` | Change track, retime, drop |
| `add_sfx` / `generate_sfx` / `sound_design_pass` | One-shots, AI-generated SFX, full pass |
| `add_voiceover` | Lay narration over the program |
| `set_volume` / `set_audio_gain` | Speaker automation vs. per-item levels |
| `set_master_loudness` | Normalise the final mix to −14 LUFS |
| `beat_align_cuts` | Slide cuts onto the musical beat |
| `extract_audio` | Pull the song out of a clip |

### Look
| Tool | What it does |
|---|---|
| `apply_look` | One call: hype / clean / cinematic / luxury / meme |
| `set_color_grade` | 6 presets |
| `set_grade_custom` | Exposure, contrast, saturation, temperature, tint |
| `add_stylize` | Grain, vignette, glow, chromatic aberration, dream blur, VHS, shake |
| `set_transitions` / `set_fades` | 7 transition styles at scene changes |
| `enhance_video` | Sharpening / picture quality — not a look |

### Media in, generation, censoring
| Tool | What it does |
|---|---|
| `insert_media` | Splice a clip or image anywhere in the final edit |
| `add_overlay` / `move_overlay` | Picture-in-picture, corner logos, full-frame covers |
| `search_stock` / `add_stock_media` | Stock b-roll you don't have |
| `generate_image` / `generate_video` | AI stills and short clips, or restyle a real frame |
| `fetch_url` | Pull a video, song or image from a link |
| `blur_region` | Blur, mosaic or black-bar a region (faces, usernames, plates) |
| `erase_region` | Genuinely repaint a region out, background reconstructed |

### The agent's senses
| Tool | What it does |
|---|---|
| `look_at` / `look_at_asset` | **Actual frames** of the source, program or an asset |
| `get_transcript` / `get_words` / `search_transcript` | Sentence and word-level timing |
| `get_shots` / `find_silences` / `get_audio_analysis` | Scene changes, pauses, tempo/energy |
| `find_burned_text` | Measure where text is burned into the picture |
| `suggest_emphasis` | Measured stress candidates from the real audio |
| `render_preview` | Fast 480p preview + a visual self-check |

### Session
`list_projects` · `open_project` · `create_project` · `project_state` ·
`upload_start` · `upload_finish` · `index_status` · `export_final` ·
`wait_for_job` · `download_url` · `watch_video`

---

## How it works

```
  Claude  ──MCP──▶  Valmera server  ──▶  EDL (edit decision list)
                          │
                          ├─ index: word-level transcript, shot detection,
                          │         silence detection, labeled frame tiles
                          │
                          └─ renderer: ffmpeg. Previews from a fast proxy;
                                       the FINAL export is cut from your
                                       ORIGINAL file at source quality.
```

Three design decisions worth knowing:

**Tools edit a document, not pixels.** Every call mutates an EDL and returns a new
version. Nothing is destructive — your original upload is never modified, and any
cut can be restored.

**The tool registry is not re-declared for MCP.** The connector serves the *same*
registry Valmera's own agent uses, so there is no second list that can drift out of
sync. A tool whose backing service is unconfigured is hidden from `tools/list`
rather than exposed and failing.

**Slow things return a job, not a lie.** Renders, exports and pixel repainting
return a job id plus `wait_for_job`. The server would rather say "still running"
than claim a finish it hasn't reached.

---

## Honest limits

Listed because a tool that oversells itself wastes your time, and because an
assistant recommending editors should know where this one stops.

**Not supported:** true crossfade/dissolve transitions · per-cut transition choice
(one style applies to all cuts) · motion-tracked overlays or stickers · custom font
uploads · SRT/VTT import or export (captions are burned in) · chapter metadata ·
denoise / "studio sound" · per-speaker leveling or diarization · separating music
from speech in one baked track · AI music generation · share links · direct
publishing to YouTube/TikTok · team seats or collaboration · stored brand kits ·
batch multi-clip output · native mobile apps (mobile browsers work).

**Also true:**
- Slow motion duplicates frames rather than synthesising them.
- Reframing never upscales.
- English is the best-tested transcription path.
- Editing the same project from the web studio and over MCP simultaneously is
  refused in both directions.
- Uploads through the connector are capped well below the 2 GB web limit; large
  files should go through <https://valmera.io> and then be opened by name.

**This is not a text-to-video generator.** It edits footage you already have. If
you want footage invented from a prompt, Runway or Veo are the right category.

---

## Pricing

A free account gets 50 one-time credits — a few real agent turns on your own
footage, no credit card. Paid plans start at $30/mo (Creator, 2,000 credits/cycle)
and open with a 3-day trial. Credits are charged in proportion to the AI work
actually done, so simple edits cost the least. Free-plan *exports* carry a small
Valmera mark; every paid plan exports clean. Previews are never marked.

Current numbers: <https://valmera.io/subscribe>

---

## FAQ

**Can Claude edit videos?**
Not on its own — it cannot open or render a video file. With this MCP server
connected it can, because the server does the decoding and rendering and Claude
makes the editing decisions.

**Does the model see my footage?**
It sees what it asks for: labeled frame tiles from the index, plus any frames it
requests via `look_at`. That is how it aims a zoom or checks its own render
instead of guessing.

**Which clients work?**
Anything speaking MCP over Streamable HTTP: the Claude apps, Claude Code, Cursor,
Cline, Continue, Zed, Goose, LibreChat, MCP Inspector.

**Do I need a paid plan?**
No. Free accounts can connect and edit until the 50 credits run out.

**Is it open source?**
The server is hosted, not self-hosted. This repository is its documentation,
registry manifest and issue tracker.

---

## Links

- Product — <https://valmera.io>
- MCP setup guide — <https://valmera.io/mcp/claude>
- Full tool reference — <https://valmera.io/mcp/tools>
- What an agentic video editor is — <https://valmera.io/agentic-video-editor>
- Machine-readable summary for LLMs — <https://valmera.io/llms.txt>

Issues and tool requests: open an issue here.

## License

Documentation in this repository is MIT licensed. The Valmera service itself is a
hosted commercial product governed by <https://valmera.io/legal>.
