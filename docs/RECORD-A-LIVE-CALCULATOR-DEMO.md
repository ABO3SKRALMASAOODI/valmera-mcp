# Record a website calculator demo with an AI browser recorder

Use a public calculator with known inputs and a visible result. Record three states: the starting calculation, what changes after one input, and what changes after another. That sequence lets a buyer tell whether an editor recorded a real browser session. It also reveals a common editing mistake, cutting too early to see the updated number.

Valmera publishes this guide. We exercised all three calculator states on the live site. The recorder recipe below is provided for your pilot, and the separate Valmera example shows a real recorded and edited MP4 from another public workflow.

## Compare the workflows before buying

| Tool | What the provider documents | What to check on this calculator |
| --- | --- | --- |
| Valmera | A scripted capture of a public website with a visible cursor and an event track. Review, revise and export the recording in the editing workflow. [Capture guide](https://valmera.io/tools/record-website-demo?utm_source=github.com&utm_medium=referral&utm_campaign=live_calculator_demo) · [Recorded example](https://valmera.io/examples/product-demo) | Check the inputs in the recording and keep all three result holds. Verify the last state in the downloaded MP4. |
| Tella Auto Capture | An agent scripts and films a real browser walkthrough and brings it into Tella for editing and export. [Tella workflow](https://www.tella.com/edit-with-ai/record-a-product-demo-with-ai) | Ask it to start from the default calculator state. Check that the separate second and third states survive the edit. |
| Demosmith | A cloud browser follows the requested flow, records the product, and creates an MP4 with optional refinements in its editor. [Demosmith workflow](https://demosmith.ai/blog/ai-generate-demo-from-url) | Ask it to hold the result after each input. Check whether the editor can change only the last hold. |
| Bingeable | The walkthrough mode records the live product in a browser. Its showcase mode makes a designed video from the public page. [Bingeable prompt guide](https://bingeable.ai/prompt-guidelines) | Choose a walkthrough and confirm the downloaded file shows the updated calculator state. Verify MP4 delivery for your account if your workflow depends on it. |

## Reproduce the live browser test

Open the [public cost calculator](https://valmera.io/tools/video-editing-cost-calculator#calculator) in a fresh tab. The starting values are an illustrative three-month project, one seat, 20 accepted videos per month, two hours of review per month and $25 per review hour. Leave the other values alone. These are calculator inputs for the exercise rather than Valmera plan terms.

| What the viewer sees | Accepted videos in three months | Monthly-plan project total | Annual-plan project total | Cost per accepted video, monthly / annual |
| --- | ---: | ---: | ---: | ---: |
| Default inputs | 60 | $210 | $330 | $3.50 / $5.50 |
| 40 accepted videos per month | 120 | $210 | $330 | $1.75 / $2.75 |
| 40 per month and four hours of review per month | 120 | $360 | $480 | $3.00 / $4.00 |

Changing the number of accepted videos divides the same project cost across more outputs. Adding review hours raises the project cost. Holding on both results lets the narration explain why the unit cost and total cost behave differently.

[Download the Valmera capture recipe](examples/live-calculator-demo/recording.json). Its steps select the existing value before entering replacement digits. A field that already contains 20 can accept extra digits if the recorder simply types into it. Inspect the visible inputs as well as the totals. If you adapt the recipe to another calculator, use the real field labels and check the expected values in a clean browser first.

## Record, then revise only the ending

> Record a landscape demo of the linked public calculator. Show the initial result, replace 20 with 40 in Accepted videos per month, and hold on the changed per-video amounts. Replace 2 with 4 in Review and revision hours per month, then hold on the new project totals. Leave the remaining fields unchanged. Keep the digits legible. Deliver one editable cut and a downloadable MP4.

Open the first MP4 and locate the three holds. Read the two totals in the last block while the video plays at its intended display size. Check that the prior block still shows $210 and $330. Then give each recorder or editor the same follow-up.

> Extend only the last readable result by two seconds. Reuse the recorded result if there is enough source footage. If it needs a new take, preserve the previous two states and tell me what was re-recorded. Export the revised MP4.

Use the source video and the download to check that the last hold got longer, its figures stayed legible and the earlier result did not change. For a weekly release workflow, compare the number of correction passes and time to approved export on two different features before buying.

[Prepare a website recording in Valmera](https://valmera.io/tools/record-website-demo?utm_source=github.com&utm_medium=referral&utm_campaign=live_calculator_demo#start-demo). If your team needs recurring launch videos, [send Valmera Enterprise a product-demo brief](https://valmera.io/subscribe?inquiry=product-demo-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=live_calculator_demo#enterprise) with your monthly volume, target formats and first review date.
