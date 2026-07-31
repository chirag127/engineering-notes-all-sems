

## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

Stop and wait protocol is a flow control protocol that is used for transmitting data over noiseless channels. It provides unidirectional data transmission, which means that either sending or receiving of data will take place at a time. It is a special category of sliding window protocol where the window size is 1. It requires only two sequence numbers, 0 and 1, to distinguish between the packets. It is also known as stop and wait ARQ (automatic repeat request), which means that the sender will retransmit the packet if it does not receive an acknowledgment from the receiver within a certain time.

Sliding window protocol is a flow control protocol that is used for transmitting data over noisy channels. It provides bidirectional data transmission, which means that both sending and receiving of data can take place simultaneously. It is a general category of protocols that use a window size greater than 1 to allow multiple packets to be sent and received without waiting for acknowledgments. It uses a larger range of sequence numbers to identify the packets. It is also known as sliding window ARQ, which means that the sender will retransmit the packets that are not acknowledged by the receiver within a certain time.

The main objectives of this experiment are:

- To understand the concepts and working of stop and wait protocol and sliding window protocol.
- To implement the stop and wait protocol and sliding window protocol using a programming language such as C, Java, or Python.
- To compare the performance and efficiency of stop and wait protocol and sliding window protocol in terms of throughput, delay, and error handling.



### Experiment 1.1 - Implementation of Stop and Wait Protocol

The stop and wait protocol is a flow control protocol that is used for transmitting data over noiseless channels. It provides unidirectional data transmission, which means that either sending or receiving of data will take place at a time. It is a simple protocol that allows the sender to send the next packet when the acknowledgment of the previous packet is received from the receiver. It is also known as a sliding window protocol with window size 1. It requires only two sequence numbers, 0 and 1, to distinguish between the packets.

The steps involved in the stop and wait protocol are:

- The sender sends a data packet to the receiver and starts a timer.
- The receiver receives the data packet and sends an acknowledgment (ACK) packet back to the sender.
- The sender receives the ACK packet and stops the timer. It then sends the next data packet and repeats the process.
- If the sender does not receive the ACK packet within the timeout period, it assumes that the data packet or the ACK packet was lost. It then retransmits the same data packet and restarts the timer.

The advantages of the stop and wait protocol are:

- It is easy to implement and understand.
- It ensures reliable data transmission over noiseless channels.
- It avoids congestion and buffer overflow at the receiver side.

The disadvantages of the stop and wait protocol are:

- It has low efficiency and throughput, as the sender has to wait for the ACK packet before sending the next data packet.
- It wastes the channel bandwidth and time, as the channel remains idle during the waiting period.
- It does not handle the case of duplicate packets, as the receiver cannot distinguish between the original and the retransmitted packets. This may lead to data corruption or duplication at the receiver side.



### Experiment 1.2 - Implementation of Sliding Window Protocol

- Sliding window protocol is a feature of packet-based data transmission protocols that ensures reliable and sequential delivery of data frames .
- Sliding window protocol uses a window size to control how many frames can be sent by the sender before receiving an acknowledgment from the receiver  .
- The window size can vary depending on the protocol and the network conditions .
- The sender maintains a send window that indicates the range of sequence numbers of frames that it can send .
- The receiver maintains a receive window that indicates the range of sequence numbers of frames that it can accept .
- The sender and the receiver exchange window information using control frames such as ACK, NAK, or SREJ .
- There are two main types of sliding window protocols: Go-Back-N ARQ and Selective Repeat ARQ .
- Go-Back-N ARQ allows the sender to send multiple frames without waiting for acknowledgments, but the receiver can only send a cumulative acknowledgment for the last correctly received frame  .
- If the sender does not receive an acknowledgment within a timeout period, it retransmits all the frames in its window, assuming that they are lost or corrupted  .
- Selective Repeat ARQ allows the sender to send multiple frames without waiting for acknowledgments, and the receiver can send individual acknowledgments for each correctly received frame  .
- If the sender does not receive an acknowledgment for a specific frame within a timeout period, it only retransmits that frame, assuming that the other frames are received correctly  .
- Selective Repeat ARQ can achieve higher efficiency and throughput than Go-Back-N ARQ, but it requires more buffer space and complexity at the sender and the receiver  .



## Experiment 2 - Study of Socket Programming and Client – Server model

- Socket programming is a way of enabling communication between two processes over a network.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol.
- A client is a process that initiates a connection to a server and requests a service or resource.
- A server is a process that listens for incoming connections and provides a service or resource to the clients.
- The client-server model is a distributed application structure that partitions tasks between the providers of a service (servers) and the requesters of a service (clients).
- The client-server model can be implemented using different types of sockets, such as stream sockets and datagram sockets.
- Stream sockets, also known as connection-oriented sockets, establish a reliable and ordered connection between the client and the server before transferring data. They use the Transmission Control Protocol (TCP) as the underlying protocol.
- Datagram sockets, also known as connectionless sockets, do not require a connection between the client and the server and can send or receive data individually. They use the User Datagram Protocol (UDP) as the underlying protocol.
- The steps involved in socket programming are:

  - Socket creation: The client and the server create a socket using the `socket()` function, which returns a socket descriptor, an integer that identifies the socket.
  - Socket binding: The server binds the socket to a specific address and port using the `bind()` function, which associates the socket with the address and port that the clients can use to find the server.
  - Socket listening: The server listens for incoming connection requests from the clients using the `listen()` function, which specifies the maximum number of connections that the server can queue.
  - Socket connection: The client connects to the server using the `connect()` function, which specifies the address and port of the server. The server accepts the connection request from the client using the `accept()` function, which returns a new socket descriptor for the communication with the client.
  - Socket communication: The client and the server can send and receive data using the `send()` and `recv()` functions (or `write()` and `read()` functions) on the socket descriptors. The data can be in the form of bytes, strings, or structures.
  - Socket closing: The client and the server can close the connection using the `close()` function, which releases the socket descriptor and the associated resources.



### Experiment 2.1 - Study of Socket Programming

- Socket programming is a way of enabling communication between different processes or machines using network protocols.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol, such as TCP or UDP.
- Socket programming involves creating, configuring, and using sockets to establish connections and exchange data.
- Socket programming can be done in various programming languages, such as C, Python, Java, etc.
- Socket programming can be used for various applications, such as web servers, chat applications, file transfer, etc.

Some basic steps involved in socket programming are:

- Create a socket using the `socket()` function, specifying the address family, socket type, and protocol.
- Set socket options using the `setsockopt()` function, such as enabling reuse of address, setting timeout, etc.
- Bind the socket to a local address and port using the `bind()` function.
- Listen for incoming connections using the `listen()` function, specifying the maximum number of queued connections.
- Accept a connection from a remote socket using the `accept()` function, which returns a new socket and the address of the remote socket.
- Send and receive data using the `send()` and `recv()` functions, or the `sendto()` and `recvfrom()` functions for connectionless sockets.
- Close the socket using the `close()` function, or the `shutdown()` function to disable further communication.

Some examples of socket programming in different languages are:

