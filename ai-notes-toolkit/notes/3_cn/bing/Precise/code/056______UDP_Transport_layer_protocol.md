#### UDP Transport layer protocol

Here is an example of a simple UDP server written in Python:

```python
import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 10000)
server_socket.bind(server_address)

while True:
    # Receive data from the client
    data, address = server_socket.recvfrom(4096)

    # Process the data and send a response back to the client
    response = data.upper()
    server_socket.sendto(response, address)
```

This code creates a UDP socket and binds it to a specific address and port. It then enters an infinite loop where it waits to receive data from a client. Once data is received, it is processed (in this case, by converting it to uppercase) and a response is sent back to the client.
