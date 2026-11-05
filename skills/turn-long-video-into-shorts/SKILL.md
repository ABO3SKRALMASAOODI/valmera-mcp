---
name: turn-long-video-into-shorts
description: Turn a long recording, podcast, interview or webinar into individually reviewed short MP4s with Valmera. Use when the user wants several self-contained highlights with framing and captions adapted to the intended platform.
license: MIT
---

# Turn a long video into shorts with Valmera

Each short has its own project, edit version and final export. Select complete stories from the source, then review the framing and captions on each deliverable.

## Connection and cost

Connect to `https://valmera.io/mcp/server` and authenticate using the [client setup guide](https://valmera.io/mcp/setup). Discover the current tools and input schemas in the connected session; the names below describe a workflow, not a permanent catalog.

Account creation and uploads are free; editing requires a paid [Valmera plan](https://valmera.io/subscribe). Before billable work, explain the intended scope and use any cost estimate exposed by the account. If an exact quote is unavailable, say so and obtain approval for a bounded preview before proceeding. Reuse an existing explicit scope and budget approval; ask again if the work would exceed it. Do not buy credits or upgrade a plan without authorization. Review a preview before an approved final export.

## Workflow

1. **Set up the source.** Open the intended project, or use `create_project` with the current shorts-project schema and upload the recording. Wait for `index_status` to report ready. Reuse the user's requested count, duration, aspect ratio and audience.
2. **Read the conversation and visual context.** Use the transcript plus available editorial and frame evidence. Choose moments that make sense without the rest of the recording, preserve the speaker's meaning and finish their thought. A hook is useful only if the rest of the clip delivers it.
3. **Resolve the selection.** If the user has chosen moments, use them. Otherwise present candidate source ranges, a working title and a short reason when selection needs their input; proceed within an already approved selection brief.
4. **Create and track the shorts.** Use the current `make_shorts` schema for the selected stories, follow `shorts_status`, and open each result with `open_short`. Follow existing jobs rather than resubmitting an operation that is still running.
5. **Polish each story.** Apply the requested framing, captions, opening text and sound. Check two-person scenes and camera changes rather than assuming one crop suits the whole clip. Use `apply_short_edit_batches` when its current schema fits an approved batch; validate a representative preview before expanding the treatment.
6. **Review each deliverable.** Render a preview, wait for its job, and inspect the opening, cut boundaries, captions and framing. Distinguish source times from output times in revision notes. Identify each short's project and reviewed edit version.
7. **Export approved versions.** For each authorized final, call `export_final` with that short's project and reviewed `edl_version`, then `wait_for_job`, then `download_url` with `kind="final"`. Report the actual files and any unfinished shorts separately. Do not present a preview or job receipt as a final export.

## Delivery and outcome

Confirm caption language and output files against current project options. State the destination and review each aspect ratio using the [delivery guide](https://valmera.io/docs/publishing). Publishing to an account is a separate action and needs the user's authorization.

No tool can guarantee virality. Explain why the chosen stories fit the brief and which parts of the result were actually reviewed. For one finished edit rather than several stories, use `edit-video-with-valmera` when installed.
