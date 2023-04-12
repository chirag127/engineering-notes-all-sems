# Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

## Introduction

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol.
- There are three types of sockets: stream sockets, datagram sockets and raw sockets.
- Stream sockets use TCP (Transmission Control Protocol) as the transport layer protocol, which provides reliable, ordered and error-free data delivery .
- Datagram sockets use UDP (User Datagram Protocol) as the transport layer protocol, which provides fast, connectionless and unreliable data delivery .
- Raw sockets can use any protocol at the network layer or lower, and allow direct access to the network interface.
- In this experiment, we will learn how to program sockets using UDP and TCP in Python, and implement some simple applications such as DNS, data & time client/server, echo client/server, and iterative & concurrent servers.

## UDP Socket Programming

- UDP sockets are created using the socket.SOCK_DGRAM parameter in the socket.socket() function.
- UDP sockets do not need to establish a connection before sending or receiving data, so they do not use the listen(), accept() or connect() methods that TCP sockets use.
- UDP sockets can send and receive data using the sendto() and recvfrom() methods, which take the data and the destination address as arguments.
- UDP sockets can also use the bind() method to associate a socket with a specific address and port, and the close() method to close the socket.
- UDP sockets are suitable for applications that require low latency, high throughput and multicast or broadcast capabilities, but do not care much about reliability, ordering or error correction.
- An example of UDP socket programming in Python is given below:

```python
# UDP client
import socket
# create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send a message to the server
message = b"Hello, server!"
server_address = ("127.0.0.1", 5000) # server IP and port
client_socket.sendto(message, server_address)
# receive a response from the server
response, address = client_socket.recvfrom(1024) # buffer size
print("Received from server:", response.decode())
# close the socket
client_socket.close()
```

```python
# UDP server
import socket
# create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind the socket to a specific address and port
server_address = ("127.0.0.1", 5000) # server IP and port
server_socket.bind(server_address)
# receive a message from a client
message, address = server_socket.recvfrom(1024) # buffer size
print("Received from client:", message.decode())
# send a response to the client
response = b"Hello, client!"
server_socket.sendto(response, address)
# close the socket
server_socket.close()
```

## TCP Socket Programming

- TCP sockets are created using the socket.SOCK_STREAM parameter in the socket.socket() function.
- TCP sockets need to establish a connection before sending or receiving data, so they use the listen(), accept() and connect() methods that UDP sockets do not use .
- TCP sockets can send and receive data using the send() and recv() methods, which take the data and the buffer size as arguments.
- TCP sockets can also use the bind() method to associate a socket with a specific address and port, the close() method to close the socket, and the gethostname() method to get the host name of the machine.
- TCP sockets are suitable for applications that require high reliability, ordering and error correction, but do not care much about latency, throughput or multicast or broadcast capabilities.
- An example of TCP socket programming in Python is given below:

```python
# TCP client
import socket
# create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server
server_address = ("127.0.0.1", 5000) # server IP and port
client_socket.connect(server_address)
# send a message to the server
message = b

```
