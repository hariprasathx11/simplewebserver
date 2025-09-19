from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>device specifications (25017723)</head>
        <title>device specifications-25017723</title>
    </head>
    <body border="3">
        <table border="3" color="blue" cellspacing="5" cellpadding="4">
            <tr>
                <th>s.no.</td>
                <th>device.</td>
                <th>device specifications.</td>
            </tr>

            <tr>
                <td>1.</td>
                <td>desktop-0uc7gcl.</td>
                <td>intel(R) core uhd graphics.</td>
            <tr>
                <td>2.</td>
                <td>inspiron 3501</td>
                <td>11th gen intel core is processor</td>
            <tr>
                <td>3.</td>
                <td>15.6"full hd wVa display</td>
                <td>hd webcam</td>
            </tr>
            </tr>
            </td>
            </td>
        </table>
    </body>
    </html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()