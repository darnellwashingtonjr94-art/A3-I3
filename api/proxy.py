import os
import urllib.request
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.proxy_request('GET')

    def do_POST(self):
        self.proxy_request('POST')

    def proxy_request(self, method):
        # 1. Define your external node destination
        # Ensure you also store the URL in your Vercel Environment Variables
        destination_url = os.environ.get('A3_EXTERNAL_URL')
        if not destination_url:
            self.send_error(500, "External URL not configured.")
            return

        # 2. Extract the path requested by the client
        # Example: /api/proxy/execute_task -> /execute_task
        path = self.path.replace('/api/proxy', '')
        target_url = f"{destination_url}{path}"

        # 3. Securely construct the request
        req = urllib.request.Request(target_url, method=method)
        
        # 4. Attach the Authorization Secret from Vercel's Environment
        secret = os.environ.get('A3_NODE_SECRET')
        if secret:
            req.add_header('Authorization', f'Bearer {secret}')

        # 5. Forward the original request body if it's a POST
        if method == 'POST':
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                post_data = self.rfile.read(content_length)
                req.data = post_data
                req.add_header('Content-Type', self.headers.get('Content-Type', 'application/json'))

        try:
            # 6. Execute the request to your external node
            with urllib.request.urlopen(req) as response:
                response_body = response.read()
                
                # 7. Relay the response back to the client
                self.send_response(response.status)
                self.send_header('Content-type', response.headers.get('Content-Type', 'application/json'))
                self.end_headers()
                self.wfile.write(response_body)
                
        except urllib.error.HTTPError as e:
            self.send_error(e.code, e.reason)
        except Exception as e:
            self.send_error(500, f"Proxy failed: {str(e)}")
