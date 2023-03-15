### IPv6 in CN

```python
# Here is an example of how to create an IPv6 socket in Python:

import socket

# Create an IPv6 socket
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
sock.bind(('::1', 12345))

# Listen for incoming connections
sock.listen(1)

# Accept a connection
conn, addr = sock.accept()

# Receive data from the client
data = conn.recv(1024)

# Send data back to the client
conn.sendall(data)

# Close the connection
conn.close()
```