- In C, the socket API is defined in the header files `<sys/socket.h>` and `<netinet/in.h>`. The socket functions return -1 on error and set the global variable `errno` to indicate the error code. The socket addresses are represented by the `struct sockaddr` and its variants, such as `struct sockaddr_in` for IPv4 addresses. The socket addresses can be converted to and from human-readable strings using the `inet_ntoa()` and `inet_aton()` functions, or the `inet_ntop()` and `inet_pton()` functions for IPv6 addresses. The socket data can be read and written using the `read()` and `write()` functions, or the `send()` and `recv()` functions with additional flags.  
- In Python, the socket module provides a high-level interface for socket programming. The socket functions raise exceptions on error and return meaningful values on success. The socket addresses are represented by tuples of host and port, or by strings for Unix domain sockets. The socket addresses can be converted to and from human-readable strings using the `socket.gethostbyname()` and `socket.gethostbyaddr()` functions, or the `socket.getaddrinfo()` and `socket.getnameinfo()` functions for IPv6 addresses. The socket data can be read and written using the `socket.send()` and `socket.recv()` methods, or the `socket.sendto()` and `socket.recvfrom()` methods for connectionless sockets.  
- In Java, the java.net package provides classes and interfaces for socket programming. The socket classes throw exceptions on error and return meaningful values on success. The socket addresses are represented by the `InetAddress` and `InetSocketAddress` classes, which provide methods to get and set the host and port. The socket addresses can be converted to and from human-readable strings using the `InetAddress.getByName()` and `InetAddress.getHostAddress()` methods, or the `InetAddress.getAllByName()` and `InetAddress.getCanonicalHostName()` methods for IPv6 addresses. The socket data can be read and written using the `InputStream` and `OutputStream` objects obtained from the `Socket` and `ServerSocket` classes, or the `DatagramPacket` and `DatagramSocket` classes for connectionless sockets.



### Experiment 2.2 - Study of Client – Server model

The client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients. Often clients and servers communicate over a computer network on separate hardware, but both client and server may reside in the same system.

The main components of the client-server model are:

- **Client**: A client is a computer program or device that requests and receives services or resources from a server. A client can be a web browser, an email client, a file transfer client, etc. A client initiates the communication with the server and sends requests to the server.
- **Server**: A server is a computer program or device that provides services or resources to clients. A server can be a web server, an email server, a file server, etc. A server listens for incoming requests from clients and responds to them accordingly.
- **Network**: A network is a system of interconnected devices that enables the communication between clients and servers. A network can be a local area network (LAN), a wide area network (WAN), or the Internet. A network can use different protocols and standards to facilitate the data transmission between clients and servers.

The main benefits of the client-server model are:

- **Centralization**: The client-server model centralizes the data and resources in a single place, which makes it easier to manage, update, and secure. The server can also control the access and permissions of the clients to the data and resources.
- **Scalability**: The client-server model can scale up or down the capacity of the clients and servers separately, depending on the demand and workload. The server can also handle multiple concurrent requests from different clients efficiently.
- **Cost-efficiency**: The client-server model reduces the maintenance and operational costs, as the clients can use thin or lightweight devices that do not require much processing power or storage capacity. The server can also share the resources among multiple clients, which reduces the duplication and wastage of resources.
- **Data recovery**: The client-server model enables the data recovery in case of any failure or loss, as the data is stored and backed up in the server, which can be accessed by the clients anytime. The server can also implement data protection and backup mechanisms to prevent data corruption or loss.



## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is a network protocol that maps an IP address to a MAC address of a device on the same network.
- RARP stands for Reverse Address Resolution Protocol. It is a network protocol that maps a MAC address to an IP address of a device on the same network.
- Both protocols use broadcast messages to request and reply the address mappings.
- The code below is a Python program that simulates the ARP and RARP protocols using sockets and threads.

```python
# Import the required modules
import socket
import threading
import time

# Define the broadcast address and port
BROADCAST_ADDR = "255.255.255.255"
BROADCAST_PORT = 5000

# Define the IP and MAC address mappings
IP_MAC_TABLE = {
    "192.168.1.1": "00:0a:95:9d:68:16",
    "192.168.1.2": "00:0a:95:9d:68:17",
    "192.168.1.3": "00:0a:95:9d:68:18",
    "192.168.1.4": "00:0a:95:9d:68:19",
}

MAC_IP_TABLE = {
    "00:0a:95:9d:68:16": "192.168.1.1",
    "00:0a:95:9d:68:17": "192.168.1.2",
    "00:0a:95:9d:68:18": "192.168.1.3",
    "00:0a:95:9d:68:19": "192.168.1.4",
}

# Define a function to create a UDP socket
def create_socket():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Enable broadcasting
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    # Bind the socket to the broadcast address and port
    sock.bind((BROADCAST_ADDR, BROADCAST_PORT))
    # Return the socket
    return sock

# Define a function to handle ARP requests
def handle_arp_request(sock, addr, data):
    # Extract the source and destination IP addresses from the data
    src_ip, dst_ip = data.split()
    # Print the ARP request message
    print(f"Received ARP request from {src_ip} to {dst_ip}")
    # Check if the destination IP address is in the IP-MAC table
    if dst_ip in IP_MAC_TABLE:
        # Get the corresponding MAC address
        dst_mac = IP_MAC_TABLE[dst_ip]
        # Create the ARP reply message
        reply = f"{dst_ip} {dst_mac}"
        # Send the ARP reply message to the source address
        sock.sendto(reply.encode(), addr)
        # Print the ARP reply message
        print(f"Sent ARP reply to {src_ip} with {dst_ip} {dst_mac}")

# Define a function to handle RARP requests
def handle_rarp_request(sock, addr, data):
    # Extract the source and destination MAC addresses from the data
    src_mac, dst_mac = data.split()
    # Print the RARP request message
    print(f"Received RARP request from {src_mac} to {dst_mac}")
    # Check if the destination MAC address is in the MAC-IP table
    if dst_mac in MAC_IP_TABLE:
        # Get the corresponding IP address
        dst_ip = MAC_IP_TABLE[dst_mac]
        # Create the RARP reply message
        reply = f"{dst_mac} {dst_ip}"
        # Send the RARP reply message to the source address
        sock.sendto(reply.encode(), addr)
        # Print the RARP reply message
        print(f"Sent RARP reply to {src_mac} with {dst_mac} {dst_ip}")

# Define a function to listen for incoming messages
def listen(sock):
    # Loop forever
    while True:
        # Receive a message from the socket
        data, addr = sock.recvfrom(1024)
        # Decode the message
        data = data.decode()
        # Check if the message is an ARP request
        if data.startswith("ARP"):
            # Handle the ARP request
            handle_arp_request(sock, addr, data[4:])
        # Check if the message is a RARP request
        elif data.startswith("RARP"):
            # Handle the RARP request
            handle_rarp_request(sock, addr, data[5

```




## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- PING and TRACEROUTE are two common network diagnostic tools that can test the connectivity and latency between two hosts on a network.
- PING sends a series of packets to a destination host and measures the time it takes for each packet to be sent and received. It also reports the number of packets lost or dropped during the transmission.
- TRACEROUTE traces the route that packets take from the source host to the destination host, showing the intermediate hops and the latency for each hop. It can also identify the network devices and their IP addresses along the path.
- To write a code simulating PING and TRACEROUTE commands, we can use the Python programming language and the socket and struct modules. The socket module provides low-level access to network interfaces, and the struct module allows us to pack and unpack binary data.
- The following steps outline the basic algorithm for the code:

  1. Import the socket and struct modules.
  2. Define a function to create a raw socket that can send and receive ICMP (Internet Control Message Protocol) packets. ICMP is a protocol used for network management and error reporting. PING and TRACEROUTE use ICMP echo request and echo reply messages to test the connectivity and latency.
  3. Define a function to calculate the checksum of a packet. The checksum is a value that verifies the integrity of the packet. It is computed by adding the 16-bit words of the packet and taking the one's complement of the sum.
  4. Define a function to create an ICMP echo request packet. The packet consists of a header and a payload. The header contains the type, code, checksum, identifier, and sequence number fields. The payload can be any arbitrary data. The type and code fields are set to 8 and 0, respectively, for an echo request. The identifier and sequence number fields are used to match the request and reply packets. The checksum field is calculated using the function defined in step 3.
  5. Define a function to send an ICMP echo request packet to a destination host and receive an ICMP echo reply packet from it. The function takes the destination host name, the packet size, and the timeout as parameters. The function uses the socket and struct modules to create and send the packet, and to receive and unpack the reply. The function also records the time it takes for the packet to be sent and received, and returns the round-trip time, the packet size, and the reply packet.
  6. Define a function to parse an ICMP echo reply packet and extract the relevant information. The function takes the reply packet as a parameter and uses the struct module to unpack the header and payload. The function returns the type, code, checksum, identifier, sequence number, and payload fields of the packet.
  7. Define a function to simulate the PING command. The function takes the destination host name, the number of packets to send, and the timeout as parameters. The function uses a loop to send and receive packets using the functions defined in steps 4 and 5. The function also calculates the minimum, maximum, average, and standard deviation of the round-trip times, and the percentage of packets lost. The function prints the results in a formatted output.
  8. Define a function to simulate the TRACEROUTE command. The function takes the destination host name and the maximum number of hops as parameters. The function uses a loop to send and receive packets using the functions defined in steps 4 and 5, but with a twist. The function sets the TTL (Time To Live) field of the packet to a value that increases by one in each iteration. The TTL field determines how many hops a packet can travel before it is discarded. By increasing the TTL value, the function can trace the route that the packet takes from the source to the destination. The function also prints the IP address and the host name of each hop, and the round-trip time for each packet. The function stops when it reaches the destination, or when it exceeds the maximum number of hops, or when it encounters an error.
  9. Write the main function that takes the user input and calls the appropriate function based on the command. The user can enter either PING or TRACEROUTE, followed by the destination host name, and optionally, the number of packets, the packet size, the timeout, and the maximum number of hops. The main function validates the user input and handles any exceptions that may occur.

