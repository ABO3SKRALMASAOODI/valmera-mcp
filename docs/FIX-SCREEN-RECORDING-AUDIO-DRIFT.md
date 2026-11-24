# Fix audio drift in a screen recording before editing

If the picture and sound match at the start but separate later, compare an identifiable sound and visible action near the start, middle, and end. A constant offset can be corrected with a single shift. A growing or changing offset needs a different fix. Check whether the source uses variable frame rate before changing your cuts or moving your captions.

## Play the same three cues in each MP4

This controlled sample mimics a screen recording that captures 30 frames per second during activity and 15 during a quiet stretch. The square flashes when the tone sounds at 2, 6, and 10 seconds. Turn sound on and check all three markers.

| File | First flash and tone | Middle flash and tone | Last flash and tone |
| --- | --- | --- | --- |
| [Original variable-rate recording](examples/screen-recording-sync/source-vfr.mp4) | Both at 2 s | Both at 6 s | Both at 10 s |
| [Broken export that ignores the source timestamps](examples/screen-recording-sync/ignored-timestamps.mp4) | Both at 2 s | Flash at 5 s, tone at 6 s | Flash at 8 s, tone at 10 s |
| [Corrected 30 fps copy](examples/screen-recording-sync/normalized-30fps.mp4) | Both at 2 s | Both at 6 s | Both at 10 s |

The broken export retimes every retained picture at 30 fps while the audio keeps its original time. The source contains 300 picture frames over 12 seconds. Reassigning those frames to consecutive 30 fps positions squeezes the picture to 10 seconds, while the audio still runs for 12. The corrected copy uses the picture timestamps to place 360 frames over 12 seconds. The three flash onsets were measured on the 30 fps frame grid, and the tone onsets in 5 ms windows of decoded audio. This is a synthetic FFmpeg test you can repeat; it gives you a known-good input for trying an editor.

Download the [cue measurements CSV](examples/screen-recording-sync/sync-measurements.csv) to compare the three files.

## Fix your own recording

1. **Check the original before converting.** Watch for a mouse click, visible mouth movement, or a keyboard action with a clear sound. Check the same kind of cue near the beginning and near the end. If the original itself has drift, investigate the capture or separate audio recording first. Frame-rate conversion preserves the input timing.
2. **Normalize a copy to your project frame rate.** For a 30 fps project, open the recording in HandBrake, choose 30 under **Framerate (FPS)** and select **Constant Framerate**. Export to a different filename and keep the original. If you use FFmpeg, apply the `fps` filter so the conversion uses the input timestamps. Use your delivery rate if it differs from the sample.
3. **Confirm the correction in the file you deliver.** Re-check the same cues in the normalized copy, then import it and make the edit. In the final MP4, check a cue before and after the region where you removed time, plus a cue near the end. If captions are part of the delivery, check their timing against the final MP4.

Use the [HandBrake frame-rate guide](https://handbrake.fr/docs/en/latest/technical/frame-rates.html) or [FFmpeg fps filter documentation](https://ffmpeg.org/ffmpeg-filters.html#fps) for the conversion settings.

```sh
ffmpeg -i source-vfr.mp4 -map 0:v:0 -map 0:a:0 -vf fps=30 \
  -c:v libx264 -pix_fmt yuv420p -c:a aac -movflags +faststart normalized.mp4
```

This command expects one video and one audio track. In a recording with separate mic and system-audio tracks, choose the tracks you need before preparing the upload.

## Evaluate the edit on one real recording

Upload the normalized copy to [Valmera’s AI video editor](https://valmera.io/ai-video-editor?utm_source=github&utm_medium=documentation&utm_campaign=screen_recording_sync). Try one revision that changes the duration within the recording but keeps the useful action.

> Shorten the wait after I click Export. Keep the click, the first moment the completed file appears, and the explanation after it. Leave the existing narration in sync with the picture. Show me the revised cut before export.

Save the source filename, the cut you asked for, and the cues you checked in the export. If you have a catalog of screen recordings to edit, send your monthly volume, an example recording, and the deliverables you need through the Enterprise contact on [Valmera’s subscription page](https://valmera.io/subscribe?utm_source=github&utm_medium=documentation&utm_campaign=screen_recording_sync).
