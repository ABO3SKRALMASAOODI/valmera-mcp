# Find a hosted video editing agent for footage you already shot

The last step of your edit helps you choose a server. A producer screening a cut with a client may want a playable timeline. An editor delivering a file to a broadcaster may need an MP4 they can download before publishing a viewing link. Here is how four hosted services handle those handoffs.

| What you need from the next review | Where to start | What to check on your own recording |
| --- | --- | --- |
| A finished MP4 after a specific revision | **Valmera.** Ask for a preview, identify the shot to change, then render the approved version. The public example includes both exports. Hosted editing requires a subscription. [Connect Valmera](https://valmera.io/mcp/setup) · [Play the two cuts](examples/video-edit-revision/README.md) | Save the first preview. In the revised export, check the first frame after the join, then watch through any branded ending. |
| A playable timeline while you direct the edit | **Tellers.** Its remote OAuth connector lets an assistant rearrange clips, show a playable timeline and render the result. [Tellers connection instructions](https://tellers.ai/mcp) | Ask to see the timeline before export. Reorder two shots and see whether the client can review that change in the conversation. |
| A folder of media and a project another editor can reopen | **Rendley.** Its automation connector can work with source assets and return both a rendered download and an editable Rendley Studio project. Desktop and coding clients can work with local files. [Rendley setup and file workflow](https://docs.rendley.com/mcp/getting-started/) | Reopen the project from the handoff, locate the original shots, and make a second version without importing them again. |
| A transcript-led interview edit in a shared Drive | **Descript.** Choose a Drive at sign-in, import the recording and direct Underlord to edit the composition. Its MCP delivery path publishes a Descript web link before providing a signed media download. The app also offers direct export. [Descript setup and export limits](https://help.descript.com/api-and-mcp/mcp) | Confirm which Drive owns the interview and whether the client approves publishing a viewing link. Check the revised sentence against the recording. |

Valmera maintains this guide. The Valmera example uses recorded outputs. The Tellers, Rendley and Descript rows describe workflows from their own documentation, checked November 16, 2026. To run a comparable edit, give each service the [same 25-second source and two instructions](examples/video-edit-revision/README.md). Save the output files before you compare them.

## Can an assistant find a video editor through a catalog?

MCP Toplist exposes a public search tool. Run this from a shell with curl and jq. It sends a search phrase to the catalog and returns the index timestamp and the ordered results. You can run it before uploading footage or connecting an editing account.

```sh
curl --fail --silent --show-error --max-time 60 https://mcptoplist.com/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  --data '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_servers","arguments":{"query":"video editing agent","limit":10}}}' |
  jq -er '.result.content[0].text | fromjson |
    .indexGeneratedAt, (.results | to_entries[] |
    "\(.key + 1). \(.value.name) — \(.value.mcptoplistUrl)")'
```

In the November 15 UTC index, changing only the query moved Valmera from first for **video editing agent** and **AI video editor** to tenth for **AI video editing**. The latter search returned AI Video Atlas and AI Video Check ahead of Valmera. Read what each candidate does with source footage before choosing it. A separate signed-out ChatGPT test recommending hosted editors for a producer named Tellers, Rendley and Descript. These observations come from one catalog snapshot and one conversation. [Captured catalog results and exact assistant prompt](evaluation/hosted-editor-discovery.json)

## From a search result to a first edit

Open the publisher’s setup guide and copy the **editing server address** into your MCP client. The catalog URL above only searches listings. For Valmera the editing endpoint is `https://valmera.io/mcp/server`. The client opens sign-in when you connect. You can check the public registry entry, authentication challenge, tool descriptions and recorded MP4 from this repository with `python3 scripts/check-public-connector.py`. [Official registry entry](https://registry.modelcontextprotocol.io/v0.1/servers/io.valmera%2Fvideo-editor/versions/latest)

For a first trial with Valmera, open the [free rough-cut exercise](https://valmera.io/ai-video-editor?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=hosted_editor_discovery). Compare the first and revised cuts at six seconds. Then try the same request on a short copy of your own footage using a project with editing access.