- The following code is an example of how the code simulating PING and TRACEROUTE commands can look like:

```python
# Import the

```




## Experiment 5 - Create a socket for HTTP for web page upload and download

- A socket is an endpoint of a communication channel between two processes or devices over a network.
- HTTP (Hypertext Transfer Protocol) is a protocol that defines how web servers and web browsers communicate and exchange data.
- To create a socket for HTTP, we need to use the socket module in Python, which provides a low-level interface to the network layer.
- The steps to create a socket for HTTP are:

  1. Import the socket module: `import socket`
  2. Create a socket object: `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  3. Specify the host and port of the web server: `host = 'www.example.com'` and `port = 80`
  4. Connect the socket to the server: `s.connect((host, port))`
  5. Send an HTTP request to the server: `s.send(b'GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n')`
  6. Receive the HTTP response from the server: `data = s.recv(1024)`
  7. Close the socket: `s.close()`
  8. Print the data: `print(data.decode())`

- To upload and download a web page, we need to use the requests module in Python, which provides a high-level interface to the HTTP protocol.
- The steps to upload and download a web page are:

  1. Import the requests module: `import requests`
  2. Specify the URL of the web page: `url = 'http://www.example.com/index.html'`
  3. Download the web page using the GET method: `r = requests.get(url)`
  4. Check the status code of the response: `r.status_code`
  5. Save the web page content to a file: `with open('index.html', 'wb') as f: f.write(r.content)`
  6. Modify the web page content as desired: `# edit the index.html file`
  7. Upload the web page using the PUT method: `r = requests.put(url, data=open('index.html', 'rb'))`
  8. Check the status code of the response: `r.status_code`



## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

- RPC (Remote Procedure Call) is a technique that allows a program to invoke a procedure or a function on a different machine or process as if it were a local call.
- RPC hides the details of the network communication, such as the message formats, protocols, and data marshalling, from the application programmer.
- RPC can be implemented using different models, such as client-server, peer-to-peer, or broker-based.
- In this experiment, we will write a simple RPC program using the client-server model, where the client invokes a remote procedure on the server and receives the result.
- The remote procedure we will implement is a calculator service that can perform basic arithmetic operations, such as addition, subtraction, multiplication, and division.
- We will use Python as the programming language and XML-RPC as the RPC protocol.
- XML-RPC is a standard that uses XML to encode the requests and responses, and HTTP as the transport protocol.
- Python provides a built-in module called xmlrpc that supports both XML-RPC client and server functionality.

### Steps to implement RPC program

1. Import the xmlrpc module in both the client and the server programs.
2. Create a server object using the xmlrpc.server.SimpleXMLRPCServer class, passing the host and port as arguments.
3. Define the remote procedures as regular Python functions, and register them with the server object using the register_function method.
4. Start the server loop using the serve_forever method, which will listen for incoming requests and dispatch them to the registered functions.
5. Create a client object using the xmlrpc.client.ServerProxy class, passing the URL of the server as an argument.
6. Invoke the remote procedures on the client object as if they were local methods, passing the arguments as normal.
7. Handle any exceptions that may occur during the RPC communication, such as xmlrpc.client.Fault or xmlrpc.client.ProtocolError.

### Example code for RPC program

#### Server code

```python
# Import the xmlrpc module
import xmlrpc.server

# Define the remote procedures
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

# Create a server object
server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))

# Register the remote procedures with the server
server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(mul, "mul")
server.register_function(div, "div")

# Start the server loop
print("Server is running on port 8000")
server.serve_forever()
```

#### Client code

```python
# Import the xmlrpc module
import xmlrpc.client

# Create a client object
client = xmlrpc.client.ServerProxy("http://localhost:8000")

# Invoke the remote procedures
try:
    print("Addition: 5 + 3 =", client.add(5, 3))
    print("Subtraction: 5 - 3 =", client.sub(5, 3))
    print("Multiplication: 5 * 3 =", client.mul(5, 3))
    print("Division: 5 / 3 =", client.div(5, 3))
except xmlrpc.client.Fault as f:
    print("Fault occurred:", f.faultCode, f.faultString)
except xmlrpc.client.ProtocolError as p:
    print("Protocol error occurred:", p.errcode, p.errmsg)
```

### Expected output

#### Server output

```
Server is running on port 8000
```

#### Client output

```
Addition: 5 + 3 = 8
Subtraction: 5 - 3 = 2
Multiplication: 5 * 3 = 15
Division: 5 / 3 = 1.6666666666666667
```



## Experiment 7 - Implementation of Subnetting

Subnetting is the process of dividing a network into smaller subnetworks or subnets. Subnetting allows us to:

- Conserve IP addresses by allocating them more efficiently.
- Reduce network traffic by isolating broadcast domains.
- Simplify network design and management by grouping hosts with similar requirements.
- Enhance network security by applying different policies to different subnets.

To perform subnetting, we need to understand the following concepts and terms:

- IP address: A 32-bit binary number that identifies a host or a network interface on the Internet Protocol (IP) network. An IP address consists of two parts: network part and host part. The network part identifies the network to which the host belongs, and the host part identifies the specific host within the network. For example, in the IP address 192.168.1.100, the network part is 192.168.1 and the host part is 100.
- Subnet mask: A 32-bit binary number that determines how many bits of the IP address are used for the network part and how many bits are used for the host part. The subnet mask has 1s in the network part and 0s in the host part. For example, the subnet mask 255.255.255.0 has 24 bits for the network part and 8 bits for the host part. The subnet mask can also be written in slash notation as /24, which means the same thing as 255.255.255.0.
- Network ID: The network part of the IP address, obtained by performing a bitwise AND operation between the IP address and the subnet mask. The network ID identifies the subnet to which the host belongs. For example, the network ID of the IP address 192.168.1.100 with the subnet mask 255.255.255.0 is 192.168.1.0.
- Broadcast ID: The IP address that has all 1s in the host part, obtained by performing a bitwise OR operation between the network ID and the inverse of the subnet mask. The broadcast ID is used to send a message to all hosts in the subnet. For example, the broadcast ID of the network ID 192.168.1.0 with the subnet mask 255.255.255.0 is 192.168.1.255.
- Total hosts: The number of possible IP addresses in the subnet, calculated by raising 2 to the power of the number of bits in the host part. For example, the total hosts in the subnet with the subnet mask 255.255.255.0 is 2^8 = 256.
- Valid hosts: The number of usable IP addresses in the subnet, calculated by subtracting 2 from the total hosts. The two IP addresses that are not usable are the network ID and the broadcast ID. For example, the valid hosts in the subnet with the subnet mask 255.255.255.0 is 256 - 2 = 254.
- Power of 2: The number that is a multiple of 2 and is equal to or greater than the number of required hosts or subnets. For example, the power of 2 for 12 hosts is 16, and the power of 2 for 5 subnets is 8.
- Block size: The difference between two consecutive network IDs or broadcast IDs in the same subnet. The block size is equal to the power of 2 for the number of bits in the host part. For example, the block size for the subnet mask 255.255.255.0 is 2^8 = 256.
- CIDR: Classless Inter-Domain Routing, a notation that combines the IP address and the subnet mask into one expression. The CIDR notation consists of the IP address followed by a slash and the number of bits in the network part. For example, the CIDR notation for the IP address 192.168.1.100 with the subnet mask 255.255.255.0 is 192.168.1.100/24.

