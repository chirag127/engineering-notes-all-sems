## Experiment 5 - Create a socket for HTTP for web page upload and download

The objective of this experiment is to learn how to use sockets to communicate with a web server using the HTTP protocol. Sockets are low-level interfaces that allow applications to send and receive data over a network. HTTP is a high-level protocol that defines the format and semantics of messages exchanged between a client and a server for web applications.

The steps of this experiment are:

1. Create a TCP socket using the `socket` module in Python. A TCP socket is a reliable and bidirectional connection between two endpoints identified by an IP address and a port number.
2. Connect the socket to a web server using the `connect` method. The web server's IP address and port number can be obtained by using the `gethostbyname` and `getservbyname` functions, respectively. Alternatively, you can use the `create_connection` method to combine these steps.
3. Send an HTTP request to the web server using the `send` method. An HTTP request consists of a request line, headers, and an optional body. The request line specifies the method, the path, and the version of the protocol. The headers provide additional information about the request, such as the host, the user-agent, the content-type, etc. The body contains the data to be sent to the server, such as a file or a form. The request must end with a blank line.
4. Receive the HTTP response from the web server using the `recv` method. An HTTP response consists of a status line, headers, and an optional body. The status line indicates the status code, the reason phrase, and the version of the protocol. The headers provide additional information about the response, such as the content-length, the content-type, the date, etc. The body contains the data sent by the server, such as a web page or a file. The response must end with a blank line.
5. Close the socket using the `close` method. This terminates the connection and releases the resources.

The following is an example of a Python program that creates a socket for HTTP for web page upload and download:

```python
# Import the socket module
import socket

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a web server
host = socket.gethostbyname("www.example.com") # Get the IP address of the server
port = socket.getservbyname("http", "tcp") # Get the port number of the service
s.connect((host, port)) # Connect to the server

# Send an HTTP request
request = "GET /index.html HTTP/1.1\r\n" # Request line
request += "Host: www.example.com\r\n" # Header
request += "User-Agent: Python\r\n" # Header
request += "\r\n" # End of request
s.send(request.encode()) # Encode and send the request

# Receive an HTTP response
response = s.recv(4096) # Receive up to 4096 bytes of data
print(response.decode()) # Decode and print the response

# Close the socket
s.close()
```