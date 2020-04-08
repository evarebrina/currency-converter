import http.server
import socketserver
import json
from routers import convert
from logger import get_logger
from os import environ

logger = get_logger()

PORT = environ.get("PORT", 8080)


class APIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/convert":
            try:
                length = int(self.headers.get('content-length'))
                content_type = self.headers.get("Content-type")
                byte_content = self.rfile.read(length)
                str_content = byte_content.decode("utf-8")
                content = json.loads(str_content)
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                resp = convert(content)
                self.wfile.write(json.dumps(resp).encode("utf-8"))
            except (ValueError, TypeError) as e:
                logger.warn(str(e))
                self.send_response(422, message="Invalid value")
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'wrong value'}).encode("utf-8"))
                return
            except ConnectionError as e:
                logger.warn(str(e))
                self.send_response(500, message="Internal server error")
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'internal server error'}).encode("utf-8"))
                return
            return
        else:
            logger.warn(f"Invalid path: {self.path}")
            self.send_response(404, message="Not Found")
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'not found'}).encode("utf-8"))
            return


with socketserver.TCPServer(("0.0.0.0", PORT), APIHandler) as httpd:
    logger.info(f"Serving port {PORT}")
    httpd.serve_forever()
