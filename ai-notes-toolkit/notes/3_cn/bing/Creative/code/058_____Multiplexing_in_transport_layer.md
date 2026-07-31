### Multiplexing in transport layer

Multiplexing in transport layer is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver. Multiplexing in transport layer extends the host-to-host delivery service provided by the network layer to a process-to-process delivery service for applications running on the hosts. Multiplexing in transport layer is needed for all computer networks.

Multiplexing in transport layer can be done in two ways: connectionless and connection-oriented. Connectionless multiplexing uses the combination of source IP address, source port number, destination IP address and destination port number to identify each segment and deliver it to the correct application process. Connection-oriented multiplexing uses the same combination of addresses and port numbers, but also establishes a connection between the sender and the receiver before sending the data. The connection is identified by a socket, which is a unique pair of IP address and port number.

A simple example of multiplexing in transport layer is shown below:

```python
# Sender side
import socket
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to a port
sock.bind(('127.0.0.1', 5000))
# Send data to two different processes on the receiver
sock.sendto(b'Hello process 1', ('127.0.0.1', 6000))
sock.sendto(b'Hello process 2', ('127.0.0.1', 7000))
# Close the socket
sock.close()
```

```python
# Receiver side
import socket
# Create two UDP sockets for two processes
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the sockets to different ports
sock1.bind(('127.0.0.1', 6000))
sock2.bind(('127.0.0.1', 7000))
# Receive data from the sender
data1, addr1 = sock1.recvfrom(1024)
data2, addr2 = sock2.recvfrom(1024)
# Print the data and the address of the sender
print(data1, addr1)
print(data2, addr2)
# Close the sockets
sock1.close()
sock2.close()
```

The output of the receiver side is:

```bash
b'Hello process 1' ('127.0.0.1', 5000)
b'Hello process 2' ('127.0.0.1', 5000)
```

This shows how the sender can send data to different processes on the receiver using different port numbers, and how the receiver can demultiplex the data using the same port numbers. This is an example of connectionless multiplexing using UDP protocol. A similar example can be done using TCP protocol, which is connection-oriented.