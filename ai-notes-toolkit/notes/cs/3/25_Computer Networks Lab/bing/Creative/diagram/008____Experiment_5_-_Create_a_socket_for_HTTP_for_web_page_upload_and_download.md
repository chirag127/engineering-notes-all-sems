## Experiment 5 - Create a socket for HTTP for web page upload and download

- A socket is an endpoint of a communication channel between two processes or devices over a network.
- HTTP (Hypertext Transfer Protocol) is an application layer protocol that defines how web pages are requested and transferred over the internet.
- To create a socket for HTTP, we need to use the socket module in Python, which provides a low-level interface to access network services.
- The socket module has two main functions: socket() and connect().
- The socket() function creates a new socket object and returns it. It takes three arguments: the address family, the socket type, and the protocol number. For HTTP, we use AF_INET as the address family, which specifies IPv4 addresses, SOCK_STREAM as the socket type, which specifies TCP connections, and 0 as the protocol number, which lets the system choose the appropriate protocol.
- The connect() function connects the socket to a remote address. It takes one argument: a tuple of the host name and the port number. For HTTP, we use port 80, which is the default port for web servers.
- To upload a web page, we need to send an HTTP request to the server, which contains the method, the URL, the headers, and the body of the request. The method specifies the action to be performed, such as GET, POST, PUT, or DELETE. The URL specifies the resource to be accessed, such as a file name or a query string. The headers provide additional information about the request, such as the content type, the content length, or the user agent. The body contains the data to be sent, such as a form or a file.
- To download a web page, we need to receive an HTTP response from the server, which contains the status code, the headers, and the body of the response. The status code indicates the result of the request, such as 200 for OK, 404 for Not Found, or 500 for Internal Server Error. The headers provide additional information about the response, such as the content type, the content length, or the server name. The body contains the data to be received, such as an HTML document or an image.
- To send and receive data, we use the send() and recv() methods of the socket object. The send() method takes a byte string as an argument and returns the number of bytes sent. The recv() method takes an integer as an argument, which specifies the maximum number of bytes to receive, and returns a byte string.
- To close the socket, we use the close() method of the socket object, which terminates the connection and releases the resources.

Here is an example of a Python program that creates a socket for HTTP and uploads and downloads a web page:

```python
# Import the socket module
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = "www.example.com" # The host name of the web server
port = 80 # The port number of the web server
s.connect((host, port))

# Send an HTTP request to upload a web page
request = b"PUT /test.html HTTP/1.1\r\n" # The request line
request += b"Host: www.example.com\r\n" # The host header
request += b"Content-Type: text/html\r\n" # The content type header
request += b"Content-Length: 13\r\n" # The content length header
request += b"\r\n" # The end of the headers
request += b"<h1>Test</h1>" # The body of the request
s.send(request) # Send the request

# Receive an HTTP response from the server
response = s.recv(1024) # Receive up to 1024 bytes
print(response.decode()) # Print the response

# Send another HTTP request to download a web page
request = b"GET /test.html HTTP/1.1\r\n" # The request line
request += b"Host: www.example.com\r\n" # The host header
request += b"\r\n" # The end of the headers
s.send(request) # Send the request

# Receive another HTTP response from the server
response = s.recv(1024) # Receive up to 1024 bytes
print(response.decode()) # Print the response

# Close the socket
s.close()
```