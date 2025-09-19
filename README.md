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

```

<!DOCTYPE html>
<html>
<head>
  <title>TCP Protocol Explanation</title>
  <style>
    table {
      border-collapse: collapse;
      width: 80%;
      margin: 20px auto;
      font-family: Arial, sans-serif;
    }
    th, td {
      border: 1px solid #333;
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #4CAF50;
      color: white;
    }
    tr:nth-child(even) {
      background-color: #f2f2f2;
    }
    caption {
      font-size: 20px;
      margin: 10px;
      font-weight: bold;
    }
  </style>
</head>
<body>

  <table>
    <caption>TCP Protocol Explanation</caption>
    <tr>
      <th>Feature</th>
      <th>Explanation</th>
    </tr>
    <tr>
      <td>Full Form</td>
      <td>Transmission Control Protocol</td>
    </tr>
    <tr>
      <td>Type</td>
      <td>Connection-oriented protocol</td>
    </tr>
    <tr>
      <td>Connection Setup</td>
      <td>Uses a 3-way handshake to establish a reliable connection before data transfer.</td>
    </tr>
    <tr>
      <td>Reliability</td>
      <td>Ensures reliable data delivery with error checking and retransmission of lost packets.</td>
    </tr>
    <tr>
      <td>Data Transfer</td>
      <td>Breaks data into segments, numbers them, and ensures they arrive in order.</td>
    </tr>
    <tr>
      <td>Flow Control</td>
      <td>Uses sliding window protocol to prevent sender from overwhelming receiver.</td>
    </tr>
    <tr>
      <td>Error Control</td>
      <td>Uses checksums to detect error
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
![alt text](<Screenshot 2025-09-17 114223.png>)

![alt text](<Screenshot 2025-09-17 114347.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.

