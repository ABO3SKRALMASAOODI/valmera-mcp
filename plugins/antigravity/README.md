# Valmera for Antigravity

Edit your recordings through conversation. This native plugin connects Antigravity to the hosted Valmera video editor and supplies three workflows: footage editing, long-video shorts, and website demos.

## Before you begin

Install [Antigravity CLI](https://antigravity.google/docs/getting-started/) and complete its normal sign-in. Create a [Valmera account](https://valmera.io) and upload a recording in Studio. Account creation and uploads are free; hosted editing requires a paid Valmera plan. Your Antigravity account and usage are separate. The plugin files are MIT-licensed.

## Install

Clone the pinned plugin release into a new directory, then install this package:

```sh
git clone --branch antigravity-v1.0.0 --depth 1 https://github.com/ABO3SKRALMASAOODI/valmera-mcp.git valmera-antigravity
agy plugin validate --strict ./valmera-antigravity/plugins/antigravity
agy plugin install ./valmera-antigravity/plugins/antigravity
agy plugin list --json
```

Review the package before installation. In Antigravity, open `/plugin` to inspect the installed skills and `/mcp` to inspect the connection. The bundled server is named `valmera_editor`. Complete the Valmera browser sign-in when requested, then ask: **“List my Valmera projects.”** Choose your uploaded recording before requesting an edit.

This package is distributed directly from Valmera's repository. It is not a claim of inclusion in Google's Marketplace.

## Start an edit

```text
Use Valmera on the uploaded recording I select.
Make a 45-second product update for LinkedIn in 16:9.
Keep the problem, the demonstration and its result in that order.
Remove waiting time and false starts. Keep interface labels readable.
Add accurate captions, keep my voice and do not add music.
Confirm the source and editing cost expectations before starting.
Show a preview; export the version I approve as an MP4.
```

- `/edit-video-with-valmera`: edit recorded footage and review the output.
- `/turn-long-video-into-shorts`: choose self-contained stories before making clips.
- `/website-demo-video`: agree on permitted pages and actions before capture.

Installing a plugin does not upload a recording or start a paid editing job. A local path in a prompt is not an upload; use Studio or authorize the chosen file's transfer through the upload workflow. Let another active edit finish before changing the same project here.

## Connection without the plugin

If you only need the tools, merge this entry into your workspace's `.agents/mcp_config.json`, preserving existing servers:

```json
{
  "mcpServers": {
    "valmera": { "serverUrl": "https://valmera.io/mcp/server" }
  }
}
```

Choose one connection route to avoid duplicate servers. Gemini CLI's `httpUrl` field and `.gemini/settings.json` location are not the Antigravity CLI configuration shown here. See [Google's MCP documentation](https://antigravity.google/docs/mcp/) and [Gemini migration guide](https://antigravity.google/docs/cli/gcli-migration).

## Verification and maintenance

On November 6, 2026, Antigravity CLI 1.5.1 strict validation recognized all three skills and one MCP server with no findings. This validates the package structure, not an authenticated editing session or a rendered video.

The skill copies in this self-contained package come from the repository's shared `skills/` directory. After editing a shared skill, run `python3 scripts/sync-antigravity-skills.py` from the repository root. Check with `python3 scripts/sync-antigravity-skills.py --check`, then rerun `agy plugin validate --strict plugins/antigravity` and increment the plugin version before release.

[Valmera setup](https://valmera.io/mcp/setup) · [Editing workflows](https://valmera.io/mcp/skills) · [Support](mailto:support@valmera.io)
