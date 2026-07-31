## Experiment 5 - Create a socket for HTTP for web page upload and download

- A socket is an endpoint of a communication channel between two processes or devices over a network.
- HTTP (Hypertext Transfer Protocol) is a protocol that defines how messages are formatted and transmitted over the web, and how servers and browsers should respond to various commands.
- To create a socket for HTTP, we need to use the socket module in Python, which provides a low-level interface to the network layer.
- The steps to create a socket for HTTP are:

  1. Import the socket module: `import socket`
  2. Create a socket object: `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  3. Specify the host and port of the server: `host = 'www.example.com'` and `port = 80`
  4. Connect the socket to the server: `s.connect((host, port))`
  5. Send an HTTP request to the server: `s.send(b'GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n')`
  6. Receive the HTTP response from the server: `data = s.recv(1024)`
  7. Print the data: `print(data.decode())`
  8. Close the socket: `s.close()`

- To upload and download a web page using the socket, we need to use the following methods:

  - To upload a web page, we need to send an HTTP POST request to the server with the content of the web page in the body of the request. For example: `s.send(b'POST /upload.html HTTP/1.1\r\nHost: www.example.com\r\nContent-Type: text/html\r\nContent-Length: 20\r\n\r\n<html>Hello</html>')`
  - To download a web page, we need to send an HTTP GET request to the server with the name of the web page in the request line. For example: `s.send(b'GET /download.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n')`
  - To receive the web page, we need to read the data from the socket until the end of the response. For example: `data = b''` and `while True: chunk = s.recv(1024) if not chunk: break data += chunk`
  - To save the web page, we need to write the data to a file. For example: `with open('download.html', 'wb') as f: f.write(data)`