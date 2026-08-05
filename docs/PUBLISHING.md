# Publishing Valmera to the MCP registries

Ordered by leverage. Every one of these is a place an assistant looks when a user
asks "how do I edit video with Claude" — and several are crawled far more
aggressively than valmera.io is.

Everything below was executed against the live services on **2026-08-05**: the
registry's health, version, validate and OpenAPI endpoints (with our actual
`server.json`); the deployed server card and both OAuth metadata documents; the
GitHub API for every list's star count and push date; `dig` for DNS; the
**submit forms of mcp.so and mcpservers.org, parsed field by field**; and the
**Smithery CLI's own compiled source** (`@smithery/cli@4.11.1`, pulled from npm
and read). Where a claim could **not** be reached from a terminal — a
Cloudflare-blocked page, a login-walled form, an ingestion cadence a site states
about itself — it is marked **unverified** and says why. Nothing here is
inferred from a search result.

**Three things in the previous revision were wrong, and two of them would have
cost you a failed submission.** Read "What changed" before you execute anything.

---

## The leverage, in one paragraph

**One publish to the official registry lands several directories at once.**
PulseMCP states on its own `/submit` page: *"We ingest entries from the Official
MCP Registry daily and process them weekly."* You do not submit to PulseMCP — you
publish once and appear there. The `augmentcode.com/mcp` and
`claudemarketplaces.com` mirrors, both of which surfaced twice in the audit's
searches, are very likely fed the same way. So the official-registry publish is
the one step that pays several times, and the steps before it exist only because
it is worthless without them.

> **Unverified, and newly so:** `pulsemcp.com/submit` returns **403** to curl
> today (bot protection). The daily/weekly quote is from the audit's browser
> read, not from a terminal, and it is the site's own claim about itself either
> way. The two mirrors document no source and expose no API, so "they ingest the
> official registry" remains an inference. Treat both as *probable*, and see the
> propagation table for the day-7 cutoff at which you stop waiting and submit by
> hand.

Live, today:

```
GET https://registry.modelcontextprotocol.io/v0.1/health
  → {"status":"ok","github_client_id":"Iv23liUydBbI7Z2Q9bOZ"}

GET https://registry.modelcontextprotocol.io/v0.1/version
  → {"version":"1.8.0","git_commit":"d813d2b8…","build_time":"2026-07-13T08:48:44Z"}

GET https://registry.modelcontextprotocol.io/v0.1/servers?search=valmera
  → {"servers":[],"metadata":{"count":0}}
```

It is live, it is taking publishes, and **Valmera is absent from the one registry
everything else ingests.** (`/health` does *not* carry the build number — an
earlier draft said it did. Version lives at `/v0.1/version`.)

The OpenAPI at `/openapi.yaml` exposes `POST /v0.1/publish` (registry JWT in the
`Authorization` header), `POST /v0.1/validate` (**unauthenticated** — use it
freely), and **five** token exchanges: `/v0.1/auth/dns`, `/v0.1/auth/http`,
`/v0.1/auth/github-at`, `/v0.1/auth/github-oidc`, `/v0.1/auth/oidc`. Reads live
at `/v0.1/servers`, `/v0.1/servers/{name}/versions` and
`/v0.1/servers/{name}/versions/{version}` — where `latest` is a documented magic
value, not a guess. Every path is mirrored under the older `/v0` prefix; publish
against `/v0.1`.

---

## What changed since the last revision

**1. `server.json` now VALIDATES.** The previous revision opened its step 5 with
a 422 and three errors. Those are fixed in the working tree — the description is
**96 characters** (cap is 100) and both `icons[].sizes` are arrays. Re-run today:

```
POST /v0.1/validate  -d @server.json  → {"valid":true,"issues":[]}
```

So step 5 is no longer "fix the manifest". It is **one field**: `remotes[0].url`
still points at `entrepreneur-bot-backend.onrender.com`, which is Blocker A2.

**2. `README.md` already carries the corrected tool count** (108 — 97 editing,
11 session). **`smithery.yaml:18` still says 110.** One file, one line, and it is
the file Smithery reads. The count is computed live by the card; never trust a
number written in a file, including this one:

```bash
curl -s https://entrepreneur-bot-backend.onrender.com/.well-known/mcp/server-card.json \
  | python3 -c "import json,sys;print(json.load(sys.stdin)['toolCount'])"   # → 108
```

**3. THE SMITHERY GUIDANCE WAS WRONG.** The previous revision said Smithery's
tool scan "will hit our 401, so it falls back to
`/.well-known/mcp/server-card.json`." Read the CLI's compiled source and neither
half survives:

- `grep -c "server-card\|card.json"` over `@smithery/cli@4.11.1` → **0**. Smithery
  never asks for that file. The `.well-known` paths it *does* fetch are
  `oauth-authorization-server`, `openid-configuration` and `skills/`.
- It does not fail on the 401 either. The release state machine has a status
  **`AUTH_REQUIRED`**, and on hitting it the CLI prints *"OAuth authorization
  required. Please authorize at https://smithery.ai/servers/{name}/releases/ …
  Once authorized, release will automatically continue."* Smithery performs a
  real OAuth sign-in against our server and then scans the **real** toolset.

The consequence is the opposite of what the old text implied, and it is
load-bearing: **whoever clicks that authorize link signs in as a real Valmera
account, and if that account is not on `MCP_ALLOWED_EMAILS` the scan gets 401 and
the release ends in `FAILURE_SCAN`.** Step 3 is a hard prerequisite for step 7,
not an adjacent nicety. (`FAILURE`, `FAILURE_SCAN`, `INTERNAL_ERROR` and
`CANCELLED` are all real terminal statuses in that state machine.)

