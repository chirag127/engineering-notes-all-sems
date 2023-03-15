## Experiment 5 - Create a socket for HTTP for web page upload and download

- A socket is an endpoint of a communication channel between two processes or devices over a network.
- HTTP (Hypertext Transfer Protocol) is a protocol that defines how messages are formatted and transmitted over the web, and how servers and clients should respond to various commands.
- To create a socket for HTTP, we need to use the socket module in Python, which provides a low-level interface to access network services.
- The steps to create a socket for HTTP are:

  - Import the socket module: `import socket`
  - Create a socket object: `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  - Specify the address and port of the server: `host = 'www.example.com'` and `port = 80`
  - Connect the socket to the server: `s.connect((host, port))`
  - Send an HTTP request to the server: `s.send(b'GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n')`
  - Receive the HTTP response from the server: `data = s.recv(1024)`
  - Print the response data: `print(data.decode())`
  - Close the socket: `s.close()`

- To upload and download web pages using the socket, we need to modify the HTTP request and response accordingly.
- For example, to upload a web page, we need to use the POST method instead of the GET method, and include the content of the web page in the request body.
- To download a web page, we need to parse the response data and extract the content of the web page from the response body.