#### TCP/IP Client Sockets in Networking

Here is an example of a simple TCP/IP client socket written in Python:

```python
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# connection to hostname on the port.
s.connect((host, 9999))

# Receive no more than 1024 bytes
msg = s.recv(1024)

s.close()

print(msg.decode('ascii'))
```