The steps to perform subnetting are as follows:

1. Determine the number of required subnets and hosts per subnet.
2. Choose a suitable subnet mask that can accommodate the required subnets and hosts. The subnet mask should have enough bits in the network part to create the subnets and enough bits in the host part to assign the hosts. The subnet mask can be chosen from the following table:

| Subnet mask | Slash notation | Bits for network | Bits for host | Total hosts | Valid hosts



## Experiment 8 - Applications using TCP Sockets

TCP sockets are a type of network communication mechanism that allows two processes to exchange data using the Transmission Control Protocol (TCP). TCP is a reliable, connection-oriented protocol that ensures the data is delivered in order and without errors. TCP sockets can be used to implement various network applications, such as:

- File transfer: TCP sockets can be used to send and receive files between a client and a server. The client can request a file from the server by sending its name, and the server can send the file contents in chunks until the end of the file is reached. The client can acknowledge each chunk and request the next one until the file transfer is complete. An example of a file transfer application using TCP sockets is the File Transfer Protocol (FTP).
- Remote command execution: TCP sockets can be used to execute commands on a remote machine and get the output. The client can send a command to the server, and the server can execute the command and send the output back to the client. The client can then display the output or process it further. An example of a remote command execution application using TCP sockets is the Secure Shell (SSH).
- Chat: TCP sockets can be used to implement a chat application that allows multiple users to communicate with each other. The client can send a message to the server, and the server can broadcast the message to all the other clients. The clients can then display the message or reply to it. An example of a chat application using TCP sockets is the Internet Relay Chat (IRC).
- Web: TCP sockets can be used to implement a web application that allows a client to request and receive web pages from a server. The client can send a request to the server using the Hypertext Transfer Protocol (HTTP), and the server can send the web page contents in response. The client can then display the web page or follow the links to request other web pages. An example of a web application using TCP sockets is the World Wide Web (WWW).

To use TCP sockets, the following steps are required:

- Create a socket object using the Socket class constructor. The constructor takes three parameters: the address family, the socket type, and the protocol type. The address family specifies the network protocol to use, such as IPv4 or IPv6. The socket type specifies the communication style, such as stream or datagram. The protocol type specifies the specific protocol to use, such as TCP or UDP. For TCP sockets, the address family is usually AddressFamily.InterNetwork, the socket type is SocketType.Stream, and the protocol type is ProtocolType.Tcp.
- Bind the socket to a local address and port using the Bind method. The Bind method takes an EndPoint object as a parameter, which specifies the network address and port to use. The network address can be an IP address or a host name, and the port can be any number between 0 and 65535. For TCP sockets, the EndPoint object is usually an IPEndPoint object, which represents an IP address and port pair.
- Listen for incoming connections using the Listen method. The Listen method takes an integer as a parameter, which specifies the maximum number of pending connections to accept. The Listen method puts the socket in a listening state, where it waits for incoming connection requests from other sockets.
- Accept an incoming connection using the Accept method. The Accept method returns a new socket object that represents the connection with the remote socket. The Accept method blocks the execution until a connection request is received. The new socket object can be used to send and receive data with the remote socket.
- Connect to a remote address and port using the Connect method. The Connect method takes an EndPoint object as a parameter, which specifies the network address and port of the remote socket. The Connect method establishes a connection with the remote socket and returns when the connection is successful or an error occurs.
- Send data to the remote socket using the Send method. The Send method takes a byte array as a parameter, which contains the data to send. The Send method returns the number of bytes sent, or throws an exception if an error occurs. The Send method blocks the execution until the data is sent or an error occurs.
- Receive data from the remote socket using the Receive method. The Receive method takes a byte array as a parameter, which is used to store the received data. The Receive method returns the number of bytes received, or throws an exception if an error occurs. The Receive method blocks the execution until data is received or an error occurs.
- Close the socket using the Close method. The Close



# Experiment 8.1 - Echo client and echo server

- An echo client and echo server are applications that allow a client and a server to communicate over a network.
- The client sends a message to the server and the server receives the message and sends back, or echoes, the same message to the client.
- The purpose of this experiment is to demonstrate the basic concepts of socket programming, such as creating sockets, binding sockets, listening for connections, accepting connections, sending and receiving data, and closing sockets.
- The experiment can be done using different programming languages, such as Java, Python, or C, and different protocols, such as TCP or UDP.
- The experiment consists of the following steps:

  - Create a server program that creates a socket, binds it to a port, listens for incoming connections, accepts a connection from a client, reads data from the client, echoes the data back to the client, and closes the connection and the socket.
  - Create a client program that creates a socket, connects to the server, writes data to the server, reads data from the server, prints the data, and closes the socket.
  - Run the server program on one machine and the client program on another machine, or on the same machine using different terminals.
  - Test the communication between the client and the server by typing different messages on the client and observing the responses from the server.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write on the topic of Experiment 8.2 - Chat. Here is the content I have generated in markdown format:

# Experiment 8.2 - Chat

- The objective of this experiment is to design and implement a chat application using sockets and threads in Python.
- A chat application allows multiple users to communicate with each other in real time over a network.
- A socket is an endpoint of a communication channel that can send and receive data using a protocol such as TCP or UDP.
- A thread is a unit of execution that can run concurrently with other threads in a process.
- The chat application consists of two components: a server and a client.
- The server is responsible for listening for incoming connections, accepting them, and managing the communication between the connected clients.
- The client is responsible for connecting to the server, sending and receiving messages, and displaying them to the user.
- The server and the client communicate using a predefined protocol that defines the format and meaning of the messages exchanged.
- The protocol can be text-based or binary-based, depending on the application requirements.
- The server and the client can use encryption and authentication mechanisms to ensure the security and privacy of the communication.

## Steps to implement the chat application

- Import the socket, threading, and sys modules in Python.
- Define the server address and port number as constants.
- Create a socket object using the socket.socket() function and bind it to the server address and port using the socket.bind() method.
- Start listening for incoming connections using the socket.listen() method.
- Define a function to handle each client connection in a separate thread. The function should:
  - Accept the connection using the socket.accept() method and get the client socket and address.
  - Send a welcome message to the client using the socket.send() method.
  - Receive messages from the client using the socket.recv() method in a loop until the client disconnects or sends a special message to indicate the end of the communication.
  - Display the messages received from the client to the server console using the print() function.
  - Send a response message to the client using the socket.send() method if needed.
  - Close the client socket using the socket.close() method when the communication is over.
- Create a thread object using the threading.Thread() function and pass the client handling function as the target argument. Start the thread using the thread.start() method.
- Repeat steps 5 and 6 for each incoming connection in a loop until the server is terminated by the user or by an exception.
- Close the server socket using the socket.close() method when the server is terminated.

