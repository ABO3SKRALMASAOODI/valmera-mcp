# Installing the Valmera MCP server (for AI agents such as Cline)

Valmera is a remote MCP server, so there is nothing to build, clone or run locally.

1. Add a remote server named `valmera`:
   - URL: `https://valmera.io/mcp/server`
   - Transport: Streamable HTTP (Cline: `"type": "streamableHttp"`)
2. Authenticate. Choose one:
   - **OAuth** (preferred). Clients that support MCP OAuth discover everything from the 401 challenge, using dynamic client registration and PKCE. The user signs in to Valmera in the browser.
   - **Bearer token.** The user creates a token at https://valmera.io/mcp/connect. Configure the header `Authorization: Bearer <token>` through the client's secret storage. Never write the token into a committed file or the chat.
3. Verify by calling `list_projects`. An empty list still means the connection works.

Cline example (`cline_mcp_settings.json`):

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

Requirements: a Valmera account (free to create at https://valmera.io) and a subscription for editing (https://valmera.io/subscribe). The final MP4 is exported with `export_final`, then `wait_for_job`, then `download_url` with `kind="final"`.
