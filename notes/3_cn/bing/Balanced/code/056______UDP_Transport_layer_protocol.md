#### UDP Transport layer protocol

UDP stands for User Datagram Protocol. It is a simple and unreliable transport layer protocol that does not establish a connection or guarantee delivery of data. It is based on best-effort delivery services and has a minimum amount of communication mechanisms. It is suitable for applications that do not require reliability, such as streaming media, online gaming, or voice over IP.

The following is an example of UDP code in Python:

```python
# Import socket module
import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
server_address = ('localhost', 10000)

# Send a message to the server
message = b'Hello, this is a UDP message'
sock.sendto(message, server_address)

# Receive a response from the server
data, address = sock.recvfrom(4096)
print('Received', data, 'from', address)

# Close the socket
sock.close()
```