# Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

## Introduction

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A socket is an endpoint of a communication channel that can send and receive data using a protocol.
- There are two main types of sockets: stream sockets and datagram sockets.
- Stream sockets use TCP (Transmission Control Protocol) as the transport layer protocol, which provides reliable, ordered and error-free data delivery .
- Datagram sockets use UDP (User Datagram Protocol) as the transport layer protocol, which provides fast, connectionless and unreliable data delivery .
- TCP sockets are suited for applications that require high reliability and transmission time is less critical, such as web browsing, file transfer, email, etc.
- UDP sockets are suited for applications that require low latency and transmission time is more critical, such as video streaming, online gaming, voice over IP, etc.

## Objectives

- To learn how to create and use TCP and UDP sockets in Python.
- To implement simple client-server applications using TCP and UDP sockets, such as:
  - Simple DNS: A client sends a domain name to a server and the server replies with the corresponding IP address.
  - Data & time client/server: A client requests the current date and time from a server and the server replies with the requested information.
  - Echo client/server: A client sends a message to a server and the server echoes back the same message to the client.
  - Iterative & concurrent servers: A server can handle multiple client requests either sequentially (iterative) or simultaneously (concurrent) using different techniques, such as threading, multiprocessing, select, etc.

## Procedure

- To create a TCP socket in Python, use the following code:

```python
import socket
# Create a TCP socket object
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- To create a UDP socket in Python, use the following code:

```python
import socket
# Create a UDP socket object
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

- To bind a socket to a port and listen for incoming connections, use the following code:

```python
# Bind the socket to a port
tcp_socket.bind((host, port))
# Listen for incoming connections
tcp_socket.listen()
```

- To accept a connection from a client and create a new socket for communication, use the following code:

```python
# Accept a connection from a client
client_socket, client_address = tcp_socket.accept()
```

- To connect to a server using a socket, use the following code:

```python
# Connect to a server
tcp_socket.connect((host, port))
```

- To send and receive data using a TCP socket, use the following code:

```python
# Send data to the server
tcp_socket.send(data.encode())
# Receive data from the server
data = tcp_socket.recv(buffer_size).decode()
```

- To send and receive data using a UDP socket, use the following code:

```python
# Send data to the server
udp_socket.sendto(data.encode(), (host, port))
# Receive data from the server
data, server_address = udp_socket.recvfrom(buffer_size).decode()
```

- To close a socket, use the following code:

```python
# Close the socket
tcp_socket.close()
```

- To implement the simple client-server applications using TCP and UDP sockets, follow the steps below:

  - Simple DNS:
    - Create a TCP or UDP socket for the client and the server.
    - The client sends a domain name to the server using the socket.
    - The server receives the domain name and performs a DNS lookup using the socket module's gethostbyname function.
    - The server sends the IP address of the domain name back to the client using the socket.
    - The client receives the IP address and prints it.
    - The client and the server close the socket.

  - Data & time client/server:
    - Create a TCP or UDP socket for the client and the server.
    - The client sends a request to the server using the socket.
    - The server