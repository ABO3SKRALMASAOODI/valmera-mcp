# Deliver edited training videos to an LMS with captions and chapters

Choose the deliverable based on what your learning system needs to do. A video lesson can use an MP4 and separate WebVTT captions. A WebVTT chapter file can add navigation if the player supports it. If the requirement is a portable course that reports completion or quiz scores through SCORM, ask for the required SCORM version and a test upload. Confirm who owns that packaging step before editing a library.

## Pick the delivery route before the pilot

| What the buyer needs | Ask for | Verify before ordering a batch |
| --- | --- | --- |
| An existing lesson needs a revised video | One approved MP4 per lesson, plus a player-selectable caption file if required. | Upload one pair to the actual course draft. Verify caption controls, the corrected wording, and whether the LMS uses its own completion rules. |
| Learners need to jump to procedures inside a long recording | A named chapter map and a WebVTT chapter track if the player accepts it. | Select each chapter in learner view. Verify the matching action and check the first relevant caption after seeking. |
| A single package must report course state to the LMS | A package in the exact SCORM version your LMS supports, plus the approved video masters for future revisions. | Import it into a test course and check session resume and completion. Test quiz score reporting if it is part of the contract. |

[Canvas documents SRT and WebVTT captions](https://community.instructure.com/en/instructure/kb/articles/662930-how-do-i-add-captions-to-new-or-uploaded-videos-in-the-rich-content-editor-in-canvas) in its Rich Content Editor, with WebVTT needed for captions in the Canvas iOS app. [Moodle documents captions and chapters](https://docs.moodle.org/503/en/video) for its player and says to upload the track files to Moodle. Check your site’s available settings. If the player lacks a chapter import, use an approved chapter list or separate lessons and test the learner’s route. [ADL’s SCORM guide](https://adlnet.gov/assets/uploads/SCORM_Users_Guide_for_Programmers.pdf) describes the package manifest and the information it supplies to the LMS.

## Try one 15-second lesson before approving the batch

Use the [sample MP4](examples/described-training-video/standard.mp4), [English captions](examples/described-training-video/standard.vtt), and [chapter file](examples/training-video-chapters/chapters.vtt). This is a fictional workspace-permissions lesson using synthetic speech. The [local test player](examples/training-video-chapters/player.html) opens both tracks separately and exposes four chapter buttons. Keep these relative paths when downloading the files.

From the repository root, use a local HTTP server that supports MP4 byte ranges. For example, with Ruby and WEBrick installed, run this command and open the player at `http://127.0.0.1:8000/docs/examples/training-video-chapters/player.html`.

```sh
ruby -rwebrick -run -e 'WEBrick::HTTPUtils::DefaultMimeTypes["vtt"] = "text/vtt"; httpd' \
  -- --bind-address=127.0.0.1 --port=8000 .
```

| Chapter button | Expected time | What to verify |
| --- | ---: | --- |
| Open Permissions | 0:00.000 | The opening instruction appears starting at 0:00.500 with captions enabled. |
| Inspect the current role | 0:04.150 | The screen displays Viewer and Draft. |
| Save the change | 0:09.150 | The caption reads “After changing the role, save your changes.” |
| Confirm the saved role | 0:12.150 | The screen shows Publisher and Saved. The earlier narration caption has ended. |

In Chromium and WebKit, the local player loaded four chapters and reached the matching caption at 9.150 seconds. The confirmation button reached 12.150 seconds with no earlier caption remaining. If a chapter button returns the video to the start, check whether the host responds with HTTP 206 to a byte-range request.

Use the player’s captions control to switch the English track on and off. The chapter buttons should still work with captions off. Replace the sample with one approved edit, its matching captions and its final chapter times. Keep the same three-file test if a subsequent cut moves the instructions. If your media player accepts only SRT for captions, provide SRT for that destination and deliver the chapter times in the format it supports.

## Scope an Enterprise editing pilot

Send a representative recording, your expected monthly volume, the destination LMS, the approved terminology and the deliverable from the table. Specify who signs off on the MP4 and who uploads and tests it. If you need alternate narration, [try the sample with a separate described edition](OUTSOURCE-TRAINING-VIDEO-CAPTIONS-AUDIO-DESCRIPTION.md). For an existing folder of approved assets, [verify each video and caption pair before upload](VERIFY-TRAINING-VIDEO-HANDOFF.md).

Valmera Enterprise edits existing training footage. Include any separate player captions, chapter tracks or course packaging in the scope so you can assign each delivery step. If your editor must also package and test SCORM, compare the quote with a provider that explicitly offers that work, such as [Margo Learning](https://www.margolearning.com/services/video-animation/post-production). [See Valmera’s training video editing service](https://valmera.io/training-video-editing-service?utm_source=github&utm_medium=documentation&utm_campaign=lms_video_chapters) or [send a pilot brief to Valmera Enterprise](https://valmera.io/subscribe?inquiry=training-video-editing-service&utm_source=github&utm_medium=documentation&utm_campaign=lms_video_chapters#enterprise).
