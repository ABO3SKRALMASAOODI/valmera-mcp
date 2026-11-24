# Record a website demo with browser sound and narration

When a website demo needs an audible result, capture the tab’s sound and the microphone as two sources. A customer should hear the confirmation chime, spoken response, or audio preview at the same moment it happens on screen. A screen recording can look correct and contain a clear voice while omitting the app’s sound entirely.

## Run an eight-second capture test

[Open the test file on GitHub](examples/website-demo-tab-audio/test-tab-audio.html), choose **Download raw file**, and open the saved HTML as a browser tab. The page plays a synthetic two-note notification. It asks for two short spoken lines and runs locally without asking for microphone or screen permissions. Your chosen recorder handles capture.

1. In your recorder, choose the test tab as the video source and enable the option to capture that tab's sound. Enable your chosen microphone if the demo needs narration. Use headphones so the microphone does not pick up the chime from the speakers.
2. Start recording. Select **Start audio test** in the shared tab. Read the first sentence, wait through the two notes, then read the final sentence.
3. Download the recording and play the saved file. Listen for speech, a rising pair of notes, and speech again. If the voice survives but there is silence where the visual says the tab plays two notes, check the browser's share setting and the recorder's tab-audio toggle.
4. Repeat the listening check after you edit and export. If your capture has the chime and the edit does not, inspect the editor's audio tracks, muting and cleanup settings. Ask for unprocessed audio first when a noise filter treats a short product sound as background noise.

## Hear what a missing tab sounds like

The two examples were assembled from screenshots of the test page, synthetic narration, and test tones. They have the same 240 decoded video frames at 30 fps. Both contain the same opening and closing voice. Only the first contains the internal notification at 3.00 and 3.38 seconds.

| Reference | What you hear |
| --- | --- |
| [Tab sound and microphone, eight seconds](examples/website-demo-tab-audio/include-tab-and-mic.mp4) | Both spoken lines with a 660 Hz and 880 Hz note between them |
| [Missing tab sound, eight seconds](examples/website-demo-tab-audio/missing-tab.mp4) | Both spoken lines with silence between them |

Decoded 48 kHz mono audio had an RMS level of 2,127.13 in the chime window for the first file and 0.00 for the second, in signed 16-bit PCM units. The voice windows measured the same in both files. The samples demonstrate the two outcomes to look for in your export. [File hashes and measurements](examples/website-demo-tab-audio/measurements.json)

## Choose a capture and editing workflow

Valmera publishes this guide. The capture routes below follow each vendor's documentation. Run the same test in the recorder, browser and operating system you expect to use, then review the actual download.

| Workflow | Where to enable the sound |
| --- | --- |
| Loom Chrome extension | Use **Current Tab** for the tab’s internal audio, and turn on the microphone for speech. Loom documents a desktop route for audio from other applications. [Loom capture guide](https://support.atlassian.com/loom/docs/capture-internal-audio-system-audio) |
| recorder.video in Chrome or Edge | Pick the browser tab with its audio box selected. Leave the microphone on for narration and check the input mix on playback. [recorder.video tab recording guide](https://recorder.video/record-browser-tab) |
| Camtasia Editor recorder | Turn on **Microphone** and **System Audio** in the recorder. Check the specific capture configuration on the workstation you will use. [TechSmith capture guide](https://support.techsmith.com/hc/en-us/articles/39968968889101-How-to-Record-Audio-and-Video-with-Camtasia-Editor) |
| Valmera | For authentic page sound, upload the recorded file and use Valmera to edit the supplied capture. Valmera's automated website capture from a URL is silent and can be paired with narration or separately supplied audio. [Valmera website-demo workflow](https://valmera.io/tools/record-website-demo?utm_source=github.com&utm_medium=referral&utm_campaign=website_demo_tab_audio) |

### Brief the edit of the supplied recording

> Cut the setup, keep the action that triggers the notification and the two notes that follow. Keep my original narration and the app's original sound. Leave the on-screen result readable for a beat. Give me a downloadable review MP4. Tell me where the notification occurs in the final cut.

If the narration and tab sound are baked into one track, check the original capture before commissioning individual volume changes. Where independent level control is required, ask for separate audio sources from the recorder on the pilot.

For a recurring launch or onboarding library, [ask Valmera Enterprise to scope a product-demo pilot](https://valmera.io/subscribe?inquiry=product-demo-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=website_demo_tab_audio#enterprise). Bring one recording with a visible action, a required app sound and spoken narration so the team can agree on the acceptance test before quoting the full batch.
