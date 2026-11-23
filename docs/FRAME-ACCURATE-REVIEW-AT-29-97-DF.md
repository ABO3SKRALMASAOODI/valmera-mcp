# Give a frame-accurate revision note at 29.97 drop-frame

A client says “keep the result at 00:10:00.” If the editor uses the wrong timecode mode, the exported picture can land 18 frames later. Attach the exact review file, timecode mode and intended picture to the request. Verify the final MP4 against that reference before approving it.

## Try the ten-minute check

Download the [synthetic 29.97 fps MP4](examples/drop-frame-review/ten-minute-drop-frame-source.mp4). It starts at `00:00:00;00` and uses the exact rate `30000/1001`. The first green result picture appears at frame 17,982. The next shot starts 18 frames later. Here, frame indexes count the first picture as zero.

| Address supplied to the editor | Zero-based frame | Seconds from file start | Picture in this MP4 |
| --- | ---: | ---: | --- |
| `00:10:00;00` at 29.97 drop-frame | 17,982 | 599.9994 | [Approved result](examples/drop-frame-review/frame-17982.png) |
| `00:10:00:00` at 29.97 non-drop-frame | 18,000 | 600.6000 | [Next shot](examples/drop-frame-review/frame-18000.png) |

We reproduced both values in [Valmera's live timecode calculator](https://valmera.io/tools/timecode-calculator) and decoded the file at frames 17,981, 17,982, 17,999 and 18,000. The difference is **0.6006 seconds**. Drop-frame changes the timecode labels. Both modes describe the same underlying pictures at the same frame rate. [Adobe's timecode display reference](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/choose-timecode-display-format.html)

To compare the exact pictures, extract each indexed frame from this same input file. Use an output filename distinct from your source.

```sh
ffmpeg -i ten-minute-drop-frame-source.mp4 -map 0:v:0 \
  -vf 'select=eq(n\,17982)' -frames:v 1 frame-17982.png
ffmpeg -i ten-minute-drop-frame-source.mp4 -map 0:v:0 \
  -vf 'select=eq(n\,18000)' -frames:v 1 frame-18000.png
```

## Give the editor a reference and a boundary

| Include in the note | Write it this way |
| --- | --- |
| Review version | Give the exact filename or version link, with its frame rate and timecode mode. |
| Starting label | Say whether the reference starts at zero or at a label such as `01:00:00;00`. Subtract the known start in the same mode before converting to a file-relative frame index. |
| Intended picture | Include the screenshot or describe the visible result. Identify whether the label refers to source media, the edited timeline or the review export. |
| Cut direction | Specify the first kept frame or the first removed frame. At a join, check the frame on each side. |
| Delivery frame rate | State the requested output rate. If the rate changes, ask the editor to map the intended visible moment to the new timeline and report any nearest-frame choice. |

> In the reference `ten-minute-drop-frame-source.mp4`, use 29.97 drop-frame from `00:00:00;00`. Keep the green **Approved result** shot from zero-based frame 17,982 through frame 17,999 inclusive. Frame 18,000 starts the next shot. Verify the first and last kept pictures in the downloaded MP4, and send the output timestamps where they appear.

If there is a long intro trimmed before this moment, the same picture appears at a different output timestamp. Track the source cue and its new output location. For a recurring service, test one reviewed revision first and agree who checks the final file, the frame rate and what makes a note complete. The synthetic MP4 above was made with FFmpeg and provides a shared test for any workflow.

**[Convert your notes with Valmera's free calculator](https://valmera.io/tools/timecode-calculator?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=drop_frame_revision)**. For editing, [bring the recording and the resolved cue into Valmera](https://valmera.io/edit-video-by-chatting-with-ai?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=drop_frame_revision). AI editing requires an eligible subscription. If a team needs a recurring review and export process, [scope an Enterprise video-editing pilot](https://valmera.io/product-demo-video-editing-service?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=drop_frame_revision) with one versioned file, your review format and expected monthly volume.
