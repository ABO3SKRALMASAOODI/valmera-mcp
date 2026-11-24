# Fix podcast audio that goes out of sync after a recorder stops

If the external microphone matches the camera until partway through the episode and suddenly runs early, find the first point where the difference changes. Compare the camera’s scratch audio with the external track just before and just after that point. When a recorder dropped a section and closed the gap in the audio file, split the external track and align the second section to the camera. Fill the missing interval with usable backup audio if you have it.

## Play three versions of the same 12 seconds

The files below use the same picture. A flash marks a known event. The standalone recorder lost 0.6 seconds of audio between camera time 6.000 and 6.600. Listen to the first two clicks, the gap and the clicks after the gap. These are locally rendered synthetic examples.

| Export | Opening and end | What happens in the middle |
| --- | --- | --- |
| [Opening offset only](examples/podcast-sync-gap/01-offset-only.mp4) | The first flash and beep align. The last beep arrives about 0.6 seconds early. | The beep at 6.1 seconds is missing. The following beep arrives early. |
| [Stretch to match both ends](examples/podcast-sync-gap/02-endpoints-only.mp4) | First and last cues align. | The 5 s beep is 215 ms late, the 6.1 s beep is missing and the 8 s beep is 213 ms early. |
| [Split and patch the gap](examples/podcast-sync-gap/03-gap-patched.mp4) | Both ends align. | All five beeps are present and within 1 ms of their flash to the nearest millisecond. |

[Download the measured cue times](examples/podcast-sync-gap/measured-cues.csv) and the [external recording with the gap](examples/podcast-sync-gap/external-recorder-gap.flac). The patched MP4 can serve as the camera reference for this exercise because its scratch cue times match every flash. The endpoint-stretch version models what a global change would do to those cue times. The synthetic test has no speech or ambient sound.

## Repair your own episode

1. Use the continuous camera as your timing reference. Turn on the camera scratch track and find one distinct sound before the fault and one after it. Tap through the recording until you can bound where the relationship changes.
2. If the offset jumps and then stays steady, keep the aligned first section. Split before the first affected sound and move the second section until its waveform lines up. If a recorder preserved the gap as silence, its later audio may already be aligned.
3. Use a backup mic, another recorded feed or the camera scratch track for the missing words. Match levels and use short fades where needed. If none of the recordings contain the words, mark the passage for a pickup or an approved cut.
4. Export a master. Reopen it and check two cues around the repair and one near each end. Listen in the final distribution player too. Then make content cuts and captions against the repaired master.

If the change grows gradually across the episode, use the [two-hour clock-drift test](FIX-AUDIO-DRIFT-IN-LONG-RECORDINGS.md) to measure a rate correction. If picture timing changed during conversion, check the [screen-recording timestamp example](FIX-SCREEN-RECORDING-AUDIO-DRIFT.md).

## Choose a workflow for the files you have

| Footage and goal | Where to start |
| --- | --- |
| Continuous video plus a partly missing external recorder track | Use a timeline editor to align the two surviving sections independently and mix in your backup for the gap. Adobe and Blackmagic document waveform or timeline controls for these tasks. [Premiere audio synchronization](https://helpx.adobe.com/ca/premiere/desktop/add-audio-effects/basic-audio-editing/synchronize-clips-in-the-timeline-panel.html) · [DaVinci Resolve Fairlight](https://www.blackmagicdesign.com/products/davinciresolve/fairlight) |
| Multiple video and audio files from the same shoot | ChatCut documents a multicamera sync workflow for separate angles and audio tracks. Hand it a sample with the interruption and check the cues before and after the gap yourself. [ChatCut multicamera guide](https://chatcut.io/docs/multicam-edit) |
| A single MP4 after sync has been verified | Upload the master to Valmera for the episode edit. Ask the agent to preserve the repaired exchange and return a reviewable cut. AI editing requires a subscription. [Valmera’s long-video editor](https://valmera.io/long-video-ai-editing?utm_source=github.com&utm_medium=referral&utm_campaign=podcast_recorder_gap) |

Valmera publishes this guide. The three examples demonstrate source timing and delivery checks. Third-party workflow descriptions come from vendor documentation.

> Use the sync-checked master for this episode. Preserve the exchange around the repaired audio. Cut the marked restarts and empty waits. Keep both speakers’ words complete, then show me the preview before exporting the full episode.

For recurring episodes, send the team one representative source, the camera and mic formats, the release schedule and the expected deliverables. [Discuss a podcast editing pilot with Valmera Enterprise](https://valmera.io/subscribe?inquiry=podcast-video-editing-service&utm_source=github.com&utm_medium=referral&utm_campaign=podcast_recorder_gap#enterprise).
