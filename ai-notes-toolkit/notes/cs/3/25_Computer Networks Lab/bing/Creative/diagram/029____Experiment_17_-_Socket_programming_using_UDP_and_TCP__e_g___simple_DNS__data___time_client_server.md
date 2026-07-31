## Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A socket is an endpoint of a communication channel that can send and receive data using a protocol.
- There are three types of sockets: stream sockets, datagram sockets and raw sockets.
- Stream sockets use TCP (Transmission Control Protocol) as the transport layer protocol, which provides a reliable, connection-oriented and byte-stream service .
- Datagram sockets use UDP (User Datagram Protocol) as the transport layer protocol, which provides an unreliable, connectionless and message-oriented service .
- Raw sockets can use any protocol, but they require the programmer to handle the headers and checksums of the packets.
- TCP and UDP have different characteristics and trade-offs for different applications .
- TCP ensures that the data is delivered in order and without errors, but it also adds overhead and latency to the communication .
- UDP is faster and simpler, but it does not guarantee the delivery, order or integrity of the data .
- Some examples of applications that use TCP are web browsers, email clients, file transfer programs and remote login sessions .
- Some examples of applications that use UDP are video streaming, online gaming, voice over IP and DNS (Domain Name System) queries .
- To program sockets in C/C++, we need to use the socket.h header file, which provides the functions and structures for creating, binding, listening, connecting, sending and receiving sockets.
- To program sockets in Python, we need to use the socket module, which provides a high-level and low-level interface for working with sockets .
- The main difference between working with TCP and UDP in Python is that, when creating the socket, we have to use SOCK_DGRAM for UDP and SOCK_STREAM for TCP.
- A simple DNS client/server program using UDP sockets can be implemented as follows:

```python
# DNS server
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('Starting DNS server on {} port {}'.format(*server_address))
sock.bind(server_address)

# A dictionary to store the domain name and IP address mappings
dns_table = {
    'www.google.com': '142.250.74.196',
    'www.facebook.com': '31.13.71.36',
    'www.amazon.com': '176.32.103.205'
}

while True:
    # Receive data from the client
    data, address = sock.recvfrom(4096)
    print('Received {} bytes from {}'.format(len(data), address))
    print(data)

    # Check if the data is a valid domain name
    if data:
        domain_name = data.decode()
        if domain_name in dns_table:
            # Send back the corresponding IP address
            ip_address = dns_table[domain_name]
            print('Sending IP address {}'.format(ip_address))
            sock.sendto(ip_address.encode(), address)
        else:
            # Send back an error message
            error = 'Domain name not found'
            print('Sending error message {}'.format(error))
            sock.sendto(error.encode(), address)
```

```python
# DNS client
import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# The server address and port
server_address = ('localhost', 10000)

# A list of domain names to query
domain_names = ['www.google.com', 'www.facebook.com', 'www.amazon.com', 'www.invalid.com']

# Send each domain name to the server and receive the response
for domain_name in domain_names:
    # Encode the domain name as bytes
    message = domain_name.encode()
    print('Sending domain name {}'.format(domain_name))
    # Send the message to the server
    sent = sock.sendto(message, server_address)

    # Receive the response from the server
    data, server = sock.recvfrom(4096)
    print('Received {} bytes from {}'.format(len(data),

```
