# Record a website form demo without submitting real data

A useful onboarding demo shows what to type, where validation appears, and how viewers know they can continue. Decide where the recording stops before you start. End on a visible, readable state. Show a receipt or confirmation only when it comes from a demonstration workflow that actually produced it.

## What we observed on a live form

We opened [Valmera's public website demo brief](https://valmera.io/tools/record-website-demo#start-demo) in Chromium and filled the website field while leaving the Continue button untouched. The form enabled Continue for both a malformed string and a correctly formatted example address. That one change in the button was an insufficient indicator of address validation.

| Input before clicking Continue | Observed button state | What you can show in the recording |
| --- | --- | --- |
| [Empty field](examples/website-demo-form-states/01-blank.png) | Disabled | The field a user is expected to complete. |
| [Malformed text](examples/website-demo-form-states/02-invalid.png) | Enabled | Text was entered. The form displayed its same address instruction. |
| [Well-formed example address](examples/website-demo-form-states/03-example-domain.png) | Enabled | The intended example text is visible. The user still needs to continue to the next step. |

The page stayed at the same URL. This test checks the UI states before submission. [Browser measurement record](examples/website-demo-form-states/measurements.json)

## Practice on a form that displays validation as you type

Download [the local practice page](examples/website-demo-form-states/local-demo.html) and open the file in your browser. It has no form submission and blocks network requests. Start with a blank field. Enter `not a url` so the format error is visible, then replace it with `https://example.com` and hold on **Address format accepted**. The example domain is reserved for documentation. Leave the Preview button untouched if the job is to demonstrate how far the user can get before acting. [IANA example domains](https://www.iana.org/help/example-domains)

| Before filming | What to specify |
| --- | --- |
| Input | Use a sample value your team approves. Replace real addresses, names, project IDs and saved autofill entries. |
| Error state | Include the exact message or cue the viewer should see. If the production form validates on submission, use a demonstration environment that can show that state safely. |
| Stop condition | Name the last result to keep on screen and the final control to leave untouched. |
| Export | Ask the reviewer to read the message and identify the final state in the downloaded MP4. An enabled button alone may only mean a field contains text. |

## Send a brief with a clear stop point

> Start on [approved public or staging URL]. Show the blank [field label]. Enter [approved invalid demo value] and hold on [exact validation message], if the staging form shows it before submission. Replace the value with [approved example value] and hold on [expected ready cue]. Stop before activating [submit control]. Keep the label, field and message visible in the MP4. Show the preview and return the time each state appears.

Use a public page for URL capture. For a local file or authenticated staging session, record the approved screen yourself, then provide the video for editing. Frame only the demo and use a clean browser profile so saved details and notifications stay out of the recording. If you claim a form sent a request, created a booking, or displayed a receipt, also show that result from the demonstration environment.

**[Prepare a website demo brief in Valmera](https://valmera.io/tools/record-website-demo?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=website_demo_form_states#start-demo)**. Brief preparation is free. New URL recordings in Studio require an eligible plan. If your team needs a series of onboarding videos, [scope a done-for-you pilot](https://valmera.io/product-demo-video-editing-service?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=website_demo_form_states) with the steps, sample inputs, delivery formats and approval deadline.
