# Record a product demo across two browser tabs and deliver one MP4

When a product link opens a second tab, check which page the recorder actually follows. A smooth shot of the original page cannot show the outcome in the new tab. Before you buy a recorder or commission a batch of demos, test the whole path on one public workflow and inspect the downloaded MP4.

## Try the same handoff on two live pages

Open [Record a Website Demo](https://valmera.io/tools/record-website-demo). In its review section, open **Compare two versions and mark the exact moment to revise** in a new tab using your browser’s open-in-new-tab gesture. The original tab remains on the recorder page. The new tab opens [Review two cuts of a product demo](https://valmera.io/tools/review-product-demo).

We observed two separate pages in Chromium. In the second tab, choosing **Match the result** set the first cut to **1.20 s** and the revised cut to **1.90 s**. We also opened the result URL directly in a clean browser session and confirmed it loaded with the same heading. That second check tells us the result can be captured independently for this example.

| Check | Evidence |
| --- | --- |
| Original tab immediately after opening the second tab | [Original page still shows the link](examples/website-demo-second-tab/entry-after.png). |
| Intended destination after selecting the result | [Two cuts at independent playback positions](examples/website-demo-second-tab/second-tab.png). |
| Joined preview for a reviewer | [Seven-second MP4](examples/website-demo-second-tab/two-take-review-preview.mp4). At 3.00 s, the picture switches to the second page. |
| Repeatable capture checks | [Browser measurement record](examples/website-demo-second-tab/measurements.json). |

The MP4 uses two stills from the live test, assembled with FFmpeg. Use it to confirm that a viewer can see the handoff and result. It does not demonstrate an automated tab switch or a full running window recording.

## Choose the capture mode before filming

| What the demo must show | Capture route | Approval check |
| --- | --- | --- |
| A continuous, visible tab switch | Record a real browser window or display and make the switch yourself. | The original action and the new tab are visible. Exclude unrelated tabs, messages and personal data. |
| Two public app pages, with room to pace each scene | Capture each approved URL separately, then join the takes. | Confirm the destination works in a clean session. Hold on a result that can be seen and read. |
| A signed-in account, a confirmation screen or a result tied to that session | Capture approved footage yourself in a demonstration account, then supply it for editing. | Verify the necessary state is present. Review for account details before delivering or uploading. |

Loom describes its [tab, window and screen capture modes](https://support.atlassian.com/loom/docs/get-started-with-the-loom-chrome-extension). Check which source it is capturing on your device. Valmera's [website recorder brief](https://valmera.io/tools/record-website-demo) is designed around public URLs and visible actions. Ask for a separate take for each approved public page when the result lives elsewhere. If the target depends on state from the first tab, prefer a continuous capture with that state already established.

## Put both outcomes in the editing brief

> Take A starts at [public URL A] and ends with the visible [link or control]. Take B starts at [approved URL B]. Show [expected heading], perform [visible action], and hold on [values or result]. Join both takes into one MP4 with a clear transition. If page B only works in the original session, tell us what approved recording you need. Return a preview and the timestamp where each outcome becomes readable.

Before release, ask a reviewer to point to the result in the exact MP4 they will publish. If the destination is visible but the expected value never changes, request an updated hold around the relevant action. The public [two-cut reviewer](https://valmera.io/tools/review-product-demo) shows how to give separate timestamps when a revision changes the timing.

**[Prepare a website demo brief in Valmera](https://valmera.io/tools/record-website-demo?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=website_demo_tab_handoff#start-demo)**. Preparing a brief is free. New recordings in Studio require a plan with website recording. For a library of recurring walkthroughs, [scope a done-for-you Enterprise pilot](https://valmera.io/product-demo-video-editing-service?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=website_demo_tab_handoff) with the approved pages, formats and delivery volume.
