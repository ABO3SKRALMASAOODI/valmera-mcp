# Connect Valmera to any MCP client

Valmera is a remote MCP server:

```text
https://valmera.io/mcp/server
```

It uses Streamable HTTP and OAuth 2.1 with dynamic client registration and PKCE (S256). Most clients only need the URL: they read the 401 challenge, register themselves, and open a Valmera sign-in page. Clients that can't run OAuth can send `Authorization: Bearer <token>`, using a token you create at [valmera.io/mcp](https://valmera.io/mcp). Keep tokens out of committed files.

The live, longer version of this page, with notes for each client, is [valmera.io/mcp/setup](https://valmera.io/mcp/setup).

Getting a 401, a sign-in loop or no tools after connecting? Use the [connection troubleshooting guide](CONNECTION-TROUBLESHOOTING.md) for symptom-specific next steps and public discovery checks that need no account or token.

## What Valmera hosts and what you set up

Valmera operates the video-editing MCP endpoint, project storage and rendering service. For
this hosted workflow, you do not deploy a server, write an API-to-MCP wrapper, install FFmpeg
or install a local video editor. Connect a compatible assistant to the existing endpoint above
and authorize access to your Valmera account. Editing requires an eligible paid Valmera plan;
your assistant may have separate access requirements or charges.

| Part of the workflow | Where it happens | What you provide |
| --- | --- | --- |
| Conversation and tool calls | Your chosen MCP client | A client that supports the remote connection and its authentication flow |
| Source footage and project versions | Your Valmera account | An uploaded recording or another supported import; a local file path alone is not an upload |
| Preview rendering and final export | Valmera's hosted service | An editing brief, review decisions and authorization to run the requested operations |
| Result inspection and download | Your client, browser or video player | Review of the actual preview and downloaded file; client display capabilities vary |

A CLI client is still software you install on your computer. An optional stdio bridge is a
local connection adapter. Neither means you must install a video-rendering engine. If your
client cannot display a preview or download link inline, open the returned URL in a browser.

The [recorded MCP run](MCP-RECORDED-EDIT.md) shows the existing project moving from a first
preview to a focused revision and a downloaded MP4. It includes the actual source and outputs,
edit versions and inspected export boundaries. That run used Codex and a silent sample; it
does not establish speech quality or successful operation in every client below. Use the
[editing workflow](WORKFLOW.md) after connecting and keep your own review record.

## Choose the plan for your editing route

There are two ways to direct Valmera's editing tools: use **your own compatible AI assistant through MCP**, or use **Valmera AI inside Studio**. Opening Studio to upload, review or export a project does not by itself mean the plan includes Valmera AI.

The following snapshot comes from [Valmera's subscription page](https://valmera.io/subscribe), checked **November 7, 2026**. Recheck that page and your account before buying; existing subscriptions may retain different terms.

| Plan | Editing assistant | Monthly subscription | Annual payment | Monthly Valmera credits |
| --- | --- | --- | --- | --- |
| Plus | Your own assistant through MCP; upload, review and export in Studio. Valmera AI is not included. | US$15 | US$150 billed once yearly | 500 |
| Pro | Valmera AI in Studio, plus MCP access for your own assistant | US$50 | US$500 billed once yearly | 1,500 |
| Max | Valmera AI in Studio and MCP, with a larger allowance | US$100 | US$1,000 billed once yearly | 4,000 |

Your external assistant provider bills separately. Having a subscription to that assistant does not include a Valmera subscription, and a Valmera plan does not grant the assistant's custom-connector permissions. Check that your chosen account or workspace supports the connection before choosing the MCP route.

**For a first project:** choose the route you will actually use. With your own assistant, connect and authorize Valmera, confirm the project is accessible, then request a short representative edit. With Valmera AI, open Studio on a plan that includes it. In either case, review the preview, request a focused revision and inspect the final download. Use the [recorded caption example](CAPTION-STYLE-EXAMPLE.md) to see two preview treatments and the delivered file; its limits and branding are documented alongside the downloads.

### Budget by accepted edits, not by a presumed credit-to-minute conversion

The subscription page meters AI and processing work. Footage length, operations and revisions affect usage; the credit count is not a guaranteed number of finished videos. Record the actual credit use of a representative project, including the revision and export you need, before estimating a larger batch.

For a **fictional budget example**, suppose you choose Plus on monthly billing and already pay for a compatible assistant. Valmera adds US$15 for that month, while your assistant's existing bill and any additional usage remain separate. If you instead need Valmera AI in Studio, the listed Pro monthly subscription is US$50. This compares access routes, not equal editing capacity, quality or total cost; the allowances differ.

Annual prices are full-year payments, not monthly cancellation offers. The current page states that credits refresh monthly and unused monthly credits do not roll over, including on annual plans. It also explains annual switching and existing-subscription treatment. Read those terms at the source rather than inferring them from a monthly equivalent.

Account creation and uploads are free; AI editing requires an eligible subscription. The current export FAQ states that a five-second Valmera end card is appended. Check the entire downloaded file, including its ending, against your delivery requirements.

## Client connection reference

| Client | Where the config goes | Auth | Key detail |
| --- | --- | --- | --- |
| Claude (web, desktop, mobile) | Settings → Connectors → Add custom connector | OAuth | Paste the URL only. Mobile can use it but not add it. |
| Claude Code | `claude mcp add` (user or project scope) | OAuth or bearer | Use `"type": "http"` when editing `.mcp.json` by hand |
| Cursor | `~/.cursor/mcp.json` or `.cursor/mcp.json` | OAuth | `mcpServers` → `url` |
| VS Code (Copilot agent mode) | `.vscode/mcp.json` | OAuth | Top-level key is `servers`, with `"type": "http"` |
| Codex CLI | `codex mcp add` / `~/.codex/config.toml` | OAuth | Run `codex mcp login valmera` |
| ChatGPT | Plugins → + → Add custom MCP server | OAuth | Install the resulting plugin, then select it with `@`; [walkthrough](CHATGPT.md) |
| Gemini CLI | `gemini mcp add --transport http` | OAuth | Then run `/mcp auth valmera` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` | OAuth or bearer | Key is `serverUrl`. Cascade caps tools at 100 across all servers. |
| Zed | `settings.json` → `context_servers` | OAuth | `url` form needs a recent Zed |
| Cline | MCP Servers → Remote Servers | Bearer | `"type": "streamableHttp"` |
| Continue | `.continue/config.yaml` | Bearer | `type: streamable-http` |
| Goose | `~/.config/goose/config.yaml` | OAuth or bearer | Key is `uri`, type `streamable_http` |
| LibreChat | `librechat.yaml` → `mcpServers` | OAuth (per user) or headers | Omit `client_id` to use dynamic registration |
| MCP Inspector | `npx @modelcontextprotocol/inspector` | OAuth or `--header` | Best tool for debugging a connection |
| Anything stdio-only | That client's stdio config | OAuth via bridge | `npx -y mcp-remote <endpoint>` |

## ChatGPT

Follow the [ChatGPT connection and first-edit walkthrough](CHATGPT.md). Creating the connection, installing the plugin, and selecting it in a conversation are distinct steps. If custom MCP is unavailable, check your account and workspace permissions or open the editing brief directly in Valmera Studio.

The [guided setup page](https://valmera.io/mcp/connect?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_chatgpt_workflow) confirms when Valmera receives your assistant's first request. ChatGPT connection instructions were checked against [OpenAI's guide](https://developers.openai.com/api/docs/guides/custom-mcp-server) on November 4, 2026; other client entries retain their own existing guidance.

## Grok

For Grok, see the [planning and custom-connector guide](GROK.md). It distinguishes the web connector, Grok Build and API routes, and records the current verification limits. The web setup form and authentication handoff were observed; a completed Grok-to-Valmera tool call has not been verified in that guide.

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

Editing tools can change a project or start billable work. Review each tool's behavior before granting permission; do not approve all Valmera tools as read-only. If you choose to allowlist inspection tools, limit that choice to the specific operations you have verified. Keep approval for project changes, rendering and export consistent with your instructions.

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
