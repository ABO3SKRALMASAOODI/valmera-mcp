"""Serve the bilingual pilot sample on this computer."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class SampleHandler(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map, ".vtt": "text/vtt", ".mp4": "video/mp4"}


if __name__ == "__main__":
    handler = partial(SampleHandler, directory=str(Path(__file__).resolve().parent))
    with ThreadingHTTPServer(("127.0.0.1", 8000), handler) as server:
        print("Open http://127.0.0.1:8000/ to play the sample.", flush=True)
        server.serve_forever()
