# Experiment 9 - Applications using TCP and UDP Sockets

## Objective
- To understand the difference between TCP and UDP sockets and how to use them in various applications.
- To implement some simple applications using TCP and UDP sockets in Python.

## Theory
- TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two of the most common transport layer protocols in the Internet Protocol suite.
- TCP provides reliable, ordered, and error-checked delivery of data between two endpoints. TCP establishes a connection-oriented communication, which means that it requires a three-way handshake to establish a connection before any data can be exchanged. TCP also implements flow control, congestion control, and retransmission mechanisms to ensure data integrity and avoid network congestion.
- UDP provides unreliable, unordered, and error-prone delivery of data between two endpoints. UDP establishes a connectionless communication, which means that it does not require any handshake or connection establishment before sending or receiving data. UDP also does not implement any flow control, congestion control, or retransmission mechanisms, which makes it faster and more efficient for some applications that can tolerate data loss or reordering.
- Some applications that use TCP sockets are web browsers, email clients, file transfer protocols, remote login, etc. Some applications that use UDP sockets are video streaming, online gaming, voice over IP, etc.

## Procedure
- To create a TCP socket in Python, we need to import the socket module and use the socket.socket() function with the arguments socket.AF_INET (for IPv4 address family) and socket.SOCK_STREAM (for TCP socket type). For example:

```python
import socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- To create a UDP socket in Python, we need to import the socket module and use the socket.socket() function with the arguments socket.AF_INET (for IPv4 address family) and socket.SOCK_DGRAM (for UDP socket type). For example:

```python
import socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

- To bind a socket to a specific port and IP address, we need to use the socket.bind() method with a tuple of (IP, port) as the argument. For example:

```python
tcp_socket.bind(("127.0.0.1", 8000)) # bind tcp socket to localhost and port 8000
udp_socket.bind(("0.0.0.0", 9000)) # bind udp socket to any IP and port 9000
```

- To listen for incoming connections on a TCP socket, we need to use the socket.listen() method with an argument that specifies the maximum number of queued connections. For example:

```python
tcp_socket.listen(5) # listen for up to 5 connections
```

- To accept a connection on a TCP socket, we need to use the socket.accept() method, which returns a new socket object and the address of the client. For example:

```python
client_socket, client_address = tcp_socket.accept() # accept a connection and get the client socket and address
```

- To send data on a TCP socket, we need to use the socket.send() method with a bytes object as the argument. For example:

```python
client_socket.send(b"Hello, client!") # send a bytes object to the client
```

- To receive data on a TCP socket, we need to use the socket.recv() method with an argument that specifies the maximum number of bytes to receive. The method returns a bytes object that contains the received data. For example:

```python
data = client_socket.recv(1024) # receive up to 1024 bytes from the client
```

- To close a TCP socket, we need to use the socket.close() method. For example:

```python
client_socket.close() # close the client socket
tcp_socket.close() # close the server socket
```

- To send data on a UDP socket, we need to use the socket.sendto() method with a bytes object and a tuple of (IP, port) as the arguments. The method sends the data to the specified destination. For example:

```python
udp_socket.sendto(b"Hello, world!", ("127.0.0.1", 9000)) # send a bytes object to localhost and port 9000
```

- To receive data on a UDP socket, we need to use the socket.recvfrom() method with an argument that specifies the maximum number of bytes to receive. The method returns a tuple of (data, address), where data is a bytes object that contains the received data, and address is a tuple of (IP, port) that contains the source address. For example:

```python
data, address = udp_socket.recvfrom(