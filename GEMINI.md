# Valmera video editing

Valmera is a hosted AI video editor connected at `https://valmera.io/mcp/server`.

- Discover the current tools and input schemas after authenticating. Use the user's intended project and editing brief.
- Account creation and uploads are free; editing requires a paid plan. Establish the scope and cost expectations before billable work. Use an available estimate; if no exact quote is exposed, say so and obtain approval for a bounded preview. Reuse existing scope and budget approval without exceeding it.
- Open the project with `list_projects` and `open_project`. Upload through the current `upload_start`/file-transfer/`upload_finish` protocol or Studio, then follow `index_status` until ready.
- Read the transcript and visual evidence before editing. Apply the tools that fit the requested cuts, captions, framing, sound and supporting visuals; confirm specialized delivery requirements against current project options.
- Render a representative preview, follow its existing job with `wait_for_job`, and inspect the result. Distinguish source times from output times when discussing revisions.
- For an authorized final export, call `export_final` with the project and reviewed `edl_version`, then `wait_for_job`, then `download_url` with `kind="final"`. A preview or job ID is not the final file.
- Let an active Studio or MCP edit finish before editing the same project from another client.

Full workflow and task-specific skills: https://github.com/ABO3SKRALMASAOODI/valmera-mcp/tree/main/skills
