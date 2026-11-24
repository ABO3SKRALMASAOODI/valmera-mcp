# Record a keyboard-only software tutorial with visible focus

A keyboard walkthrough needs to show both the key and the control it affects. If you cut from a dialog straight to the next screen, a learner may miss where focus returned and press the next key on the wrong control. Show the focus change and the outcome in the downloaded MP4.

[Download the keyboard practice page](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/evaluation/keyboard-demo/keyboard-walkthrough.html) as an HTML file and open it in a browser. It is a single file with no network requests. Use it to rehearse the source recording, then run the test again on the software your viewers will use.

## Capture five keystrokes as one continuous take

Start with fresh focus in the page, no dialog open and **Ready to review** visible. After each key, hold long enough to identify the focused control. If the first Tab goes to the browser toolbar, move focus into the page before recording.

| Key | Keep visible in the recording |
| --- | --- |
| Tab | The outline appears around **View export settings**. |
| Enter | The **Export settings** dialog opens. The outline appears around **Cancel**. |
| Escape | The dialog closes. Focus visibly returns to **View export settings**. |
| Tab | Focus moves to **Continue to review**. |
| Enter | The page reports **Review opened for Updating a shared report**. |

For a second take, open the dialog and press Tab to move from **Cancel** to **Confirm settings**. Press Enter to close it and show **Export settings confirmed**. The two takes end differently. The first shows what happens when the learner dismisses the dialog. The second shows a confirmed choice.

The visible focus ring in this small practice page is deliberate. Your own application may choose a different initial control or a different destination when the opener no longer exists. Check what the learner will actually see. For the interaction pattern and exceptions, see [W3C's modal dialog guidance](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/).

## Give an editor two requests they can verify

> Cut the keyboard-only recording into a short lesson. Show five keys in order: Tab, Enter, Escape, Tab, Enter. Add each key label when its action happens and keep the focused control in frame. Keep the **Ready to review** state at the start and the **Review opened** message at the end. Leave the pointer still.

> Shorten the pause after the dialog closes. Keep enough of the returned focus on **View export settings** to show where the next Tab starts. Preserve the focused **Continue to review** button and the last status message. Export a new MP4 and retime separate captions if the request changes their timestamps.

Download both versions. Play the revision at the size learners will see. At the Escape cut, pause where the ring returns to the opener. Resume and check that the next outline is on **Continue to review**. If the video uses a zoom, show both controls without cutting off the ring. Keep the label **Escape** clear of the dialog and both surrounding controls. Ask a teammate to reproduce the task from the revised MP4 alone.

## Choose the capture and editing route

- **Public demonstration page.** Valmera's website recorder documents a scripted `press` action, including Tab and Enter. Review the exported MP4 for visible focus in the page's initial state, then use labels or narration if the keys need explanation. The capture is silent. [Valmera website demo recorder](https://valmera.io/tools/record-website-demo?utm_source=github.com&utm_medium=referral&utm_campaign=keyboard_tutorial).
- **Signed-in software.** Record your demo account with a local screen recorder and supply that recording to the editor. Use fictional lesson names and keep account menus and private records out of the take. [OBS quick start](https://obsproject.com/kb/quick-start-guide) · [Valmera screen recording workflow](SCREEN-RECORDING-TUTORIALS.md).
- **Recurring training work.** Start with a keyboard-only take and a mouse-driven take on the same workflow. Ask the service to deliver two MP4s, the caption files you need for your player and one revision of only the keyboard version. Agree who will check the final controls and captions in your learner's player. [Ask Valmera Enterprise about recurring training edits](https://valmera.io/subscribe?inquiry=keyboard-training-tutorial&utm_source=github.com&utm_medium=referral&utm_campaign=keyboard_tutorial#enterprise).

The practice page uses fictional data and needs no account. Use it to rehearse the tutorial handoff. Run accessibility tests on the real application separately.
