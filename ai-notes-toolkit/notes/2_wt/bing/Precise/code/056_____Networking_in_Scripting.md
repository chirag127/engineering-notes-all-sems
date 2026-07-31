### Networking in Scripting

Here is an example of a Python script that uses the `socket` module to establish a network connection and send data:

```python
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# connection to hostname on the port.
s.connect((host, 8080))

# send a thank you message to the client.
s.sendall(b'Thank you for connecting')

# receive data from the client
data = s.recv(1024)

# close the socket
s.close()

# print the received data
print(data.decode('utf-8'))
```
