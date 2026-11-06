# Keep webinar slides readable in vertical video

A vertical crop can keep the presenter in frame while removing the evidence they are explaining. For slide-heavy webinar clips, choose the layout around the **specific chart, labels and spoken point**, then inspect the exported video at its intended viewing size.

Use this guide with the [webinar replay-and-clips workflow](WEBINARS.md). It covers framing decisions and review requests for Valmera; it is not a product benchmark. You can apply the same review method to any editor.

**Start an edit:** [connect your assistant](https://valmera.io/mcp/setup), identify the recording in [Valmera Studio](https://valmera.io/studio), and use the current tool schemas. Account creation and uploads are free; editing requires a [subscription](https://valmera.io/subscribe). Your assistant provider's charges are separate.

## 1. Decide what the viewer must be able to read

Before choosing 9:16, write one sentence describing the clip's point. Then identify the visible evidence needed to understand it.

For example: “The chart shows retention improving after onboarding changed.” The viewer may need the series labels, time axis, vertical scale and the date of the change. A close-up of the rising line alone can hide the baseline or make a small movement look dramatic.

Use a frame from the actual source to mark:

- The region containing the relevant evidence.
- The title, units, legend, filters or qualification that must remain visible with it.
- Any caption or presenter area that could cover that region.
- Whether a higher-resolution original slide is available.

Ask your assistant to inspect the frame and propose the layout before changing the project:

> Inspect [source project and version] at original source [time]. Our clip must explain [one-sentence point]. Identify the chart or interface region and every label, unit and qualification needed to understand it. Propose a full-slide view and a focused detail view. Explain what each crop would omit. Do not change the edit yet.

A screenshot cannot reveal information missing from the recording. If a label is already illegible in the source, request the original slide or a clearer recording. Enlarging that raster does not recover the missing detail.

## 2. Understand why “fit the whole slide” can still fail

Here is a **geometric teaching example**, not a measured export. Assume a 1920 × 1080 source slide, square pixels, no extra margins, and a 1080 × 1920 portrait output. A small label occupies approximately 24 source pixels in height.

When the entire slide fits the output width, its scale is 1080 ÷ 1920 = 0.5625. The slide becomes about 1080 × 608 pixels; the label becomes about 13.5 pixels high. If the video is displayed at 360 CSS pixels wide, that label is about 4.5 CSS pixels high.

Putting the presenter below the slide does not increase the slide's width. A larger vertical canvas can add space around the slide without making its small labels larger.

| Region fitted to the same 1080-pixel output width | Scale from source | Approximate height of that 24-pixel label in the export | At a 360-CSS-pixel-wide display |
| --- | --- | --- | --- |
| Whole slide, 1920 pixels wide | 0.5625× | 13.5 pixels | 4.5 CSS pixels |
| Detail region, 960 pixels wide | 1.125× | 27 pixels | 9 CSS pixels |
| Detail region, 640 pixels wide | 1.6875× | 40.5 pixels | 13.5 CSS pixels |

The narrower regions enlarge the label by omitting surrounding content. That is useful only if the chosen region still contains the evidence and its necessary context. These numbers are scale estimates, not readability thresholds. Font shape, contrast, source quality, compression and viewing conditions still matter; inspect the actual file.

A full-height fill crop has a different trade-off. Filling this portrait frame from the same landscape source shows only about **608 of the source's 1920 horizontal pixels**, or **32% of its width**, at any one moment. A centered crop can discard a legend on one side and an axis label on the other.

## 3. Choose a layout for each part of the explanation

| Situation | Layout to try | What to check |
| --- | --- | --- |
| Speaker introduces the topic | Presenter view or full-slide overview | The viewer knows what the clip is about before the detail appears. |
| One chart or interface control carries the explanation | Focused detail, with enough surrounding labels | Units, axes, legend, selected state and qualifiers survive. |
| Speaker compares distant parts of a slide | Overview followed by separate detail views | The sequence preserves the comparison; it does not imply that unrelated values belong together. |
| Dense slide needs to be read as a whole | A clearer original slide, a longer reading hold, or a landscape version | Test the actual viewing size, including landscape orientation where appropriate. |
| Presenter and screen both matter | Screen-first composition with a smaller presenter area | The presenter and captions do not cover the evidence. |

A landscape deliverable is an option, not an automatic readability fix: a wide slide displayed in a small portrait feed can still be tiny. Check how the intended player displays it. If the information cannot be understood in the chosen format, simplify the excerpt or deliver it in another format instead of hiding essential context.

Use only approved source material. Replacing a chart with an original slide should preserve the spoken claim, version, units and dates. If the source and slide disagree, resolve the difference before publishing.

## 4. Brief a twelve-second explanation with two views

This hypothetical clip uses original source **12:10–12:22** at unchanged speed. Its own output clock starts at zero. Its 12-second program contains no added-duration cards or transitions; any end card added at export comes after 00:12 and does not change these times.

| Clip output clock | Original source clock | Framing decision |
| --- | --- | --- |
| 00:00–00:03 | 12:10–12:13 | Show the full slide to establish the topic. |
| 00:03–00:08 | 12:13–12:18 | Show the approved detail region while the speaker explains it. |
| 00:08–00:12 | 12:18–12:22 | Return to the overview for the conclusion. |

The durations total 3 + 5 + 4 = 12 seconds. This is a planning pattern, not a prescription to give every slide three seconds. Let the explanation and a real reading check determine the holds.

After approving the region and viewing the proposed crop, adapt this request:

> Create a separate 9:16 clip from source [12:10–12:22] in [source project and version], preserving the source project. At normal speed, use a full-slide overview for clip [00:00–00:03], the approved detail region for [00:03–00:08], and the overview again for [00:08–00:12]. Keep [name the axes, legend, units and qualification] visible whenever that detail is shown. Put captions in a separate clear area, without covering the evidence or making the slide smaller than our reviewed layout. Preserve the original speech and its meaning. Discover the current tools; if they cannot create a separate clip without changing the source project, tell me instead of editing it. Render a preview, and return the clip project/version and source-to-output map.

The bracketed timestamps belong to this example. Replace them with the ranges and approved layout from your recording. Caption placement may require a different composition; ask the assistant to explain a conflict instead of silently shrinking the slide.

## 5. Review the same moment in the source, preview and export

Choose a point inside the detail view and compare the same source moment across files. In the example, original source 12:16 is clip output 00:06. Comparing unrelated frames can conceal a framing error.

Check the downloaded export as well as the preview. The preview may use a smaller encode; the final file can also be affected by scaling, compression or destination playback.

| Review check | Pass only when… | If it fails |
| --- | --- | --- |
| Evidence | The relevant labels, units, baseline and qualification are present. | Widen or reposition the approved region; use another layout if needed. |
| Reading | You can read the necessary text at the intended playback size without pausing to zoom. | Use clearer source material, a more focused view, more time or another format. |
| Caption placement | Speech captions remain readable and clear of the chart or controls. | Move captions or revise the composition, then inspect both. |
| Sequence | View changes follow what the speaker explains and allow enough time to understand it. | Adjust the holds against the actual audio. |
| Meaning | Cropping and shot order do not change the apparent claim. | Restore the missing context and review the whole explanation. |
| Delivery | The final file plays correctly, including sound and ending, and any published player preserves readability. | Correct the specific file or publishing configuration and check again. |

For a focused correction, name the version, clock and invariant parts:

> In [clip project and reviewed version], at clip output [00:03–00:08], the right-hand legend is outside the frame. Revise the detail framing to include [legend text] and [required axes/units]. Keep the speech, cuts, speed and program duration unchanged. Keep captions readable and clear of the evidence. If the wider region makes the labels unreadable at our target size, propose a different composition rather than treating “nothing is cropped” as success. Render a new preview and identify the new version.

This is a layout change. If it leaves the cut timing unchanged, its source-to-output map should remain unchanged too. Inspect the result; do not infer that the replay or other clips changed with it.

## 6. Keep a small review record

Copy this table into your delivery notes. Record failures as failures, and keep the exact file associated with the review.

| Item | Your record |
| --- | --- |
| Source project/version and source moment | |
| Clip project/version and matching output moment | |
| Intended destination, aspect ratio and viewing size | |
| Required labels, units and qualification | |
| Source quality or original-slide limitations | |
| Preview checked; findings | |
| Exported filename; findings | |
| Published-player check, if published | |
| Correction requested and resulting version | |
| Reviewer and date | |

For the next step, use the [webinar edit pack](https://valmera.io/downloads/webinar-replay-edit-pack.txt) to track the replay and each clip separately. [Open the webinar guide and starting briefs](https://valmera.io/use-cases/webinars?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=slide_readability#webinar-briefs) or [build a brief for your footage](https://valmera.io/prompts#prompt-builder).

Maintained by Valmera. The dimensions, label size and twelve-second sequence are illustrative. For an actual original-source and exported-file record, see the [trim-and-reframe example](https://valmera.io/examples/trim-and-reframe); it demonstrates a square crop, not slide readability in a real webinar.
