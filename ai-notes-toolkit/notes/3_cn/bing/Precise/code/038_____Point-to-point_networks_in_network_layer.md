### Point-to-point networks in network layer

A point-to-point network is a type of network topology in which each pair of nodes is connected by a dedicated communication link. In the network layer, point-to-point networks are used to establish a direct connection between two devices, allowing them to communicate with each other without the need for intermediate devices.

Here is an example of how a point-to-point network can be implemented in the network layer using the Python programming language:

```python
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# Connect to the server on the local computer
s.connect(('127.0.0.1', port))

# Send a message to the server
s.sendall(b'Hello, server!')

# Receive data from the server
data = s.recv(1024)

# Print the received data
print(data)

# Close the socket
s.close()
```

This code creates a socket object and uses it to establish a connection to a server running on the local computer. Once the connection is established, the client can send and receive data from the server using the `sendall` and `recv` methods, respectively. Finally, the socket is closed to release the resources associated with the connection.
