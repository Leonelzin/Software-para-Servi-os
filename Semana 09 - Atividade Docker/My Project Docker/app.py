import http.server
import socketserver
from flask import Flask

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!\n"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
