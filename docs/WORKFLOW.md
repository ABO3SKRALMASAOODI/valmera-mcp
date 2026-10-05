# A complete agent-assisted video editing workflow

This guide follows one recorded interview from project discovery through preview review to the final MP4 export. The prompts are examples. They do not claim a measured customer result.

## 1. Establish the connection without editing anything

Connect your client using the [setup guide](https://valmera.io/mcp/setup), then ask:

> List my Valmera projects. Do not change them yet.

Use `list_projects` to establish that the authenticated connection reaches the intended account. If the result is empty, upload a recording in [Studio](https://valmera.io) or use the file-transfer workflow your client's upload tools provide. A local file path in a chat message does not by itself upload the file.

If authentication fails, inspect the returned error and check that the account has MCP access. Do not repeatedly recreate projects to diagnose a connection problem. AI editing also requires an active subscription and available credits.

## 2. Read the source before deciding what to cut

Ask the assistant to open the intended project and check `project_state` and `index_status`. Wait until indexing completes. It can then read the transcript, inspect frame samples and identify the speaker, framing and major sections.

> Open the interview project I selected. Tell me its duration and summarize the topics using the actual transcript. Inspect the opening, a middle section and the ending. Flag uncertain names or unclear audio before editing.

An assistant should distinguish source observations from editorial suggestions. If it cannot inspect an audio or image result in the current client, it should say what still needs human review.

## 3. Give a specific brief

Useful instructions specify the audience, length goal, material to keep, changes allowed and review criteria:

> Make a concise interview edit for our product page. Keep the speaker's meaning and answer order. Remove obvious dead air, false starts and repeated filler words, but preserve complete sentences and pauses that make the answers understandable. Do not add claims, change quoted numbers or add music yet. Add captions using the transcript. Render a review preview when the edits finish.

The assistant can use tools such as `cut_silences`, `remove_filler_words`, `cut_range` and `add_captions`, choosing arguments from the live schema. It should inspect the current kept transcript after cutting. A plan or a tool request is not evidence that the edit succeeded.

## 4. Inspect the rendered edit

After `render_preview`, use the returned job information and `wait_for_job` as instructed. A queued or running job is still unfinished. Once a preview is available, the assistant can inspect frames using the available review tools. You should watch the preview as well.

Check these independent outcomes:

| Check | What to look for |
| --- | --- |
| Meaning | No removed word changes a claim, qualification or answer |
| Cuts | No clipped syllables, unnatural jumps or missing context |
| Captions | Correct names and numbers, readable size, good timing |
| Framing | Faces and relevant products remain in view |
| Audio | Speech is intelligible and music does not cover important words |
| Ending | The final thought finishes before the content ends |

Reference the time shown in the current preview when requesting a change. Source time and edited output time can differ after cuts; the assistant should choose the appropriate tool and time basis.

## 5. Revise one issue at a time

> In the current preview, the answer around 00:42 starts too abruptly. Restore the lead-in from the original recording, preserve the later edits, and render a fresh preview.

Then, if a vertical version is needed:

> Reframe this project to 9:16. Keep the speaker's face and the product they hold inside the frame. Move captions into a readable area and inspect frames at the opening, at the product demonstration and near the end. Flag shots where the crop loses important context.

The assistant may use `restore_range`, `auto_reframe`, `set_frame` and caption styling tools where available. Frame inspection samples specific moments; it does not prove that every frame throughout a moving shot is correct. Review the full preview before delivery.

## 6. Add music with a defined role

> Add a quiet background track that suits an explanatory interview. Keep speech clear and lower the music under speaking. Show me which track was selected and its available license information, then render a preview of the mix.

Use your own licensed media or evaluate the license supplied with retrieved media for your intended use. Finding a track does not establish that every license permits every commercial use. Listen to the rendered mix rather than judging it only from a volume setting.

## 7. Export the approved edit

After you approve the last preview, ask for the finished file:

> Export the version I just approved as a full-quality MP4 and give me the download link. Tell me the final duration.

The assistant calls `export_final` with the project id and the reviewed `edl_version`. It then polls `wait_for_job` until the job finishes and calls `download_url` with `kind="final"`. The final H.264 MP4 renders from the original source file, not the preview proxy. Export runs the same checks, queue and plan rules as Studio export, and Studio's Export button is still available if you'd rather start it yourself.

Watch the downloaded file before publishing and check its duration, framing, captions, audio and ending. An approved preview doesn't prove the final render finished, and a job id isn't a finished MP4.

## Troubleshooting

| Symptom | Next useful check |
| --- | --- |
| No projects appear | Confirm the connected account; upload through Studio or the client's supported transfer flow |
| Editing is refused while indexing | Read `index_status`; wait for analysis or investigate its terminal error |
| Editing requires payment | Check the active subscription and available credits in Studio |
| A requested tool is missing | Refresh the live catalog; do not invent a tool name or assume it is enabled |
| A job remains in progress | Inspect the same returned job identifier rather than starting duplicate renders |
| Studio or MCP says the project is busy | Let the active editing operation finish before switching editors |
| Preview picture looks softer | Previews use a proxy; inspect the completed Studio final for delivery quality |
| `export_final` is missing from the tool list | Reconnect or refresh the client so it reloads the catalog; Studio Export also works |

Current connection details and supported operations are in the [README](../README.md), the [live server card](https://valmera.io/.well-known/mcp/server-card.json), the [tool catalog](TOOLS.md) and the [tool reference](https://valmera.io/mcp/tools).