**4. mcp.so's submit form REQUIRES a repository URL.** Parsed today:
`https://mcp.so/submit` 307s to `?type=server`, and the form is two fields —
**`Repository URL*`** (required, placeholder `https://github.com/owner/repository`)
and `Name`. So mcp.so joins Glama, cursor.directory, Cline and mcpmarket on the
list of listings that are **impossible without step 1**. That is five, not four.

**5. `docs/MCP.md` does not exist.** The previous revision told you to update it
in two places. `docs/` contains this file and nothing else. Where it said
`docs/MCP.md`, read `README.md` plus the frontend `/mcp` and `/mcp/tools` pages.

---

## Read this before you run anything

**Two human decisions** stand between here and a listing anyone can use. No
command resolves either.

### A1 — four generative tools may get the connector rejected by Anthropic

Anthropic's Connectors Directory review criteria bar connectors that *"generate
images, video, or audio via AI models."* The live card confirms all four are on
the MCP surface today — `generate_image`, `generate_video`, `generate_sfx` and
`add_voiceover` are all present in the published groups (verified by reading the
card's `toolGroups`). That is a genuine rejection risk on the single
highest-value listing that exists.

The honest remedy is also the better positioning: **gate those four off the MCP
tool surface** and keep them in the studio. Valmera's whole differentiator is
that it edits footage you already have — a directory card that *also* says
"generates video with AI" sells the thing every competitor sells and buries the
thing none of them do.

Mechanically this is one small edit, because everything downstream derives from
one function. Filtering the list `_editor_tools()` returns
(`backend/routes/mcp.py:319`) takes the tools out of `tools/list`, out of the
`known` set that `tools/call` validates against (`:1116`) — so a call to a gated
name gets the existing honest "not on this deployment" answer rather than a
crash — and out of the card's live `toolCount` (`:1215`). One denylist, three
surfaces, no drift.

Decide this **before step 6**, so the tool count is stable in every listing that
quotes it. If you gate them, **108 becomes 104**, and `README.md`,
`smithery.yaml` and the marketing pages move in the same pass.

### A2 — the endpoint is `entrepreneur-bot-backend.onrender.com`

Three separate problems, one cause:

1. Anthropic's criteria say the MCP server domain should match the service.
2. A directory card reading `entrepreneur-bot-backend.onrender.com` reads as an
   unrelated product. It breaks the brand chain at the exact moment a stranger is
   deciding whether to trust it.
3. DNS namespace verification (step 6) proves you own **valmera.io** while
   `server.json` points at a host on someone else's domain. Coherent to a
   validator, incoherent to a human.

It is not hypothetical — this is the live OAuth metadata, which is what a strict
client (and Smithery) fetches before it will talk to us at all:

```
GET /.well-known/oauth-authorization-server
  → issuer:                 https://entrepreneur-bot-backend.onrender.com
    authorization_endpoint: …/mcp/oauth/authorize
    token_endpoint:         …/mcp/oauth/token
    registration_endpoint:  …/mcp/oauth/register
    revocation_endpoint:    …/mcp/oauth/revoke
    code_challenge_methods_supported: ["S256"]
    scopes_supported: ["valmera.edit"]

GET /.well-known/oauth-protected-resource
  → resource:      https://entrepreneur-bot-backend.onrender.com/mcp
    resource_name: "Valmera Video Editor"
```

Everything a client sees at connect time says `onrender.com`. Moving to
`https://mcp.valmera.io/mcp` fixes all three problems, and every future listing
then carries a **valmera.io URL** — which, for a domain with effectively zero
backlinks, is itself part of the point. `dig +short mcp.valmera.io` returns
**nothing** today. This is step 4, and it drags `server.json`, `smithery.yaml`,
`README.md`, the `/mcp` and `/mcp/tools` marketing pages, and the OAuth issuer
and metadata URLs with it.

---

## 0. Install the tooling and confirm the server is up

**Who:** machine, except one browser login. Two minutes, and it prevents the two
dumbest failures.

Confirmed absent on this machine today: `gh`, `mcp-publisher` and `smithery` all
return nothing from `command -v`. Steps 1, 10 and 12 are written entirely in
`gh`. Homebrew carries `mcp-publisher` **1.8.0** — the same version the live
registry reports.

```bash
brew install gh mcp-publisher
gh auth login                      # human: browser flow, once
openssl version                    # → OpenSSL 3.6.3 here; must be 3.x, see 6b
```

Smithery has no Homebrew formula; it is `@smithery/cli` on npm (**4.11.1**
today). Run it with `npx` rather than installing:

```bash
npx -y @smithery/cli@latest --help
```

Then confirm the backend is actually serving before you submit anything anywhere:

```bash
curl -s -o /dev/null -w "healthz %{http_code}\n" \
  https://entrepreneur-bot-backend.onrender.com/healthz
curl -s -o /dev/null -w "card    %{http_code}\n" \
  https://entrepreneur-bot-backend.onrender.com/.well-known/mcp/server-card.json
```

Want `200` and `200` (both confirmed today). A `502` means Render is mid-deploy —
wait it out. This machine saw a run of them for several minutes after the
round-87 push, and **several of these directories scan your endpoint at
submission time**; a submission that lands during a redeploy is recorded as a
dead server.

---

## 1. Create and push the public GitHub repo

**Who:** human (creates the repo), then machine (pushes). **First, because five
listings are impossible without it.**

This repo has **no git remote** — `git remote -v` prints nothing. It exists on one
laptop, with one commit (`15092f3`). That is not cosmetic: **Glama,
cursor.directory, Cline's marketplace, mcpmarket and — newly verified today —
mcp.so all key off a public GitHub repo**, so without one Valmera is ineligible
for five listings outright. The audit's headline finding was that github.com is
the single most recurring domain across every agent-adjacent query, and Valmera
is structurally absent from that source class. This is the step that ends that.

```bash
cd ~/Documents/valmera-mcp
git config user.name "ABO3SKRALMASAOODI"
git config user.email "shmarymuslim@gmail.com"

gh repo create ABO3SKRALMASAOODI/valmera-mcp --public \
  --description "Agentic AI video editor as a remote MCP server — 108 tools over an edit decision list." \
  --homepage "https://valmera.io/mcp"

git remote add origin https://github.com/ABO3SKRALMASAOODI/valmera-mcp.git
git branch -M main
git push -u origin main
```

Then set **topics** — this is how the auto-indexers find you:

```bash
gh api -X PUT repos/ABO3SKRALMASAOODI/valmera-mcp/topics \
  -f names[]=mcp -f names[]=model-context-protocol -f names[]=mcp-server \
  -f names[]=video-editing -f names[]=ai-video-editor -f names[]=agentic \
  -f names[]=ffmpeg -f names[]=captions -f names[]=transcription -f names[]=shorts
```

Commit identity matters here for the same reason it matters everywhere in this
project: Vercel Hobby blocks deploys from unrecognised committers, and a repo
whose history is signed by someone else reads as a fork.

**While you are here, grab the numeric repo id.** The registry's `Repository`
schema carries an optional `id` whose documented purpose is *"to detect
repository resurrection attacks — if a repository is deleted and recreated, the
ID should change."* Adding it makes the registry entry harder to hijack and costs
one command:

```bash
gh api repos/ABO3SKRALMASAOODI/valmera-mcp --jq '.id'
# → paste into server.json as repository.id (string), then re-run the validator in step 5
```

**Verify:**

```bash
curl -s https://api.github.com/repos/ABO3SKRALMASAOODI/valmera-mcp \
  | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['full_name'],d['private'],d['topics'])"
# → ABO3SKRALMASAOODI/valmera-mcp False ['agentic', 'captions', ...]
```

---

## 2. Reconcile every number against the live card

**Who:** machine. Smaller than it was — `README.md` is already correct.

The card is live and computes the count from the running catalog. Read the truth
off the server, then make every file agree with it:

```bash
curl -s https://entrepreneur-bot-backend.onrender.com/.well-known/mcp/server-card.json \
  | python3 -c "
import json,sys
d=json.load(sys.stdin)
g=d['toolGroups']
print('toolCount   ', d['toolCount'])
print('editor tools', sum(len(v) for v in g.values()))
print('session     ', len(d['sessionTools']))
print('families    ', {k: len(v) for k, v in g.items()})
"
```

Today that prints:

```
toolCount    108
editor tools 97
session      11
families     {'audio': 15, 'captions and on-screen text': 10, 'colour and finishing': 8,
              'cutting': 6, 'editing': 5, 'framing and motion': 17,
              'media, generation and screen capture': 14, 'reading the footage': 16,
              'repair and censoring': 6}
```

**The one file still wrong:**

- `smithery.yaml:18` — `110 tools operating on an edit decision list` → **108**

```bash
cd ~/Documents/valmera-mcp
grep -rn "110" README.md smithery.yaml   # should return nothing when you are done
```

**Three drifts between the card and `server.json`.** Both get read by strangers,
and the two are rendered side by side in some directories:

| Field | Live card | `server.json` |
|---|---|---|
| `version` | `0.1.0` | `1.0.0` |
| `websiteUrl` | `https://valmera.io` | `https://valmera.io/mcp` |
| `title` | `Valmera — agentic AI video editor` | `Valmera — Agentic AI Video Editor` |

Pick one of each. The registry entry's `version` is what you bump on republish
(see "Keeping the entry true"), so make the card and the manifest start from the
same number or the first bump is ambiguous.

**What the card carries**, so you can fill in a submission form accurately
without opening a file: `name` (`io.valmera/video-editor`), `title`, a
402-character `description`, `version`, `websiteUrl`, `documentationUrl`
(`valmera.io/mcp`), `toolReferenceUrl` (`valmera.io/mcp/tools`), `iconUrl`
(`valmera.io/icon-512.png`), the `streamable-http` `remotes` entry, an
`authentication` block (`oauth2`, `dynamicClientRegistration: true`,
`pkce: S256`, `alsoAccepts` the bearer token, and the metadata URL), a **live**
`toolCount`, `toolGroups` (tool names bucketed into 9 families), `sessionTools`
(11 names), `notes`, `notSupported` (9 honest limits) and `pricing`
(`50 one-time credits, no credit card` / `USD 30/month` /
`valmera.io/subscribe`). No user data, no tokens, no per-account state.

Note the shape: tool names are under **`toolGroups`**, not a flat `tools` key. An
earlier version of this file's verify command looked for `tools` and would have
printed `0` for a perfectly healthy card.

The per-tool `title` and `annotations` that Anthropic's wizard checks are on the
`tools/list` response, not the card — `_annotations_for()`
(`backend/routes/mcp.py:299`) emits `readOnlyHint`, `destructiveHint` (**true
only for `reset_edit`**), `idempotentHint` (`set_*` and `remove_*`) and
`openWorldHint`. You cannot curl that without a token. It is deployed: `0ac21c6`
*"round 87: the MCP registry can read the toolset without logging in"* is
committed, pushed, and the working tree is clean against it.

---

## 3. Open the door — `MCP_ALLOWED_EMAILS`

**Who:** human (Render dashboard), plus a one-line code decision. **Blocks step 7
as well as every human visitor.**

`backend/routes/mcp.py:71`:

```python
ALLOWED_EMAILS = {e.strip().lower()
                  for e in os.getenv("MCP_ALLOWED_EMAILS", ADMIN_EMAIL).split(",")}
```

Re-checked on **every request** (`:177`), for OAuth sessions and minted tokens
alike. With `MCP_ALLOWED_EMAILS` unset on Render, exactly one address on earth can
use this server. Meanwhile the card you are about to publish to the world says
`pricing.free = "50 one-time credits, no credit card"`, and `README.md:265` says
*"Free accounts can connect and edit until the 50 credits run out."*

Publish today and every visitor a directory sends you completes an OAuth flow and
is then told **"this account is not enabled for MCP access."** And now that we
know Smithery signs in for real (see "What changed", item 3), the same wall ends
your Smithery release in `FAILURE_SCAN`. Two coherent answers:

- **Open it.** Change the code so an empty/absent value means *any signed-in
  Valmera account* — today an empty set means **nobody**, because
  `not in ALLOWED_EMAILS` is true for everyone. This matches what the card and the
  README both promise, and costs nothing that isn't already metered: the plan gate
  and the credit gate are both live on the MCP path, and the free pool is 50
  credits, so "open" does not mean "unbilled".
- **Stage it.** Keep the allowlist and hand the URL to a dozen people first.
  Legitimate — but then **do not publish**, because a listing you cannot serve is
  the expensive kind of mistake: failed first runs get written up, and the
  write-up outranks you.

Either way, the card's `pricing.free`, `README.md:265` and the `/mcp` marketing
page must say the true thing before step 6.

**Verify** — from a *non-admin* account's token:

```bash
curl -s -o /dev/null -w "%{http_code}\n" -X POST \
  -H "Authorization: Bearer vlm_mcp_..." -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' \
  https://entrepreneur-bot-backend.onrender.com/mcp
```

`200` = open. `401` with *"this account is not enabled for MCP access"* = still
gated. (An **unauthenticated** POST returns `401` either way — verified again
today. That one is correct: it is what tells a client to go and do OAuth.)

---

## 4. Move the endpoint to `mcp.valmera.io`

**Who:** human (Cloudflare + Render), then machine (code edits). **Blocker A2.**

valmera.io is on **Cloudflare** — `dig +short NS valmera.io` →
`hank.ns.cloudflare.com`, `christina.ns.cloudflare.com` — so this is a Cloudflare
DNS record plus a Render custom domain.

1. Render → backend service → **Settings → Custom Domains → Add** →
   `mcp.valmera.io`. Render prints the CNAME target.
2. Cloudflare → valmera.io → DNS → **Add record**: type `CNAME`, name `mcp`,
   target whatever Render printed. **Proxy status: DNS only (grey cloud)** —
   Render cannot complete its ACME challenge through Cloudflare's proxy. You can
   turn the orange cloud on afterwards, but only with SSL mode **Full (strict)**.
3. Wait for Render to show the domain verified with a certificate issued.
4. Render → **Environment** → `BACKEND_URL=https://mcp.valmera.io`. **This one
   variable is the entire switch.** `backend/routes/mcp_oauth.py:56` `base_url()`
   reads it, and it is the OAuth **issuer** plus every metadata, resource and
   remote URL — including the ones inside the server card. Its docstring is right
   that the value "has to be byte-identical everywhere it appears or a strict
   client rejects the metadata it just fetched" — so change it in the env, once,
   and never hardcode the new host anywhere.
5. Then update, in this repo and the others:
   - `server.json` → `remotes[0].url` (this is the last thing keeping step 5 open)
   - `smithery.yaml` → `startCommand.url` (line 10 today)
   - `README.md` — four occurrences of the onrender host (lines 16, 47, 55, 64)
   - the frontend `/mcp` and `/mcp/tools` marketing pages
6. **Keep the old host answering.** Do *not* redirect `/mcp` — OAuth clients that
   already registered against the old issuer will break. Leave both live; the new
   one is what you publish.

**Verify:**

```bash
dig +short mcp.valmera.io                      # must return something (empty today)

curl -s -o /dev/null -w "card %{http_code}\n" \
  https://mcp.valmera.io/.well-known/mcp/server-card.json

curl -s https://mcp.valmera.io/.well-known/oauth-authorization-server \
  | python3 -c "import json,sys;print(json.load(sys.stdin)['issuer'])"
# → https://mcp.valmera.io      (says entrepreneur-bot-backend.onrender.com today)

curl -s https://mcp.valmera.io/.well-known/oauth-protected-resource \
  | python3 -c "import json,sys;print(json.load(sys.stdin)['resource'])"
# → https://mcp.valmera.io/mcp

curl -s https://mcp.valmera.io/.well-known/mcp/server-card.json \
  | python3 -c "import json,sys;print(json.load(sys.stdin)['remotes'][0]['url'])"
# → https://mcp.valmera.io/mcp
```

If `issuer` still says `entrepreneur-bot-backend.onrender.com`, `BACKEND_URL` did
not take — redeploy.

---

## 5. `server.json` — one field left

**Who:** machine.

The previous revision opened this step with a 422. **That is fixed.** As it sits
in the working tree today the file returns `{"valid":true,"issues":[]}` from the
live validator. What remains is the A2 edit: `remotes[0].url`.

Two constraints worth carrying in your head, because they are the two that bit us:

- **`description` is capped at 100 characters.** This is the field every mirror
  renders, so the cap is not an inconvenience — those 100 characters *are* the
  pitch, in every directory, forever. Ours is **96**.
- **`icons[].sizes` is an array**, not a string.

A hosted server needs **no npm or PyPI package**, so there is no
package-ownership proof step and no `packages` block at all — `remotes` is the
entire distribution story.

The file, with the step-4 host and the step-1 repo id:

```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
  "name": "io.valmera/video-editor",
  "title": "Valmera — Agentic AI Video Editor",
  "description": "Agentic video editing on real footage: cut, caption, reframe, score, and export at full quality.",
  "version": "1.0.0",
  "repository": {
    "url": "https://github.com/ABO3SKRALMASAOODI/valmera-mcp",
    "source": "github",
    "id": "<gh api repos/ABO3SKRALMASAOODI/valmera-mcp --jq .id>"
  },
  "websiteUrl": "https://valmera.io/mcp",
  "icons": [
    { "src": "https://valmera.io/icon-512.png", "sizes": ["512x512"], "mimeType": "image/png" },
    { "src": "https://valmera.io/icon-192.png", "sizes": ["192x192"], "mimeType": "image/png" }
  ],
  "remotes": [ { "type": "streamable-http", "url": "https://mcp.valmera.io/mcp" } ]
}
```

Count before you touch the description:

```bash
python3 -c "import json;print(len(json.load(open('server.json'))['description']))"   # → 96
```

Both icon URLs return `200 image/png`, and both marketing pages
(`valmera.io/mcp`, `valmera.io/mcp/tools`) return `200` — all four checked today.
The description deliberately does **not** quote a tool count: one fewer number to
keep in sync, and 100 characters is too few to spend two of them on it.

**Verify:**

```bash
curl -s -X POST -H "Content-Type: application/json" \
  -d @server.json https://registry.modelcontextprotocol.io/v0.1/validate
# → {"valid":true,"issues":[]}
```

---

## 6. Publish to the Official MCP Registry — the leverage step

**Who:** human for the DNS record; machine for everything else.

### 6a. The publisher

Installed in step 0. Confirm:

```bash
mcp-publisher --help
```

(`brew info mcp-publisher` today: `stable 1.8.0 (bottled)` — the same version the
live registry reports at `/v0.1/version`.)

### 6b. Prove the namespace with an Ed25519 key

`server.json` claims `io.valmera/video-editor` — the reverse-DNS form of a domain
you own. Worth the extra step over the anonymous `io.github.<user>/…` form: it
reads as a company rather than a side project, and it is the name every
downstream mirror copies.

**DNS verification covers the domain *and its subdomains* — `com.domain/*` plus
`com.domain.anything/*`. HTTP verification (`/v0.1/auth/http`) covers only the
exact domain.** So proving `valmera.io` by DNS covers `io.valmera/*` today and
anything you namespace under it later. Prefer DNS for that reason alone.

DNS auth is a **signed challenge**, not a token you paste: you generate an
Ed25519 keypair, publish the *public* key as a TXT record, and `mcp-publisher`
signs an RFC3339 timestamp that the registry verifies against it. The endpoint is
`POST /v0.1/auth/dns` (`SignatureTokenExchangeInput` → `TokenResponse`,
summarised in the OpenAPI as *"Exchange DNS signature for Registry JWT"*), and
that JWT is what `POST /v0.1/publish` takes in the `Authorization` header.

```bash
cd ~/Documents/valmera-mcp
echo "key.pem" >> .gitignore          # BEFORE you generate it
MY_DOMAIN="valmera.io"

openssl genpkey -algorithm Ed25519 -out key.pem
PUBLIC_KEY="$(openssl pkey -in key.pem -pubout -outform DER | tail -c 32 | base64)"
echo "${MY_DOMAIN}. IN TXT \"v=MCPv1; k=ed25519; p=${PUBLIC_KEY}\""
```

> **The TXT record goes on the APEX.** An earlier draft said
> `_mcp-registry.valmera.io`; that is wrong and fails. It is SPF-style, not
> DKIM-style — a record under a selector is simply never read, and you get a
> generic signature error with no hint as to why.

> `openssl genpkey -algorithm Ed25519` needs **OpenSSL 3.0+**. This machine has
> **3.6.3**, so it works. On a Mac using the stock LibreSSL binary it fails with
> `Algorithm Ed25519 not found` — `brew install openssl@3` and call the binary
> explicitly. Homebrew here lives at `/usr/local` (Intel), so that path is
> `/usr/local/opt/openssl@3/bin/openssl`; on Apple Silicon it is
> `/opt/homebrew/opt/openssl@3/bin/openssl`.

In **Cloudflare** → valmera.io → DNS → Add record:

```
Type:  TXT
Name:  @                (this is what makes it apex — not "_mcp-registry")
Value: v=MCPv1; k=ed25519; p=<PUBLIC_KEY from above>
TTL:   Auto
```

`dig +short TXT valmera.io` returns **four** records today — two
`google-site-verification`, one `v=spf1 include:_spf.mx.cloudflare.net ~all`, one
`brevo-code`. A fifth coexists fine. **If you ever rotate this key, delete the old
record** — a stale one gets tried and fails verification.

`.gitignore` holds only `.DS_Store` and `node_modules/` today, which is why the
`echo` above is the first line of the block. Back the key up outside the repo — it
is the only thing that can ever republish under this namespace.

**Verify the record before you try to publish** (propagation is usually seconds on
Cloudflare, but a failed publish tells you nothing useful):

```bash
dig +short TXT valmera.io | grep MCPv1
```

### 6c. Log in and publish

```bash
PRIVATE_KEY="$(openssl pkey -in key.pem -noout -text | grep -A3 "priv:" | tail -n +2 | tr -d ' :\n')"
mcp-publisher login dns --domain "${MY_DOMAIN}" --private-key "${PRIVATE_KEY}"

mcp-publisher validate    # local, exhaustive — reports every issue at once
mcp-publisher publish
```

The two `mcp-publisher` invocations are **unverified**: the binary is not
installed on this machine, so the flag names come from the registry's own docs
rather than from a run. The HTTP endpoints they hit *are* verified, and so is the
manifest they will send. If a flag has drifted,
`mcp-publisher login dns --help` is the authority, not this file.

**Fallback if DNS is genuinely blocked:** change `name` to
`io.github.ABO3SKRALMASAOODI/valmera-mcp` and run `mcp-publisher login github`
(browser OAuth; grants `io.github.<username>/*`). No DNS at all. You can migrate
to the domain namespace later, but the mirrors will have cached the github-form
name by then — so prefer DNS.

**Verify:**

```bash
curl -s "https://registry.modelcontextprotocol.io/v0.1/servers?search=valmera" | python3 -m json.tool

curl -s "https://registry.modelcontextprotocol.io/v0.1/servers/io.valmera%2Fvideo-editor/versions/latest" \
  | python3 -m json.tool
```

Note the URL-encoded `%2F` — the registry requires it in path parameters — and
that `latest` is a documented magic value on that route, not a guess.

---

## 7. Smithery — bring your own hosting

**Who:** machine (CLI) plus **one human browser click** you cannot skip.
**Requires step 3.**

Smithery lists servers you host yourself. The command, read out of the CLI's own
help text rather than from a docs page:

```bash
npx -y @smithery/cli@latest auth login          # human: browser (WorkOS)
npx -y @smithery/cli@latest mcp publish "https://mcp.valmera.io/mcp" -n valmera/video-editor
```

Two corrections to the obvious guesses. The name flag takes a **bare
`org/server`** — the CLI's own examples are `-n myorg/my-server`, with no `@`
prefix. And `smithery.ai/new` is not the form URL: it **308s to
`/servers/new`**, which then **302s to a WorkOS sign-in**. There is no anonymous
web submission.

**What actually happens on an OAuth-protected server** (this is the part the
previous revision got wrong). Smithery scans the live endpoint to build the tool
list. Ours answers `401` unauthenticated — verified again today — so the release
enters status **`AUTH_REQUIRED`** and the CLI prints:

```
⚠ OAuth authorization required.
Please authorize at: https://smithery.ai/servers/valmera/video-editor/releases/
Once authorized, release will automatically continue.
```

A human opens that page and signs in **as a real Valmera account**. Which means:

- If that account is not on `MCP_ALLOWED_EMAILS`, the scan gets `401`, and the
  release lands in **`FAILURE_SCAN`** — a terminal status, not a retry.
- After authorizing, `--resume` picks the paused release back up:
  `npx -y @smithery/cli@latest mcp publish "https://mcp.valmera.io/mcp" -n valmera/video-editor --resume`
- Smithery reads `/.well-known/oauth-authorization-server` (it is one of only
  three `.well-known` paths in the whole CLI). It **never** requests
  `/.well-known/mcp/server-card.json` — `grep -c` over the compiled CLI returns
  **0**. The card is still worth having for every other scraper; just do not
  expect it to rescue this step.

`smithery.yaml` in this repo is already written for the HTTP transport and
carries the OAuth note, four categories and four example prompts — but line 18
still says **110 tools** and line 10 still points at the onrender host, so do
steps 2 and 4 first.

**Verify:**

```bash
npx -y @smithery/cli@latest mcp search valmera --json
```

Then the server page at `https://smithery.ai/servers/valmera/video-editor`.

---

## 8. mcp.so — the best-value paid link in the whole audit

**Who:** human. <https://mcp.so/submit> (307s to `?type=server`).
**Requires step 1 — the repo URL is a required field.**

Ranked **#1** for "mcp server video editing" — the exact query a person with our
problem types. Self-reports DR 72, 2.58K referring domains, 2.2M annual uniques
(their own numbers; **unverified** by us).

The form, parsed from the live page today, is **two fields**:

| Field | Required | Value |
|---|---|---|
| `Repository URL` | **yes** (`*`) | `https://github.com/ABO3SKRALMASAOODI/valmera-mcp` |
| `Name` | no (2–120 chars) | `Valmera` |

That is it — everything else is scraped from the repo, which is another reason
the README's first screen matters more than any submission blurb. There is no
description, endpoint or icon field to fill in.

The paid tier, quoted verbatim from the page: **"$39 one-time publishing fee —
Publish immediately without review · Verified badge · Featured and priority
placement · Dofollow project link."**

Say it plainly: for a site with effectively zero backlinks, the two $39 dofollow
links — this one and mcpservers.org — are **the best-value paid spend found in
the entire audit**. Far better than the reported **$347** for There's An AI For
That, a domain that appeared in **none** of the audit's eight result sets.

**Verify:** search `valmera` at <https://mcp.so>. Browser only.

---

## 9. mcpservers.org — one form, two surfaces

**Who:** human. <https://mcpservers.org/submit>

`wong2/awesome-mcp-servers` (**4,245 stars**, GitHub API, 2026-08-05) **refuses
pull requests** — its README's first note is *"We do not accept PRs. Please submit
your MCP on the website: https://mcpservers.org/submit"*, and its
`CONTRIBUTING.md` is a **404**. The form is the only door, and it feeds both the
site and the list.

The form, parsed from the live page today:

| Field | Placeholder | Value to use |
|---|---|---|
| Server Name | `e.g., Brave Search` | `Valmera` |
| Short Description | `One sentence about your server` | the **96-character** `server.json` description, verbatim |
| Link (GitHub or docs) | `https://github.com/owner/repo` | `https://github.com/ABO3SKRALMASAOODI/valmera-mcp` |
| Category | select | see below |
| Contact Email | `you@example.com` | yours |

**There is no media, video or content category.** The full list is: Development,
Productivity, Database, Search, Web Scraping, File System, Version Control,
Communication, Cloud Service, Cloud Storage, Marketing, Finance, Design, Memory,
Other. Do not hunt for a better fit that isn't there — **Other** is the honest
pick; *Design* and *Productivity* are the only arguable alternatives, and both
put Valmera next to things it is not.

Premium, quoted verbatim: **"$39 one-time review fee — Skip the wait. Faster
review approval. Official badge on your MCP listing. Dofollow link."** The second
of the two dofollow buys worth making.

Reuse the `server.json` description here and at mcp.so so every card in every
directory reads the same. A visitor who sees three different pitches concludes
there are three different products.

**Verify:** the entry appears in the site's directory, and on the next sync in the
repo README. Browser only.

---

## 10. `punkpeye/awesome-mcp-servers` — use the agent lane

**Who:** machine. This one is genuinely automatable.

**91,826 stars, pushed 2026-08-03** (GitHub API, 2026-08-05). The largest MCP
list on GitHub, and its `CONTRIBUTING.md` carries an explicit agent lane, quoted
verbatim:

> If you are an automated agent, we have a streamlined process for merging agent
> PRs. Just add `🤖🤖🤖` to the end of the PR title to opt-in. Merging your PR
> will be fast-tracked.

The section is `### 🎥 Multimedia Process` (README line ~2717) — **not** "Media /
Video Processing", which does not exist in that README. Entries are
**case-insensitively alphabetical by GitHub owner**; the live neighbours today
are `a-y-ibrahim/after-effects-mcp` and `AceDataCloud/MCPSuno`, so
`ABO3SKRALMASAOODI` slots exactly between them. Format is
`- [owner/repo](url) <legend emoji> - description`, where the legend is 🐍 Python,
📇 TypeScript, ☁️ Cloud Service, 🏠 Local, and 🍎🪟🐧 for OS support.

```bash
gh repo fork punkpeye/awesome-mcp-servers --clone --remote
cd awesome-mcp-servers
git checkout -b add-valmera
# edit README.md — insert into 🎥 Multimedia Process, between a-y-ibrahim and AceDataCloud
git commit -am "Add Valmera video editor"
git push origin add-valmera
gh pr create --title "Add Valmera — agentic AI video editor 🤖🤖🤖" \
  --body "Adds Valmera under Multimedia Process. Hosted remote MCP server (streamable HTTP, OAuth 2.1 + PKCE), 108 tools, free tier."
```

The line — keep it factual, these lists reject marketing copy:

```markdown
- [ABO3SKRALMASAOODI/valmera-mcp](https://github.com/ABO3SKRALMASAOODI/valmera-mcp) 🐍 ☁️ 🍎 🪟 🐧 - Agentic video editing on real footage you upload: cut silences and filler words, word-timed captions, reframe to 9:16, splice b-roll, score and master audio, full-quality export from the original file. 108 tools over an edit decision list. Remote (streamable HTTP, OAuth 2.1 + PKCE), free tier.
```

**Verify:** `gh pr status`, then the entry on `main` after merge.

---

## 11. Glama — <https://glama.ai/mcp/servers>

**Who:** human. **Requires step 1.**

Auto-indexes public GitHub repos containing an MCP manifest; submitting directly
is faster. Glama assigns a quality score — and this is the one that visibly
compounds: **most entries in punkpeye's Multimedia Process section render a
`glama.ai/mcp/servers/<owner>/<repo>/badges/score.svg` image next to the link**
(verified by reading that section today). Your Glama score becomes a badge on the
91k-star list.

The card's `notSupported` list (9 honest limits) and its `notes` help here rather
than hurt: the score rewards accurate, complete metadata, not enthusiasm.

**Verify:** the server page exists at `glama.ai/mcp/servers/<owner>/<repo>` and
the badge image resolves.

---

## 12. The remaining GitHub lists

**Who:** machine (PRs). Star counts and push dates from the GitHub API,
**2026-08-05**.

| Repo | Stars | Last push | Where it goes | Notes |
|---|---|---|---|---|
| `modelcontextprotocol/servers` | 89,208 | 2026-08-04 | README → Community Servers | official-adjacent, highest trust of the three |
| `appcypher/awesome-mcp-servers` | 5,735 | 2026-05-06 | Media | standard PR; list is 3 months stale, expect a slow merge |

Read each repo's `CONTRIBUTING.md` at the moment you open the PR — the punkpeye
agent-marker convention is **not** universal (wong2's is a 404 and its list takes
no PRs at all), and using a marker where it is not recognised just looks like
noise.

---

## 13. Client-specific directories

**Who:** human (forms and issue templates). The first three **require step 1**.

- **cursor.directory** — <https://cursor.directory/mcp> (keys off a public repo)
- **Cline** — MCP Marketplace, issue template on `cline/mcp-marketplace` (keys off a public repo)
- **mcpmarket** — <https://mcpmarket.com/submit> (keys off a public repo)
- **Continue** — <https://hub.continue.dev>
- **Goose** — `block/goose` extensions list
- **LibreChat** — docs MCP examples

The repo requirement on the first three is inherited from the audit and is
**unverified** field-by-field the way mcp.so's and mcpservers.org's now are; all
three sit behind logins or issue templates that curl cannot read.

---

## 14. Anthropic Connectors Directory — highest value, gated

**Who:** human, and only a human on the right plan.
<https://claude.ai/admin-settings/directory/submissions/new>

This is the highest-value listing that exists: it installs Valmera **into Claude
itself**, which is where the users we want already are.

**The gate:** the submission form lives under **admin settings**, and admin
settings do not exist on individual plans. You need a Claude **Team or
Enterprise** organization. There is no way around it — create the org, or this
step waits. (The URL cannot be reached from a terminal, so everything in this
section is **unverified** from this machine and comes from the audit's
browser session.)

The wizard is **11 steps**. It connects to the live server, **syncs the tool
list**, and flags any tool missing a `title` or `annotations`. **That gate is
already cleared** — `0ac21c6` is deployed, and `_editor_tools()`
(`backend/routes/mcp.py:319`) emits a `title` per tool plus `readOnlyHint`,
`destructiveHint` (true only for `reset_edit`), `idempotentHint` (setters and
removers) and `openWorldHint` on every one of the 97.

Then re-read **A1** (the four generative tools) and **A2** (the domain). This is
the reviewer who applies both criteria literally, and a rejection here costs a
resubmission cycle you cannot shorten.

**Verify:** the submission's status in admin settings, then search the in-product
connectors directory for Valmera.

---

## Propagation checks — what to poll, and when

Publishing is not the finish line; the mirrors are. Put these on a schedule
instead of refreshing by hand.

| When | Check |
|---|---|
| Immediately after step 6 | `curl -s "https://registry.modelcontextprotocol.io/v0.1/servers?search=valmera"` → `count: 1` |
| Immediately | `.../v0.1/servers/io.valmera%2Fvideo-editor/versions/latest` → `_meta` shows `status: active`, `isLatest: true` |
| Immediately after step 7 | `npx -y @smithery/cli@latest mcp search valmera --json` → the release is `SUCCESS`, not `AUTH_REQUIRED` or `FAILURE_SCAN` |
| +24h | PulseMCP ingests the official registry **daily** (their claim). Search `valmera` at pulsemcp.com |
| +7d | PulseMCP listing actually published — the weekly half of their stated cadence |
| +7d | `augmentcode.com/mcp` and `claudemarketplaces.com`. **Unverified** that these ingest the official registry. If nothing has appeared by day 7, stop waiting and treat them as manual submissions |
| +48h | Glama server page + score badge resolve |
| Per-PR | `gh pr status` in each awesome-list fork |
| +7d, then monthly | `site:github.com valmera mcp` and `valmera mcp server` in Google — the point of all of this is that the *search result* changes |
| +30d | Ask Claude and ChatGPT "what MCP server edits video?" cold. That answer is the actual scoreboard |

The daily poll, as a one-liner:

```bash
curl -s "https://registry.modelcontextprotocol.io/v0.1/servers?search=valmera" \
  | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['metadata']['count'], [s['server']['name'] for s in d['servers']])"
```

And the daily health check on our own side, which is the thing that quietly
breaks — the run of 502s during the round-87 deploy is exactly what this catches,
and by then several directories will be scanning us on their own schedule:

```bash
HOST=https://mcp.valmera.io      # entrepreneur-bot-backend.onrender.com until step 4
curl -s -o /dev/null -w "health %{http_code}\n" "$HOST/healthz"
curl -s -o /dev/null -w "card   %{http_code}\n" "$HOST/.well-known/mcp/server-card.json"
curl -s -o /dev/null -w "oauth  %{http_code}\n" "$HOST/.well-known/oauth-authorization-server"
curl -s -o /dev/null -w "res    %{http_code}\n" "$HOST/.well-known/oauth-protected-resource"
curl -s -o /dev/null -w "mcp    %{http_code}\n" -X POST -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' "$HOST/mcp"   # 401 is correct here
```

Want `200 200 200 200 401`.

---

## Keeping the entry true

`server.json` carries a `version`. Bump it and republish whenever the tool
surface changes materially. A registry entry describing a server that no longer
behaves that way is worse than no entry — it produces failed first runs, and
failed first runs get written up.

Republishing is the same two commands (`mcp-publisher login dns …`, then
`mcp-publisher publish`); the registry keeps every version and serves the latest.

**Never write a tool count down and trust it.** That is not a style note — it is
the specific mistake two revisions of this file have now caught: `README.md` and
`smithery.yaml` both claimed 110 while the running server had 108, and nobody
noticed because nobody asked the server. `README.md` is fixed; `smithery.yaml`
still isn't. The card computes the number live from the catalog, so the card is
the only source worth quoting:

```bash
curl -s https://mcp.valmera.io/.well-known/mcp/server-card.json \
  | python3 -c "import json,sys;d=json.load(sys.stdin);g=d['toolGroups'];print(d['toolCount'],'=',sum(len(v) for v in g.values()),'+',len(d['sessionTools']))"
```

If A1 is resolved by gating the four generative tools off the MCP surface, that
number becomes **104** — and `README.md`, `smithery.yaml`, the marketing pages and
every directory listing move in the same pass, or the next person to check finds
four different tool counts and believes none of them.
