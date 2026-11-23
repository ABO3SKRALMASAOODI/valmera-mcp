# Check a podcast clip batch after revising one clip

When a team approves three clips and asks for one change to clip B, bring back the original approved MP4s for A and C. Open the replacement B with sound. This procedure gives you a repeatable check for both jobs.

## Save the review baseline

1. Export the first review batch into an `approved` folder using stable IDs such as `A.mp4`, `B.mp4` and `C.mp4`. Save B's first export even if it goes back for changes.
2. Give the editor a source anchor and identify what should carry through. For example, “In B, restore the sentence that begins ‘Only for returning customers.’ Keep its speaker framing and caption style, and keep the approved A and C files.” Use the actual wording and source time from your recording.
3. Export B again. Put the new B and the original A and C into a separate `delivered` folder and keep the same IDs across both folders. Keep the baseline folder for comparison.

## Check the actual files

Download [the batch checker](../scripts/check-approved-clips.py). Run it with Python 3 from the folder where you saved it. Both folders are read locally.

```sh
python3 check-approved-clips.py approved delivered --revised B.mp4
```

| Output | What to do |
| --- | --- |
| `APPROVED FILE MATCHES` | The file is byte-for-byte identical to the version saved for review. |
| `REVISED, REVIEW THIS FILE` | Open the replacement. Check the restored sentence, the surrounding cut and the captions. Compare those captions with the original speech. Check duration, framing, and the exported ending. |
| `UNEXPECTED CHANGE` | Restore the approved file or reopen that clip for review. A fresh encode can change bytes even when playback looks the same. |
| `MISSING` or `UNEXPECTED FILE` | Reconcile the filenames and the delivery list before publishing. |
| `REVISION FILE MATCHES ORIGINAL` | Check which version you downloaded and replace B with the correct export. |

The checker compares MP4s directly under the two folders. It exits successfully when every expected file is present, the named revision differs, and the other files match. Omit `--revised` to verify that a delivery copy matches the whole reviewed batch. The editorial review happens when you play the revised export.

## Try it on a recorded example

The [caption revision example](CAPTION-STYLE-EXAMPLE.md#watch-the-files-and-compare-the-same-moment) has two published previews of the same 9.6-second dialogue selection. Save the documentary preview as `approved/B.mp4` and the clean preview as `delivered/B.mp4`. Put a copy of any one approved MP4 in both folders as A. The checker should flag B for review and report that A matches. Replace delivered A with a different MP4 and run the same command again to see how an unexpected change is reported.

This is a Valmera-authored workflow. The recorded B example demonstrates a caption-style change on a short dialogue excerpt. Use your own interview for the source selection and full delivery test.

[Try a clip brief in Valmera](https://valmera.io/use-cases/podcasters?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=podcast_batch_review) · [Scope recurring done-for-you editing](https://valmera.io/subscribe?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=podcast_batch_review#enterprise)
