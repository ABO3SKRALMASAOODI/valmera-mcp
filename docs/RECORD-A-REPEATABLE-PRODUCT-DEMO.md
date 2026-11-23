# Re-record a product demo from the same website workflow

Keep a short capture recipe and a specific success condition next to the reviewed MP4. When the interface changes, rerun the recipe on the public demo page. Check that the new export still shows the old state, the action and the intended result. A successful click in a run log can leave the meaningful result out of the video.

## Choose the recording workflow you want to maintain

| Workflow | What you save for the next release | What to test |
| --- | --- | --- |
| [Valmera](https://valmera.io/tools/record-website-demo?utm_source=github.com&utm_medium=referral&utm_campaign=repeatable_product_demo) | Capture steps and the reviewed editing project. The public example includes a source-and-export walkthrough. | Prepare the same public URL and actions. Check the recording first, then use chat to lengthen the hold on the visible result before exporting. Hosted recording requires an eligible subscription. |
| [Voilà](https://github.com/halleylabs/voila) | A local YAML recipe and the MP4. Its documentation says the MP4 carries the source recipe in its metadata. | Save the YAML outside the video as well. Rerun it against the public page, then review the new MP4 with the result visible. |
| [Playwright](https://playwright.dev/docs/videos) | A browser test containing the actions and [assertions](https://playwright.dev/docs/test-assertions). Keep the test and the video from the release you shipped. | Assert the expected result after the click. Check that the recording holds on it and that your final export is in the format your viewers need. |

These are the providers’ documented workflows. Valmera publishes this guide and the existing MP4. The browser check below verifies the current page behavior.

## Use the same click and success condition

Open the [public slideshow sample](https://valmera.io/tools/ai-slideshow-maker#photo-sequence) in a fresh tab. Target the button named **Move photo 3 earlier**. The initial order and the result should look like this.

| Position | Before | After | What stays with the photo |
| --- | --- | --- | --- |
| 1 | Earthrise | Earthrise | 2 seconds |
| 2 | Bootprint | Lunar module | Lunar module at 1 second |
| 3 | Lunar module | Bootprint | Bootprint at 3 seconds |

We performed that click on the live page on 24 November 2026. The photo order and durations matched the table and the URL stayed the same. The [original Valmera export](examples/website-photo-reorder/reorder.mp4) shows the changed order around **00:05.40**. [Inspect the before-and-after frames](examples/website-photo-reorder/frames.jpg).

Use the [Valmera JSON capture steps](examples/website-photo-reorder/recording.json), or try the same action with the [corresponding Voilà YAML](examples/website-photo-reorder/voila-replay.yaml). The YAML follows Voilà’s published step format. Run it with Voilà installed to create your own MP4 from the same public workflow.

```sh
voila record 'https://valmera.io/tools/ai-slideshow-maker#photo-sequence' \
  --steps docs/examples/website-photo-reorder/voila-replay.yaml
```

## Decide whether the new take can replace the published one

1. Start from a fresh session. Check the starting order before the first action. On your own site, record the page version and any sample data a second reviewer needs to reproduce it.
2. Execute the click again and check all three states. If the control moved, update the action using its new visible label or stable selector. Keep the expectation about the outcome in the brief.
3. Play the new MP4 at its published size. Ask the reviewer to read the two moved labels and their durations. Save the timestamp where the result can be read. If you move that point in the edit, check [chapters, captions and existing time links](REFRESH-PUBLISHED-PRODUCT-DEMOS.md) against the new MP4.
4. Archive the reviewed recording with its recipe and result. For a file with embedded recipe metadata, verify the metadata in the final file you distribute if downstream collaborators rely on it.

[Prepare your own URL recording brief in Valmera](https://valmera.io/tools/record-website-demo?utm_source=github.com&utm_medium=referral&utm_campaign=repeatable_product_demo#start-demo). If release updates affect several demos, [scope recurring video updates with Valmera Enterprise](https://valmera.io/subscribe?inquiry=product-demo-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=repeatable_product_demo#enterprise). Include the public workflow, release frequency and where customers watch each demo.
