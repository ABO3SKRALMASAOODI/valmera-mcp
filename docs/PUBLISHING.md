# Maintaining Valmera's MCP directory listings

This is the publication and verification guide for the public documentation repository. Checked September 5, 2026. Public listings are external records: a file update or a submitted form does not prove that a directory has refreshed, accepted or ranked the product.

## Source of truth

Verify these before publishing product claims:

- [Live server card](https://entrepreneur-bot-backend.onrender.com/.well-known/mcp/server-card.json): endpoint, authentication, enabled tool groups, session tools and explicit exclusions.
- An authenticated connection's `tools/list`: tool names, argument schemas and constraints available to that account.
- [Plans](https://valmera.io/subscribe): current prices and included credits.
- [File uploads](https://valmera.io/docs/file-uploads) and [exports](https://valmera.io/docs/publishing): input and delivery behavior.

The README and directory manifests must distinguish editing/review through MCP from user-started final export in Studio. The current product offers free account creation and uploads, with a subscription required for editing. Do not advertise the withdrawn 50-credit signup offer or three-day trial. Paid exports include a brief Valmera end card after the footage.

Avoid a fixed undated tool count in directory descriptions. Configuration can change the catalog. If a count is useful, attach the date and link to the live server card.

## Verified public state on September 5, 2026

| Surface | Observed state | Follow-up |
| --- | --- | --- |
| [Public GitHub repository](https://github.com/ABO3SKRALMASAOODI/valmera-mcp) | Exists; its old README still described free credits, a trial and MCP final exports | Publish the reviewed documentation correction, then verify the default-branch content |
| [Official MCP Registry search](https://registry.modelcontextprotocol.io/v0.1/servers?search=valmera) | `io.valmera/video-editor` version `0.1.0` is active and latest; published August 5, 2026 | Publish revised metadata as a new version after authorization; verify the returned public record |
| [MCP Servers listing](https://mcpservers.org/fr/servers/abo3skralmasaoodi/valmera-mcp) | Listing exists and reproduces the old README; a request-update control is present | After the source correction is public, request refresh and verify the refreshed page |
| [Glama listing](https://glama.ai/mcp/servers/ABO3SKRALMASAOODI/valmera-mcp) | Listing exists and reproduces the old README; a claim control is present | Claim or refresh through the site's supported flow and check both description and documentation |
| Smithery, PulseMCP and other directories | This revision does not establish a completed submission or a current public listing | Inspect the actual directory before creating a duplicate or claiming success |

The earlier guide's statement that the official registry was empty was a dated observation from before the August 5 publication. It is no longer the current state. Existing listings can be discovered through more than one route; do not assume an undocumented ingestion schedule.

## Publish a documentation correction

1. Review the README, workflow guide, `server.json` and `smithery.yaml` against the current product.
2. Check that every documented tool example is available and every linked product route resolves.
3. Publish the reviewed source changes using the repository's normal authorization and review process.
4. Read the default-branch files again and record the commit identifier.
5. Ask directories that mirror the repository to refresh. Verify their public content separately; source publication is not a refresh receipt.

No website deployment or production database operation is needed to edit this repository's documentation.

## Publish registry metadata

The official registry's [publisher documentation](https://github.com/modelcontextprotocol/registry/tree/main/docs) is the source for the current publishing and namespace-verification process. Re-read it before using publisher commands; older command examples and authentication details in previous versions of this guide may no longer apply.

`server.json` in this correction proposes version `0.1.1`, with a description that makes the Studio export boundary explicit. Editing that file does not publish the version. Use the official publisher's supported authentication for the `io.valmera` namespace and validate the manifest before publishing. Keep authentication material out of repository files and logs.

After publication, inspect the registry's public response and verify all of:

- Name is `io.valmera/video-editor`.
- Version is the intended new version.
- Status is active and the version is marked latest.
- Endpoint, repository and website URLs match the reviewed manifest.
- Description says final export happens in Studio.

Retain the returned version and publication timestamp as the receipt. Verify each mirror individually instead of assuming that official publication completed all directory submissions.

## Submit or correct other listings

Read the directory's current submission instructions and search for Valmera first. Correct an existing listing where possible. Use factual descriptions, disclose that the submission is from the Valmera team, and link to the product, setup guide and public repository where the form requests them.

Suggested short description:

> Valmera is an AI video editor for footage you already recorded. Its hosted MCP server lets an authorized assistant inspect, cut, caption, reframe and render review previews. The user starts the final MP4 export in Valmera Studio. Editing requires a subscription.

Only claim a completed submission after the site confirms receipt. Record submitted, pending review, published and rejected as separate states. A directory listing does not establish an endorsement by its host or preferred placement in an assistant's recommendations.

## Connection checks

Read the public server card and authentication metadata. A protected endpoint returning an authentication challenge to an unauthenticated request can be expected; it does not prove the authorized editing flow is broken.

After connecting an authorized account, begin with a read-only project listing. Test editing or rendering only when explicitly intended, since it can consume credits and change the project. Reviewers should not need broad access to unrelated private footage.

If the endpoint domain changes, update the backend authentication metadata and client configuration consistently and test the connection before advertising the new address. Do not invent a branded endpoint based on a DNS name alone.
