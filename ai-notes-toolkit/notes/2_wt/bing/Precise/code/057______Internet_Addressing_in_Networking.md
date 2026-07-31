#### Internet Addressing in Networking
An Internet address is a unique identifier that is assigned to a device connected to the Internet. It is used to route data to and from the device. The most common form of Internet addressing is the Internet Protocol (IP) address. An IP address is a numerical label assigned to each device participating in a computer network that uses the Internet Protocol for communication. There are two versions of the IP address: IPv4 and IPv6. IPv4 addresses are 32-bit numbers, while IPv6 addresses are 128-bit numbers. Both versions of the IP address are used to identify devices on the Internet and to route data to and from those devices.

Here is an example of how to assign an IPv4 address to a device in Python:

```python
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

# bind the socket to a public host, and a well-known port
s.bind((host, 80))

# become a server socket
s.listen(5)
```
