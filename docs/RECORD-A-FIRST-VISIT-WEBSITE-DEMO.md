# Record a website demo when a first-visit notice covers the page

A product demo can work in your everyday browser and fail in a new capture session. A welcome notice or cookie dialog can appear before the button your script expects. Record from the same initial state you want to show, then use the finished MP4 to verify the click and the page it opened.

[Save the practice page as HTML](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/evaluation/first-visit-demo/first-visit.html) and open the local file in a browser. It models two starting states with fictional data. It makes no network requests and stores no preferences.

## Run the same task from two starting states

| Starting state | Action to film | Evidence to keep |
| --- | --- | --- |
| Clear page | Select **Open report preview**. | The button is visible before the click and **Monthly report preview ready** appears after it. |
| First visit with a notice | Use **Continue with required settings**, then select **Open report preview**. | The notice closes, the report button is available and the same result appears. |

In the second run, press Tab while the practice notice is open. Focus moves to **About this practice notice** inside the dialog. The report button is present under the backdrop, but a pointer action cannot reach it. In a real capture that can look like a script that clicked the right label and still failed. Check the starting frames and which control actually received the action.

## Describe the initial state in your script

> Record this public page in a fresh browser. Hold on the opening state. If the site offers its standard required-settings choice, use that visible control, wait for the notice to close and show the page before the next click. Open **[the actual product control]**, then hold on **[the visible confirmation or destination]**. Keep the click and the result in the edited MP4.

Use the text that appears on the site. If a capture tool only records a fixed sequence, check a rehearsal first and include the notice action only for the version that needs it. Give the editor the source recording and the two expected states when working from an uploaded capture. For a signed-in demonstration, record a demo account in a local recorder and avoid showing credentials.

## Review the result after editing

1. Start the exported MP4 from the beginning. Watch at the size your audience will see.
2. Check whether the first action matches the stated starting state. If you trim a notice from the published version, begin the edit on a clear page after it closes.
3. Pause at the main click. Check the visible target and the pointer position.
4. Resume to the held result. Verify the resulting page or actual status message. A title card alone cannot establish that the workflow succeeded.
5. Compare the source event log where available. In [Valmera’s public browser capture](https://valmera.io/examples/website-capture), you can check the documented click at about 3.6 seconds and the destination at 4 seconds. That example illustrates checking the action and its result.

## Choose which workflow to test

| Route | What to test with your own public page |
| --- | --- |
| [Valmera website demo recorder](https://valmera.io/tools/record-website-demo?utm_source=github.com&utm_medium=referral&utm_campaign=first_visit_website_demo) | Supply a public URL and explicit click, scroll and wait steps. Check the starting frame, click and destination in the capture, then revise the result in the editor and export an MP4. Check eligible plans before starting. |
| [Tella Auto Capture](https://www.tella.com/auto-capture) | Give the capture agent the opening state and final screen you want. It plans the browser steps. Review the delivered recording in Tella and check that it shows both states. |
| [DemoBot](https://getdemobot.com/demo-video/software) | Read the proposed browser plan before filming. See whether its planned opening matches the viewer’s first visit and whether the rendered MP4 shows the final page. |
| [Demofy](https://demofy.io/) | Check the editable script before recording and use the same starting-state brief if you re-record after the interface changes. |
| Local screen capture plus an editor | Start from your chosen demo browser state and record the action yourself. Before handing off the source, write down the target and the result that must survive the edit. |

Provider workflows are based on their official documentation. The downloadable page is for rehearsal and checking the behavior of the two starting states. Test each production recorder on your own approved public page to establish how it handles that site.

For a team editing a series of software walkthroughs, include one clear opening and one first-visit opening in the brief. Ask for a draft and a targeted revision on each so your approver can check the first action and the final screen. [Discuss a recurring editing pilot with Valmera Enterprise](https://valmera.io/subscribe?inquiry=website-demo-capture&utm_source=github.com&utm_medium=referral&utm_campaign=first_visit_website_demo#enterprise).
