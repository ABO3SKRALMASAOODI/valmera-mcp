# Video editing prompts for AI assistants

These are paste-ready prompts for an assistant connected to Valmera (Claude, ChatGPT, Cursor, Codex, VS Code or any MCP client). They also work in Valmera Studio's own chat. Be specific about the audience, the length, what must stay, and how you'll judge the result. The assistant reads the transcript and frames, edits, renders a preview, and reports what it changed.

## Talking-head and YouTube cleanup

1. `Remove dead air and filler words (um, uh, you know) but keep natural pauses between ideas. Don't cut inside sentences. Render a preview and list every cut longer than two seconds.`
2. `Find every retake where I restart a sentence and keep only the last clean take. Show me the transcript before and after.`
3. `Tighten this to under 8 minutes without losing any of the five main points. Tell me which sections you shortened and why.`
4. `Cut everything before I say "okay, let's get started" and everything after "see you in the next one".`
5. `Add a jump-cut rhythm: remove pauses longer than 0.4 seconds, then punch in 10% on alternate cuts so the jumps feel intentional.`
6. `Punch in on the three most important lines for emphasis, and don't zoom during the screen-share sections.`

## Captions

7. `Add word-by-word captions: bold white text, the active word highlighted in yellow, two lines max, placed above the bottom third.`
8. `Add captions, then audit them against the audio. Fix the spelling of "Valmera", "Kubernetes" and "Anthropic" everywhere.`
9. `Make the captions smaller and move them up so they don't cover the product I'm holding.`
10. `Mute the captions during the intro music and the outro card.`
11. `This video already has burned-in subtitles in Spanish. Find and erase them, then add clean English captions.`

## Shorts, Reels and TikToks from long videos

12. `Turn this 60-minute podcast into 6 vertical shorts of 30 to 60 seconds. Each one needs a complete story with a hook in the first 2 seconds, captions, and the speaker kept in frame.`
13. `Find the most surprising or contrarian moments in this interview and make each one a short with a bold title card.`
14. `Make one 45-second highlight reel of the funniest moments, cut to the beat of upbeat music.`
15. `Turn this webinar into 5 clips for LinkedIn: square format, captions on, each clip answering one question from the Q&A.`
16. `For every short you made, give me the start and end time in the original, a title, and why it works as a standalone clip.`

## Podcasts and interviews

17. `This is a two-person interview. Reframe to 9:16 and keep whoever is speaking centered. Use a split screen when both talk over each other.`
18. `Remove the off-topic tangent about the weather and the section where the guest asks to restart.`
19. `Normalize the loudness to about -14 LUFS for YouTube and keep the music well under the voices.`
20. `Find every place the guest mentions a number or a statistic and add an on-screen text callout.`

## Reframing and aspect ratios

21. `Make a 9:16 version for TikTok, a 1:1 version for Instagram feed and keep the 16:9 master. Check that faces stay in frame in all three.`
22. `Reframe to vertical but keep the whiteboard visible when I point at it.`
23. `Start the video in 16:9, then expand to full vertical when the product demo starts.`

## B-roll, overlays and graphics

24. `Add relevant b-roll where I mention specific places, products or actions. Keep each insert under 3 seconds and never cover my face during a punchline.`
25. `Add my logo (uploaded as logo.png) in the top-right corner at 70% opacity for the whole video.`
26. `Add a lower-third with my name and title the first time I appear.`
27. `Put a "Subscribe" title card at the end with my channel name.`
28. `Place the headline text behind me so it looks like it's in the scene.`

## Music and sound design

29. `Add calm background music that ducks under my voice, then swells for the last 5 seconds.`
30. `Cut the montage on the beat of the music.`
31. `Add a subtle whoosh on each transition and a pop when each caption keyword appears. Keep it tasteful.`
32. `Remove the background music from this clip, keep the voice, and add a new track.`

## Color and finishing

33. `Give it a warm, cinematic grade but keep skin tones natural.`
34. `Make it look brighter and punchier for social, without blowing out the highlights.`
35. `Fade in from black at the start and out to black at the end.`

## Screen recordings and product demos

36. `Record a 30-second demo of https://example.com: scroll the hero, open the pricing page and hover the main call to action. Then zoom on each click.`
37. `This is a screen recording of a tutorial. Enlarge the cursor, zoom in where I click, and cut the parts where I'm waiting for pages to load.`
38. `Turn this product walkthrough into a 60-second promo with captions, music and a closing title card.`

## Privacy and repair

39. `Blur the face of the person walking behind me between 1:10 and 1:25.`
40. `Blur the license plate visible between 0:42 and 0:51.`
41. `Erase the old date overlay in the bottom-right corner of my recording.`

## Review and delivery

42. `Render a preview, watch it, and tell me anything that looks or sounds wrong before I review it.`
43. `Restore the pause before the final answer; it felt too abrupt. Keep everything else.`
44. `Undo the last change and show me the previous version.`
45. `Export the reviewed version as a full-quality MP4 and give me the download link.`

## Tips that make results better

- **State the goal and the audience.** For example: "a 60-second hook for founders on LinkedIn".
- **Say what must stay.** Names, numbers, the punchline, the call to action.
- **Ask for a preview first** on long or risky edits, and revise one issue at a time.
- **Refer to times in the current preview.** Times shift after cuts, and the assistant maps them back to the source.
- **Ask what changed.** Good agents report each change and anything they couldn't do.

More examples: [valmera.io/prompts](https://valmera.io/prompts) and [valmera.io/blog/ai-video-editing-prompts](https://valmera.io/blog/ai-video-editing-prompts).
