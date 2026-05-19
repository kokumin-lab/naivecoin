import http.server
import ssl
import os

PORT = 8443  # 80/443 は管理者権限が必要なので 8443 推奨
#DOCUMENT_ROOT = r"\\wsl.localhost\Ubuntu\home\user\dev"  # Windows で動かす場合
DOCUMENT_ROOT = r"/home/user/dev"  # WSL(Ubuntu) 内で動かす場合

os.chdir(DOCUMENT_ROOT)

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]

httpd = http.server.HTTPServer(("", PORT), handler)

# ★ Python 3.12 以降は SSLContext を使う
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="ssl/server.crt", keyfile="ssl/server.key")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving HTTPS on port {PORT}")
httpd.serve_forever()
