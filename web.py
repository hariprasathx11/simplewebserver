from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
    <head>
        <title>device specifications</title>
    </head>
    <body>
        <h1>device specification-(25017723)</h1>
        <table border="4" celspacing="4" celpadding=""4> 
            <tr>
                <td>S.NO</td>
                <td>device</td>
                <td>specifications</td>
            </tr>
            <tr>
                <td>1.</td>
                <td>dell inspiron3601</td>
                <td>intelcore i3</td>
            </tr>
            <tr>
                <td>2.</td>
                <td>desktop-gcl0838</td>
                <td>15.6 fullHDWVA</td>

            </tr>
            <tr>
                <td>2.</td>
                <td>desktop320-18cd</td>
                <td>spill-resistant keyboard</td>
            
            
            
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