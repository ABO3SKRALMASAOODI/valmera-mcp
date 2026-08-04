# Publishing Valmera to the MCP registries

Ordered by leverage. Every one of these is a place an assistant looks when a user
asks "how do I edit video with Claude" — and several are crawled far more
aggressively than valmera.io is.

---

## 1. Official MCP Registry (do this first)

The registry that `modelcontextprotocol.io` publishes and that most clients and
directories mirror.

### Namespace

`server.json` claims `io.valmera/video-editor` — the reverse-DNS form of a domain
you own. This is worth the extra step over the anonymous `io.github.<user>/...`
form: it reads as a company, not a side project, and it is the name that will
appear in every downstream mirror.

Proving it needs one DNS record on `valmera.io`:

```
Type:  TXT
Name:  _mcp-registry            (i.e. _mcp-registry.valmera.io)
Value: <the token the publisher CLI prints>
TTL:   300
```

### Publish

```bash
# install the publisher
brew install mcp-publisher      # or: go install github.com/modelcontextprotocol/registry/cmd/publisher@latest

cd valmera-mcp

# authenticate against the domain namespace (prints the TXT value to add)
mcp-publisher login dns --domain valmera.io

# after the TXT record resolves:
mcp-publisher publish
```

**Fallback if DNS is a problem:** change `name` to
`io.github.ABO3SKRALMASAOODI/valmera-mcp` and run `mcp-publisher login github`.
That authenticates off repo ownership with no DNS at all. You can migrate to the
domain namespace later.

### Verify

```bash
curl -s "https://registry.modelcontextprotocol.io/v0/servers?search=valmera" | jq
```

---

## 2. Smithery — <https://smithery.ai/new>

The most-trafficked third-party MCP directory; its listings rank well and it is a
common citation in "best MCP servers" answers. `smithery.yaml` in this repo is
ready. Connect the GitHub repo and it picks it up.

## 3. Glama — <https://glama.ai/mcp/servers>

Auto-indexes public GitHub repos containing an MCP manifest, but submitting
directly is faster. Glama assigns a quality score — the honest-limits section in
the README helps here rather than hurting.

## 4. PulseMCP — <https://www.pulsemcp.com/submit>

Hand-curated, weekly newsletter, heavily scraped by AI tooling.

## 5. mcp.so — <https://mcp.so/submit>

High-volume directory, fast approval.

## 6. MCP Market — <https://mcpmarket.com/submit>

## 7. Awesome lists (pull requests — these are the backlinks that compound)

| Repo | Where it goes |
|---|---|
| `punkpeye/awesome-mcp-servers` | 🎬 Media / Video Processing |
| `wong2/awesome-mcp-servers` | Community servers |
| `modelcontextprotocol/servers` | README → Community Servers table |
| `appcypher/awesome-mcp-servers` | Media |

Suggested line (keep it factual — these lists reject marketing copy):

```markdown
- [Valmera](https://github.com/ABO3SKRALMASAOODI/valmera-mcp) - Agentic video editing on real footage: cut silences and filler words, word-timed captions, reframe to 9:16, music and mastering, full-quality export. Remote (streamable HTTP, OAuth).
```

## 8. Client-specific directories

- **Cursor** — <https://cursor.directory/mcp> (submit via PR)
- **Cline** — MCP Marketplace, issue template on `cline/mcp-marketplace`
- **Continue** — <https://hub.continue.dev>
- **Goose** — `block/goose` extensions list
- **LibreChat** — docs MCP examples

---

## Keeping the entry true

`server.json` carries a `version`. Bump it and republish whenever the tool surface
changes materially — a registry entry that describes a server that no longer
behaves that way is worse than no entry, because it produces failed first runs and
those get written up.

The tool count in the README (110 = 99 editing + 11 session) comes from
`agent_tools.TOOLS` plus `SESSION_TOOLS`. Re-check it before republishing rather
than trusting the number in this file.
