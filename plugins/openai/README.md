# Valmera for ChatGPT and Codex

Bring your recordings into a conversational editing workflow. This plugin bundles Valmera's OAuth MCP connection, guided setup and three editing skills: footage editing, long-video shorts and website demos.

## Use Valmera today

For ChatGPT, follow the [connection and first-edit guide](https://valmera.io/mcp/chatgpt?utm_source=github&utm_medium=plugin&utm_campaign=openai_plugin_1_0_0). Add the custom MCP server at `https://valmera.io/mcp/server`, complete Valmera sign-in, install the resulting plugin and select it in a conversation. Account and workspace availability apply. This custom connection is separate from installing the four bundled skills in this repository package.

For supported Codex clients, this repository includes a marketplace at `.agents/plugins/marketplace.json`. After reviewing the package, add the repository as a marketplace with the CLI:

```sh
codex plugin marketplace add ABO3SKRALMASAOODI/valmera-mcp --ref main
codex plugin list --marketplace valmera --available --json
```

In the desktop Plugins Directory, select **Valmera video editing**, install **Valmera**, and complete its connection setup. Client support and workspace policies can vary. See [OpenAI's package and marketplace documentation](https://developers.openai.com/plugins/build/plugins). The `main` reference follows repository updates; review changes before upgrading your installed marketplace.

Avoid adding a second Valmera connection if you already have a working one. Installing the package does not itself demonstrate a successful authenticated connection. Ask the assistant to list your Valmera projects and select the intended recording before editing.

## Start with your footage

Create a Valmera account and upload your recording in [Studio](https://valmera.io/studio). Account creation and uploads are free; hosted editing requires a paid [Valmera plan](https://valmera.io/subscribe). Your assistant subscription and usage are separate. Plugin files are MIT-licensed.

- **get-started:** connect, find a recording and prepare an editing brief.
- **edit-video-with-valmera:** edit uploaded footage, review a preview and export the approved version.
- **turn-long-video-into-shorts:** select self-contained stories before making clips.
- **website-demo-video:** agree on the walkthrough, permitted pages and actions before capture.

Try: “Use the recording I select. Make a 60-second vertical highlight that keeps the speaker's meaning, removes repeated starts and adds accurate captions. Confirm the source and cost expectations before starting. Show a preview, then export the version I approve.”

## Public Directory status

This is a source-distributed package, not a claim of approval or listing in OpenAI's public Directory. Public submission requires publisher verification, domain verification, automated checks, a dedicated reviewer account, five executed positive cases, three negative cases and a demonstration recording. Those requirements are tracked separately from package publication. No credentials or invented test results belong in this package.

## Maintenance

The three editing skills are copied from the shared root `skills/` directory. Run `python3 scripts/sync-openai-skills.py` after changing them, or add `--check` to detect drift. The setup skill is maintained here. Increment this package's version before publishing an update. This package uses OpenAI's supported Codex layout. Build a ZIP from this directory's contents, preserving `.codex-plugin/plugin.json`, `.mcp.json`, `skills/` and `assets/`; exclude repository history, credentials and other client packages.

Package/schema and source-integrity checks do not establish authenticated installation or editing behavior. See the [existing cuts-and-crop result](https://valmera.io/examples/trim-and-reframe) for a documented Valmera export; it is not a test of this plugin package.

[Editing workflows](https://valmera.io/mcp/skills) · [Support](mailto:support@valmera.io) · [OpenAI submission requirements](https://developers.openai.com/plugins/deploy/submission)
