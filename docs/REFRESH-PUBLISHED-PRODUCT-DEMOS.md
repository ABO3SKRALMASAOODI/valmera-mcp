# Update a published product demo after a UI change

Replace the smallest sequence that teaches the changed action. Record the screen the viewer starts from, the new action and the result that proves it worked. After editing, update any captions, chapters and links that point into the old cut. A working embed can still open at the wrong moment.

## Choose what to re-record

| What changed | What to capture | What to keep |
| --- | --- | --- |
| Wording in a separate title card | The corrected title and any matching narration. Check whether the old wording also appears inside the recorded app. | The approved footage when it still shows the current UI. |
| The button moved or its label changed on screen | The new starting state, where to find the button, the click and the resulting screen. | Earlier or later scenes that still show the same account state and workflow. |
| The order or result of the workflow changed | The complete affected sequence, including any new prerequisite and confirmation. | Other chapters with a separate task and an accurate description. |

Use a demo account with sample data. Match the original viewport, zoom and theme so the replacement joins without a distracting resize. Take a few extra seconds before and after the changed action. Give the editor the published link, editable project or master if available, new recording, captions, and approved wording for the revised steps.

## Check that a viewer can still follow the action

Valmera published an example using its documentation site. The [10.83-second source](examples/product-demo-refresh/source-recording.mp4) shows the pointer opening Captions around 3.57 seconds. In the [six-second edited MP4](examples/uae-bilingual-video-editing/product-demo.mp4), the viewer can still see the pointer reach the link and the resulting heading. Play both, then describe which control opened the new screen. The example demonstrates what a cut needs to preserve. It is a revision of one source recording, with no change to the underlying app. [Example and edit notes](https://valmera.io/product-demo-video-editing-service)

## Map chapters, captions and links to the new cut

Suppose the same demo used to open Settings at 00:18, invite a teammate at 00:42 and show confirmation at 01:04. The new Settings sequence grows by five seconds, and a wait before confirmation shrinks by three. The invitation moves to about **00:47**, while confirmation moves to about **01:06**. Check where the step actually begins in the final file. An anchor inside the replaced section needs to be found again by its screen action or spoken line.

For one replacement that changes the runtime, [calculate the revised chapter time and check both sides of the join](https://valmera.io/blog/update-help-center-video-after-ui-change?utm_source=github.com&utm_medium=referral&utm_campaign=help_video_refresh_guide#chapter-calculator).

Use the [demo refresh delivery sheet](DEMO-REFRESH-DELIVERY.csv) to give each live destination its own row. The supplied rows are illustrative and use reserved example links. Record which version each destination should serve, who can update it, and which event to expect after opening an old chapter or timestamped link.

| Publishing surface | Verify after replacement |
| --- | --- |
| Wistia embed and hosted page | Replace Media can preserve the current embed. Wistia says existing chapters stay at their timestamps and the replacement gets a new transcript. Test each marker, captions and any separately shared copy. [Replace media](https://support.wistia.com/en/articles/8274050-replacing-your-media) · [Chapter behavior](https://support.wistia.com/en/articles/8283768-chapters-in-your-video) |
| Vimeo player | A shorter file can remove chapters beyond its new ending. The same runtime can preserve chapter timestamps even when the action moved. Open the viewer-facing chapter menu and verify the step behind each title. [Vimeo chapter behavior](https://help.vimeo.com/hc/en-us/articles/12426231245585-How-to-use-chapters) |
| Help article or course | Open the page as a viewer. Verify the desktop and mobile embed, screenshots, chapter links and any separate subtitles or downloadable copy. |
| Sales enablement and onboarding emails | Test shared time links and check the attachment or hosted clip in the current template. Send corrected time links to the teams that reuse them. |

## Verify the public MP4 against the approved export

For a direct MP4 download, compare the bytes served to a viewer with the file you approved. A successful response, an old filename or an unchanged player link tells you little about which version the viewer receives. Run the [MP4 verification script](evaluation/verify_published_demo.py) with Python 3.9 or later. It downloads the complete file to calculate its SHA-256 hash without writing a local copy.

```sh
python3 verify_published_demo.py --approved approved.mp4 https://example.com/demos/current.mp4
```

| Result | What to do |
| --- | --- |
| `match` (exit 0) | This request received the approved bytes. Open the page with the actual player and test the updated action, chapters and captions as a viewer. |
| `different` (exit 1) | The URL served a different MP4. Check that the public link points to the approved asset. Repeat with `--revalidate` to request cache validation. If that returns the approved file, compare the reported cache headers and inspect the host’s cache settings. If the host transcodes uploads, verify against its approved downloadable rendition. |
| `unavailable` (exit 2) | Check that the link gives viewers a full MP4. A player page, stream manifest or access error needs a different verification route. |

The script checks the link from the network where you run it. A revalidated response only describes that request, so retain the result of the normal request too. For adaptive streams or hosts that serve different versions by device, play the viewer-facing embed on the relevant devices and compare the updated screen directly. [HTTP request revalidation](https://www.rfc-editor.org/rfc/rfc9111.html#section-5.2.1.4)

### Run both checks on the recorded demo

Use the [approved Captions walkthrough](examples/uae-bilingual-video-editing/product-demo.mp4) and the [earlier cut](examples/product-demo-refresh/earlier-cut.mp4). Both MP4s can play. Only the approved version serves the expected file. With the repository checked out, run these commands from its root.

```sh
valmera_demo=https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/examples
valmera_approved=docs/examples/uae-bilingual-video-editing/product-demo.mp4
python3 docs/evaluation/verify_published_demo.py --approved "$valmera_approved" "$valmera_demo/uae-bilingual-video-editing/product-demo.mp4"
python3 docs/evaluation/verify_published_demo.py --approved "$valmera_approved" "$valmera_demo/product-demo-refresh/earlier-cut.mp4"
```

The first command returns `match` (exit 0) at **1,016,111 bytes**. The second returns `different` (exit 1). Play the source and both cuts to see why checking that the file opens is only one part of approval.

## Brief a pilot before assigning the full library

> Refresh the published “Invite a teammate” walkthrough using our new Settings recording. Keep the approved introduction and confirmation unless the new screen makes either inaccurate. Include the click and the result, update the spoken instructions and captions where the UI changed, and send one reviewed MP4, the revised caption file, and a chapter map with the old and new positions. Tell us which existing links or exports need an update.

Use the approved pilot to estimate recurring scope. List the number of walkthroughs, replacement sections, caption languages and downstream copies. Decide who checks timing after the edit and who replaces and verifies the file on each live destination.

**[Scope recurring demo refreshes with Valmera Enterprise](https://valmera.io/subscribe?inquiry=product-demo-video-editing-service&utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=published_demo_refresh#enterprise)**. Include one old link, what changed and when you need the replacement. If the contact page is unavailable, [email the same brief](mailto:support@valmera.io?subject=Enterprise%20editing%20inquiry%20-%20product%20demo%20refresh).

For a self-serve edit, [record a clean demo from a public URL or bring your own capture](https://valmera.io/tools/record-website-demo?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=published_demo_refresh). Hosted AI editing requires eligible paid access.
