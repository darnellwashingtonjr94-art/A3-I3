from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Construct response headers
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Payload
        response = {
            "status": "success",
            "message": "Vercel Serverless Python API is fully operational.",
            "compute_model": "Fluid",
            "data": {"version": "1.0.0"}
        }
        
        # Write response
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
