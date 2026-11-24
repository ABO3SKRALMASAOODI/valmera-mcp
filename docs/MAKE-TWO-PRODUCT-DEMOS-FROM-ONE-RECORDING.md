# Make a sales demo and an onboarding video from one screen recording

Approve the action and result once, then make a separate version for each audience. Sales viewers need a reason to request a walkthrough. New customers need the next step inside the product. Give each version one job and one ending. When a reviewer changes the sales ending, check that the approved action and result still play the same way.

[Start a demo from a public URL or an existing recording](https://valmera.io/tools/record-website-demo?utm_source=github.com&utm_medium=referral&utm_campaign=shared_demo_cta_variants#start-demo)

## Compare workflows for reusing a recorded demo

| Workflow | What the vendor documents | What to verify before buying |
| --- | --- | --- |
| [Tella reusable clips](https://www.tella.com/features/reuse-video-clips) | Bring an existing Tella clip into another video and edit it there. | Check how to reuse the approved clip, change only one ending and deliver the two files separately. |
| [Wistia editor](https://support.wistia.com/en/articles/15177441-getting-started-with-the-editor) and [player CTA](https://support.wistia.com/en/articles/8283756-call-to-action) | Edit hosted media and set a call to action in the Wistia player. | Test the link in the actual hosted player. If the sales team needs a standalone MP4, open the downloaded file and check how viewers will reach its destination. |
| [Valmera](https://valmera.io/tools/record-website-demo) | Start with a public URL or upload a recording and describe the cut to make. Review and export your selected edit. | Request two named MP4s with the same approved source range and different end cards. Change one CTA and re-check both deliveries. |

Valmera publishes this guide. The descriptions reflect vendor documentation. The sample below combines a public Valmera screen capture with locally assembled end cards.

## Inspect three MP4s with the same approved footage

In the shared clip, the **Earlier** control moves Lunar module ahead of Bootprint. The result stays visible and the item durations remain attached. The audience-specific end card starts at **00:05.60**. The label shown inside each MP4 is part of the picture. Put any clickable destination in the host, page or email that delivers the file.

| Export | What viewers see after the result | Where to test the real next step |
| --- | --- | --- |
| [Sales, first pass](examples/demo-cta-variants/sales-first.mp4) | “Review a sample project” | Verify the linked example opens for a prospect without a workspace. |
| [Sales, revised](examples/demo-cta-variants/sales-revised.mp4) | “Book a guided walkthrough” | Open the scheduling link in the delivery page or email and verify availability. |
| [Onboarding](examples/demo-cta-variants/onboarding.mp4) | “Open your slideshow” | Open the handoff as a signed-in customer in a test workspace. |

All three files run **8.60 seconds at 30 fps**. The first **168 decoded frames** match across all three. Only frames **168–257** change in the sales revision, counting from zero. The files are silent to isolate picture and version differences. [Original recording and shared clip](MAKE-A-MUTED-PRODUCT-DEMO-LOOP.md) · [Frame hashes and file measurements](examples/demo-cta-variants/measurements.json)

## Run the same two-version pilot with a vendor

> Use the approved product clip up to and including the visible result. Make a landscape sales MP4 ending with “Review a sample project” and an onboarding MP4 ending with “Open your slideshow.” Keep the source range, speed and framing the same. After review, we will ask you to change the sales card only. Return distinct, versioned filenames and report where the end card starts.

1. Open the downloads and review the action and result before each card. For a narrated job, listen through the join and confirm that the new ending starts after the approved explanation.
2. Send one change to the sales copy. Keep the onboarding file that you approved. Compare the two versions of the sales file around the card boundary.
3. Open the actual emails, embeds or lesson pages with test access. Click the external action and verify the correct destination for each audience. Check for destination changes during later releases.

[Prepare both demo variants in Valmera](https://valmera.io/tools/record-website-demo?utm_source=github.com&utm_medium=referral&utm_campaign=shared_demo_cta_variants#start-demo). Hosted AI editing requires an eligible subscription. For a release calendar with several variants per month, [scope an Enterprise editing pilot](https://valmera.io/subscribe?inquiry=product-demo-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=shared_demo_cta_variants#enterprise) with one approved recording, the audiences, the intended destinations and the first review date.
