# Edit screen recordings with AI without losing the steps

A useful software tutorial lets someone repeat the task. Its edit must preserve three things for each step: **the starting state, the action and the visible result**. Removing a silent pause is helpful when it removes waiting; it is harmful when it removes the only view of a setting the viewer must copy.

This guide shows how to brief an AI video editor, plan cuts, review zooms and revise a tutorial without losing that chain. The worked example is fictional teaching material, not a recorded Valmera test or a performance claim.

[Build a brief for your recording](https://valmera.io/prompts?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=screen_recording_tutorials#prompt-builder) · [Connect Valmera to your assistant](https://valmera.io/mcp/setup) · [Current plans](https://valmera.io/subscribe)

Valmera edits uploaded footage, including through its hosted MCP connector. Use an authorized client and discover its current tools before editing. Account creation and uploads are free; AI editing requires a subscription. Your assistant's availability and charges are separate.

For another-language subtitles with the original voice, use the [software-tutorial subtitle handoff](TUTORIAL-SUBTITLE-HANDOFF.md): visible UI labels, conditional instructions, revisions and delivery files.

For a tutorial delivered inside a course, use the [course lesson guide and review worksheet](COURSE-LESSON-EDITING.md) to track prerequisites, practice material, caption versions and the learner-facing release.

## Start with the viewer's task

Write the finished outcome before asking for a faster cut: “A first-time user can filter this demo report by month, apply the filter and confirm the saved result.” That gives the editor a reason to preserve the month picker and confirmation screen even if neither contains speech.

Record the application's version or recording date, starting screen, required account role and any prerequisite setup. Use a demonstration account and sample data when recording. If a prerequisite happens outside the recording, explain it in the introduction rather than implying that the filmed steps are sufficient on their own.

Keep the original capture. A native recorder project may contain separate camera, microphone or cursor tracks that a flattened MP4 does not. An imported MP4 contains only the pointer that was rendered into it, if any; do not assume that a new editor can independently restyle it or recover click events. Ask what the actual file and current editing tools support.

## Make a step map before removing pauses

For each important step, identify the frame before the action, the action itself and the resulting state. A transcript is useful for speech; it cannot, by itself, prove which field was selected or whether the save succeeded.

| Step | Starting state to preserve | Action to show | Result to verify |
| --- | --- | --- | --- |
| Choose month | The report and the currently selected period | Open the month picker and choose April | April appears in the selected-period field |
| Apply filter | April remains selected; Apply is available | Activate Apply | A loading state begins, then the report changes |
| Verify result | The updated report is visible | Inspect the period label and save indicator | April is still selected and the saved state is shown |

The labels above belong to the fictional example, whose application saves the applied filter automatically. Replace them with the wording and states in your recording; include a separate save action if your application requires one. If the source never shows the result, flag the missing evidence. A decorative check mark is not a substitute for the application actually confirming success.

Ask for the map first:

> Inspect [recording and project version]. The audience is [viewer] and the tutorial must teach [task]. Identify the required starting state, visible action and result for each step, with original source times. Mark repeated takes, loading waits and missing evidence separately. Preserve necessary silent actions as well as spoken instructions. Propose a cut plan before editing; do not invent a successful outcome that the recording does not show.

## Worked example: shorten a 76-second recording to 58 seconds

Assume one continuous recording at normal speed. Its source clock starts at zero. The source contains an uninterrupted silent loading wait from 00:24 to 00:46, with no meaningful interaction, changing instruction or required progress detail inside it. The application result becomes visible at 00:46.

The plan keeps the start and end of that wait and removes source **00:26–00:44**. Add a small “Wait shortened” overlay across the join; it describes the edit without claiming the application completed the task in four seconds. The overlay adds no duration. There are no added cards, speed changes or overlapping transitions in this example.

| Original source interval | Planned output interval | Duration | What stays visible |
| --- | --- | --- | --- |
| 00:00–00:08 | 00:00–00:08 | 8 s | Starting report and the tutorial's outcome |
| 00:08–00:18 | 00:08–00:18 | 10 s | Open picker, choose April, confirm selection |
| 00:18–00:24 | 00:18–00:24 | 6 s | Apply the chosen filter |
| 00:24–00:26 | 00:24–00:26 | 2 s | Beginning of the loading state |
| 00:44–00:46 | 00:26–00:28 | 2 s | End of the loading state |
| 00:46–00:54 | 00:28–00:36 | 8 s | Updated report appears |
| 00:54–01:06 | 00:36–00:48 | 12 s | Check the selected period and saved state |
| 01:06–01:16 | 00:48–00:58 | 10 s | Recap and next step |

The kept intervals total **8 + 10 + 6 + 2 + 2 + 8 + 12 + 10 = 58 seconds**. Intervals include their start and exclude their end. These are illustrative second-level boundaries; place real cuts at appropriate frames after inspecting motion and sound.

The critical distinction is why the 18 seconds are removable: inspection established that they contain only waiting. “No speech” alone would not justify the cut. A silent drag, typed value, confirmation dialog or important progress message may be necessary to understand the task.

For your own edit, use the assistant's inspected ranges rather than copying these times:

> In [project/version], apply the approved cut plan to a separate editable version if supported. Preserve all required actions and results, original speech and normal-speed demonstration segments. Shorten only the approved waiting intervals. Mark compressed waits with a readable “Wait shortened” overlay without covering controls. Do not add narration or alter the demonstrated values. Render a preview and return its version, duration and source-to-output map. If the requested separation or treatment is unsupported, explain before changing the source project.

## Frame the action and its context together

A zoom should make the relevant control readable while preserving enough surrounding interface to locate it. Start wide enough to establish the screen, move closer before the action, and keep the selected value and result visible long enough to understand them.

| Framing problem | Focused revision |
| --- | --- |
| The pointer is visible but the control's label is cropped | Include the label and selected state in the close-up. |
| The camera bubble covers the confirmation message | Move or reduce the camera view for that passage, keeping the screen legible. |
| Captions cover the field being edited | Move captions to a clear region or change the composition. |
| A zoom arrives after the click | Start the move earlier and review it against the spoken instruction. |
| The result flashes too briefly to read | Restore suitable source time or propose a clearly identified still hold. |

A still hold can give a settled screen more reading time, but it cannot show an action that was never captured. Preserve truthful timing and narration, and include any added hold in the output map. See [slide and interface readability](SLIDE-READABILITY.md) for a worked explanation of why fitting a whole screen into a vertical frame can make its labels too small.

Check the downloaded file at the intended playback size. A comfortable full-screen desktop preview does not establish that controls are readable in an embedded help article or on a phone. If a vertical composition cannot preserve the essential interface, offer a landscape tutorial or a narrower excerpt with enough context.

## Revise one passage and update downstream times

Suppose the example's wait feels too abrupt. Restore source **00:42–00:44**, extending the retained tail from 00:44–00:46 to **00:42–00:46**. The first 26 output seconds remain unchanged; the tail now occupies 00:26–00:30.

| Passage | First version | Revised version |
| --- | --- | --- |
| Updated report | 00:28–00:36 | 00:30–00:38 |
| Verification | 00:36–00:48 | 00:38–00:50 |
| Recap | 00:48–00:58 | 00:50–01:00 |

The “Wait shortened” overlay remains associated with the same join at output 00:26; review its hold against the longer tail. The program becomes **60 seconds**. Original source 00:50 appeared at output 00:32 before the revision and appears at **00:34** afterward. Captions, callouts and chapter references after the insertion must follow the revised timing.

> In [reviewed version], extend the loading tail using original source [00:42–00:46] instead of [00:44–00:46]. Keep the preceding 26 output seconds unchanged and preserve the later source selections, speech and framing. Update downstream captions, callouts and the “Wait shortened” overlay to match the new cut. Render a new preview and identify its version, duration and updated time map. Do not replace the approved export until this revision is reviewed.

This request describes the fictional example. For a real revision, provide your own project, source intervals and reviewed output version. If the editor cannot preserve a separate version, resolve that before proceeding. For caption-specific timing issues, use the [caption revision guide](CAPTION-REVISIONS.md).

## Review the lesson by trying to follow it

Ask a reviewer to reproduce the task in the demonstrated software version using sample data. Record where they need to pause, guess or leave the video for missing information. A shorter video is only an improvement if the required explanation survives.

| Check | Record before publishing |
| --- | --- |
| Repeatable task | Starting state, prerequisites and every required action are present. |
| Narration alignment | The named control and its result appear with the relevant instruction. |
| Visible evidence | Values, selections and confirmation messages agree across cuts. |
| Reading | Controls and captions are legible at the intended viewing size. |
| Sensitive material | The entire export, including transitions, contains only approved demo information. |
| Delivery | The downloaded file matches the reviewed version; its sound and ending play correctly. |
| Destination | The processed upload or embedded player preserves the reviewed legibility. |

If private information was captured, handle the original according to your team's policy. A cover applied to the final video does not remove that information from the original upload. Inspect the full affected interval rather than checking one still frame.

Keep a compact delivery record: source filename/version, application version or date, brief, removed intervals, preview version, approved export filename, reviewer findings and any unresolved limitation. For future software updates, that record shows which tutorial section needs replacing and which later timestamps will move.

[Start a screen-recording brief](https://valmera.io/prompts?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=screen_recording_tutorials#prompt-builder), then use the [YouTube delivery guide](YOUTUBE.md) or [website-demo workflow](WEBSITE-DEMO.md) for your destination. Maintained by Valmera; the example and prompts are an editorial review method, not a claim that every edit or client supports every operation.
