from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/xml")
        self.end_headers()

        xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://psg-bunk.vercel.app/</loc>
    <priority>1.0</priority>
  </url>
</urlset>
"""
        self.wfile.write(xml.encode("utf-8"))
