# Replace music in a TikTok ad and keep the approved voiceover

Start from the approved picture and the separate narration or session tracks. Remove the old music layer, add the approved replacement and render a new mix against the same picture. Save the outgoing ad and the review versions so the producer can verify which file to run.

## Confirm the intended use before editing

TikTok directs businesses to its Commercial Music Library for commercial TikTok content. Its Ads Help Center lets buyers filter availability by campaign region and usable placement. Record the chosen track, campaign regions and placements in the delivery brief. For audio sourced elsewhere, have the rights owner or legal reviewer confirm the required permission for the specific use. Check each other platform on its own terms. [TikTok's commercial music guidance](https://ads.tiktok.com/resources/help/article/commercial-music-library) · [Filter tracks by region and placement](https://ads.tiktok.com/resources/help/article/how-to-use-the-commercial-music-library)

## Play three versions of one locked cut

The [original four-second Valmera sample](https://valmera.io/examples/filler-word-cut/original.mp4) uses a synthetic narrator and a color-label demonstration. We copied its H.264 picture without re-encoding and used the same narration track at the same level in all three mixes. Two synthetic tones mark the old and replacement music channels so you can detect the difference in the exported MP4. No commercial tracks are included in the sample.

| Download | Old bed marker, 997 Hz | New bed marker, 1,373 Hz | What changed |
| --- | ---: | ---: | --- |
| [Previous mix](examples/replace-ad-music/previous-mix.mp4) | −23.3 dBFS | −85.5 dBFS | The original test bed plays under the voice. |
| [Both beds by mistake](examples/replace-ad-music/layered-by-mistake.mp4) | −23.3 dBFS | −23.3 dBFS | A new bed was added but the old one is still at the same level. |
| [Replacement mix](examples/replace-ad-music/replacement-mix.mp4) | −99.9 dBFS | −23.3 dBFS | We mixed the same narration with only the new bed. |

All 100 decoded video frames matched the source in each export. The narration samples are identical at the mix input. The final audio streams are AAC encodes of different mixes. The marker values measure only those frequencies over seconds 0.50–3.50, with background energy from the narration and the codec. Use listening, source tracks and export checks for actual songs. [File measurements](examples/replace-ad-music/measurements.json)

## Choose the workflow by the source you have

| What you have | What to ask the editor to do |
| --- | --- |
| Editable project or separate voice and music stems | Disable the original music layer. Import the approved replacement, preserve narration timing and check the result at playback level. |
| Locked picture and a separate voiceover | Rebuild the mix against the locked picture. Verify the audio start, end and narration level. Copy the picture stream when the deliverable allows it. |
| Only a flattened MP4 with the old music under speech | Request the clean voice track first. If you try vocal isolation, review the voice, pauses and tail for remaining music and damaged syllables before approval. |

[Valmera’s audio guide](https://valmera.io/docs/audio-and-music) describes supplied music, narration and ducking. [TikTok’s Symphony editor](https://ads.tiktok.com/resources/help/article/how-to-edit-videos-with-symphony-creative-studio) also documents separate music and voiceover controls. Confirm whether the selected workflow can deliver the exact locked picture when that is a contract requirement.

## Send a brief for the first replacement

> Start with the approved [ad version] and separate [narration filename]. Remove [old music layer]. Use [approved replacement track or silence for platform placement]. Keep the picture, subtitles, disclosure, voice timing and end card fixed. Send the new MP4, note the track used and call out any change outside the audio.

Play the downloaded file through its final frame. Compare the picture in the same aspect ratio, and check the quietest spoken line and the final voiceover tail. Attach the approved audio record to the delivery ID that the media buyer will upload.

[Try a music revision in Valmera](https://valmera.io/tools/add-music-to-video?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=ad_music_replacement) or [send the recurring ad volume and placement list to Valmera Enterprise](https://valmera.io/paid-social-video-editing-service?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=ad_music_replacement#scope).
