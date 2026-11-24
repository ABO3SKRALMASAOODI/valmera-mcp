# Valmera security reporting

Report a suspected security issue privately to [support@valmera.io](mailto:support@valmera.io) with the subject “Security report”. This channel covers the hosted Valmera editor and MCP endpoint as well as the client integrations and plugin packages published from this repository.

Include the affected product or plugin version, the date and time with timezone, what you observed, and the potential impact. Use your own account and demonstration footage. Redact credentials, session cookies, project links and other private material before sending logs or screenshots. Keep vulnerability details out of public GitHub issues while Valmera investigates. For a routine sign-in or connector question, use the [connection troubleshooting guide](docs/CONNECTION-TROUBLESHOOTING.md).

## Verify the connector before you authorize it

- The official registry name is `io.valmera/video-editor`. Its [registry record](https://registry.modelcontextprotocol.io/v0.1/servers/io.valmera%2Fvideo-editor/versions/latest) and [Valmera’s server card](https://valmera.io/.well-known/mcp/server-card.json) identify the HTTPS endpoint `https://valmera.io/mcp/server`.
- The [OAuth resource metadata](https://valmera.io/.well-known/oauth-protected-resource) advertises `valmera.edit`. An authorized client can read project information and perform editing operations. Use a dedicated account with demonstration footage when reviewing the connector.
- Install client packages from the [Valmera MCP releases](https://github.com/ABO3SKRALMASAOODI/valmera-mcp/releases). If a report involves an older installation, include its exact release tag and the client name.
- Use the [public connection check](docs/CONNECTION-TROUBLESHOOTING.md#check-public-discovery-without-an-account) to verify the registry, endpoint and authorization discovery without sending footage or credentials. For data handling and deletion, see [Valmera’s privacy policy](https://valmera.io/legal#privacy).
