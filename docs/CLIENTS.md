# Connect Valmera to any MCP client

Valmera is a remote MCP server:

```text
https://valmera.io/mcp/server
```

It uses Streamable HTTP and OAuth 2.1 with dynamic client registration and PKCE (S256). Most clients only need the URL: they read the 401 challenge, register themselves, and open a Valmera sign-in page. Clients that can't run OAuth can send `Authorization: Bearer <token>`, using a token you create at [valmera.io/mcp](https://valmera.io/mcp). Keep tokens out of committed files.

The live, longer version of this page, with notes for each client, is [valmera.io/mcp/setup](https://valmera.io/mcp/setup).

| Client | Where the config goes | Auth | Key detail |
| --- | --- | --- | --- |
| Claude (web, desktop, mobile) | Settings → Connectors → Add custom connector | OAuth | Paste the URL only. Mobile can use it but not add it. |
| Claude Code | `claude mcp add` (user or project scope) | OAuth or bearer | Use `"type": "http"` when editing `.mcp.json` by hand |
| Cursor | `~/.cursor/mcp.json` or `.cursor/mcp.json` | OAuth | `mcpServers` → `url` |
| VS Code (Copilot agent mode) | `.vscode/mcp.json` | OAuth | Top-level key is `servers`, with `"type": "http"` |
| Codex CLI | `codex mcp add` / `~/.codex/config.toml` | OAuth | Run `codex mcp login valmera` |
| ChatGPT | Settings → developer mode → add connector | OAuth | Refresh the connector after server updates |
| Gemini CLI | `gemini mcp add --transport http` | OAuth | Then run `/mcp auth valmera` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` | OAuth or bearer | Key is `serverUrl`. Cascade caps tools at 100 across all servers. |
| Zed | `settings.json` → `context_servers` | OAuth | `url` form needs a recent Zed |
| Cline | MCP Servers → Remote Servers | Bearer | `"type": "streamableHttp"` |
| Continue | `.continue/config.yaml` | Bearer | `type: streamable-http` |
| Goose | `~/.config/goose/config.yaml` | OAuth or bearer | Key is `uri`, type `streamable_http` |
| LibreChat | `librechat.yaml` → `mcpServers` | OAuth (per user) or headers | Omit `client_id` to use dynamic registration |
| MCP Inspector | `npx @modelcontextprotocol/inspector` | OAuth or `--header` | Best tool for debugging a connection |
| Anything stdio-only | That client's stdio config | OAuth via bridge | `npx -y mcp-remote <endpoint>` |

## Claude Code

```sh
claude mcp add --transport http valmera https://valmera.io/mcp/server
# then inside Claude Code:
/mcp
```

`claude mcp list` should show `✔ Connected`. Add `--scope user` to make it available in every repository, or `--scope project` to write a shared `.mcp.json`.

## Cursor

```json
{
  "mcpServers": {
    "valmera": { "url": "https://valmera.io/mcp/server" }
  }
}
```

Most of an edit is reading (`look_at`, `get_words`, `project_state`), so allowlist read-only tools. Otherwise every call asks for confirmation.

## VS Code

```json
{
  "servers": {
    "valmera": { "type": "http", "url": "https://valmera.io/mcp/server" }
  }
}
```

## Codex CLI

```sh
codex mcp add valmera --url https://valmera.io/mcp/server
codex mcp login valmera
```

## Gemini CLI

```sh
gemini mcp add --transport http valmera https://valmera.io/mcp/server
# then inside Gemini CLI:
/mcp auth valmera
```

## Windsurf

```json
{
  "mcpServers": {
    "valmera": {
      "serverUrl": "https://valmera.io/mcp/server",
      "headers": { "Authorization": "Bearer <your-valmera-token>" }
    }
  }
}
```

The headers block is optional if the OAuth sign-in works for you.

## Cline

```json
{
  "mcpServers": {
    "valmera": {
      "type": "streamableHttp",
      "url": "https://valmera.io/mcp/server",
      "headers": { "Authorization": "Bearer <your-valmera-token>" },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

## Zed

```json
{
  "context_servers": {
    "valmera": { "url": "https://valmera.io/mcp/server" }
  }
}
```

## Continue

```yaml
mcpServers:
  - name: valmera
    type: streamable-http
    url: https://valmera.io/mcp/server
    requestOptions:
      headers:
        Authorization: Bearer <your-valmera-token>
```

## Goose

```yaml
extensions:
  valmera:
    enabled: true
    type: streamable_http
    name: valmera
    description: Agentic video editor
    uri: https://valmera.io/mcp/server
    timeout: 60
```

## LibreChat

```yaml
mcpServers:
  valmera:
    type: streamable-http
    url: https://valmera.io/mcp/server
    oauth:
      authorization_url: https://valmera.io/mcp/oauth/authorize
      token_url: https://valmera.io/mcp/oauth/token
      redirect_uri: http://localhost:3080/api/mcp/valmera/oauth/callback
```

## MCP Inspector

```sh
npx @modelcontextprotocol/inspector --server-url https://valmera.io/mcp/server --transport http
```

If the Inspector connects and lists the tools, the server is fine and any problem is in the other client's configuration.

## stdio bridge

```json
{
  "mcpServers": {
    "valmera": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://valmera.io/mcp/server"]
    }
  }
}
```

`mcp-remote` runs the OAuth flow in your browser for you.

## Discovery endpoints

- Server card: https://valmera.io/.well-known/mcp/server-card.json
- Protected resource metadata: https://valmera.io/.well-known/oauth-protected-resource
- Authorization server metadata: https://valmera.io/.well-known/oauth-authorization-server
- Scope: `valmera.edit`
