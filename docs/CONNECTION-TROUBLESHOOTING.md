# Fix a Valmera MCP connection: 401, sign-in and missing tools

Connect your AI assistant to `https://valmera.io/mcp/server` to edit your footage with Valmera. If opening that address in a browser returns **401 Unauthorized**, start with your client's sign-in flow: the endpoint requires authentication. A response to an anonymous request is not a test of your authorized editing session.

For installation, use the [client setup guide](CLIENTS.md), the [ChatGPT walkthrough](CHATGPT.md), or [guided connection setup](https://valmera.io/mcp/connect?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_connection_help). Account creation and uploads are free; editing requires a [subscription](https://valmera.io/subscribe).

## Find the next step from the symptom

| What you see | What it tells you | Next step |
| --- | --- | --- |
| A browser or anonymous request gets 401 with a Bearer challenge | The endpoint responded and requests authorization | Add the endpoint in your MCP client and complete Valmera sign-in |
| The client still gets 401 after sign-in | The authorized request was rejected; an expired or missing token is one possible cause | Reconnect through the client's supported sign-in flow; confirm the endpoint is the branded URL above |
| 403 | Access was refused; the status alone does not identify the account or permission problem | Check the client error and account access; share a redacted error with support if unresolved |
| DNS, TLS or connection timeout before an HTTP response | The request did not complete from that network | Record the time and exact error; check the address and retry from your normal connection without disabling certificate verification |
| 429 or a temporary 5xx response | This request was rate limited or encountered a server/proxy error | Respect any retry delay, then retry; preserve the timestamp if it persists |
| The client says connected but shows no Valmera tools | Connection, installation and tool selection may be separate client steps | Finish installation, select Valmera in the conversation and refresh tool discovery; see your client guide |
| Tools appear, but your video is missing | Authentication succeeded far enough to discover tools; project access remains to be checked | Ask for a read-only project listing and confirm that the intended Valmera account is connected |
| A directory calls Valmera read-only | Its assessment may not include authenticated editing tools | Inspect the published editing definitions and recorded results below; verify tools in your own connection |
| A directory says “unverified” or “not responding” | Its result describes its own probe and check time | Compare that probe with the public checks below; do not infer that it tested an authenticated edit |

If setup is unavailable in your assistant or workspace, [open Valmera Studio](https://valmera.io/online-video-editor?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_connection_help#start-editing) and direct the edit there.

## Does Valmera edit video, or only read projects?

**Valmera is an editing connector, not a read-only project catalog.** It includes inspection tools alongside operations that save edits, render previews and export videos. An anonymous directory probe can fail to enumerate authenticated tools without establishing that the service is read-only.

The public [server card](https://valmera.io/.well-known/mcp/server-card.json), inspected November 7, 2026, distinguishes these operations:

| Stage | Example operation | What the published definition describes | Evidence to inspect |
| --- | --- | --- | --- |
| Inspect | `list_projects`, `project_state` | Returns account projects or the identified project's existing state | The returned project identity and state. No completed edit is implied. |
| Revise the cut | `cut_range` | Removes a source interval and saves a new edit version | The saved ranges, reported boundary adjustments and resulting version. |
| Revise captions | `set_caption_style` | Changes supplied appearance settings while retaining wording and timing | The saved settings and the affected passage in a rendered preview. |
| Preview | `render_preview` | Produces review media for an edit version, or returns pending job information | The completed preview and whether it covers the changed section or full program. |
| Export | `export_final` | Creates or recovers a final export for an explicit reviewed version | The existing job's terminal result and matching final asset. |
| Retrieve | `download_url` | Returns a link and receipt for an existing render | The actual file; retrieving its URL does not create an export. |

In that observation, `cut_range`, `set_caption_style`, `render_preview` and `export_final` were explicitly marked `readOnlyHint: false`. These published annotations help describe intent; they are not an authorization mechanism or an independent guarantee about execution. Use the current tool descriptions and schemas from your authenticated connection, and authorize the work you intend to run.

### Check capability without launching an edit

Use this initial request in your connected assistant:

> Inspect the available Valmera tool definitions and list my projects. Do not upload, edit, render or export. Report the tools available for changing a cut, changing caption style, rendering a preview and exporting a final file. Distinguish tools you discovered from actions you actually executed. If discovery fails, report the error; do not infer that the editor is read-only.

A successful inspection proves access to that information, not that every operation will succeed. If a required tool is missing, refresh discovery and check the intended account and plan through the [client guide](CLIENTS.md). Do not test a write operation on an unrelated project just to establish that editing exists.

### Inspect a recorded edit before starting your own

Two public examples provide stronger evidence than a capability label:

- [Recorded cut and focused revision](MCP-RECORDED-EDIT.md): original source, changed previews and a final MP4 from a silent motion graphic. It demonstrates a specific selection/revision/export sequence, not speech-editing quality.
- [Recorded caption-style revision](CAPTION-STYLE-EXAMPLE.md): two treatments on a licensed dialogue excerpt, matching decoded audio between previews and a separate full-resolution export. The guide reports branding, duration differences and review limitations.

Download the artifacts and read the method to see what those runs establish. For your own footage, identify the project and approved scope, make the requested edit, review its preview and inspect the downloaded final file. That sequence establishes an outcome for your recording; a directory badge or tool count does not.

## Check public discovery without an account

These commands make public requests only. They do not upload footage, register a client, sign in, create a project or run an editing tool. Run them in a terminal with `curl`. No token is needed. The requests have time limits so an unavailable endpoint does not leave the check running indefinitely.

First inspect the anonymous response headers:

```sh
curl -sS --connect-timeout 10 --max-time 20 \
  -D - -o /dev/null https://valmera.io/mcp/server
```

An observed authorization challenge is:

```text
HTTP/2 401
WWW-Authenticate: Bearer realm="valmera", resource_metadata="https://valmera.io/.well-known/oauth-protected-resource"
```

Header capitalization and HTTP version can differ. Check the status and metadata URL, not their formatting. The [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization#authorization-server-discovery) describes discovery through a 401 challenge and protected-resource metadata. This is a protocol reference, not a certification of this deployment.

Then read the linked public metadata:

```sh
curl -sS --connect-timeout 10 --max-time 20 \
  -D - https://valmera.io/.well-known/oauth-protected-resource

curl -sS --connect-timeout 10 --max-time 20 \
  -D - https://valmera.io/.well-known/oauth-authorization-server
```

For Valmera, confirm that the resource is `https://valmera.io/mcp/server`, that `authorization_servers` includes `https://valmera.io`, and that the authorization metadata's `issuer` matches that URL. The metadata advertises the authorization and token endpoints and PKCE `S256`. Reading it does not complete those flows.

Directories can inspect the public [server card](https://valmera.io/.well-known/mcp/server-card.json) for the endpoint, authentication information and published tool definitions without accessing a creator's account:

```sh
curl -sS --connect-timeout 10 --max-time 20 \
  -D - https://valmera.io/.well-known/mcp/server-card.json
```

The card is Valmera's public description. Your authenticated client's current `tools/list` establishes which tools are actually exposed to that connection. Neither a successful card request nor a public tool definition proves that a render or export succeeds.

## What has been checked

On November 4, 2026 at 20:04 UTC, unauthenticated GET and JSON-RPC `initialize` POST requests to the endpoint both returned 401 with the resource-metadata challenge above. Protected-resource metadata, authorization-server metadata and the server card each returned 200. The resource and issuer matched the branded URLs described above.

This dated check establishes public reachability and authentication discovery from the checking network. It does **not** establish continuous uptime, successful OAuth completion, compatibility with every client, paid editing health, rendering quality or an independent directory grade. Repeat the commands for a current observation.

## Continue from connection to a first edit

After signing in, ask your assistant:

> List my Valmera projects so I can choose the video. Do not change or render anything yet.

An empty list may simply mean that no projects exist in the connected account. Upload your intended footage in Valmera, choose its project, then use the [creator workflow guide](CREATOR-WORKFLOWS.md) or [editing brief builder](https://valmera.io/prompts?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_connection_help#prompt-builder). Tell the assistant the desired result, review its preview and request revisions before approving the final export.

## Report an unresolved connection issue

Open an issue in this repository or contact support@valmera.io with the client name and version, timestamp with timezone, endpoint, stage that failed, HTTP status and redacted error text. Say whether it failed before sign-in, after sign-in, during tool discovery or while using a specific tool. A public discovery result helps isolate the stage; it cannot replace evidence from the failing client.

Do not include tokens, cookies, authorization codes, private footage links or a complete unredacted client log. Directory maintainers can link to the public metadata and this guide without requesting access to a creator's footage.
