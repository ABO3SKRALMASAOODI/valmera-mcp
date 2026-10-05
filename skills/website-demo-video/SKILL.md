---
name: website-demo-video
description: Record a product or website demo video from a URL and edit it into a polished promo with the Valmera connector. Use when the user wants a SaaS demo, product walkthrough, launch video, landing-page promo or screen-recording edit with zooms, cursor highlights, captions or music.
---

# Make a website or product demo video with Valmera

Valmera can drive a real browser through a public website, recording a visible cursor that clicks, scrolls and types. It can then cut the recording like a product video, with zooms that follow each click.

## Workflow

1. **Create a project** with `create_project`, or open the user's project.
2. **Plan a short story.** Write 4–10 steps that show one clear flow, such as the landing page, then the key feature, then the call to action. A demo that clicks everything shows nothing. Ask the user for the URL and the one thing viewers must understand.
3. **Record.** Call `record_website_demo` with the URL, an orientation (`landscape` for websites, `portrait` for social) and the steps. Steps look like `{do:'click', text:'Get started'}`, `{do:'scroll', to:'Pricing'}`, `{do:'hover', text:'Plans'}`, `{do:'type', selector:'input[type=email]', text:'you@example.com'}` and `{do:'wait', seconds:1.5}`. It records the public site as a visitor sees it, and never types into password or payment fields. For a simple scrolling capture, use `record_website`.
4. **Cut it like a product video.** Call `showcase_demo` with the recorded clip. It places the clip and adds zooms that travel between the clicks. For a recording the user uploaded, pass `click_times`, and use `enhance_cursor` and `add_zoom_path` when the pointer is hard to follow.
5. **Add the story layer.** Add a title card (`add_title_card`), short on-screen text for each step (`add_text`), music (`add_music`), and a closing call to action.
6. **Render and check.** Call `render_preview`, then `wait_for_job`, then `look_at` with `rendered=true` at each click, so you can confirm the zooms land on the right element.
7. **Export when asked.** Call `export_final`, then `wait_for_job`, then `download_url` with `kind="final"`.

## Limits

- Only public pages can be recorded. Desktop apps and logged-in areas can't, so ask the user to upload their own screen recording for those.
- Editing requires a Valmera subscription (https://valmera.io/subscribe).
