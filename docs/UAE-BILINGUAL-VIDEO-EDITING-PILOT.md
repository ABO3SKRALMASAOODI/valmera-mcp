# Monthly video editing with Arabic and English subtitles in the UAE

Use one product walkthrough to compare done-for-you editing providers before you commit to a monthly volume. Give each provider the same recording, glossary, deliverable list and revision. A useful pilot ends with files you can play in your actual player and a written quote you can compare line by line.

## Four providers to compare

We are Valmera. We checked each provider's public service page on November 24, 2026. The table describes advertised scope. We checked the caption timings and the visible product label on our own sample. Scope the 12-recording example with each provider to confirm availability and the actual quote.

| Provider | What the provider publishes | What to ask for in your quote |
| --- | --- | --- |
| [Valmera Enterprise](https://valmera.io/ar/video-editing-services-uae?utm_source=valmera_mcp_docs&utm_medium=repository&utm_campaign=enterprise_uae_vendor_pilot) | Recurring editing from your existing footage. The sample below includes the same product edit with separate English and Arabic files in SubRip (SRT) and WebVTT. | Confirm who supplies the approved translations, your separate caption-file format and how revisions and cutdowns count toward the monthly scope. |
| [The Arabic Studio](https://thearabicstudio.com/video-editing/) | Editing with approved multilingual assets. Separate subtitle or audio deliverables and review rounds are scoped for the project. | Ask for editing and translation as separate quote lines if you need both. Confirm the monthly delivery calendar. |
| [Ranku](https://ranku.ae/video-editing-dubai/) | A published monthly pack for eight short videos, English and Arabic subtitles, and two creative revision rounds. | Ask whether your product walkthroughs count as short edits and whether the subtitle tracks are delivered as files you can upload separately. |
| [Progmize](https://progmize.ae/en/services/video-editing) | A monthly editing service with Arabic and English subtitles. Product demos are among its listed formats. | Confirm how many edits the monthly quote covers, the revision allowance and separate subtitle-file delivery. |

## Send this brief to every provider

> We record 12 product walkthroughs each month. For each recording, quote one approved landscape MP4 and two separate caption files for the same cut, one in Arabic and one in English. Quote 12 optional vertical cutdowns as a separate line. We will supply the source media, approved language copy, and a glossary for product names, on-screen labels and numbers.
>
> For the pilot, use one representative recording. After we approve vocabulary, remove the first half-second of footage and deliver both subtitle files for the new cut. Keep the visible interface labels unchanged in both languages. Tell us how one requested change is counted when it updates an MP4 and two subtitle files.

For the baseline quote, count **12 MP4s and 24 caption files per month**. A vertical cutdown can require its own edit and different cue timings. Ask the vendor to state the files and review rounds included for those 12 optional videos. Give vendors the same first-review deadline in Gulf Standard Time.

## Check the files before you approve the pilot

Download the approved [Valmera MP4](examples/uae-bilingual-video-editing/product-demo.mp4) and its [English WebVTT](examples/uae-bilingual-video-editing/product-demo.en.vtt) and [Arabic WebVTT](examples/uae-bilingual-video-editing/product-demo.ar.vtt). The [sample folder](examples/uae-bilingual-video-editing) also includes a browser player for both tracks. In the published clip the guide-opening cue starts at **1.900 seconds** in both files. Switch tracks near that point and check that the visible label `Captions` keeps its spelling inside the Arabic line.

To use the included player, save the files from the sample folder together, run `python3 serve.py` from that folder, and open `http://127.0.0.1:8000/`. You can also load the MP4 and each WebVTT into your own player.

1. **Check sync after a real edit.** For the example brief, trimming 0.500 seconds from the beginning with no other timing changes would move the opening cue to 1.400 seconds. Reload both revised files against the new MP4. Check the on-screen action and both tracks in the player your viewers will use.
2. **Check the words that must survive.** Give an Arabic-language reviewer your glossary. Have them check product names, numbers, punctuation and mixed Arabic and English text on the finished player, including on mobile if your audience uses it.
3. **Check the delivery as a set.** Put the filenames for the approved MP4 and both matching tracks in one manifest. Include format, language, version and review status. Open the delivery link as a reviewer to make sure they can access every file.
4. **Price the change at volume.** Ask the provider to put the full monthly deliverable count, included revisions, first review date and any translation work in writing. Separate additional exports from new editorial cuts so you can compare quotes on the same scope.

## Download the Arabic and English SRT review sets

The second clip is a copy of the Valmera sample trimmed by half a second for this exercise. Both revised subtitle files preserve the original wording. Use the matching pair for each video.

| Video | Arabic SRT | English SRT | Guide-opening cue starts at |
| --- | --- | --- | --- |
| [Original MP4](examples/uae-bilingual-video-editing/product-demo.mp4) | [Arabic](examples/uae-bilingual-video-editing/product-demo.ar.srt) | [English](examples/uae-bilingual-video-editing/product-demo.en.srt) | 00:00:01,900 |
| [Trimmed MP4](examples/uae-bilingual-video-editing/product-demo-trimmed.mp4) | [Arabic](examples/uae-bilingual-video-editing/product-demo-trimmed.ar.srt) | [English](examples/uae-bilingual-video-editing/product-demo-trimmed.en.srt) | 00:00:01,400 |

Load the trimmed MP4 with an original SRT in an SRT-capable player to see the half-second delay. Then load the revised SRT for the same language and check that the cue starts at the new time. In the Arabic cue, the English interface label remains `Captions`. Open the actual destination player before approving punctuation and text direction. YouTube accepts basic UTF-8 SubRip files. [YouTube format requirements](https://support.google.com/youtube/answer/2734698?hl=en)

## Check both SRTs before signing off

The [delivery checker](evaluation/verify_srt_cut_delivery.py) compares each language to its own original track. It reports timing and wording differences without printing subtitle text. Download it with [the SRT reader](evaluation/check_srt_revision.py) and [the retiming helper](evaluation/retime_srt_after_cuts.py), or use this command from the repository root.

```sh
sample=docs/examples/uae-bilingual-video-editing
python3 docs/evaluation/verify_srt_cut_delivery.py --remove 0 0.500 \
  --pair ar "$sample/product-demo.ar.srt" "$sample/product-demo-trimmed.ar.srt" \
  --pair en "$sample/product-demo.en.srt" "$sample/product-demo-trimmed.en.srt"
```

The command returns 0 for a match, 1 for differences and 2 for unreadable or unsupported files. To reproduce a stale delivery, pass the original Arabic file as both its original and delivered argument. The English track still passes and the Arabic track reports the two mismatched cue times. This check assumes edits only remove time and the wording stays the same. Play the approved MP4 in the destination player to verify sync, text direction and readability.

To ask Valmera about the batch, [open Enterprise contact on /subscribe](https://valmera.io/subscribe#enterprise). Include your monthly recording count, the two subtitle languages, and the first review date. If the contact page is unavailable, [email Valmera Enterprise](mailto:support@valmera.io?subject=Enterprise%20editing%20inquiry%20-%20UAE%20bilingual%20pilot) with the same details.