- Create a socket object using the socket.socket() function and connect it to the server address and port using the socket.connect() method.
- Receive the welcome message from the server using the socket.recv() method and display it to the user using the print() function.
- Define a function to send messages to the server in a separate thread. The function should:
  - Get the user input using the input() function in a loop until the user enters a special message to indicate the end of the communication.
  - Send the user input to the server using the socket.send() method.
  - Close the socket using the socket.close() method when the communication is over.
- Create a thread object using the threading.Thread() function and pass the message sending function as the target argument. Start the thread using the thread.start() method.
- Receive messages from the server using the socket.recv() method in a loop until the server disconnects or the communication is over.
- Display the messages received from the server to the user using the print() function.
- Close the socket using the socket.close() method when the communication is over.



### Experiment 8.3 - File Transfer

- File transfer is the process of copying or moving a file from one computer to another over a network or the Internet.
- File transfer can be done using different protocols, such as FTP, HTTP, SCP, SFTP, etc.
- File transfer can be done for different purposes, such as backup, synchronization, sharing, distribution, etc.
- File transfer can be done in different modes, such as binary, ASCII, or auto-detect.
- File transfer can be done using different tools, such as command-line utilities, graphical user interfaces, web browsers, etc.

- In this experiment, you will learn how to perform file transfer using FTP and SCP protocols.
- You will need two computers connected to the same network or the Internet, and a file to transfer.
- You will also need an FTP server and an SCP server running on one of the computers, and an FTP client and an SCP client on the other computer.
- You will use the FTP client and the SCP client to connect to the FTP server and the SCP server, respectively, and transfer the file in both directions.
- You will compare the speed, security, and ease of use of FTP and SCP protocols.



## Experiment 9 - Applications using TCP and UDP Sockets

TCP and UDP are two protocols that are used to send and receive data over the internet. They are part of the transport layer of the internet protocol suite, which provides end-to-end communication between applications. TCP and UDP have different characteristics and use cases, depending on the requirements of the applications.

### TCP (Transmission Control Protocol)

TCP is a connection-oriented protocol, which means that it establishes a reliable and ordered communication channel between two endpoints before sending any data. TCP uses a three-way handshake to create a connection, and a four-way handshake to terminate it. TCP also provides mechanisms for error detection, congestion control, and flow control, to ensure that the data is delivered correctly and efficiently.

Some of the applications that use TCP are:

- Web browsers and servers, which use HTTP (Hypertext Transfer Protocol) to exchange web pages and files.
- Email clients and servers, which use SMTP (Simple Mail Transfer Protocol) to send and receive emails.
- File transfer applications, which use FTP (File Transfer Protocol) or SCP (Secure Copy Protocol) to upload and download files.
- Remote login applications, which use SSH (Secure Shell) or Telnet to access remote computers.
- Streaming media applications, which use RTSP (Real Time Streaming Protocol) to control the playback of audio and video.

### UDP (User Datagram Protocol)

UDP is a connectionless protocol, which means that it does not establish or maintain any connection between the endpoints. UDP simply sends datagrams, which are packets of data, without any guarantee of delivery, order, or error correction. UDP is faster and more efficient than TCP, but it also has more risks of data loss, duplication, or corruption.

Some of the applications that use UDP are:

- Domain name system (DNS), which resolves domain names to IP addresses.
- Dynamic host configuration protocol (DHCP), which assigns IP addresses to devices on a network.
- Network time protocol (NTP), which synchronizes the clocks of devices on a network.
- Voice over IP (VoIP), which transmits voice calls over the internet.
- Online gaming, which requires low latency and high responsiveness.

### Sockets

Sockets are the endpoints of a communication channel between two applications. Sockets are identified by a combination of an IP address and a port number, which specify the source and destination of the data. Sockets can be either TCP or UDP, depending on the protocol used by the applications.

Sockets are used by applications to send and receive data over the network. Sockets can be either blocking or non-blocking, depending on how they handle the data. Blocking sockets wait for the data to be available before returning, while non-blocking sockets return immediately even if the data is not ready.

Some of the functions that are used to create and manipulate sockets are:

- socket(), which creates a new socket and returns a file descriptor.
- bind(), which assigns a local address and port to a socket.
- listen(), which marks a socket as ready to accept incoming connections.
- accept(), which accepts a connection request from a remote socket and returns a new socket.
- connect(), which initiates a connection to a remote socket.
- send(), which sends data to a connected socket.
- recv(), which receives data from a connected socket.
- sendto(), which sends data to a specific socket address.
- recvfrom(), which receives data from a specific socket address.
- close(), which closes a socket and releases its resources.



### Experiment 9.1 - DNS

DNS stands for Domain Name System. It is a system that maps domain names to IP addresses. Domain names are human-readable names that identify websites, such as www.google.com. IP addresses are numerical identifiers that computers use to communicate over the Internet, such as 142.250.74.196.

The purpose of DNS is to allow users to access websites using domain names instead of IP addresses, which are easier to remember and type. DNS also provides other services, such as email routing, load balancing, and security.

DNS works by using a hierarchical structure of servers, called name servers, that store and distribute information about domain names and IP addresses. There are four types of name servers:

- Root servers: These are the top-level servers that know the addresses of all the authoritative servers for the top-level domains, such as .com, .org, .net, etc.
- Top-level domain (TLD) servers: These are the servers that know the addresses of all the authoritative servers for the second-level domains, such as google.com, wikipedia.org, amazon.net, etc.
- Authoritative servers: These are the servers that know the exact IP address of a specific domain name, such as www.google.com, en.wikipedia.org, www.amazon.net, etc.
- Recursive servers: These are the servers that act as intermediaries between users and other name servers. They cache the results of previous queries and forward the queries to the appropriate name servers if they do not have the answer.

When a user wants to access a website using a domain name, the following steps occur:

- The user's browser sends a DNS query to a recursive server, asking for the IP address of the domain name.
- The recursive server checks its cache to see if it has the answer. If not, it sends a query to a root server, asking for the address of the TLD server for the domain name.
- The root server responds with the address of the TLD server and the recursive server sends a query to the TLD server, asking for the address of the authoritative server for the domain name.
- The TLD server responds with the address of the authoritative server and the recursive server sends a query to the authoritative server, asking for the IP address of the domain name.
- The authoritative server responds with the IP address of the domain name and the recursive server sends the answer back to the user's browser.
- The user's browser uses the IP address to establish a connection with the website and request the web page.

The following diagram illustrates the DNS resolution process:

```
+----------------+        +----------------+        +----------------+
| User's browser |        | Recursive      |        | Root           |
|                |        | server         |        | server         |
|                |        |                |        |                |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
      |                        |                        |
      | DNS query              |                        |
      |----------------------->|                        |
      |                        |                        |
      |                        | DNS query              |
      |                        |----------------------->|
      |                        |                        |
      |                        | DNS response           |
      |                        |<-----------------------|
      |                        |                        |
      |                        |                        |
+----------------+        +----------------+        +----------------+
| User's browser |        | Recursive      |        | TLD            |
|                |        | server         |        | server         |
|                |        |                |        |                |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
      |                        |                        |
      |                        | DNS query              |
      |                        |----------------------->|
      |                        |                        |
      |                        | DNS response           |
      |                        |<-----------------------|
      |                        |                        |
      |                        |                        |
+----------------+        +----------------+        +----------------+
| User's browser |        | Recursive      |        | Authoritative  |
|                |        | server         |        | server         |
|                |        |                |        |                |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
      |                        |                        |
      |                        | DNS query              |
      |                        |----------------------->|
      |                        |                        |
      |                        | DNS response           |
      |                        |<-----------------------|
      |                        |                        |
      | DNS response          |                        |
      |<----------------------|                        |
      |                        |                        |
      |                        |                        |
+----------------+        +----------------+        +----------------+
| User's browser |        | Recursive      |

```




