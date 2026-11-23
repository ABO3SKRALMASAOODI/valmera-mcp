# Fix audio drift in a two-hour video with a separate microphone track

If the clap lines up at the start but the microphone is a second late near the end, measure sync in three places before shortening the episode. A single shift fixes a constant offset. When the offset grows steadily, the microphone track may need a speed correction. A sudden jump calls for inspecting that point for a recording interruption, missing frames or a timestamp discontinuity.

## See what one-click sync can miss

These two five-second excerpts show the same flash near the end of a synthetic two-hour recording. Turn on sound and listen for the beep.

| Export near 01:59:50 | Audio arrives after the flash | What was applied |
| --- | ---: | --- |
| [Opening aligned only](examples/audio-drift-two-hour/start-aligned-last-anchor.mp4) | 898 ms | Shifted the microphone so the first clap matched. |
| [Opening and rate corrected](examples/audio-drift-two-hour/rate-corrected-last-anchor.mp4) | Under 1 ms | Corrected the offset and rate and checked all three anchors on a full-length MP4. |

Download the original [two-hour camera MP4](examples/audio-drift-two-hour/camera-2h.mp4) and [external microphone FLAC](examples/audio-drift-two-hour/external-mic.flac). The camera file is a silent, constant 30 fps frame with three flashes. The external track contains three beeps at 8 kHz. This intentionally sparse fixture tests timing and export. It does not represent transcription quality, real mixing conditions, a large camera file, or an edit rendered by Valmera. If your editor accepts WAV instead of FLAC, use `ffmpeg -i external-mic.flac -ar 48000 external-mic.wav`. That conversion preserves the offsets for testing.

In your own footage, use a clap, a visible hard consonant or another event shared by the camera and microphone. A waveform match between the camera scratch track and external microphone is more precise than guessing from a face alone. Use distinct events near the beginning, middle and end, and keep the camera's timestamps as the reference.

## Diagnose the pattern

Our fixture adds a 160 ms start offset and 125 parts per million of clock error. Aligning the first pair removes 161 ms at every point. That still leaves about half a second of mismatch in the middle.

| Anchor | Camera flash (s) | External track beep (s) | Delay after aligning the first anchor |
| --- | ---: | ---: | ---: |
| Opening | 8.000 | 8.161 | 0 ms |
| Middle | 3600.000 | 3600.610 | 449 ms |
| End | 7190.000 | 7191.059 | 898 ms |

- **Same delay at all three anchors.** Nudge the track, then check the exported MP4.
- **Delay increases at a steady rate.** Measure the microphone time between the first and last anchors and divide it by the corresponding camera interval. The result here is **1.000125× playback speed**, or **100.0125%**. Apply the speed adjustment to the microphone, align the opening event again, then verify the middle. An editor that rounds this value to 100.01% can leave a visible error near the end of a long take.
- **Delay changes abruptly or the middle does not fit.** Inspect playback and source timestamps around the change. Align each uninterrupted section separately when necessary. Check across every join. A guessed global speed can move good sections out of sync.

For this fixture, the following command reproduces the corrected two-hour MP4. It keeps the original video stream and trims the starting offset from the microphone. It interprets the 8,000 Hz track at 8,001 Hz to remove the measured 125 ppm drift, then resamples the corrected stream to 48 kHz. The rate change also changes pitch by the same small proportion. Measure your own tracks before substituting these values and consider pitch-preserving retiming for larger adjustments. [FFmpeg audio filter documentation](https://www.ffmpeg.org/ffmpeg-filters.html#asetrate)

```sh
ffmpeg -i camera-2h.mp4 -i external-mic.flac \
  -map 0:v:0 -map 1:a:0 -c:v copy \
  -af 'atrim=start=0.160,asetpts=PTS-STARTPTS,asetrate=8001,aresample=48000,apad' \
  -c:a aac -t 7200 -movflags +faststart synced.mp4
```

I verified the decoded two-hour MP4 at 00:00:08, 01:00:00 and 01:59:50. In this controlled fixture, the first audio sample above the detection threshold was within 1 ms of the flash's presentation time at all three checks. A real clip's visual event is limited by the camera's frame interval and what you can identify in the frame.

## What to ask an editor or post-production team to show

| Requirement | Ask for this evidence before committing the series |
| --- | --- |
| Import and keep the entire take | Supported duration, file size, camera format and audio format, with the sample fully imported at native timing. |
| Correct a standalone microphone track | A clear initial offset or measured retiming value, plus the three reference events. For irregular drift, ask where the edit was split and why. |
| Edit the long episode | Review the corrected master before tightening cuts. Keep the microphone and camera linked during later trims and revisions. |
| Deliver one MP4 | Reopen the downloaded export, then confirm sync where the opening, midpoint and end anchors ended up after any cuts. Spot-check the version uploaded to the final player. |

Blackmagic documents [Elastic Wave speed keyframes in Fairlight](https://documents.blackmagicdesign.com/UserManuals/DaVinci-Resolve-18-Fairlight-Audio-Post.pdf) for manual waveform retiming. Adobe documents the [Clip Speed/Duration controls](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/change-clip-speed-using-the-speedduration-option.html) for adjusting a clip's timing. These are controls you can use to verify the result yourself. When comparing an AI editor, ask it to export the two-hour fixture and report the opening and end checks before buying for this workflow.

If you already have a sync-checked master, **[upload it for long-form editing in Valmera](https://valmera.io/long-video-ai-editing?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=long_recording_sync)**. AI editing requires an eligible subscription. If you have separate microphone tracks and recurring episodes, [scope done-for-you editing with Valmera](https://valmera.io/podcast-video-editing-service?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=long_recording_sync#scope). Give the team one sample, the number and length of episodes per month, and the requested delivery files so it can confirm the sync work in the pilot.
