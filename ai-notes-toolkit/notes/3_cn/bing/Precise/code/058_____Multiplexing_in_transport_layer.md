### Multiplexing in transport layer

Multiplexing in the transport layer refers to the process of combining multiple data streams from different applications into a single data stream for transmission over the network. This is achieved by assigning a unique identifier, known as a port number, to each application. The transport layer protocol, such as TCP or UDP, uses these port numbers to distinguish between different data streams and ensure that the data is delivered to the correct application on the receiving end.

Here is an example of how multiplexing works in the transport layer using the TCP protocol:

```python
import socket

# create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server_address = ('localhost', 10000)
server_socket.bind(server_address)

# listen for incoming connections
server_socket.listen(1)

while True:
    # wait for a connection
    connection, client_address = server_socket.accept()

    # receive and process data from the client
    data = connection.recv(1024)
    # process data...

    # send response back to the client
    connection.sendall(response)

    # clean up the connection
    connection.close()
```

In this example, the server creates a TCP/IP socket and binds it to a specific address and port (in this case, `localhost` and port `10000`). The server then listens for incoming connections on this port. When a client connects to the server, the server accepts the connection and receives data from the client. The server processes the data and sends a response back to the client before closing the connection. This process is repeated for each incoming connection, allowing the server to handle multiple clients simultaneously.