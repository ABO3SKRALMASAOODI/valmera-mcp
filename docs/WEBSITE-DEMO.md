# Make a website demo video with an AI assistant

Turn a public product page into a short walkthrough with Valmera, or edit a screen recording you already made. Give the assistant a viewer, one task and a visible result. Then review the recorded actions and the finished video before sharing it.

**[Start from your website URL](https://valmera.io/tools/record-website-demo?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_website_demo#start-demo)** · [Choose a ready-to-edit brief](https://valmera.io/tools/record-website-demo?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_website_demo#demo-briefs) · [Watch a finished example](https://valmera.io/examples/product-demo)

This guide is written by the Valmera team. Creating an account and uploading are free; recording and AI editing require a subscription. See [current plans](https://valmera.io/subscribe). Your assistant provider's access and billing are separate.

## Choose the starting material

| Starting material | Use this route | Include in the brief |
| --- | --- | --- |
| A public landing page, feature page or documentation flow | Record from its public URL | The exact page, visible controls, order of actions and intended result |
| A signed-in dashboard or desktop application | Upload your own screen recording made with demonstration data | The source project, steps to keep, waits to remove and narration |
| An existing launch video needing a shorter cut | Open that project and revise its current version | Destination, target length and the explanation that must survive |

A URL recording does not inherit the login session in your own browser. For an authenticated workflow, start with your own recording rather than supplying a password to a recording step.

You can start directly in [Valmera's website-demo workspace](https://valmera.io/tools/record-website-demo?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_website_demo#start-demo). Enter your domain or full public URL and continue through sign-in. Review the proposed sequence before recording.

For direct editing from an assistant, follow the [client setup guide](https://valmera.io/mcp/setup) and authorize `https://valmera.io/mcp/server`. Refresh the available tools and select the intended project. An assistant without that connection can help write the brief; bring the brief to Valmera to execute it.

## Plan one visible outcome

A useful short demo answers one question: “How do I accomplish this task?” Use this four-part sequence, filling in the actual controls from your website:

| Moment | What the viewer sees | What to check |
| --- | --- | --- |
| Establish the task | The starting page and a short benefit or task label | The label describes what the demo actually shows |
| Show the action | A visible pointer reaches and activates the relevant control | The intended control is selected and the page responds |
| Explain the result | The changed page, setting or output remains readable | The change proves the promised outcome |
| Close with a next step | A concise invitation appropriate to the destination | The final frame stays long enough to read |

Do not prescribe every feature on the site. If the task needs more explanation than the target length allows, preserve the necessary steps and shorten the promise.

## Three briefs to adapt

Replace bracketed details with your own material before sending.

### A 30-second product walkthrough

> Make a landscape demo of [public URL] for [audience]. Show how to [one task], ending on [visible result]. Propose three visible actions using the actual controls on the page before recording. Keep the interface readable, remove long waits, and add short step labels. Use a restrained zoom only when a control needs emphasis. Show me the recorded result and an edited preview before export.

### A vertical feature launch

> Make a 20-second vertical demo of [public feature URL]. Open with [benefit], demonstrate [one feature], and finish with [next step]. Check whether the page works in a portrait layout. Keep the important control and its result visible together where possible. If the desktop layout becomes unreadable, propose a different composition. Keep music below any supplied narration and show me the final crop for review.

### Onboarding from an uploaded dashboard recording

> Use [project or uploaded recording] to explain how to [task]. Keep [required actions] in order and finish on [result screen]. Remove setup time and long waits, add a short label for each step, and align the sequence with [supplied narration]. Keep the final result visible long enough to understand it. Use demonstration data and flag visible account details or notifications for review. Show me a preview before exporting.

The [saved briefs on the website](https://valmera.io/tools/record-website-demo?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_website_demo#demo-briefs) carry into sign-in as drafts. Supply your URL or recording and review the brief before submitting it.

## From the brief to an exported video

1. **Choose the project and plan.** Agree on the source, orientation, actions and result. Use the current tool schema exposed by your authorized connection.
2. **Capture or open the recording.** For a public page, the website recording tools can produce the capture and an event track. For uploaded footage, inspect the source before choosing cuts or zooms.
3. **Inspect the actions.** Check for skipped steps and watch whether each interaction reaches the intended result. A completed recording job can still contain a missed click.
4. **Edit the story.** Tighten waits, make important controls readable, add concise labels and place supplied narration or music. Keep the explanation aligned with what is visible.
5. **Review a rendered preview.** Wait for the render to finish. Watch the result with sound and inspect each important action, page change and final frame.
6. **Export the reviewed version.** Follow the current export workflow, wait for completion, obtain the final download and open the file. A job identifier alone is not the deliverable.

The bundled [website-demo skill](../skills/website-demo-video/SKILL.md) describes the tool-oriented sequence. The [general MCP workflow](WORKFLOW.md) covers projects, source inspection, preview and export.

## What an actual capture shows

The [public documentation capture](https://valmera.io/examples/website-capture) was recorded on September 9, 2026. Its [request and event evidence](https://valmera.io/examples/website-capture/evidence.json) describes a 1920 × 1080, 30 fps, approximately 10.8-second silent capture: wait, click the Captions link in the visible sidebar, scroll and hold.

The first two requests produced recordings but reported no completed click. The third used a selector scoped to the visible sidebar and reported one click at 3.57 seconds and one scroll at 5.72 seconds. Sampled frames showed the Captions page after navigation. The lesson is practical: inspect both the event report and the video before adding polish to a captured sequence.

That is a dated example from one public site, not a guarantee that an arbitrary page or selector will work. Inspect the current page and current tool schema for a new recording. The raw capture is separate from the [finished product-demo example](https://valmera.io/examples/product-demo), which shows an edited result.

## Review and revise precisely

- **Actions:** Did each intended click, scroll or page change happen in order?
- **Readability:** Can a new viewer identify the controls and read the result at the intended viewing size?
- **Timing:** Are long waits removed while required steps and the result remain understandable?
- **Sound and labels:** Do narration and labels describe the action currently on screen? Can the viewer hear the voice clearly?
- **Release:** Does the downloaded version contain the reviewed edits, with appropriate demonstration data and a readable ending?

For a targeted revision, identify the current preview and the problem:

> In the current preview, the result screen after [action] disappears before I can read it. Hold that screen longer and reduce the zoom enough to show [important control]. Keep the other cuts and labels unchanged. Render the revised preview.

If you reference a time, specify whether it belongs to the original recording or the edited preview. Cuts and speed changes can move the same moment to a different time.

[Start your website demo](https://valmera.io/tools/record-website-demo?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=mcp_website_demo#start-demo) · [More creator workflows](CREATOR-WORKFLOWS.md) · [Connection troubleshooting](CONNECTION-TROUBLESHOOTING.md)
