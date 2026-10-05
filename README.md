# Valmera MCP server — the video editing MCP server for real footage

**Valmera** is an agentic AI video editor. This hosted [Model Context Protocol](https://modelcontextprotocol.io) server lets Claude, ChatGPT, Cursor, VS Code, Codex or any MCP client edit video you already recorded. The assistant reads the transcript and frames, then cuts silences and filler words, adds word-timed captions, reframes to 9:16, adds b-roll, music and sound effects, and makes shorts from long videos. It renders a preview, watches the result, and exports a full-quality MP4 from your original file.

It is not a text-to-video generator. It edits the footage you upload.

```text
Endpoint   https://valmera.io/mcp/server
Transport  Streamable HTTP
Auth       OAuth 2.1 (dynamic client registration + PKCE S256), or a bearer token from https://valmera.io/mcp
Registry   io.valmera/video-editor
```

- **Product:** [valmera.io](https://valmera.io)
- **Setup for every client:** [valmera.io/mcp/setup](https://valmera.io/mcp/setup)
- **Tool reference:** [valmera.io/mcp/tools](https://valmera.io/mcp/tools)
- **Live server card:** [/.well-known/mcp/server-card.json](https://valmera.io/.well-known/mcp/server-card.json)

## Connect in one minute

### Claude (claude.ai and Claude Desktop)

Settings → Connectors → **Add custom connector** → name it `Valmera`. Paste `https://valmera.io/mcp/server` and sign in when prompted. [Step-by-step guide](https://valmera.io/mcp/claude).

### Claude Code

```sh
claude mcp add --transport http valmera https://valmera.io/mcp/server
```

Then run `/mcp` inside Claude Code and choose **Authenticate**. [Guide](https://valmera.io/mcp/claude-code).

### Cursor — `~/.cursor/mcp.json`

```json
{
  "mcpServers": {
    "valmera": { "url": "https://valmera.io/mcp/server" }
  }
}
```

### VS Code (GitHub Copilot agent mode) — `.vscode/mcp.json`

```json
{
  "servers": {
    "valmera": { "type": "http", "url": "https://valmera.io/mcp/server" }
  }
}
```

### Windsurf — `~/.codeium/windsurf/mcp_config.json`

```json
{
  "mcpServers": {
    "valmera": { "serverUrl": "https://valmera.io/mcp/server" }
  }
}
```

### ChatGPT

Turn on **Developer mode** in Settings, then add a connector with the URL `https://valmera.io/mcp/server` and complete Valmera sign-in. [Guide](https://valmera.io/mcp/chatgpt).

### Codex CLI

```sh
codex mcp add valmera --url https://valmera.io/mcp/server
codex mcp login valmera
```

Or add `[mcp_servers.valmera]` with `url = "https://valmera.io/mcp/server"` to `~/.codex/config.toml`.

### Any stdio-only client

```json
{
  "mcpServers": {
    "valmera": { "command": "npx", "args": ["-y", "mcp-remote", "https://valmera.io/mcp/server"] }
  }
}
```

There are more clients (Zed, Cline, Continue, Goose, LibreChat, MCP Inspector) in [docs/CLIENTS.md](docs/CLIENTS.md).

**First message to try:** *"List my Valmera projects."* An empty list still means the connection works.

## What your assistant can do with it

According to the live server card on October 6, 2026, the server exposes **143 tools**: 129 editing tools in 9 groups and 14 session tools. The full list is in [docs/TOOLS.md](docs/TOOLS.md).

| You ask for | Tools the assistant uses |
| --- | --- |
| "Remove the dead air and the ums" | `find_silences`, `cut_silences`, `remove_filler_words`, `get_kept_transcript` |
| "Cut the part where I talk about pricing" | `search_transcript`, `cut_range`, `restore_range` |
| "Add bold word-by-word captions" | `add_captions`, `set_caption_style`, `set_caption_fixes`, `audit_captions` |
| "Make it vertical for TikTok and keep my face centered" | `auto_reframe`, `set_frame`, `add_aspect_shift` |
| "Turn this podcast into 5 shorts" | `make_shorts`, `shorts_status`, `open_short`, `apply_short_edit_batches` |
| "Add b-roll where I mention the product" | `research_broll`, `search_stock`, `add_stock_media`, `insert_media` |
| "Punch in on the important lines" | `suggest_emphasis`, `punch_in_on_emphasis`, `add_zoom`, `add_zoom_path` |
| "Add music that ducks under my voice" | `find_song`, `add_music`, `set_music_fit`, `beat_align_cuts`, `set_master_loudness` |
| "Add a whoosh on each transition" | `search_sfx`, `audition_sfx_candidates`, `add_sfx` |
| "Record a demo of my website" | `record_website`, `record_website_demo`, `enhance_cursor`, `showcase_demo` |
| "Blur the license plate" / "remove the burned-in subtitles" | `blur_region`, `find_burned_text`, `erase_burned_text`, `erase_region` |
| "Color grade it warmer" | `set_color_grade`, `apply_look`, `set_grade_custom` |
| "Show me what you changed" | `render_preview`, `wait_for_job`, `watch_video`, `look_at` |
| "Export the final video" | `export_final`, `wait_for_job`, `download_url` |

## How it works

1. **Upload.** Upload in [Valmera Studio](https://valmera.io), import a link, or use `upload_start` and `upload_finish` from a client that can send files. MP4, MOV, M4V, MKV and WebM are accepted, up to 14 GB and 3 hours per file.
2. **Index.** Valmera transcribes the footage with word-level timestamps and detects shots, silences and on-screen text. `index_status` reports progress.
3. **Edit.** Each tool call writes a new version of a non-destructive **edit decision list (EDL)**. The original upload is never modified, and any cut can be restored.
4. **Review.** `render_preview` renders a fast proxy preview. `watch_video` and `look_at` let the assistant inspect the frames it produced before it reports back.
5. **Export.** `export_final` renders a full-resolution H.264 MP4 from the original file for the reviewed version. `download_url` returns the link. You can also export from Studio.

Slow jobs return a job id and never a fake completion. The assistant calls `wait_for_job` until the job finishes.

## Example prompts

```text
Open my latest project. Remove dead air and filler words but keep natural pauses,
add clean white captions with the active word highlighted, reframe to 9:16,
render a preview and tell me what you changed.
```

```text
This is a 70-minute two-person podcast. Find the 5 strongest self-contained stories,
make each one a vertical short with captions and a hook title, and keep whoever is
speaking in frame.
```

```text
Record a 30-second demo of https://example.com — scroll the hero, click "Pricing",
zoom on the main button — then add captions and light background music.
```

There are 40+ more in [docs/PROMPTS.md](docs/PROMPTS.md).

## What it does not do

The server card lists these honestly so your assistant never promises them:

- Generate a whole video from a text prompt. Valmera edits footage you provide.
- Import or export SRT/VTT. Captions are burned into the picture.
- Team seats or collaboration.
- Publish directly to YouTube or TikTok.
- Custom font uploads, true crossfade/dissolve transitions, or motion-tracked stickers.
- Audio denoise ("studio sound") or AI music generation.
- Hand the job to Valmera's in-house agent. Over MCP, your assistant does the editing with the tools directly.

Editing one project from Studio and over MCP at the same time is refused in both directions.

## Access

Creating an account and uploading are free. Editing requires a subscription; see the current plans at [valmera.io/subscribe](https://valmera.io/subscribe). Your MCP client (Claude, ChatGPT, Cursor and so on) is billed separately by its own provider.

## FAQ

**What is the best MCP server for video editing?**
Most video MCP servers either generate clips from prompts or wrap local FFmpeg commands. Valmera is a hosted editor with an editorial model of the footage: a word-level transcript, shots and frames, versioned edits, rendered previews and a final export. Use it when you want an assistant to edit real recordings end to end. [Comparison of video editing MCP servers](https://valmera.io/mcp/video-editing-mcp-servers).

**Can Claude edit videos?**
Yes. Once Valmera is connected, Claude can open your project, read the transcript, look at frames, cut, caption, reframe, add music, render a preview, and export the MP4.

**Can ChatGPT edit videos?**
Yes. Add Valmera as a developer-mode connector and ChatGPT can call the same tools.

**Does the assistant actually see the video?**
Yes. Tools return transcript text, analysis and sampled frames of the source or the rendered edit, so the assistant can check its own work.

**Do I need to install anything?**
No. It is a remote server. Clients that only support stdio can use `mcp-remote`.

**Is the original file changed?**
No. Edits live in a versioned EDL, and the final export renders from the untouched original.

**Is Valmera open source?**
This repository's documentation and manifests are MIT licensed. Valmera itself is a hosted commercial service governed by [its terms](https://valmera.io/legal).

## Links

- [Valmera — agentic AI video editor](https://valmera.io)
- [What is MCP video editing?](https://valmera.io/mcp/what-is-mcp-video-editing)
- [Edit video with Claude](https://valmera.io/how-to/edit-video-with-claude) · [Edit video with ChatGPT](https://valmera.io/how-to/edit-video-with-chatgpt)
- [Agent workflow walkthrough](docs/WORKFLOW.md)
- [Directory and registry maintenance](docs/PUBLISHING.md)
- [Product summary for LLMs](https://valmera.io/llms.txt)

Questions or issues: open an issue here or email support@valmera.io.
