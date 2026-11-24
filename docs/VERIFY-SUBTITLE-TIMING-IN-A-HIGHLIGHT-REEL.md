# Check subtitle timing after cutting a webinar into a highlight reel

Ask the editor for the finished MP4, a separate SRT, and a cut map with original and output time ranges. Each retained caption should move by the same offset as the source frames it describes. Captions from deleted speech should disappear. Captions spanning a cut need a check against the words actually audible on both sides.

## Run the same test with each editor

Use three cues in the pilot: a sentence wholly inside a kept clip, a cue wholly inside a removed interval, and a cue that overlaps the edit. Load the delivered SRT over the actual MP4 in your publishing player. At each join, listen for the first and last audible word, check the cue boundary, and compare the source and output times. After requesting a revision to the cut, run the same checks on the revised MP4 and SRT.

When you compare quotes for recurring edits, ask what a revised cut includes: updated captions, any affected translations, and a filename or version that identifies the matching MP4. A short recording with three cues is enough to test the handoff before committing an entire event library.

## Try it on a recorded Valmera cut map

Valmera's [highlight-reel example](https://valmera.io/tools/highlight-reel?utm_source=github&utm_medium=referral&utm_campaign=highlight_reel_caption_handoff#source-to-export) has seven source-backed edits from a 49-minute recording. Source time `14:20.000` maps to `00:13.350` in the reel. Source times between `14:13.000` and `14:13.330` were removed. The ending hold has no source-backed caption interval in this map.

Download the [published cut map](https://valmera.io/downloads/real-ai-video-edit-cut-map.csv), the [example source SRT](evaluation/highlight-reel-review-source.srt), and the [mapping script](evaluation/map_subtitles_to_highlight_reel.py). The sample cues below use synthetic words and the published timing boundaries. Use them as timing markers.

```sh
python3 map_subtitles_to_highlight_reel.py highlight-reel-review-source.srt real-ai-video-edit-cut-map.csv > review.srt
```

| Source cue | Expected time in the reel | Check |
| --- | --- | --- |
| Boundary cue, `14:12.800–14:13.500` | `00:06.760–00:06.960` and `00:06.960–00:07.130` | Two retained fragments meet at the join. Rewrite the cue against the final audio if the wording needs to change. |
| Removed cue, `14:13.050–14:13.200` | No output cue | It should never appear over the reel. |
| Kept cue, `14:20.000–14:21.000` | `00:13.350–00:14.350` | The cue retains its full duration at its new time. |

The script uses millisecond precision and maps only 1×-speed cuts. It omits source-free rows such as an end slate and flags the count of clipped, split or removed cues on stderr. Its output is a timing draft. It keeps the text of a split cue on both fragments, so listen before approving that text. Use a separate timing approach for crossfades, variable-speed cuts or captions reauthored from final audio.

For recurring edits from recorded webinars, [see Valmera's done-for-you webinar editing and request a quote](https://valmera.io/webinar-video-editing-service?utm_source=github&utm_medium=referral&utm_campaign=highlight_reel_caption_handoff). Bring one existing recording, your caption delivery format, and the cadence you need.
