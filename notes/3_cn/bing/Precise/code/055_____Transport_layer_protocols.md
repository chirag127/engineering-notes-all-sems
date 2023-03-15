### Transport layer protocols

The transport layer is responsible for providing end-to-end communication services for applications. It provides services such as connection-oriented data stream support, reliability, flow control, and multiplexing. The two most common transport layer protocols are the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP).

Here is an example of how to create a TCP socket in Python:

```python
import socket

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the server
server_address = ('localhost', 10000)
sock.connect(server_address)
```

And here is an example of how to create a UDP socket in Python:

```python
import socket

# create a UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind the socket to the port
server_address = ('localhost', 10000)
sock.bind(server_address)
```
