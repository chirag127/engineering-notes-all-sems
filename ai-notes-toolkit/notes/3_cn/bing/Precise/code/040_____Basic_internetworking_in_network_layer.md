### Basic internetworking in network layer

Internetworking is the process of connecting multiple computer networks together to form a larger network. The network layer is responsible for providing logical addressing and routing services in an internetwork. Here is an example of how basic internetworking can be implemented in the network layer using the Internet Protocol (IP):

```python
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name
host = socket.gethostname()

# Reserve a port for your service
port = 12345

# Bind the socket to the port
s.bind((host, port))

# Become a server socket
s.listen(5)

while True:
    # Establish a connection
    clientsocket, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    clientsocket.send("Thank you for connecting")
    clientsocket.close()
```

This code creates a socket object, binds it to a port, and listens for incoming connections. When a connection is established, the server sends a message to the client and closes the connection. This is a basic example of how internetworking can be implemented in the network layer using the IP protocol.