# Verify a video editing API's preview and final MP4 before buying

Test whether a pipeline can deliver the exact revision a reviewer approves. Start with a public recording and verify its download. Then run a separate upload and revision trial with your own footage.

Valmera publishes this guide and offers the API used in the example. Its [video editing API](https://valmera.io/video-editing-api?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=api_export_verification) uses JSON-RPC over Streamable HTTP via the Model Context Protocol. An eligible subscription is required for editing.

## Check an actual export without an account

Run the [Python verifier](evaluation/verify_public_video_editing_api_export.py) using Python 3. It makes three read-only requests to Valmera's public website. It checks the current published declarations for timestamped cuts, captions, preview, final export, job polling and download. It then verifies that the public MP4 matches the size and SHA-256 in the recorded export receipt and that the receipt names the same edit version for export and download.

```bash
python3 docs/evaluation/verify_public_video_editing_api_export.py
```

The recorded example exported **edit version 14**, a **2,230,792-byte MP4**. [Watch the finished video](https://valmera.io/examples/product-demo) or [open the receipt](https://valmera.io/examples/product-demo/evidence.json). The example is a silent browser capture. The check does not exercise an authenticated account, time the renderer, evaluate caption accuracy, or independently prove anything about the file before it was published. For those checks, use your own recording for the next step.

## Run a buyer trial with your own source

Use a short recording containing dialogue, a pause and a visible action you need to keep. Specify a target format and request one precise revision after the first preview. Use a fresh trial project and record the actual identifiers returned by the API.

| Step | What to keep | What to verify |
| --- | --- | --- |
| Upload and edit | Source filename, returned project ID, tool arguments and first edit version | The preview preserves the visible action and makes the dialogue intelligible. |
| Revise | A written request such as “restore one second of the confirmation screen and fix one caption word,” plus the new edit version | The revision preserves the earlier cuts outside the requested change. Review the exported caption at the size viewers will see. |
| Approve | Project ID, approved edit version, file requirements and review timestamp | Your release record points to the approved revision even if work continues on the project. |
| Export and download | Final job ID and file checksum | Poll the job until terminal, then download the approved version. Play the MP4 and confirm the change is present before handing it over. |

For Valmera, pass both the project ID and the approved edit version to `export_final`. Keep the returned job ID and follow the job rather than launching a second one while it is still running. Ask for the final download by version. Discover the live tool schemas from your connection before writing the integration. [Read the API walkthrough](https://valmera.io/video-editing-api?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=api_export_verification) · [Connect and get a token](https://valmera.io/mcp/connect?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=api_export_verification)

If you need recurring edits finished for your team, include the monthly volume, typical recording length, required delivery formats and first review date in your request. [Contact Valmera Enterprise](https://valmera.io/subscribe?inquiry=video-editing-service&utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=api_export_verification#enterprise)
