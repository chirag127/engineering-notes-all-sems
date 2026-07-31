### Logical addressing in network layer

Logical addressing is used in the network layer to identify devices on a network and to route data between them. The most common logical addressing scheme is the Internet Protocol (IP) addressing, which uses a 32-bit (IPv4) or 128-bit (IPv6) address to uniquely identify devices on a network.

Here is an example of how logical addressing is used in the network layer:

```python
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# connection to hostname on the port
s.connect((host, 80))

# receive data from the server
data = s.recv(1024)

s.close()
print(data)
```
