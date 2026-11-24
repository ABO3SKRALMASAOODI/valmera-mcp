#!/usr/bin/env python3
"""Compare one public MP4 download with an approved local export."""

import argparse
import hashlib
import http.client
import json
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


def mp4_fingerprint(stream):
    header = stream.read(12)
    if len(header) < 12 or header[4:8] != b"ftyp":
        raise ValueError("Expected an MP4 file with an initial ftyp box.")
    digest = hashlib.sha256(header)
    size = len(header)
    while chunk := stream.read(1024 * 1024):
        digest.update(chunk)
        size += len(chunk)
    return {"sha256": digest.hexdigest(), "bytes": size}


def read_public_export(url, revalidate, timeout):
    parsed = urlsplit(url)
    if parsed.scheme not in ("http", "https") or not parsed.hostname or parsed.username is not None:
        raise ValueError("Use an HTTP or HTTPS MP4 URL without embedded credentials.")
    headers = {"Accept-Encoding": "identity"}
    if revalidate:
        headers["Cache-Control"] = "no-cache"
    with urlopen(Request(url, headers=headers), timeout=timeout) as response:
        if response.status != 200:
            raise ValueError(f"Expected a complete HTTP 200 response, got {response.status}.")
        if response.headers.get("Content-Encoding", "identity").lower() != "identity":
            raise ValueError("The server returned encoded bytes instead of the requested MP4.")
        actual = mp4_fingerprint(response)
        content_length = response.headers.get("Content-Length")
        if content_length is not None and int(content_length) != actual["bytes"]:
            raise ValueError("The response was shorter or longer than its Content-Length.")
        response_headers = {
            name: response.headers[name]
            for name in ("Age", "Cache-Control", "Content-Type", "ETag", "Last-Modified")
            if name in response.headers
        }
        return actual, urlsplit(response.url).hostname, response_headers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="Public URL that serves the downloadable MP4.")
    parser.add_argument("--approved", type=Path, required=True, help="Approved MP4 on disk.")
    parser.add_argument("--revalidate", action="store_true", help="Send Cache-Control: no-cache.")
    parser.add_argument("--timeout", type=float, default=30, help="Timeout for network operations in seconds.")
    args = parser.parse_args()
    if not 0 < args.timeout < float("inf"):
        parser.error("--timeout must be a positive finite number")

    try:
        with args.approved.open("rb") as source:
            expected = mp4_fingerprint(source)
        actual, hostname, headers = read_public_export(args.url, args.revalidate, args.timeout)
    except HTTPError as error:
        print(json.dumps({"result": "unavailable", "http_status": error.code}))
        return 2
    except ValueError as error:
        print(json.dumps({"result": "unavailable", "reason": str(error)}))
        return 2
    except (OSError, http.client.HTTPException) as error:
        print(json.dumps({"result": "unavailable", "error_type": type(error).__name__}))
        return 2

    matches = expected == actual
    print(json.dumps({
        "result": "match" if matches else "different",
        "delivery_host": hostname,
        "requested_revalidation": args.revalidate,
        "approved": expected,
        "served": actual,
        "headers": headers,
    }, indent=2))
    return 0 if matches else 1


if __name__ == "__main__":
    raise SystemExit(main())