### Experiment 9.2 - SNMP

- SNMP stands for Simple Network Management Protocol. It is a way for different devices on a network to share information about their current state, and also a channel through which an administrator can modify pre-defined values .
- SNMP is widely used in network management for network monitoring. SNMP exposes management data in the form of variables on the managed systems organized in a management information base (MIB) which describe the system status and configuration.
- SNMP is a component of the Internet Protocol Suite as defined by the Internet Engineering Task Force (IETF). It consists of a set of standards for network management, including an application layer protocol, a database schema, and a set of data objects.
- SNMP operates on a client-server model, where the client is called a manager and the server is called an agent. The manager can request information from the agent, or instruct the agent to perform some action. The agent can also send unsolicited notifications to the manager, called traps or informs .
- SNMP uses four basic operations: GET, SET, GETNEXT, and TRAP. GET is used to retrieve a value from the agent. SET is used to assign a value to the agent. GETNEXT is used to retrieve the next value in a MIB table. TRAP is used to send an alert from the agent to the manager .
- SNMP has three versions: SNMPv1, SNMPv2c, and SNMPv3. SNMPv1 is the original version, which has limited security and functionality. SNMPv2c is an extension of SNMPv1, which adds support for 64-bit counters, bulk transfers, and community-based security. SNMPv3 is the latest version, which adds support for encryption, authentication, and access control  .
- SNMP is a simple and flexible protocol that can be used to manage and monitor a variety of devices on a network. It allows devices to communicate even if the devices are different hardware and run different software. However, SNMP also has some limitations, such as scalability, performance, and security issues. Therefore, SNMP should be used with caution and proper configuration.



### Experiment 9.3 - File Transfer

- The objective of this experiment is to learn how to transfer files between different devices using various protocols and tools.
- The prerequisites for this experiment are:
  - Basic knowledge of networking concepts and protocols such as TCP/IP, FTP, HTTP, etc.
  - Access to at least two devices that can communicate over a network, such as computers, smartphones, tablets, etc.
  - Access to a file server that supports FTP or HTTP, such as Apache, IIS, etc.
  - Access to a file transfer client that supports FTP or HTTP, such as FileZilla, WinSCP, etc.
- The steps for this experiment are:
  - Connect the devices to the same network, either wired or wireless, and ensure that they can ping each other.
  - On the file server, create a folder and copy some files of different types and sizes into it, such as text, image, audio, video, etc.
  - On the file server, configure the FTP or HTTP service to allow access to the folder and its contents, and note down the server address, port number, username, and password if required.
  - On the file transfer client, enter the server address, port number, username, and password, and connect to the file server.
  - On the file transfer client, browse the folder and select some files to download or upload, and observe the transfer speed, progress, and status.
  - On the file transfer client, disconnect from the file server and close the application.
  - On the file server, verify that the files have been transferred correctly and delete them if necessary.
  - Repeat the steps with different combinations of devices, protocols, and files, and compare the results.
- The expected outcomes of this experiment are:
  - The file transfer client can connect to the file server and access the folder and its contents.
  - The file transfer client can download or upload files from or to the file server, and the transfer is completed successfully and accurately.
  - The file transfer speed, progress, and status depend on various factors, such as the network bandwidth, the file size, the file type, the protocol, the device, etc.
  - The file transfer client can disconnect from the file server and close the application without any errors or issues.
- The questions for this experiment are:
  - What are the advantages and disadvantages of using FTP or HTTP for file transfer?
  - How can you secure the file transfer using encryption, authentication, or authorization?
  - How can you optimize the file transfer using compression, chunking, or caching?



## Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

- Network simulator (NS) is a name for a series of discrete event network simulators, specifically ns-1, ns-2, and ns-3   .
- NS is used for simulation of TCP, routing, and multicast protocols over wired and wireless (local and satellite) networks .
- NS is free, open-source software, licensed under the GNU GPLv2 license, and maintained by a worldwide community.
- NS is written in C++ and uses Tcl as a scripting language .
- NS provides a modular framework for creating and composing network components, such as nodes, links, queues, protocols, applications, and traffic sources .
- NS also provides a graphical user interface called NAM (Network Animator) for visualizing the simulation results .
- Congestion control algorithms are mechanisms that aim to regulate the amount of data sent by the sources in a network, in order to avoid congestion and ensure fair and efficient use of the network resources.
- Some examples of congestion control algorithms are TCP Reno, TCP NewReno, TCP Vegas, TCP Tahoe, and TCP SACK.
- Each congestion control algorithm has its own characteristics and performance in different network scenarios, such as packet loss, delay, throughput, fairness, and stability.
- NS can be used to simulate and compare different congestion control algorithms, by setting the parameters and variables of the network topology, traffic sources, and protocols.
- The steps to simulate and compare congestion control algorithms using NS are:

  - Install NS on your system, following the instructions from the official website.
  - Create a Tcl script that defines the network topology, traffic sources, protocols, and output files for the simulation.
  - Run the script using the command `ns filename.tcl`.
  - Analyze the output files, such as trace files and NAM files, using tools like awk, gnuplot, xgraph, or NAM.
  - Compare the results of different congestion control algorithms, such as packet loss, delay, throughput, fairness, and stability.



## Experiment 11 - Perform a case study about the different routing algorithms to select the network path with its optimum and economical during data transfer

- Routing algorithms are the methods used by routers to determine the best path for sending packets in a network.
- Routing algorithms can be classified into two main categories: adaptive and non-adaptive.
- Adaptive algorithms change their routing decisions whenever network topology or traffic load changes. They can adapt to network conditions and optimize performance, but they require more computation and communication overhead. Examples of adaptive algorithms are distance vector, link state, and multipath routing.
- Non-adaptive algorithms do not change their routing decisions once they are initialized. They are simpler and faster, but they may not be able to cope with network failures or congestion. Examples of non-adaptive algorithms are shortest path, flooding, and broadcast routing.
- A case study of the evolution of routing algorithms in a network planning tool is presented in   . The authors describe how they developed and improved a software system for transmission network planning, which involves combining network topology, traffic demand, and routing algorithms to find the optimal network configuration.
- The authors compare three different routing algorithms: shortest path, minimum interference, and minimum cost routing. They evaluate the algorithms based on their performance, complexity, and suitability for different network scenarios. They also discuss the challenges and trade-offs involved in implementing and evolving routing algorithms in a network planning tool.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content in markdown format on the topic of Experiment 11.1 - Link State routing. Here is the content:

### Experiment 11.1 - Link State routing

- Link state routing is a dynamic routing protocol that uses the concept of link state advertisements (LSAs) to exchange information about the network topology and the cost of reaching different destinations.
- LSAs are broadcasted periodically by each router to all its neighbors, and then flooded throughout the network. Each router maintains a link state database (LSDB) that contains all the LSAs it has received.
- Based on the LSDB, each router computes the shortest path to every other router in the network using an algorithm such as Dijkstra's algorithm. This results in a routing table that maps each destination to the next hop router along the shortest path.
- Link state routing has some advantages over distance vector routing, such as faster convergence, loop-free routing, and support for hierarchical routing. However, it also has some disadvantages, such as higher memory and bandwidth requirements, and vulnerability to misconfigured or malicious routers.



### Experiment 11.2 - Flooding

- Flooding is a natural phenomenon that occurs when a large amount of water overflows onto land that is normally dry.
- Flooding can be caused by various factors, such as heavy rainfall, snowmelt, storm surges, dam failures, or river overflow.
- Flooding can have positive and negative impacts on the environment, society, and economy.
- Positive impacts of flooding include:
  - Replenishing soil nutrients and groundwater resources.
  - Creating habitats for aquatic and wetland species.
  - Supporting agriculture and fisheries.
