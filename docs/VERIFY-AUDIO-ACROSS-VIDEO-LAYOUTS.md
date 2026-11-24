# Check that portrait and landscape video exports keep the same narration

When a revised cut is approved, a 9:16 version should keep the approved narration if the brief asks for reframing only. A portrait draft can look finished and still contain the prior voice take. Compare the first audio track against the approved export, then watch the same sync points in each version.

Use this check for a **layout-only** revision with the same audio master. For a short cutdown, translation, new mix or a delivery that intentionally normalizes the audio again, approve the changes by listening to the new version.

## Put one review change into a paid pilot

1. Send a landscape edit with a representative voice correction, such as a product name or number. Approve the corrected audio in the landscape export.
2. Ask for a portrait and square version using the approved soundtrack. Give the editor the exact file and revision number. Specify the speaker position and where captions may sit.
3. Check the new exports against the approved file. Also watch the same sync anchors in each layout, such as a clap, a visible word or a click with a matching sound.
4. Ask the editor to correct one layout issue. Recheck both the new picture and the audio before marking that version approved.

[Download the local audio comparison script](https://raw.githubusercontent.com/ABO3SKRALMASAOODI/valmera-mcp/main/docs/evaluation/compare_variant_audio.py). With Python 3 and a recent FFmpeg on your path, run it in the delivery folder.

```sh
python3 compare_variant_audio.py approved-landscape.mp4 \
  portrait.mp4 square.mp4
```

| Result | What it tells the reviewer |
| --- | --- |
| `MATCH` | The first tracks decoded to the same 24-bit PCM WAV bytes, including sample rate and channel metadata. Listen and confirm that the audio starts at the right time relative to the picture. |
| `DIFFERENT` | Check for an older take, an intentional remix or a different audio encode. Lossy re-encoding can change the decoded samples even when the words sound the same. |
| `ERROR` | The tool could not obtain audio, for example because an export has no audio track. Open the file and check the delivery. |

The script exits with 0 for all matches, 1 for a difference, or 2 if decoding fails. Files stay on your machine. It checks the first audio track, which fits a single delivery mix. For exports with multiple tracks, verify the selected track and each required language separately. The check does not measure the audio’s start time relative to video, caption timing or visual framing.

## Try it on a repeatable example

This example makes three local test videos with synthetic tones. The first portrait copy keeps the landscape audio stream. The second has a different tone at the same duration and sample rate.

```sh
ffmpeg -f lavfi -i color=size=320x180:rate=24 -f lavfi -i sine=frequency=440:sample_rate=48000 \
  -t 2 -c:v libx264 -c:a aac approved-landscape.mp4
ffmpeg -f lavfi -i color=size=180x320:rate=24 -i approved-landscape.mp4 \
  -map 0:v -map 1:a -t 2 -c:v libx264 -c:a copy portrait.mp4
ffmpeg -f lavfi -i color=size=180x320:rate=24 -f lavfi -i sine=frequency=660:sample_rate=48000 \
  -t 2 -c:v libx264 -c:a aac portrait-old-take.mp4
python3 compare_variant_audio.py approved-landscape.mp4 portrait.mp4 portrait-old-take.mp4
```

The output should show `MATCH portrait.mp4` and `DIFFERENT portrait-old-take.mp4`. This test isolates the audio comparison from visual and editorial judgment.

## Scope a recurring batch

Send your paid pilot brief with the monthly count of unique cuts, how many layouts each needs, the approved audio reference, and who checks the first and final versions. Ask the editing team to quote the pilot and include one layout correction. A vendor can then estimate the work using an actual revision and the review time it took.

[Plan a batch with Valmera Enterprise](https://valmera.io/video-editing-service?utm_source=github&utm_medium=referral&utm_campaign=enterprise_variant_audio) or [contact the Enterprise team](https://valmera.io/subscribe?inquiry=video-editing-service&utm_source=github&utm_medium=referral&utm_campaign=enterprise_variant_audio#enterprise).
