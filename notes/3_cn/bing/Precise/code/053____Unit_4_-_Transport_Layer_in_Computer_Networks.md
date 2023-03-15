## Unit 4 - Transport Layer in Computer Networks

The transport layer is responsible for providing end-to-end communication between applications on different devices in a computer network. This layer is responsible for establishing, maintaining, and terminating connections between applications, as well as ensuring reliable data transfer and flow control.

Here is an example of a simple transport layer protocol implemented in Python:

```python
import socket

def transport_layer_send(data, destination_ip, destination_port):
    # create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # connect to the destination
    sock.connect((destination_ip, destination_port))
    
    # send the data
    sock.sendall(data)
    
    # close the connection
    sock.close()

def transport_layer_receive(port):
    # create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # bind the socket to the port
    server_address = ('localhost', port)
    sock.bind(server_address)
    
    # listen for incoming connections
    sock.listen(1)
    
    # accept a connection
    connection, client_address = sock.accept()
    
    # receive the data
    data = connection.recv(1024)
    
    # close the connection
    connection.close()
    
    return data
```