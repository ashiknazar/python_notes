import http.server
import socketserver

PORT = 8000

# Create a handler that will respond to HTTP requests
class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Send a response header
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        # Send the response body (HTML content)
        self.wfile.write(b"Hello, World!")  # You can send a byte string

# Set up the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()
