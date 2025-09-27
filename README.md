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
rom http.server import HTTPServer, BaseHTTPRequestHandler
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

~~~

## OUTPUT:
<img width="1920" height="1080" alt="Screenshot (7)" src="https://github.com/user-attachments/assets/c177c6e4-2b7c-48f8-a6d3-3c1b6c1f7bc2" />

## RESULT:
The program for implementing simple webserver is executed successfully.

