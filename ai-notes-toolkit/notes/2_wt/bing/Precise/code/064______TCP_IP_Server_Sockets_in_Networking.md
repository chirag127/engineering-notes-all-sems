#### TCP/IP Server Sockets in Networking

Here is an example of a simple TCP/IP server socket in Python:

```python
import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind the socket to a public host, and a well-known port
server_socket.bind((host, port))

# become a server socket
server_socket.listen(5)

while True:
    # establish a connection
    client_socket, addr = server_socket.accept()

    print("Got a connection from %s" % str(addr))

    msg = 'Thank you for connecting'+ "\r\n"
    client_socket.send(msg.encode('ascii'))
    client_socket.close()
```
