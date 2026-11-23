# Trim an MP4 and keep both selectable audio languages

If your company already has a training video with English and Spanish audio, a short trim can break the handoff in two ways. An export may drop the second stream. It may also carry both streams while leaving the alternate language on the old timeline. Check both the file structure and what plays immediately before and after the cut.

## Try the edit with four downloadable MP4s

The [eight-second source](examples/dual-audio-training-edit/source-two-audio.mp4) contains one video stream and two separate AAC mono tracks tagged `eng` and `spa`. The English test stream uses a lower tone and the Spanish stream uses a higher tone. These are synthetic cues for inspecting sync, with no spoken translations. Remove the orange setup card from **2.00 s up to 4.00 s**. The training step should start at 2.00 s in the resulting six-second video.

| File | Audio streams | What to check |
| --- | --- | --- |
| [Correct six-second export](examples/dual-audio-training-edit/trim-both-languages.mp4) | English and Spanish | Both have cues around 0.30, 2.70 and 4.15 s. English is default. |
| [Alternate track missing](examples/dual-audio-training-edit/trim-one-language-missing.mp4) | English only | A normal play-through in English can pass even though the language switch is gone. |
| [Alternate track stale](examples/dual-audio-training-edit/trim-alternate-audio-stale.mp4) | English and Spanish | The Spanish cues near the join remain around 2.35 and 4.70 s. The track list looks correct. |

We decoded both audio streams in each applicable file and measured the first sample at each cue above a fixed detection threshold. They agreed with the intended times within 3 ms in this controlled fixture. All three post-edit videos decoded to 180 frames at 30 fps. The example tests separation and sync after a trim. A real language delivery also needs a review by someone who understands each track.

To test the language switch, open the downloaded file in the player or learning platform your team will actually use. Switch tracks at the training step and replay across the edit. Browser interfaces differ in their support for [exposing alternative audio tracks](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMediaElement/audioTracks). A player without a track selector can hide correctly muxed audio streams. Recheck after the learning platform processes your upload. If distribution requires separate language files, request those from the same approved cut instead.

## Inspect the delivered file

The following command reads stream metadata without editing the file. Expect two AAC audio streams and the agreed language and default flags. Follow with playback for each language. Tags and stream counts alone cannot detect the stale-track failure.

```sh
ffprobe -v error -select_streams a \
  -show_entries stream=index,codec_name,channels:stream_tags=language,handler_name:stream_disposition=default \
  -of json trim-both-languages.mp4
```

If an editor accepts the source but exports one mixed track, ask for the approved picture and **separate audio stems from the same timeline**. You can then put them into one MP4 without re-encoding the picture. This command assumes one H.264 picture stream, two time-aligned WAV files and a reviewed stereo or mono channel layout in each WAV. Check the duration, language labels and sync again before release. Explicit output mapping is documented in [FFmpeg’s stream selection reference](https://ffmpeg.org/ffmpeg.html#Manual-stream-selection).

```sh
ffmpeg -i reviewed-picture.mp4 -i english-final.wav -i spanish-final.wav \
  -map 0:v:0 -map 1:a:0 -map 2:a:0 -c:v copy -c:a aac \
  -metadata:s:a:0 language=eng -metadata:s:a:1 language=spa \
  -disposition:a:0 default -disposition:a:1 0 -movflags +faststart final-training.mp4
```

## Brief a pilot before asking for a batch quote

> Remove [start]–[end] based on the original training master. Apply the same cut to picture and both existing language tracks. Deliver one MP4 with selectable English and Spanish audio, English default, plus separate approved audio stems. Include the source and output timings for the cut. Verify both tracks across the join in [target player or LMS], and send one reviewed file for approval before the rest of the batch.

Start with an episode that includes a timing-sensitive instruction. Agree on the exact deliverables, monthly volume and who signs off on each language. If you also need subtitle or caption files, list and review those separately for each language.

**[Scope a done-for-you training video pilot with Valmera Enterprise](https://valmera.io/training-video-editing-service?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=dual_audio_training_edit)**. Include your target player and required track layout so the team can confirm the delivery format. For standard single-language videos, [try editing your recorded footage with Valmera](https://valmera.io/ai-video-editor?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=dual_audio_training_edit). AI editing requires an eligible subscription. The test files above were made with FFmpeg.
