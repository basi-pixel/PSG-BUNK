from http.server import BaseHTTPRequestHandler
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = os.path.join(os.path.dirname(__file__), "../static/favicon.ico")

        if not os.path.exists(path):
            self.send_response(404)
            self.end_headers()
            return

        self.send_response(200)
        self.send_header("Content-Type", "image/x-icon")
        self.end_headers()

        with open(path, "rb") as f:
            self.wfile.write(f.read())
