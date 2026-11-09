"""Dev server: serves this folder and proxies /api to the Flask backend.

Run from the repo root:  python frontend/dev_server.py
Open http://localhost:5173  (backend must be running on 127.0.0.1:5000).
The proxy rewrites Host and Origin because the backend rejects any
Origin that differs from its own address (see docs/api.md, 403).
"""
import http.client
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

BACKEND = ("127.0.0.1", 5000)
PORT = 5173
HERE = os.path.dirname(os.path.abspath(__file__))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=HERE, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def proxy(self):
        length = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(length) if length else None
        headers = {k: v for k, v in self.headers.items() if k.lower() not in ("host", "origin", "connection")}
        headers["Host"] = "%s:%d" % BACKEND
        if self.headers.get("Origin"):
            headers["Origin"] = "http://%s:%d" % BACKEND
        try:
            conn = http.client.HTTPConnection(*BACKEND, timeout=10)
            conn.request(self.command, self.path, body=body, headers=headers)
            resp = conn.getresponse()
            data = resp.read()
        except OSError:
            data = b'{"error":{"code":"backend_down","message":"Backend is not running on port 5000.","fields":{}}}'
            self.send_response(503)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return
        self.send_response(resp.status)
        for k, v in resp.getheaders():
            if k.lower() not in ("transfer-encoding", "connection", "server", "date"):
                self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def route(self):
        if self.path.startswith("/api/"):
            self.proxy()
            return True
        return False

    def do_GET(self):
        self.route() or super().do_GET()

    def do_HEAD(self):
        self.route() or super().do_HEAD()

    do_POST = do_PUT = do_PATCH = do_DELETE = lambda self: self.route()


if __name__ == "__main__":
    print("TaskTrack frontend on http://localhost:%d (proxy -> %s:%d)" % ((PORT,) + BACKEND))
    ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
