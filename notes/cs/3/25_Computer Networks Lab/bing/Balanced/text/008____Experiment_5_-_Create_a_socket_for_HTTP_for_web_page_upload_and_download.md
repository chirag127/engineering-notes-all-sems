## Experiment 5 - Create a socket for HTTP for web page upload and download

- A socket is an endpoint of a communication channel between two processes or devices over a network.
- HTTP (Hypertext Transfer Protocol) is an application layer protocol that defines how web pages are requested and transferred over the internet.
- To create a socket for HTTP, we need to use the socket module in Python, which provides a low-level interface to access network services.
- The steps to create a socket for HTTP are:

  1. Import the socket module: `import socket`
  2. Create a socket object: `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  3. Specify the host and port of the web server: `host = "www.example.com"` and `port = 80`
  4. Connect the socket to the server: `s.connect((host, port))`
  5. Send an HTTP request to the server: `s.send(b"GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n")`
  6. Receive the HTTP response from the server: `data = s.recv(1024)`
  7. Print the response data: `print(data.decode())`
  8. Close the socket: `s.close()`

- To upload and download web pages using the socket, we need to use the following methods:

  - To upload a web page, we need to send an HTTP POST request to the server with the content of the web page in the request body. For example: `s.send(b"POST /upload.html HTTP/1.1\r\nHost: www.example.com\r\nContent-Type: text/html\r\nContent-Length: 20\r\n\r\n<html>Hello</html>")`
  - To download a web page, we need to send an HTTP GET request to the server with the name of the web page in the request line. For example: `s.send(b"GET /download.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n")`
  - To receive the uploaded or downloaded web page, we need to read the response data from the socket and parse the HTTP headers and the body. For example: `data = s.recv(1024)` and `headers, body = data.split(b"\r\n\r\n", 1)`