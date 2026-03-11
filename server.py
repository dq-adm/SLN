import http.server
import socketserver

PORT = 8080

class SecurityHeadersHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Implement the requested security headers
        self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://code.jquery.com; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; connect-src 'self'")
        self.send_header('Permissions-Policy', "geolocation=(), microphone=(), camera=()")
        self.send_header('Referrer-Policy', 'strict-origin-when-cross-origin')
        self.send_header('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('X-Frame-Options', 'SAMEORIGIN')
        super().end_headers()

Handler = SecurityHeadersHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT, "with Security Headers enabled.")
    httpd.serve_forever()
