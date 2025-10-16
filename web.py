from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>localhost:8000</title>
</head
<body>
<table border="2" cellspacing="10" cellpadding="10">
<caption>Device Specificationn -S. HARIPRASATH 25017723</caption>
<tr>
<th>1</th>
<th>Device name</th>
<th>TMP215-75-G2</th.
</tr>
<tr>
<th>2</th>
<th>Processor</th>
<th>Intel(R) Core(TM) Ultra 5125H (1.20 GHz)</th>
</tr>
<tr>
<th>3</th>
<th>Installed RAM</th>
<th>16.0 GB (15.5 GB usable)</th>
</tr>
<tr>
<th>4</th>
<th>Graphic Card</th>
<th>128 MB</th>
</tr>
<tr>
<th>5</th>
<th>Storage</th>
<th>954 GB</th>
</tr>
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