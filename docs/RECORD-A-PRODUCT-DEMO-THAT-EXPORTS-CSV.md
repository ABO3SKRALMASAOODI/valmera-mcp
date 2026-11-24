# Record a product demo that proves a CSV export worked

For a software walkthrough that promises a download, check two things. The video should show the requested report, the export action and the resulting confirmation. A separate file check should establish that the browser saved the expected file and that its rows match the selected report. A toast can tell the viewer that a download started. The saved file establishes what actually arrived.

## Try the same export with any recorder

[Download the offline demo workspace](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/examples/demo-csv-download/export-demo.html), save it as an HTML file and open it in a regular desktop browser. It uses fictional activity data, runs locally and needs no account. Record your tab or use your recorder’s supported test environment. For a recorder that accepts only public URLs, run the same brief on a public test page your team controls.

1. Select **Nov 16–22, 2026** under **Report week**.
2. Click **Export CSV**. The fixture shows **Preparing report…** briefly so you can test the edit around an intermediate state.
3. Hold on **Download started for activity-2026-11-16.csv (2 rows)** for at least two seconds in the finished edit. This confirmation appears in the page itself, where a tab recorder can see it.
4. Open the saved file outside the recording. The header should read `week_start,action,count`. The two rows should be `2026-11-16,Reviewed,27` and `2026-11-16,Published,6`.
5. Switch weeks and repeat. Nov 9–15 should save `activity-2026-11-09.csv` with 19 reviewed and 3 published. This catches demos that show a valid file from the wrong week.

If your buyer needs to see the CSV in the video, open the saved file in a clean spreadsheet window or tab and capture that view separately. Check that cursor callouts and captions leave the header and counts readable. Record with a fresh browser profile and sample data so your downloads history, local paths and other files stay out of shot.

## Edit the walkthrough by prompt

Upload the screen recording to Valmera and give it an observable brief.

> Make a short walkthrough from this recording. Keep the Nov 16–22 report selection, the Export CSV click and two seconds on the in-page confirmation. Shorten the wait between the click and confirmation. Keep the filename readable. If the recording includes a separate shot of the opened CSV, show the header and both rows. Use “download started” over the confirmation and reserve “verified CSV” for the shot of the opened file.

Review the exported MP4 at its actual delivery size. Run a revision that shortens the opening while keeping the report selection and result intact. [See how to make a website demo](https://valmera.io/tools/record-website-demo?utm_source=github&utm_medium=referral&utm_campaign=demo_csv_download_pilot). Editing the footage requires a subscription.

## What counts as a passed pilot

| Check | Evidence |
| --- | --- |
| The viewer can repeat the action | The week, Export CSV control and confirmation are all legible in the finished video. |
| The download came from the shown report | The downloaded filename and every CSV row carry the selected week. |
| The edit survives a revision | The revised MP4 still shows the click and two seconds of confirmation and preserves any separately captured CSV proof. |
| The flow is repeatable for the next release | Another reviewer can follow the same brief and obtain the same result using the fixture. |

For a recurring editing pilot, send Valmera Enterprise one source recording, your delivery size, the steps that must survive each edit, and the number of demos you publish per month. Ask for a short first delivery and judge it against the same checks. [Contact Enterprise from Valmera’s subscribe page](https://valmera.io/subscribe?utm_source=github&utm_medium=referral&utm_campaign=demo_csv_download_pilot&inquiry=product-demo-video-editing-service#enterprise).
