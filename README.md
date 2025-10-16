# EX01 Developing a Simple Webserver
## Date:05/09/2025

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```

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

```

## OUTPUT:
![alt text](<Screenshot (21).png>)
![alt text](<Screenshot (22).png>)



## RESULT:
The program for implementing simple webserver is executed successfully.

