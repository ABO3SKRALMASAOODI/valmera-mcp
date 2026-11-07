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

## After the connection check

Use the [documentation task index](docs/README.md) to find the guide for the user's recording, including speech cleanup, caption corrections, batch editing and downloadable examples.

Ask which uploaded project to edit, or use the client's supported upload flow. Calling `list_projects` proves authenticated access; it does not prove that a video was edited or exported. A file path in a chat message is not an upload.

- For a first real recording, follow the [editing workflow](docs/WORKFLOW.md): inspect the source, apply the user's brief, review a preview, make a focused revision and export the reviewed version. Use the current tool schemas and the project ID returned for this account.
- To inspect a completed example first, open the [recorded MCP run](docs/MCP-RECORDED-EDIT.md). It includes the original source, first preview, revised MP4, file hashes and exact exported boundary frames. This silent sample checks cuts, framing and revision; it does not test speech or creative quality.
- To compare the same task across editors, use the [evaluation kit](docs/EDITOR-EVALUATION.md). Preserve failed attempts, extra work and export conditions alongside successful results.

Return the final file link only after the existing export job completes. Identify its edit version and distinguish the edited program's duration from the delivered file's total duration, including any appended material. Report any part of the requested review the client could not perform.
