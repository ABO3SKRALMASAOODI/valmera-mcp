# Record a product demo from localhost before launch

Run your app on your own computer, capture the feature in a local browser, and export the recording as an MP4. The app can stay on `127.0.0.1` while you prepare a product launch, review a release branch, or film a feature that needs demo data. If your editor runs in the cloud, give it the recording after capture. Its own `localhost` is a different machine.

## Watch the difference between selecting and saving

This example runs a fictional digest settings screen on a loopback address. Both recordings select **Weekly**. The first still says **Saved schedule: Monthly** beneath the dropdown. The second clicks **Save changes** and holds on **Saved schedule: Weekly**. The public files are the MP4s from the local browser. In the saved clip, the final state stays visible for 2.36 seconds. The fixture updates its displayed state in memory, so it demonstrates the on-screen check. For an app with persistent settings, reload the page to verify that the saved value survives.

| Capture | Visible evidence | Review decision |
| --- | --- | --- |
| [Selection only](examples/localhost-product-demo/01-selection-only.mp4) | Dropdown shows Weekly. The saved status remains Monthly. | Request the save step before using the clip in release materials. |
| [Selection saved](examples/localhost-product-demo/02-selection-saved.mp4) | Dropdown and saved status both show Weekly. | Use the clip to demonstrate the setting change. |

[Compare the final frames side by side](examples/localhost-product-demo/result-comparison.jpg). The [capture fixture](examples/localhost-product-demo/preview.html), [recorder](examples/localhost-product-demo/record.mjs), and [file measurements](examples/localhost-product-demo/measurements.json) are included.

## Choose a capture route

| Situation | Route to try | Ask for this in a paid pilot |
| --- | --- | --- |
| The product is still on your laptop and a developer maintains the walkthrough | Run a local browser recording using Playwright. A browser context saves the video when it closes. [Playwright video recording](https://playwright.dev/docs/videos) | Keep the script beside the feature and assert the saved state after the click. Re-run it on the next release. |
| You want a tool that documents capture from a local URL | LittleDemo documents local CLI recording, including `localhost`, with optional hosting. [LittleDemo CLI documentation](https://docs.littledemo.com/cli/record) | Record the demo without uploading it during the first review. Check what the tool writes locally and what happens when publishing is enabled. |
| Your recording workflow runs remotely | Screen Browser documents using a reachable URL for cloud capture of a local app. Give that workflow a controlled demo environment your team has cleared for access. [Screen Browser local-app documentation](https://screenbrowser.com/docs/local-apps/) | Verify the recorder can reach the exact build and the demo account only contains sample records. |
| You already have footage and need an edit for launch, sales, or onboarding | Give Valmera or your editor the capture, the exact saved state, and the required output sizes. Include an untouched recording for later revisions. [Valmera’s website demo workflow](WEBSITE-DEMO.md) | Watch the exported cut. Confirm that the click and resulting label are both readable at the delivery size, especially in a portrait version. |

## Repeat the example on your machine

In a checkout of this repository, install the example’s dependency in `docs/examples/localhost-product-demo`. The recorder uses Node.js 22 or later, Google Chrome, and FFmpeg with H.264 encoding.

```sh
cd docs/examples/localhost-product-demo
npm install --no-save --package-lock=false playwright@1.65.1
npx playwright install ffmpeg
node record.mjs
```

The script starts a temporary loopback server and opens a separate browser context for each take. The browser test checks the input and saved label independently. It closes the context to finalize each capture, then writes the MP4s and screenshots to `localhost-demo-output`. Supply an output directory as the first argument or set `FFMPEG` to the path of your encoder if it is outside your shell’s path.

## Hand off the edit for a real release

Give the editor the build identifier, the starting screen, the action and the exact evidence you expect after it. For this release, keep the saved status on screen long enough to read it at normal speed. If you remove a wait or add a zoom, watch the exported file again and check that the result still follows the actual action. For a monthly batch, include one recurring workflow and one change request in the pilot. Send the expected number of videos, formats, and first publish date to Valmera Enterprise. [Request a recurring editing quote](REQUEST-ENTERPRISE-VIDEO-EDITING.md)
