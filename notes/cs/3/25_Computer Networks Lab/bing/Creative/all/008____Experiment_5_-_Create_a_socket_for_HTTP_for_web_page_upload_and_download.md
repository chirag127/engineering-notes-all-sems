## Experiment 5 - Create a socket for HTTP for web page upload and download

- A socket is an endpoint of a communication between two processes or machines on a network.
- HTTP (Hypertext Transfer Protocol) is a protocol that defines how messages are formatted and transmitted over the web, and how servers and browsers should respond to various commands.
- To create a socket for HTTP, we need to use the socket module in Python, which provides a low-level interface to the network layer.
- The steps to create a socket for HTTP are:

  - Import the socket module: `import socket`
  - Create a socket object: `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  - The first argument `socket.AF_INET` specifies the address family, which is IPv4 in this case. The second argument `socket.SOCK_STREAM` specifies the socket type, which is TCP in this case.
  - Connect the socket to a server address and port: `s.connect((host, port))`
  - The host can be a domain name or an IP address. The port is usually 80 for HTTP.
  - Send an HTTP request to the server: `s.send(request.encode())`
  - The request should follow the HTTP protocol format, which consists of a request line, headers, and an optional body. For example, a GET request to retrieve a web page could look like this:

    ```
    GET /index.html HTTP/1.1
    Host: www.example.com
    User-Agent: Python-socket
    Connection: close
    ```
  - The request should be encoded as bytes before sending.
  - Receive the HTTP response from the server: `response = s.recv(buffer_size)`
  - The response should also follow the HTTP protocol format, which consists of a status line, headers, and an optional body. For example, a 200 OK response could look like this:

    ```
    HTTP/1.1 200 OK
    Date: Wed, 15 Mar 2023 22:10:34 GMT
    Server: Apache
    Content-Type: text/html
    Content-Length: 1234
    Connection: close

    <html>
    <head>
    <title>Example Page</title>
    </head>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>
    ```
  - The response should be decoded as a string after receiving.
  - Close the socket: `s.close()`
  - This will terminate the connection and free up the resources.

- To upload and download a web page using the socket, we need to modify the request and response accordingly.
- To upload a web page, we need to use a POST request instead of a GET request, and include the content of the web page in the body of the request. For example, a POST request to upload a web page could look like this:

    ```
    POST /upload.html HTTP/1.1
    Host: www.example.com
    User-Agent: Python-socket
    Content-Type: text/html
    Content-Length: 5678
    Connection: close

    <html>
    <head>
    <title>Uploaded Page</title>
    </head>
    <body>
    <h1>This is a page uploaded by socket</h1>
    </body>
    </html>
    ```
  - The server should respond with a status code indicating the success or failure of the upload, and optionally a message or a redirect to the uploaded page.
- To download a web page, we need to use a GET request as before, but save the content of the response body to a file. For example, to download a web page and save it as download.html, we could do something like this:

    ```
    request = "GET /download.html HTTP/1.1\r\nHost: www.example.com\r\nUser-Agent: Python-socket\r\nConnection: close\r\n\r\n"
    s.send(request.encode())
    response = s.recv(4096)
    response = response.decode()
    headers, body = response.split("\r\n\r\n", 1)
    with open("download.html", "w") as f:
        f.write(body)
    s.close()
    ```