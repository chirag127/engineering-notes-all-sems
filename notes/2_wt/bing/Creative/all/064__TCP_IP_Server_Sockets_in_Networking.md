#### TCP/IP Server Sockets in Networking

- A network socket is a software structure that serves as an endpoint for sending and receiving data across a network.
- A network socket is identified by a socket address, which consists of an IP address and a port number.
- A port number is a 16-bit integer that identifies a specific service or application running on a host.
- Port numbers are divided into three ranges: well-known ports (0-1023), registered ports (1024-49151), and dynamic or ephemeral ports (49152-65535).
- TCP/IP is a protocol suite that consists of two main protocols: Transmission Control Protocol (TCP) and Internet Protocol (IP).
- TCP is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of data .
- IP is a connectionless protocol that provides routing and addressing of data packets.
- A TCP socket is a type of network socket that uses TCP as the transport protocol.
- A TCP socket requires a three-way handshake to establish a connection: the client sends a SYN packet, the server responds with a SYN-ACK packet, and the client acknowledges with an ACK packet.
- A TCP socket is defined by the IP address of the machine and the port it uses.
- A TCP server socket is a TCP socket that listens for incoming connections from TCP client sockets.
- A TCP server socket is created by binding it to a local IP address and port number, and then calling the listen() method to start listening for incoming connections.
- A TCP server socket accepts a connection request from a TCP client socket by calling the accept() method, which returns a new TCP socket that represents the established connection.
- A TCP server socket can communicate with the TCP client socket by using the send() and receive() methods to exchange data.
- A TCP server socket can close the connection with the TCP client socket by calling the close() method, which sends a FIN packet to indicate the end of the data transmission.
- A TCP server socket can handle multiple TCP client sockets by using threads, processes, or asynchronous I/O.

Here is an example of a TCP server socket in Python:

```python
# Import socket module
import socket

# Create a TCP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a local address and port
server_socket.bind(('127.0.0.1', 8080))

# Start listening for incoming connections
server_socket.listen()

# Accept a connection request from a client
client_socket, client_address = server_socket.accept()

# Print the client address
print(f'Connected to {client_address}')

# Receive data from the client
data = client_socket.recv(1024)

# Print the data
print(f'Received: {data.decode()}')

# Send data to the client
client_socket.send(b'Hello from server')

# Close the connection
client_socket.close()

# Close the server socket
server_socket.close()
```

Here is an example of a TCP client socket in Python:

```python
# Import socket module
import socket

# Create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server socket
client_socket.connect(('127.0.0.1', 8080))

# Send data to the server
client_socket.send(b'Hello from client')

# Receive data from the server
data = client_socket.recv(1024)

# Print the data
print(f'Received: {data.decode()}')

# Close the connection
client_socket.close()
```

Advantages of TCP sockets:

- They provide reliable, ordered, and error-checked delivery of data .
- They handle congestion control, flow control, and retransmission of lost or corrupted packets .
- They are widely used for applications that require reliable data transmission, such as web, email, file transfer, etc. .

Disadvantages of TCP sockets:

- They have more overhead and latency than UDP sockets, due to the connection establishment, acknowledgment, and retransmission mechanisms .
- They are not suitable for applications that require real-time or multicast communication, such as video streaming, gaming, etc. .

Some mnemon