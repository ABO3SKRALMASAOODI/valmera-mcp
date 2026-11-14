"""Compare Valmera's public registry, endpoint, OAuth metadata and directory record."""

import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ENDPOINT = "https://valmera.io/mcp/server"
RESOURCE = "https://valmera.io/.well-known/oauth-protected-resource"
AUTH = "https://valmera.io/.well-known/oauth-authorization-server"
CARD = "https://valmera.io/.well-known/mcp/server-card.json"
REGISTRY = "https://registry.modelcontextprotocol.io/v0.1/servers/io.valmera%2Fvideo-editor/versions/latest"
DIRECTORY = "https://trustedmcp.io/api/v1/lookup?q=https%3A%2F%2Fvalmera.io%2Fmcp%2Fserver"


def fetch(url):
    request = Request(url, headers={"Accept": "application/json", "User-Agent": "Valmera-public-identity-check/1"})
    with urlopen(request, timeout=15) as response:
        return json.load(response)


def check():
    entry = fetch(REGISTRY)
    server = entry["server"]
    card = fetch(CARD)
    resource = fetch(RESOURCE)
    auth = fetch(AUTH)
    directory = fetch(DIRECTORY)["data"]
    expected_remote = {"type": "streamable-http", "url": ENDPOINT}
    checks = {
        "registry name": server["name"] == "io.valmera/video-editor",
        "registry status": entry["_meta"]["io.modelcontextprotocol.registry/official"]["status"] == "active",
        "registry repository": server["repository"]["url"] == "https://github.com/ABO3SKRALMASAOODI/valmera-mcp",
        "registry and card endpoint": all(expected_remote in doc["remotes"] for doc in (server, card)),
        "OAuth resource": resource["resource"] == ENDPOINT,
        "OAuth issuer": auth["issuer"] == "https://valmera.io" and auth["issuer"] in resource["authorization_servers"],
        "edit scope advertised": all("valmera.edit" in doc["scopes_supported"] for doc in (resource, auth)),
        "PKCE S256 advertised": "S256" in auth["code_challenge_methods_supported"],
    }
    try:
        with urlopen(Request(ENDPOINT, headers={"Accept": "application/json"}), timeout=15) as response:
            checks["anonymous OAuth challenge"] = False
    except HTTPError as err:
        checks["anonymous OAuth challenge"] = err.code == 401 and f'resource_metadata="{RESOURCE}"' in err.headers.get("WWW-Authenticate", "")
    listings = [item for item in directory["graded"] if item["slug"] == "valmera-mcp"]
    checks["directory matches endpoint"] = "remote:valmera.io/mcp/server" in directory["identifiers"] and bool(listings)
    return {
        "registry_version": server["version"],
        "scopes_advertised": auth["scopes_supported"],
        "trustedmcp_grade": listings[0]["grade"] if listings else None,
        "checks": checks,
    }


if __name__ == "__main__":
    try:
        result = check()
    except (OSError, URLError, ValueError, KeyError, TypeError) as exc:
        sys.exit(f"Could not read a public record: {exc}")
    print(json.dumps(result, indent=2))
    sys.exit(0 if all(result["checks"].values()) else 1)
