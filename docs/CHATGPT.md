# Edit your first video with ChatGPT and Valmera

Connect Valmera, select a recording, and turn a clear brief into an edit you can review. This walkthrough is maintained by Valmera. Adapt its example prompts to your own recording. Connection instructions checked November 4, 2026.

[Open guided connection setup](https://valmera.io/mcp/connect?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_chatgpt_workflow) · [Open the brief directly in Valmera](https://valmera.io/chatgpt-video-editor?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_chatgpt_workflow#first-brief)

Valmera hosts the video editing service. You do not need to clone this repository, install FFmpeg or run a local server. Creating an account and uploading are free; editing requires an eligible [Valmera plan](https://valmera.io/subscribe). Your ChatGPT subscription is separate. For the distinction between Plus MCP Connect and plans that include Valmera AI, see [plans and editing routes](CLIENTS.md#choose-the-plan-for-your-editing-route).

## 1. Add, install and select Valmera

Use ChatGPT on the web. Custom MCP availability follows your account and workspace permissions.

1. Open [ChatGPT Plugins](https://chatgpt.com/plugins). Choose **+ → Add custom MCP server**.
2. Name it **Valmera** and enter this server URL:

   ```text
   https://valmera.io/mcp/server
   ```

3. Choose OAuth, review the permissions and risk notice, and create the plugin. Sign in to the Valmera account you intend to edit with and authorize the connection.
4. Find the resulting Valmera plugin in your personal or workspace directory and **install it**.
5. Start a new conversation, type `@` and select Valmera.

Creating the connection does not replace installing the plugin. See [OpenAI's custom MCP instructions](https://developers.openai.com/api/docs/guides/custom-mcp-server) for account restrictions and installation behavior.

## 2. Confirm the account and choose your footage

Send:

> Use Valmera to list my projects with their names and IDs. Do not change any project yet. I will choose the recording to edit.

An empty list can mean you have not uploaded a project. Upload the recording in [Valmera Studio](https://valmera.io/studio), then ask ChatGPT to list the projects again. Attaching a file to a ChatGPT message does not automatically upload it to Valmera.

Choose the exact project rather than relying on “latest” when several recordings are available. Replace the bracketed field below:

> Open Valmera project [project ID]. Check that the source is ready to edit. Summarize its main topic and duration from the available project information, then wait for my brief.

The [guided connection page](https://valmera.io/mcp/connect?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_chatgpt_workflow) can confirm when Valmera receives the assistant's first request. It checks connection activity; it does not claim that an edit or export has completed.

## 3. Ask for a first cut

For a spoken recording, try:

> Edit this recording into a clear 60-second vertical video for someone hearing the topic for the first time. Start with the strongest complete point. Remove repeated starts and long pauses, while preserving qualifications that affect the meaning. Keep the speaker readable in a 9:16 frame and add clear captions. Do not invent quotes or replace the speaker's words. Render a preview and give me the link before the final export.

Adapt the duration, audience and format to your footage. For a screen tutorial, preserve the required actions and readable interface; a vertical crop may be the wrong choice. The [creator briefs](CREATOR-WORKFLOWS.md) cover tutorials, webinars, product videos and travel footage.

For direct Studio editing, [open an editable brief](https://valmera.io/chatgpt-video-editor?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_chatgpt_workflow#first-brief). The request is saved through sign-in and waits for you to review it before sending. This route uses Valmera's Studio editing agent without requiring a ChatGPT connection.

## 4. Review and revise in the same conversation

Watch the preview with sound. Check the opening, complete words around cuts, caption names and numbers, framing, and the final sentence.

Give a focused revision using your own phrase or preview time:

> In the preview, the answer beginning “[exact phrase]” starts too abruptly. Restore its complete lead-in from the source. Keep the later approved cuts and caption style, then render another preview.

If you supply a time, say whether it refers to the original recording or the edited preview. Cuts change the relationship between those clocks. A preview link proves that a preview is available; it does not prove that the final export is complete.

## 5. Export the version you approved

After reviewing the revision, send:

> Export the project and version I just approved as a full-quality MP4. Wait for the export job to finish, then give me the download link and final duration.

The assistant uses the current export tools and follows the returned job. Open the downloaded file and check its sound, framing and ending before posting. You can also export from Studio.

## When the next step is unclear

| What you see | Next step |
| --- | --- |
| No option to add a custom MCP server | Check ChatGPT account and workspace permissions. You can use the direct Studio brief meanwhile. |
| Valmera was created but is missing from the conversation | Find and install the resulting plugin, then select it in a new conversation. |
| The project list is empty | Confirm the Valmera account and upload through Studio. A local path or chat attachment is not a completed upload. |
| The assistant describes an edit without a preview | Ask it to use the connected Valmera project and return the actual preview result. |
| A job is still running | Continue checking the returned job; do not start duplicate renders to make it finish sooner. |
| Tools look outdated | Refresh the custom connection in ChatGPT Plugins, then start a new conversation. |
| Sign-in succeeds but editing is unavailable | Read the returned account or plan message and check the current Valmera plan. |

OpenAI documents the [custom-connection refresh procedure](https://developers.openai.com/plugins/deploy/connect-chatgpt). Refreshing a connection is separate from installing a newly created plugin.

## Continue with your own recording

- [Connect ChatGPT to Valmera](https://valmera.io/mcp/connect?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_chatgpt_workflow)
- [Start directly with an editable brief](https://valmera.io/chatgpt-video-editor?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_chatgpt_workflow#first-brief)
- [Build a different editing brief](https://valmera.io/prompts?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_chatgpt_workflow#prompt-builder)
- [Full review-and-export workflow](WORKFLOW.md)
- [Current tool reference](https://valmera.io/mcp/tools)