- Negative impacts of flooding include:
  - Damaging infrastructure and property.
  - Disrupting transportation and communication.
  - Causing injuries, deaths, and diseases.
  - Displacing people and animals.
  - Increasing the risk of landslides, erosion, and pollution.
- Flooding can be measured by various indicators, such as flood frequency, flood duration, flood magnitude, and flood extent.
- Flood frequency is the average number of times a flood of a given size occurs in a given period of time.
- Flood duration is the length of time that a flood lasts.
- Flood magnitude is the amount of water that flows during a flood, usually expressed in cubic meters per second (m3/s) or cubic feet per second (cfs).
- Flood extent is the area that is covered by water during a flood, usually expressed in square kilometers (km2) or square miles (mi2).
- Flooding can be prevented or mitigated by various methods, such as:
  - Building levees, dams, or reservoirs to control water flow and storage.
  - Implementing flood warning systems and emergency plans to alert and evacuate people.
  - Restoring natural floodplains and wetlands to absorb excess water and reduce runoff.
  - Adopting sustainable land use and management practices to reduce soil erosion and sedimentation.
  - Enhancing flood resilience and adaptation by improving infrastructure, insurance, and education.



### Experiment 11.3 - Distance vector

- Distance vector is a routing algorithm that calculates the best route for a packet based on the distance or hop count to the destination.
- Distance vector routers exchange their routing tables periodically with their neighbors to update their knowledge of the network topology.
- Distance vector routers use the Bellman-Ford algorithm to compute the shortest path to each destination based on the information received from their neighbors.
- Distance vector routers suffer from two major problems: slow convergence and count-to-infinity.
- Slow convergence means that it takes a long time for the routers to reach a consistent view of the network after a change in the topology, such as a link failure or a new link addition.
- Count-to-infinity means that the routers may increment the distance to a destination indefinitely in the presence of a loop in the network, making the destination unreachable.
- Distance vector routers can use some techniques to overcome these problems, such as split horizon, poison reverse, triggered updates, and hold-down timers.



## Experiment 12 - To learn handling and configuration of networking hardware like RJ-45 connector, CAT-6 cable, crimping tool, etc

- The objective of this experiment is to learn how to handle and configure some common networking hardware devices, such as RJ-45 connector, CAT-6 cable, crimping tool, etc.
- The RJ-45 connector is a standard type of connector for Ethernet cables, which are used to connect computers and other devices to a network. The RJ-45 connector has eight pins that correspond to the eight wires in the cable.
- The CAT-6 cable is a type of twisted pair cable that can support data transmission speeds up to 10 Gbps. The CAT-6 cable has four pairs of wires, each with a different color code. The wires are twisted together to reduce interference and crosstalk.
- The crimping tool is a device that is used to attach the RJ-45 connector to the CAT-6 cable. The crimping tool has a blade that cuts the cable to the desired length, a stripper that removes the insulation from the wires, and a crimper that presses the pins of the connector into the wires.
- The steps to handle and configure the networking hardware are as follows:

  1. Cut the CAT-6 cable to the desired length using the blade of the crimping tool.
  2. Strip about 2 cm of the insulation from both ends of the cable using the stripper of the crimping tool.
  3. Untwist the wires and arrange them according to the color code of the RJ-45 connector. The standard color code is as follows:

    - Pin 1: White and green
    - Pin 2: Green
    - Pin 3: White and orange
    - Pin 4: Blue
    - Pin 5: White and blue
    - Pin 6: Orange
    - Pin 7: White and brown
    - Pin 8: Brown

  4. Insert the wires into the RJ-45 connector, making sure that they are aligned with the pins and that they reach the end of the connector.
  5. Crimp the connector to the cable using the crimper of the crimping tool, applying enough pressure to secure the connection.
  6. Repeat the steps for the other end of the cable, using the same or a different color code depending on the type of connection (straight-through or crossover).
  7. Test the cable using a cable tester or by connecting it to the network devices and checking the network connectivity.

- The expected outcome of this experiment is to have a functional CAT-6 cable with RJ-45 connectors that can be used to connect network devices. The possible sources of error are:

  - Improper cutting, stripping, or crimping of the cable or the connector, which can result in loose or broken connections, short circuits, or open circuits.
  - Incorrect wiring or color coding of the cable or the connector, which can result in mismatched or reversed signals, or no signal at all.
  - Damaged or defective cable, connector, or crimping tool, which can affect the quality or performance of the connection.



## Experiment 13 - Configuration of router, hub, switch etc. (using real devices or simulators)

- The objective of this experiment is to learn how to configure and connect different network devices such as routers, hubs, switches, etc. using real devices or simulators.
- The network devices are used to create and manage local area networks (LANs) and wide area networks (WANs) that allow communication and data transfer among different hosts and networks.
- The configuration of network devices involves setting up parameters such as IP addresses, subnet masks, default gateways, routing protocols, etc. that enable the devices to function properly and efficiently.
- The connection of network devices involves using cables, connectors, ports, etc. that physically link the devices and establish the network topology and architecture.
- The experiment can be performed using real devices or simulators. Real devices are physical hardware that can be connected and configured using console cables, Ethernet cables, serial cables, etc. Simulators are software applications that can emulate the behavior and functionality of network devices and allow the user to create and configure virtual networks using graphical user interfaces (GUIs) or command-line interfaces (CLIs).
- The steps for performing the experiment are as follows:

  1. Identify the network devices that are required for the experiment. For example, routers, hubs, switches, PCs, etc.
  2. If using real devices, connect the devices using the appropriate cables and connectors. For example, connect routers using serial cables, connect switches using Ethernet cables, connect PCs to switches using Ethernet cables, etc. If using simulators, create the devices and drag and drop them on the workspace.
  3. Configure the devices using the appropriate interfaces. For example, configure routers using console cables and terminal emulation software, configure switches using console cables or Ethernet cables and web browser or terminal emulation software, configure PCs using keyboard and mouse, etc. If using simulators, configure the devices using the GUI or CLI provided by the simulator.
  4. Set up the parameters for the devices such as IP addresses, subnet masks, default gateways, routing protocols, etc. For example, assign IP addresses and subnet masks to the interfaces of routers and PCs, set up default gateways for routers and PCs, enable routing protocols such as RIP, OSPF, EIGRP, etc. on routers, etc. If using simulators, set up the parameters using the GUI or CLI provided by the simulator.
  5. Verify the connectivity and functionality of the network devices and the network using various tools and commands. For example, use ping, traceroute, ipconfig, show ip route, show ip interface brief, etc. to test the connectivity and functionality of the devices and the network. If using simulators, use the tools and commands provided by the simulator.
  6. Observe and analyze the results and output of the experiment. For example, observe the packet flow, routing tables, interface status, etc. of the network devices and the network. If using simulators, observe the results and output provided by the simulator.
  7. Document the experiment by recording the steps, parameters, results, and output of the experiment. For example, write a report or a lab manual that describes the experiment and its outcomes. If using simulators, save or print the results and output of the experiment.



## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

- The objective of this experiment is to learn how to use some common network utilities for troubleshooting and information gathering.
- The network utilities are programs that run on a host computer and interact with the network or other hosts.
- Some of the network utilities that will be covered in this experiment are:

  - ping: a program that sends a packet to a destination IP address and waits for a reply. It is used to test the connectivity and latency between two hosts .
  - traceroute: a program that sends a series of packets to a destination IP address and records the routers that the packets pass through. It is used to trace the path and measure the hop count and delay between two hosts .
  - nslookup: a program that queries the Domain Name System (DNS) to obtain the IP address or domain name of a host or other DNS records. It is used to verify the DNS configuration and resolve host names  .
  - arp: a program that displays or modifies the Address Resolution Protocol (ARP) cache of a host. The ARP cache is a table that maps the IP addresses to the MAC addresses of the hosts on the same network. It is used to view or manipulate the ARP entries of a host  .
  - telnet: a program that establishes a remote terminal session with another host using the Telnet protocol. It is used to access and control another host over the network .
  - ftp: a program that transfers files between two hosts using the File Transfer Protocol (FTP). It is used to upload or download files over the network .

