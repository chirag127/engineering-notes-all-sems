## Unit 5 - Application Layer in Computer Networks

The application layer is the highest layer in the OSI model and the TCP/IP model. It is where the user interacts with the network through various applications and services. The application layer provides the interface and the protocols for communication between different hosts and networks. The application layer is not an application itself, but a set of rules and methods that applications follow to exchange data.

Some of the functions and benefits of the application layer are:

- It enables the user to access, retrieve and manage files on a remote computer.
- It allows the user to send and receive emails, messages and other types of data.
- It supports various types of services, such as web browsing, online gaming, video conferencing, streaming media, etc.
- It provides security, encryption, authentication and error handling for the data transmission.
- It adapts the data to the format and requirements of the underlying network layers.

Some of the examples of application layer protocols are:

- HTTP: Hypertext Transfer Protocol is used for web browsing and transferring web pages and other resources between a web server and a web client.
- SMTP: Simple Mail Transfer Protocol is used for sending and receiving emails between mail servers and mail clients.
- FTP: File Transfer Protocol is used for transferring files between a file server and a file client.
- DNS: Domain Name System is used for resolving domain names to IP addresses and vice versa.
- DHCP: Dynamic Host Configuration Protocol is used for assigning IP addresses and other network parameters to hosts dynamically.
- SSH: Secure Shell is used for establishing a secure and encrypted connection between a remote host and a local host.
- Telnet: Telnet is used for accessing and controlling a remote host using a command-line interface.

The following is a sample code for creating a simple HTTP client that sends a GET request to a web server and prints the response:

```python
# Import the socket module
import socket

# Create a socket object
s = socket.socket()

# Define the host and port
host = "www.example.com"
port = 80

# Connect to the server
s.connect((host, port))

# Send the GET request
request = "GET / HTTP/1.1\r\nHost: " + host + "\r\n\r\n"
s.send(request.encode())

# Receive the response
response = s.recv(1024)

# Print the response
print(response.decode())

# Close the socket
s.close()
```