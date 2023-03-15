# Computer Networks

Computer networks are systems of interconnected devices that can communicate and exchange data using protocols and standards. Some examples of devices that can be part of a computer network are computers, printers, routers, switches, modems, and servers. Some examples of protocols and standards that enable computer network communication are TCP/IP, Ethernet, Wi-Fi, HTTP, and FTP.

There are different types of computer networks based on their size, topology, architecture, and purpose. Some common types are:

- Local Area Network (LAN): A network that connects devices within a small geographic area, such as a home, office, or school. LANs typically use Ethernet or Wi-Fi as the medium of communication.
- Wide Area Network (WAN): A network that connects devices across a large geographic area, such as a city, country, or the world. WANs typically use leased lines, satellite links, or cellular networks as the medium of communication.
- Personal Area Network (PAN): A network that connects devices within a short range, such as a few meters. PANs typically use Bluetooth, infrared, or NFC as the medium of communication.
- Metropolitan Area Network (MAN): A network that connects devices within a metropolitan area, such as a city or a campus. MANs typically use fiber-optic cables, microwave links, or WiMAX as the medium of communication.
- Wireless Local Area Network (WLAN): A network that connects devices using wireless signals, such as radio waves or microwaves. WLANs typically use Wi-Fi or Bluetooth as the medium of communication.

Computer network programming is the process of creating software applications that can communicate and exchange data over a computer network. Some examples of computer network programming are:

- Web development: Creating websites and web applications that can be accessed by clients using browsers and HTTP protocol.
- Socket programming: Creating low-level applications that can establish connections and send/receive data using sockets and TCP/IP protocol.
- Remote procedure call (RPC): Creating applications that can invoke functions or methods on remote servers using RPC protocol.
- Distributed computing: Creating applications that can perform parallel or distributed computations using multiple devices or nodes over a computer network.

Here is an example of computer network programming using Python. This code creates a simple client-server application that can send and receive messages using sockets and TCP/IP protocol.

```python
# Server code
import socket

# Create a socket object
s = socket.socket()

# Bind the socket to a port
port = 40674
s.bind(('', port))

# Listen for incoming connections
s.listen(5)

# Accept a connection from a client
c, addr = s.accept()

# Send a message to the client
c.send(b'Hello from the server')

# Receive a message from the client
msg = c.recv(1024)
print(msg.decode())

# Close the connection
c.close()
```

```python
# Client code
import socket

# Create a socket object
s = socket.socket()

# Connect to the server
port = 40674
s.connect(('127.0.0.1', port))

# Receive a message from the server
msg = s.recv(1024)
print(msg.decode())

# Send a message to the server
s.send(b'Hello from the client')

# Close the connection
s.close()
```