- To run these network utilities, you need to open a command prompt or a terminal window on your host computer and type the name of the utility followed by the parameters or options. For example, to ping the IP address 8.8.8.8, you would type:

  ```
  ping 8.8.8.8
  ```

- The output of the network utilities will vary depending on the operating system, the network configuration, and the destination host. You can use the help option (-h or /?) to see the available parameters or options for each utility. For example, to see the help for ping, you would type:

  ```
  ping -h
  ```

- In this experiment, you will run and use the network utilities to perform various tasks and observe the results. You will also learn how to interpret the output and troubleshoot common network problems.



## Experiment 15 - Network packet analysis using tools like Wireshark, tcpdump, etc

- Network packet analysis is the process of capturing, inspecting, and interpreting the data packets that are exchanged between devices on a network.
- Network packet analysis tools are software applications that can capture, filter, decode, and analyze the packets on a network.
- Network packet analysis tools can help network administrators, security analysts, and forensic investigators to monitor network performance, troubleshoot problems, detect anomalies, and investigate malicious activities.
- Some of the common network packet analysis tools are:

  - Wireshark: A free and open-source tool that can capture and analyze packets on various network protocols and interfaces. It has a graphical user interface (GUI) and a command-line interface (CLI) and supports various filters, statistics, and visualization features .
  - tcpdump: A free and open-source tool that can capture and display packets on a network using a CLI. It can filter packets based on various criteria and save them to a file for later analysis. It can also read packets from a file and display them on the screen.
  - Colasoft Capsa: A commercial tool that can capture and analyze packets on both wired and wireless networks. It has a GUI and supports various features such as network topology mapping, protocol analysis, packet decoding, and network diagnosis.
  - Paessler PRTG: A commercial tool that can capture and analyze packets on various network devices and sensors. It has a web-based interface and supports various features such as network traffic classification, bandwidth monitoring, and alerting.
  - Arkime: A free and open-source tool that can capture and index packets on a network and store them in a database. It has a web-based interface and supports various features such as packet search, session reconstruction, and data extraction.

- To perform network packet analysis using these tools, the following steps are typically involved:

  - Select a network interface or device to capture packets from.
  - Apply filters or rules to capture only the packets of interest.
  - Start the packet capture and stop it when enough data is collected.
  - Analyze the captured packets using various tools and techniques, such as packet decoding, protocol analysis, statistics, graphs, etc.
  - Save or export the analysis results for further investigation or reporting.



# Experiment 16 - Network simulation using tools like Cisco Packet Tracer, NetSim, OMNeT++, NS2, NS3, etc

- Network simulation is the process of modeling the behavior and performance of a network using software tools.
- Network simulation tools can help students, researchers, and professionals to design, test, and analyze various network scenarios and protocols.
- Network simulation tools can support different types of networks, such as wired, wireless, mobile, ad hoc, sensor, software-defined, etc.
- Network simulation tools can vary in their features, capabilities, complexity, and licensing.
- Some of the popular network simulation tools are:

  - Cisco Packet Tracer: A network simulation tool developed by Cisco that allows users to create and configure network devices and scenarios using a graphical user interface. It is mainly used for learning and teaching purposes. It supports basic and advanced networking concepts, such as routing, switching, security, IoT, etc. It is available for free for Cisco Networking Academy students and instructors.
  - NetSim: A network simulation tool developed by Tetcos that allows users to simulate various network technologies and protocols, such as TCP/IP, LAN, WAN, wireless, mobile, IoT, etc. It supports packet-level simulation, network emulation, network visualization, and network animation. It is a licensed software that offers different editions for academic, research, and industrial purposes.
  - OMNeT++: An open-source network simulation tool that allows users to create modular and component-based network models using C++. It supports discrete event simulation, network emulation, parallel simulation, and graphical user interface. It can be extended with various frameworks and libraries, such as INET, VEINS, SimuLTE, etc. It can simulate various types of networks, such as software-defined, wireless, mobile, ad hoc, sensor, etc .
  - NS2: An open-source network simulation tool that allows users to simulate various network protocols and scenarios using a combination of C++ and OTcl. It supports discrete event simulation, network emulation, network visualization, and network animation. It can simulate various types of networks, such as mobile, ad hoc, sensor, satellite, etc .
  - NS3: An open-source network simulation tool that allows users to simulate various network protocols and scenarios using C++ or Python. It supports discrete event simulation, network emulation, network visualization, and network animation. It can simulate various types of networks, such as software-defined, hybrid, wireless, mobile, ad hoc, sensor, etc .

- To perform network simulation using any of these tools, the following steps are generally required:

  - Define the network topology, parameters, and devices.
  - Configure the network protocols, applications, and traffic.
  - Run the simulation and collect the output data.
  - Analyze the results and evaluate the network performance.



## Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol.
- There are three types of sockets: stream sockets, datagram sockets and raw sockets.
- Stream sockets use TCP (Transmission Control Protocol) as the transport layer protocol, which provides a reliable, connection-oriented and byte-stream service .
- Datagram sockets use UDP (User Datagram Protocol) as the transport layer protocol, which provides an unreliable, connectionless and message-oriented service .
- Raw sockets can use any protocol, but they require the programmer to handle the headers and checksums of the packets.
- TCP and UDP have different characteristics and trade-offs, depending on the application requirements .
- TCP ensures that the data is delivered in order and without errors, but it adds more overhead and latency than UDP .
- UDP is faster and more efficient than TCP, but it does not guarantee the delivery, order or integrity of the data .
- Some examples of applications that use TCP are web browsers, email clients, file transfer programs and remote login sessions .
- Some examples of applications that use UDP are video streaming, online gaming, voice over IP and DNS (Domain Name System) queries .
- To program sockets using TCP or UDP in C/C++, we need to use the socket.h header file, which provides the functions and structures for creating, binding, listening, connecting, sending and receiving sockets.
- To program sockets using TCP or UDP in Python, we need to use the socket module, which provides the same functionality as the socket.h header file in C/C++ .
- The main difference between working with TCP and UDP in Python is that, when creating the socket, we have to use SOCK_DGRAM for UDP and SOCK_STREAM for TCP.
- To create a simple DNS client/server using UDP, we need to do the following steps:
  - Create a UDP socket on the server side and bind it to a port number.
  - Create a UDP socket on the client side and send a DNS query to the server's IP address and port number.
  - Receive the DNS query on the server side and process it to find the corresponding IP address of the domain name.
  - Send the IP address back to the client side using the same UDP socket.
  - Receive the IP address on the client side and print it to the console.
- To create a simple data & time client/server using TCP, we need to do the following steps:
  - Create a TCP socket on the server side and bind it to a port number.
  - Listen for incoming connections on the server side using the listen() function.
  - Create a TCP socket on the client side and connect it to the server's IP address and port number using the connect() function.
  - Accept the connection on the server side using the accept() function, which returns a new socket for the communication with the client.
  - Send the current date and time to the client side using the send() function on the new socket.
  - Receive the date and time on the client side using the recv() function on the original socket and print it to the console.
  - Close the sockets on both sides using the close() function.
- To create a simple echo client/server using TCP or UDP, we need to do the following steps:
  - Create a TCP or UDP socket on the server side and bind it to a port number.
  - Listen for incoming connections on the server side using the listen() function (only for TCP).
  - Create a TCP or UDP socket on the client side and connect it to the server's IP address and port number using the connect() function (only for TCP).
  - Accept the connection on the server side using the accept() function, which returns a new socket for the communication with the client (only for TCP).
  - Send a message to the server side using the send() or sendto() function on the client socket.
  - Receive the message on the server side using the recv() or recvfrom

