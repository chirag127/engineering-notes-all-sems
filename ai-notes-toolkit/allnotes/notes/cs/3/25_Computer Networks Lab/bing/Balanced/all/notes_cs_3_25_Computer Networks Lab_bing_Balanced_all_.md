

# Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

## Objective
The objective of this experiment is to understand and implement two data link layer protocols for reliable and sequential delivery of data frames: stop and wait protocol and sliding window protocol.

## Theory
- Stop and wait protocol is a simple protocol that allows the sender to send one data frame at a time and wait for the acknowledgment from the receiver before sending the next frame. The sender uses a single bit to indicate the sequence number of the frame (0 or 1) and the receiver sends back the same bit as acknowledgment. The sender and the receiver use a half-duplex link, which means that they cannot send and receive data simultaneously. The efficiency of this protocol is low, as the sender has to wait for a round trip time (RTT) between sending and receiving the acknowledgment. The efficiency is given by:

  Efficiency = Tt / (Tt + 2Tp)

  where Tt is the transmission time of a frame and Tp is the propagation time of a frame.

- Sliding window protocol is a more efficient protocol that allows the sender to send multiple frames at a time without waiting for the acknowledgment. The sender and the receiver use a window size to indicate how many frames can be sent or received at a time. The window size can vary from 1 to the maximum sequence number. The sender and the receiver use a full-duplex link, which means that they can send and receive data simultaneously. There are two variants of sliding window protocol: go-back-N ARQ and selective repeat ARQ.

  - Go-back-N ARQ is a sliding window protocol with a fixed window size of 1 for the receiver and a variable window size of wt for the sender. The sender can send up to wt frames at a time and the receiver can only accept the frames in order. If the receiver receives a frame out of order, it discards the frame and sends a negative acknowledgment (NAK) to the sender. The sender then retransmits all the frames from the last acknowledged frame to the current frame. The efficiency of this protocol is given by:

    Efficiency = wt / (1 + 2a)

    where a is the ratio of propagation time to transmission time (a = Tp / Tt).

  - Selective repeat ARQ is a sliding window protocol with a variable window size of wr for the receiver and a variable window size of wt for the sender. The sender can send up to wt frames at a time and the receiver can accept the frames in any order. If the receiver receives a frame out of order, it buffers the frame and sends a positive acknowledgment (ACK) to the sender. The sender then retransmits only the frames that are lost or corrupted. The efficiency of this protocol is given by:

    Efficiency = 1 - p

    where p is the probability of frame loss or corruption.



# Experiment 1.1 - Implementation of Stop and Wait Protocol

## Objective
The objective of this experiment is to implement the stop and wait protocol, which is a flow control protocol that ensures reliable data transmission over a noisy channel.

## Theory
- The stop and wait protocol is a data link layer protocol that uses a half-duplex link between the sender and the receiver. This means that only one direction of data transmission is possible at a time.
- The sender sends one data packet at a time and waits for an acknowledgment (ACK) from the receiver before sending the next packet. The receiver sends an ACK after receiving a packet and checking its error detection code.
- The sender and the receiver use sequence numbers to identify the packets and avoid duplication. The sequence numbers alternate between 0 and 1, as only two sequence numbers are required for this protocol.
- The stop and wait protocol can handle three types of errors: lost packets, corrupted packets, and delayed packets. The sender uses a timer to detect lost or delayed packets and retransmits them after the timer expires. The receiver discards corrupted packets or packets with incorrect sequence numbers and sends a negative acknowledgment (NAK) to the sender.
- The efficiency of the stop and wait protocol is low, as the sender has to wait for an ACK before sending the next packet. The efficiency can be calculated as:

`Efficiency = Tt / (Tt + 2Tp)`

where Tt is the transmission time of a packet and Tp is the propagation time of a packet.

## Procedure
- To implement the stop and wait protocol, we need two programs: one for the sender and one for the receiver. The programs can be written in any programming language, such as C, Java, or Python.
- The sender program should perform the following steps:
  - Create a socket and bind it to a port number.
  - Generate a data packet with a sequence number and an error detection code, such as a checksum or a cyclic redundancy check (CRC).
  - Send the data packet to the receiver and start a timer.
  - Wait for an ACK or a NAK from the receiver or until the timer expires.
  - If an ACK is received, increment the sequence number and generate the next data packet.
  - If a NAK is received or the timer expires, retransmit the same data packet.
  - Repeat the steps until all the data packets are sent.
- The receiver program should perform the following steps:
  - Create a socket and bind it to a port number.
  - Listen for incoming data packets from the sender.
  - Receive a data packet and check its error detection code and sequence number.
  - If the data packet is valid and has the expected sequence number, send an ACK to the sender and process the data.
  - If the data packet is invalid or has an unexpected sequence number, send a NAK to the sender and discard the data.
  - Repeat the steps until all the data packets are received.

## Output
- The output of the experiment should show the data packets sent and received by the sender and the receiver, along with their sequence numbers and error detection codes.
- The output should also show the ACKs and NAKs exchanged by the sender and the receiver, and the timer values used by the sender.
- The output should demonstrate the working of the stop and wait protocol in different scenarios, such as normal transmission, lost packets, corrupted packets, and delayed packets.



# Experiment 1.2 - Implementation of Sliding Window Protocol

## Objective
- To understand the concept of sliding window protocol and its types.
- To implement sliding window protocol using Python programming language.
- To simulate the transmission and reception of data frames using sliding window protocol.

## Theory
- Sliding window protocol is a method of flow control and error control for reliable data transmission in computer networks.
- It allows the sender to send multiple data frames before waiting for an acknowledgment from the receiver.
- It also allows the receiver to accept multiple data frames before sending an acknowledgment to the sender.
- The sender and the receiver maintain a window of frames that can be sent or received at any time. The window size is determined by the available buffer space and the bandwidth of the channel.
- The window slides along the sequence of frames as the sender transmits new frames and the receiver acknowledges them.
- There are two types of sliding window protocol: stop-and-wait and go-back-N.

### Stop-and-wait
- In stop-and-wait protocol, the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame.
- The receiver sends an acknowledgment for each frame it receives.
- The sender and the receiver have a window size of one frame.
- The advantage of stop-and-wait protocol is its simplicity and reliability.
- The disadvantage of stop-and-wait protocol is its low efficiency and utilization of the channel, as the sender has to wait for a round-trip time (RTT) between each frame transmission.

### Go-back-N
- In go-back-N protocol, the sender can send up to N frames at a time without waiting for an acknowledgment from the receiver, where N is the window size.
- The receiver sends an acknowledgment for the last frame it receives in order, and discards any out-of-order frames.
- The sender maintains a timer for each frame it sends. If the timer expires before receiving an acknowledgment, the sender assumes that the frame or the acknowledgment is lost, and retransmits all the frames from the last acknowledged frame.
- The advantage of go-back-N protocol is its higher efficiency and utilization of the channel, as the sender can send multiple frames in a burst.
- The disadvantage of go-back-N protocol is its higher complexity and overhead, as the sender and the receiver have to maintain a larger window size and handle retransmissions.

## Implementation
- To implement sliding window protocol using Python, we need to use the following modules:
  - socket: to create and manage sockets for communication between the sender and the receiver.
  - threading: to create and manage threads for concurrent execution of the sender and the receiver functions.
  - random: to generate random numbers for simulating frame loss and corruption.
  - time: to measure and control the time intervals for frame transmission and acknowledgment.
- We also need to define the following constants and variables:
  - MAX_SEQ: the maximum sequence number of a frame, which is 7 in this experiment.
  - FRAME_SIZE: the size of a frame in bytes, which is 4 in this experiment.
  - WINDOW_SIZE: the size of the sliding window, which is 4 in this experiment.
  - TIMEOUT: the timeout interval for a frame in seconds, which is 5 in this experiment.
  - LOSS_PROB: the probability of frame loss in the channel, which is 0.1 in this experiment.
  - CORRUPT_PROB: the probability of frame corruption in the channel, which is 0.1 in this experiment.
  - sender_socket: the socket object for the sender.
  - receiver_socket: the socket object for the receiver.
  - sender_address: the address tuple for the sender, which is ('localhost', 8000) in this experiment.
  - receiver_address: the address tuple for the receiver, which is ('localhost', 8001) in this experiment.
  - data: the list of data frames to be sent by the sender, which is ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111'] in this experiment.
  - ack: the list of acknowledgment frames to be sent by the receiver, which is ['ACK0', 'ACK1', 'ACK2', 'ACK3', 'ACK4', 'ACK5', 'ACK6', 'ACK7'] in this experiment.
  - next_frame_to_send: the sequence number of the next frame to be sent by the sender, initialized to 0.
  - frame_expected: the sequence number of the next frame expected by the receiver, initialized to 0.
  - buffer: the list of frames buffered by the receiver, initialized to an empty list.
  - timer



# Experiment 2 - Study of Socket Programming and Client – Server model

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A socket is an endpoint of a communication channel between two processes or machines.
- Socket programming can be used to implement different types of network applications, such as web browsers, email clients, chat servers, etc.
- Client-server model is a distributed application structure that partitions tasks between the providers of a resource or service, called servers, and service requesters, called clients.
- In the client-server model, the client initiates a request to the server, and the server responds with the desired service or resource.
- The client and the server can communicate using sockets, which are identified by a combination of an IP address and a port number.
- There are two types of sockets: stream sockets and datagram sockets.
  - Stream sockets, also known as connection-oriented sockets, establish a connection before transferring data. They are reliable, in-order, and use Transmission Control Protocol (TCP) as the underlying protocol.
  - Datagram sockets, also known as connectionless sockets, do not require a connection before transferring data. They are unreliable, out-of-order, and use User Datagram Protocol (UDP) as the underlying protocol.
- To create a socket, the socket() function is used, which takes three arguments: the domain, the type, and the protocol.
  - The domain specifies the address family, such as AF_INET for IPv4 or AF_INET6 for IPv6.
  - The type specifies the socket type, such as SOCK_STREAM for stream sockets or SOCK_DGRAM for datagram sockets.
  - The protocol specifies the protocol to be used by the socket, such as IPPROTO_TCP for TCP or IPPROTO_UDP for UDP.
- To bind a socket to an address, the bind() function is used, which takes two arguments: the socket descriptor and the address structure.
  - The socket descriptor is an integer that identifies the socket returned by the socket() function.
  - The address structure is a data structure that contains the IP address and the port number of the socket.
- To listen for incoming connections on a stream socket, the listen() function is used, which takes two arguments: the socket descriptor and the backlog.
  - The backlog is an integer that specifies the maximum number of pending connections that can be queued for the socket.
- To accept a connection on a stream socket, the accept() function is used, which takes three arguments: the socket descriptor, the address structure of the client, and the size of the address structure.
  - The accept() function blocks until a connection request arrives, and then returns a new socket descriptor for the established connection.
  - The address structure of the client contains the IP address and the port number of the client that initiated the connection.
  - The size of the address structure is an integer that specifies the size of the address structure in bytes.
- To connect to a server on a stream socket, the connect() function is used, which takes three arguments: the socket descriptor, the address structure of the server, and the size of the address structure.
  - The connect() function blocks until a connection is established with the server, or an error occurs.
  - The address structure of the server contains the IP address and the port number of the server that offers the service or resource.
  - The size of the address structure is an integer that specifies the size of the address structure in bytes.
- To send data on a stream socket, the write() function is used, which takes three arguments: the socket descriptor, the buffer, and the size of the buffer.
  - The socket descriptor is an integer that identifies the socket returned by the socket() or the accept() function.
  - The buffer is a pointer to a memory location that contains the data to be sent.
  - The size of the buffer is an integer that specifies the number of bytes to be sent.
- To receive data on a stream socket, the read() function is used, which takes three arguments: the socket descriptor, the buffer, and the size of the buffer.
  - The socket descriptor is an integer that identifies the socket returned by the socket() or



# Experiment 2.1 - Study of Socket Programming

- Socket programming is a way of enabling communication between different processes or machines using network protocols.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol, such as TCP or UDP.
- Socket programming involves creating, binding, connecting, listening, sending and receiving sockets using various functions and methods provided by the operating system or a programming language.
- Socket programming can be done in different languages, such as C, C++, Python, Java, etc. Each language has its own syntax and library for socket programming.
- Socket programming can be used for various applications, such as web servers, chat applications, file transfer, remote control, etc.

## Objectives of the experiment

- To understand the basic concepts and terminology of socket programming.
- To learn how to create and use sockets in different languages and platforms.
- To implement simple client-server programs using sockets.
- To explore different types of sockets and protocols, such as stream sockets, datagram sockets, TCP, UDP, etc.
- To learn how to handle errors and exceptions in socket programming.
- To compare and contrast the advantages and disadvantages of socket programming.

## Procedure of the experiment

- Choose a language and a platform for socket programming, such as C on Linux, Python on Windows, etc.
- Review the syntax and library of the chosen language for socket programming, such as socket.h for C, socket module for Python, etc.
- Write a simple program to create a socket and print its attributes, such as family, type, protocol, address, etc.
- Write a simple program to create a client socket and a server socket, and establish a connection between them using TCP protocol.
- Write a simple program to send and receive messages between the client and the server using the send and recv functions or methods.
- Write a simple program to create a client socket and a server socket, and exchange data between them using UDP protocol.
- Write a simple program to handle errors and exceptions in socket programming, such as socket creation failure, connection failure, timeout, etc.
- Test and run the programs on different machines or networks, and observe the output and behavior of the sockets.
- Analyze the results and compare the performance and reliability of different types of sockets and protocols.



# Experiment 2.2 - Study of Client – Server model

## Objective
To understand the basic concepts and features of the client-server model, a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.

## Theory
- The client-server model is a network architecture that describes how servers share resources and services with clients over a network or the Internet .
- A server is a powerful computer that runs one or more server programs that can handle requests from multiple clients.
- A client is a computer or a program that initiates contact with a server in order to access a service or a resource.
- The communication between the client and the server is based on a protocol, which is a set of rules and standards that define how data is exchanged and formatted.
- The client-server model can be classified into two types: thin client and thick client.
  - A thin client is a client that relies heavily on the server for processing and data management, and only performs minimal tasks such as input and output.
  - A thick client is a client that can perform more complex operations and computations locally, and only communicates with the server when necessary.

## Advantages of the client-server model 
- Centralized system with all data in a single place, which facilitates data security, backup, and recovery.
- Cost efficient, as it requires less maintenance cost and less hardware resources for the clients.
- Scalable, as the capacity of the clients and servers can be changed separately according to the demand and workload.
- Modular, as different services and functions can be assigned to different servers, which increases flexibility and performance.

## Disadvantages of the client-server model 
- Dependency, as the clients depend on the availability and functionality of the servers, which can cause problems if the servers fail or malfunction.
- Congestion, as the servers can become overloaded with requests from many clients, which can degrade the quality of service and response time.
- Security, as the servers are exposed to various threats and attacks from malicious users or hackers, which can compromise the data and the system.



## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is a network protocol that maps an IP address to a MAC address of a device on the same network.
- RARP stands for Reverse Address Resolution Protocol. It is a network protocol that maps a MAC address to an IP address of a device on the same network.
- Both ARP and RARP are used to resolve the addresses of devices on a network, but they work in opposite directions.
- To write a code simulating ARP /RARP protocols, we need to use the following steps:

  - Import the socket and struct modules in Python. These modules provide low-level access to network interfaces and data structures.
  - Create a raw socket object using socket.AF_PACKET and socket.SOCK_RAW as the address family and socket type. This allows us to send and receive packets at the link layer.
  - Bind the socket object to a network interface using the bind() method. For example, bind(('eth0', 0)) binds the socket to the eth0 interface with any protocol.
  - Define the MAC and IP addresses of the source and destination devices. For example, src_mac = b'\x00\x0c\x29\x4f\x55\x1b' and src_ip = b'\xc0\xa8\x01\x64' are the MAC and IP addresses of the source device in hexadecimal format.
  - Construct the ARP packet using the struct.pack() method. The ARP packet consists of the following fields:

    - Hardware type: 2 bytes, specifies the type of network hardware. For Ethernet, it is 1.
    - Protocol type: 2 bytes, specifies the type of network protocol. For IPv4, it is 0x0800.
    - Hardware length: 1 byte, specifies the length of the hardware address. For MAC address, it is 6.
    - Protocol length: 1 byte, specifies the length of the protocol address. For IP address, it is 4.
    - Operation: 2 bytes, specifies the type of ARP operation. For ARP request, it is 1. For ARP reply, it is 2. For RARP request, it is 3. For RARP reply, it is 4.
    - Sender hardware address: 6 bytes, specifies the MAC address of the sender device.
    - Sender protocol address: 4 bytes, specifies the IP address of the sender device.
    - Target hardware address: 6 bytes, specifies the MAC address of the target device. For ARP request, it is 0. For ARP reply, it is the MAC address of the device that sent the ARP request. For RARP request, it is the MAC address of the device that needs an IP address. For RARP reply, it is the MAC address of the device that sent the RARP request.
    - Target protocol address: 4 bytes, specifies the IP address of the target device. For ARP request, it is the IP address of the device that needs a MAC address. For ARP reply, it is the IP address of the device that sent the ARP request. For RARP request, it is 0. For RARP reply, it is the IP address of the device that sent the RARP request.

  - For example, to construct an ARP request packet, we can use the following code:

    ```python
    arp_request = struct.pack('!HHBBH6s4s6s4s', 1, 0x0800, 6, 4, 1, src_mac, src_ip, b'\x00\x00\x00\x00\x00\x00', dst_ip)
    ```

  - To construct a RARP request packet, we can use the following code:

    ```python
    rarp_request = struct.pack('!HHBBH6s4s6s4s', 1, 0x0800, 6, 4, 3, src_mac, b'\x00\x00\x00\x00', dst_mac, b'\x00\x00\x00\x00')
    ```

  - Send the packet using the send() method of the socket object. For example, s.send(arp_request) sends the ARP request packet through the socket s.
  - Receive the packet using the recv() method of the socket object. For example, s.recv(1024) receives up to 1024 bytes of data from the socket s.
  - Unpack the packet using the struct.unpack() method. The format string should match the one used in the struct.pack() method. For example, to unpack an ARP reply packet, we can use the following code:

    ```python

```




## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- PING and TRACEROUTE are common commands you can use to troubleshoot network problems  .
- PING is a simple command that can test the reachability of a device on the network by sending and receiving ICMP packets   .
- TRACEROUTE is a command you use to 'trace' the route that a packet takes when traveling to its destination by sending and receiving ICMP packets with varying TTL values    .
- To write a code simulating PING and TRACEROUTE commands, you need to follow these steps:

  - Import the necessary modules, such as socket, struct, time, sys, etc.
  - Define a function to calculate the checksum of an ICMP packet, which is used to verify the integrity of the packet .
  - Define a function to create an ICMP packet, which consists of a header and a payload. The header contains the type, code, checksum, identifier, and sequence number fields. The payload contains the timestamp and some arbitrary data .
  - Define a function to send an ICMP packet to a given destination address and port, using a raw socket. The function should also receive the ICMP reply packet and calculate the round-trip time (RTT) and the hop count .
  - Define a function to perform the PING operation, which involves sending and receiving multiple ICMP packets to a given destination and displaying the statistics, such as the number of packets sent, received, lost, the minimum, maximum, and average RTT, etc   .
  - Define a function to perform the TRACEROUTE operation, which involves sending and receiving ICMP packets with increasing TTL values, starting from 1, to a given destination and displaying the intermediate routers and their RTTs    .
  - Write the main code to take the user input for the destination address and the operation (PING or TRACEROUTE) and call the corresponding function to execute it.

- Here is an example of a code simulating PING and TRACEROUTE commands in Python:

```python
# Import the necessary modules
import socket
import struct
import time
import sys

# Define a function to calculate the checksum of an ICMP packet
def checksum(packet):
    # Initialize the sum to zero
    sum = 0
    # Loop through the packet in 16-bit chunks
    for i in range(0, len(packet), 2):
        # Add the 16-bit chunks to the sum
        sum += (packet[i] << 8) + packet[i+1]
    # Add the carry bits to the sum
    sum = (sum >> 16) + (sum & 0xffff)
    # Invert the sum and return it
    return ~sum & 0xffff

# Define a function to create an ICMP packet
def create_packet(id, seq, data):
    # Define the ICMP header fields
    type = 8 # Echo request
    code = 0 # No code
    checksum = 0 # Placeholder
    identifier = id # Identifier
    sequence = seq # Sequence number
    # Pack the header fields into a binary format
    header = struct.pack('!BBHHH', type, code, checksum, identifier, sequence)
    # Append the payload to the header
    packet = header + data
    # Calculate the checksum of the packet
    checksum = checksum(packet)
    # Repack the header with the checksum
    header = struct.pack('!BBHHH', type, code, checksum, identifier, sequence)
    # Return the packet
    return header + data

# Define a function to send and receive an ICMP packet
def send_packet(dest, port, id, seq, ttl, data):
    # Create a raw socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    # Set the socket timeout
    sock.settimeout(1)
    # Set the socket TTL
    sock

```




## Experiment 5 - Create a socket for HTTP for web page upload and download

- A socket is an endpoint of a communication channel between two processes or devices over a network.
- HTTP (Hypertext Transfer Protocol) is a protocol that defines how messages are formatted and transmitted over the web, and how servers and clients should respond to various commands.
- To create a socket for HTTP, we need to use the socket module in Python, which provides a low-level interface to the network layer.
- The steps to create a socket for HTTP are:

  1. Import the socket module: `import socket`
  2. Create a socket object: `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  3. Specify the host and port of the server: `host = 'www.example.com'` and `port = 80`
  4. Connect the socket to the server: `s.connect((host, port))`
  5. Send an HTTP request to the server: `s.send(b'GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n')`
  6. Receive the HTTP response from the server: `data = s.recv(1024)`
  7. Print the data: `print(data)`
  8. Close the socket: `s.close()`

- To upload and download a web page using the socket, we need to modify the HTTP request and response accordingly.
- For example, to upload a web page, we need to use the POST method instead of the GET method, and include the content of the web page in the request body.
- To download a web page, we need to parse the HTTP response and extract the content of the web page from the response body.



## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

- RPC is a technique for creating distributed client-server applications. It allows a client to invoke a function or a procedure on a remote server as if it were a local call .
- RPC hides the details of network communication, such as protocols, data formats, and message passing, from the application developers. The RPC runtime stubs and libraries handle these details.
- RPC can be implemented using different technologies, such as sockets, message queues, or web services. In this experiment, we will use RabbitMQ, a popular message broker, to implement a simple RPC system  .
- The RPC system will consist of a client and a server. The client will send a request message to the server, containing a number n. The server will compute the n-th Fibonacci number and send a response message back to the client. The client will print the result on the console  .
- The steps to implement the RPC system are as follows:

  - Install RabbitMQ on your machine. You can follow the instructions on the official website: https://www.rabbitmq.com/download.html
  - Choose a programming language that supports RabbitMQ. In this experiment, we will use Python, but you can also use JavaScript, C#, or any other language that has a RabbitMQ client library. You can find the list of supported languages here: https://www.rabbitmq.com/devtools.html
  - Install the RabbitMQ client library for your chosen language. For Python, you can use pip to install pika, the official RabbitMQ library: `pip install pika`
  - Write the server code. The server code will do the following:
    - Import the RabbitMQ library and create a connection and a channel to the RabbitMQ server.
    - Declare a queue to receive the request messages from the client. The queue name can be anything, but we will use `rpc_queue` for simplicity.
    - Define a function to compute the Fibonacci number for a given input. The function can be recursive or iterative, but we will use a simple recursive version for simplicity.
    - Define a callback function to handle the request messages. The callback function will do the following:
      - Extract the number n from the request message body.
      - Call the Fibonacci function to compute the n-th Fibonacci number.
      - Send a response message back to the client, containing the result. The response message will have the same correlation ID as the request message, to match the request and the response. The response message will also have the reply-to property set to the queue name that the client specified in the request message, to indicate where to send the response.
    - Start consuming the messages from the `rpc_queue` and pass them to the callback function.
  - Write the client code. The client code will do the following:
    - Import the RabbitMQ library and create a connection and a channel to the RabbitMQ server.
    - Declare an anonymous queue to receive the response messages from the server. The queue name will be generated by the RabbitMQ server and returned to the client.
    - Define a callback function to handle the response messages. The callback function will do the following:
      - Check if the correlation ID of the response message matches the one that the client generated for the request message. If not, ignore the message.
      - Extract the result from the response message body and print it on the console.
      - Close the connection to the RabbitMQ server.
    - Generate a random correlation ID for the request message. The correlation ID can be any string, but we will use a UUID for simplicity.
    - Read the number n from the user input.
    - Send a request message to the server, containing the number n. The request message will have the correlation ID and the reply-to property set to the anonymous queue name that the client declared.
    - Start consuming the messages from the anonymous queue and pass them to the callback function.

- You can find the complete code for the server and the client in Python here: https://www.rabbitmq.com/tutorials/tutorial-six-python.html
- You can also find the code for other languages here: https://www.rabbitmq.com/getstarted.html
- To run the experiment, you need to do the following:
  - Start the RabbitMQ server on your machine. You can use the command `rabbitmq-server` or follow the instructions on the official website: https://www.rabbitmq.com/install.html
  - Start



## Experiment 7 - Implementation of Subnetting

Subnetting is a technique of dividing a network into smaller subnetworks, each with its own range of IP addresses and network prefix. Subnetting can help improve network performance, security, and management.

The objectives of this experiment are:

- To understand the concept and purpose of subnetting.
- To learn how to calculate subnet masks and subnet addresses using binary and decimal methods.
- To configure and test subnetting on a network simulator.

The steps of this experiment are:

1. Review the basic concepts of IP addressing and subnetting, such as network classes, network bits, host bits, network prefix, and subnet mask.
2. Use a network simulator, such as Packet Tracer, to create a network topology with two routers and four hosts.
3. Assign IP addresses and subnet masks to the routers and hosts according to the network requirements.
4. Use the ping command to test the connectivity between the hosts and routers.
5. Use the show ip route command to verify the routing table entries on the routers.
6. Use the show ip interface brief command to check the status and configuration of the interfaces on the routers and hosts.
7. Modify the subnet mask and IP addresses of the network to create different subnets and observe the changes in the network connectivity and routing table entries.
8. Compare the advantages and disadvantages of using different subnet sizes and network prefixes.



## Experiment 8 - Applications using TCP Sockets

- TCP sockets are a type of network communication mechanism that use the Transmission Control Protocol (TCP) to establish reliable and ordered data transfer between two processes.
- TCP sockets are connection-oriented, meaning that they require a three-way handshake (SYN, SYN-ACK, ACK) to establish a connection before any data can be exchanged.
- TCP sockets are identified by a combination of IP address and port number, which form a socket address.
- TCP sockets can be used to implement various network applications, such as file transfer, chat, web, email, remote shell, etc.
- TCP sockets can be programmed using various languages and platforms, such as C, Java, Python, .NET, etc.
- TCP sockets can be created, bound, connected, listened, accepted, sent, received, and closed using various socket APIs, such as socket(), bind(), connect(), listen(), accept(), send(), recv(), and close().
- TCP sockets can be configured with various options, such as timeout, buffer size, keep-alive, etc. using the setsockopt() and getsockopt() functions.
- TCP sockets can handle various errors and exceptions, such as connection refused, connection reset, connection timed out, etc. using the errno variable or the SocketException class.
- TCP sockets can be tested and debugged using various tools, such as telnet, netcat, wireshark, etc.



# Experiment 8.1 - Echo client and echo server

- An echo client and echo server are applications that allow a client and a server to communicate over a network using sockets.
- A socket is an endpoint of a bidirectional communication channel between two processes running on different machines.
- An echo server is a server that receives data from a client and sends back an identical copy of the data to the client. This is useful for testing the connectivity and performance of the network.
- An echo client is a client that connects to an echo server, sends some data, and waits for the server to echo it back. The client can then compare the sent and received data to verify the integrity and reliability of the network.
- To create an echo client and echo server using Java, the following steps are required:
  - Import the java.net and java.io packages, which provide classes and methods for network programming and input/output operations.
  - Create a ServerSocket object on the server side, which listens for incoming connections on a specified port number.
  - Create a Socket object on the client side, which connects to the server's IP address and port number.
  - Create input and output streams on both the server and the client sides, which allow reading and writing data to and from the sockets.
  - Use a loop on the server side to accept connections from multiple clients, and create a new thread for each client to handle the communication.
  - Use a loop on the client side to read data from the standard input, write it to the output stream of the socket, read the echoed data from the input stream of the socket, and print it to the standard output.
  - Close the sockets and the streams when the communication is done.



# Experiment 8.2 - Chat

- The objective of this experiment is to learn how to create a simple chat application using HTML, CSS, and JavaScript.
- The chat application will allow users to send and receive messages in real time using a web browser and a server.
- The chat application will consist of the following components:
  - A web page that displays the chat interface and the messages.
  - A style sheet that defines the appearance and layout of the web page.
  - A script that handles the user input, the communication with the server, and the updating of the web page.
  - A server that receives and broadcasts the messages to all connected clients.
- The steps to create the chat application are as follows:
  - Create a web page that contains a text input field, a send button, and a message area.
  - Create a style sheet that styles the web page elements and positions them using a grid layout.
  - Create a script that adds an event listener to the send button and sends the user input to the server using an XMLHttpRequest object.
  - Create a script that creates a WebSocket object and connects to the server using the ws protocol.
  - Create a script that listens for messages from the server and appends them to the message area using the innerHTML property.
  - Create a server that creates a WebSocket server using the ws module and listens for connections on a port.
  - Create a server that listens for messages from the clients and broadcasts them to all connected clients using the send method.
- The expected outcome of this experiment is to have a functional chat application that allows users to exchange messages in real time.



# Experiment 8.3 - File Transfer

- The objective of this experiment is to learn how to transfer files between different devices using various protocols and tools.
- The prerequisites for this experiment are:
  - Basic knowledge of networking concepts and protocols such as TCP/IP, FTP, HTTP, etc.
  - Access to at least two devices that can communicate over a network, such as computers, smartphones, tablets, etc.
  - Access to a file server that supports FTP or HTTP, such as Apache, IIS, etc.
- The steps for this experiment are:
  - Create a text file on one device and name it test.txt. Write some content in the file, such as "Hello, world!".
  - Transfer the file to another device using FTP. FTP stands for File Transfer Protocol and it is a standard network protocol for transferring files between hosts. To use FTP, you need an FTP client and an FTP server. You can use any FTP client software, such as FileZilla, WinSCP, etc. You also need to know the IP address, username, and password of the FTP server. To transfer the file, follow these steps:
    - Launch the FTP client and connect to the FTP server by entering the IP address, username, and password.
    - Navigate to the directory where you want to upload the file on the server.
    - Drag and drop the file from your device to the server directory or use the upload button.
    - Verify that the file has been uploaded successfully by checking the file size and timestamp on the server.
  - Transfer the file back to the original device using HTTP. HTTP stands for Hypertext Transfer Protocol and it is a standard network protocol for transferring data over the web. To use HTTP, you need a web browser and a web server. You can use any web browser, such as Chrome, Firefox, Safari, etc. You also need to know the URL of the web server where the file is located. To transfer the file, follow these steps:
    - Launch the web browser and enter the URL of the web server, followed by the file name. For example, http://192.168.1.100/test.txt.
    - The browser will display the file content or prompt you to download the file, depending on the file type and browser settings.
    - Save the file to your device or open it with a text editor.
    - Verify that the file has been downloaded successfully by checking the file size and content on your device.
- The expected outcomes of this experiment are:
  - You will learn how to use FTP and HTTP to transfer files between different devices over a network.
  - You will understand the differences and similarities between FTP and HTTP in terms of functionality, security, and performance.
  - You will be able to compare and contrast FTP and HTTP with other file transfer protocols, such as SCP, SFTP, TFTP, etc.



# Experiment 9 - Applications using TCP and UDP Sockets

## Objective
- To understand the difference between TCP and UDP sockets and how to use them in various applications.
- To implement some simple applications using TCP and UDP sockets in Python.

## Theory
- TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two of the most common transport layer protocols in the Internet Protocol suite.
- TCP provides reliable, ordered, and error-checked delivery of data between two endpoints. TCP establishes a connection-oriented communication, which means that it requires a three-way handshake to establish a connection before any data can be exchanged. TCP also implements flow control, congestion control, and retransmission mechanisms to ensure data integrity and avoid network congestion.
- UDP provides unreliable, unordered, and error-prone delivery of data between two endpoints. UDP establishes a connectionless communication, which means that it does not require any handshake or connection establishment before sending or receiving data. UDP also does not implement any flow control, congestion control, or retransmission mechanisms, which makes it faster and more efficient for some applications that can tolerate data loss or reordering.
- Some applications that use TCP sockets are web browsers, email clients, file transfer protocols, remote login, etc. Some applications that use UDP sockets are video streaming, online gaming, voice over IP, etc.

## Procedure
- To create a TCP socket in Python, we need to import the socket module and use the socket.socket() function with the arguments socket.AF_INET (for IPv4 address family) and socket.SOCK_STREAM (for TCP socket type). For example:

```python
import socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- To create a UDP socket in Python, we need to import the socket module and use the socket.socket() function with the arguments socket.AF_INET (for IPv4 address family) and socket.SOCK_DGRAM (for UDP socket type). For example:

```python
import socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

- To bind a socket to a specific port and IP address, we need to use the socket.bind() method with a tuple of (IP, port) as the argument. For example:

```python
tcp_socket.bind(("127.0.0.1", 8000)) # bind tcp socket to localhost and port 8000
udp_socket.bind(("0.0.0.0", 9000)) # bind udp socket to any IP and port 9000
```

- To listen for incoming connections on a TCP socket, we need to use the socket.listen() method with an argument that specifies the maximum number of queued connections. For example:

```python
tcp_socket.listen(5) # listen for up to 5 connections
```

- To accept a connection on a TCP socket, we need to use the socket.accept() method, which returns a new socket object and the address of the client. For example:

```python
client_socket, client_address = tcp_socket.accept() # accept a connection and get the client socket and address
```

- To send data on a TCP socket, we need to use the socket.send() method with a bytes object as the argument. For example:

```python
client_socket.send(b"Hello, client!") # send a bytes object to the client
```

- To receive data on a TCP socket, we need to use the socket.recv() method with an argument that specifies the maximum number of bytes to receive. The method returns a bytes object that contains the received data. For example:

```python
data = client_socket.recv(1024) # receive up to 1024 bytes from the client
```

- To close a TCP socket, we need to use the socket.close() method. For example:

```python
client_socket.close() # close the client socket
tcp_socket.close() # close the server socket
```

- To send data on a UDP socket, we need to use the socket.sendto() method with a bytes object and a tuple of (IP, port) as the arguments. The method sends the data to the specified destination. For example:

```python
udp_socket.sendto(b"Hello, world!", ("127.0.0.1", 9000)) # send a bytes object to localhost and port 9000
```

- To receive data on a UDP socket, we need to use the socket.recvfrom() method with an argument that specifies the maximum number of bytes to receive. The method returns a tuple of (data, address), where data is a bytes object that contains the received data, and address is a tuple of (IP, port) that contains the source address. For example:

```python
data, address = udp_socket.recvfrom(

```




# Experiment 9.1 - DNS

DNS stands for Domain Name System. It is a system that maps domain names to IP addresses. Domain names are human-readable names that identify websites, such as www.google.com. IP addresses are numerical identifiers that computers use to communicate over the Internet, such as 142.250.72.196.

The purpose of DNS is to allow users to access websites using domain names instead of IP addresses, which are easier to remember and type. DNS also provides other services, such as email delivery, load balancing, and security.

The main components of DNS are:

- DNS servers: These are computers that store and provide DNS records, which are mappings between domain names and IP addresses. There are different types of DNS servers, such as authoritative servers, recursive servers, and caching servers.
- DNS clients: These are devices that request DNS records from DNS servers. For example, a web browser is a DNS client that asks for the IP address of a website before connecting to it.
- DNS records: These are data entries that contain information about a domain name and its corresponding IP address. There are different types of DNS records, such as A records, CNAME records, MX records, and NS records.
- DNS zones: These are logical partitions of the DNS namespace, which is the entire set of domain names and their IP addresses. Each DNS zone is managed by one or more authoritative servers, which are responsible for providing the DNS records for the domain names in that zone.
- DNS queries: These are messages that DNS clients send to DNS servers to request DNS records. There are different types of DNS queries, such as iterative queries, recursive queries, and non-recursive queries.
- DNS responses: These are messages that DNS servers send to DNS clients to provide DNS records. There are different types of DNS responses, such as positive responses, negative responses, and referral responses.

The basic steps of DNS resolution are:

- A DNS client sends a DNS query to a DNS server, asking for the IP address of a domain name.
- The DNS server checks its local cache and zone files to see if it has the DNS record for the domain name. If it does, it sends a positive response to the DNS client with the IP address. If it does not, it sends a referral response to the DNS client with the IP address of another DNS server that may have the DNS record.
- The DNS client repeats the process with the next DNS server until it receives a positive response or a negative response, which indicates that the domain name does not exist or has no IP address.
- The DNS client uses the IP address to connect to the website or perform other actions.



# Experiment 9.2 - SNMP

- SNMP stands for Simple Network Management Protocol. It is a way for different devices on a network to share information about their current state, and also a channel through which an administrator can modify pre-defined values .
- SNMP is widely used in network management for network monitoring. SNMP exposes management data in the form of variables on the managed systems organized in a management information base (MIB) which describe the system status and configuration.
- SNMP is a component of the Internet Protocol Suite as defined by the Internet Engineering Task Force (IETF). It consists of a set of standards for network management, including an application layer protocol, a database schema, and a set of data objects.
- SNMP operates on a client-server model, where the client is called a manager and the server is called an agent. The manager sends requests to the agent and the agent responds with the requested information or performs the requested action.
- SNMP uses four basic operations: GET, SET, GETNEXT, and TRAP. GET is used to retrieve a value from an agent, SET is used to modify a value on an agent, GETNEXT is used to retrieve the next value in a MIB, and TRAP is used to send an unsolicited notification from an agent to a manager.
- SNMP uses a simple data format called SNMP messages, which consist of a header and a payload. The header contains the SNMP version, the community name, and the message type. The payload contains the variable bindings, which are pairs of object identifiers (OIDs) and values.
- SNMP supports three versions: SNMPv1, SNMPv2c, and SNMPv3. SNMPv1 is the original version, which has limited security and functionality. SNMPv2c is an extension of SNMPv1, which adds support for 64-bit counters, bulk operations, and improved error handling. SNMPv3 is the latest version, which adds support for encryption, authentication, and access control.



### Experiment 9.3 - File Transfer

- File transfer is the process of sending or receiving files between two or more devices over a network or the internet.
- File transfer can be done using different protocols, such as FTP, HTTP, SCP, SFTP, etc.
- File transfer can be done in different modes, such as binary, ASCII, or auto.
- File transfer can be done using different tools, such as command-line utilities, graphical user interfaces, or web browsers.
- File transfer can be done for different purposes, such as backup, synchronization, sharing, or distribution.

- In this experiment, you will learn how to perform file transfer using FTP and SCP protocols.
- You will need two devices, one as a server and one as a client, connected to the same network or the internet.
- You will also need an FTP server software and an SCP client software installed on the respective devices.
- You will follow these steps to perform file transfer using FTP and SCP protocols:

  - FTP protocol:
    - On the server device, start the FTP server software and configure the username, password, and directory for file transfer.
    - On the client device, start the FTP client software and connect to the server using the username and password.
    - On the client device, use the FTP commands to list, upload, download, or delete files on the server.
    - On the server device, use the FTP server software to monitor the file transfer activity and logs.
    - On the client device, use the FTP commands to disconnect from the server and exit the FTP client software.
    - On the server device, stop the FTP server software.

  - SCP protocol:
    - On the server device, start the SCP server software and configure the username, password, and directory for file transfer.
    - On the client device, start the SCP client software and connect to the server using the username and password.
    - On the client device, use the SCP commands to upload or download files to or from the server.
    - On the server device, use the SCP server software to monitor the file transfer activity and logs.
    - On the client device, use the SCP commands to disconnect from the server and exit the SCP client software.
    - On the server device, stop the SCP server software.



# Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

## Aim
To study the basic concepts and features of network simulator (NS) and to simulate the congestion control algorithms using NS.

## Theory
- Network simulator (NS) is a name for a series of discrete event network simulators, specifically ns-1, ns-2, and ns-3. All are discrete-event computer network simulators, primarily used in research and teaching.
- NS simulates the behavior of networks and protocols by using a scripting language called Tcl (Tool Command Language). NS can simulate various types of networks, such as wired, wireless, satellite, and mobile networks.
- NS can also simulate various network components, such as nodes, links, queues, routers, applications, and transport protocols. NS provides a modular and extensible architecture that allows users to create and modify network models.
- Congestion control algorithms are mechanisms that aim to regulate the traffic flow in a network and prevent congestion. Congestion occurs when the network resources, such as bandwidth or buffer space, are insufficient to meet the demand of the traffic.
- Congestion control algorithms can be classified into two categories: end-to-end and network-assisted. End-to-end algorithms rely on the feedback from the receivers or the network to adjust the sending rate of the sources. Network-assisted algorithms involve the cooperation of the network devices, such as routers, to signal the sources about the network conditions.
- Some examples of congestion control algorithms are: TCP, which uses end-to-end feedback based on packet loss and round-trip time; RED (Random Early Detection), which uses network-assisted feedback based on queue length; and ECN (Explicit Congestion Notification), which uses network-assisted feedback based on packet marking.

## Procedure
- To install NS on a Linux system, follow the steps given in the official website or use the package manager of your distribution.
- To run a simulation using NS, create a Tcl script that defines the network topology, the traffic sources, the simulation parameters, and the output files.
- To execute the script, use the command `ns <script_name>.tcl` in the terminal.
- To analyze the results of the simulation, use tools such as NAM (Network Animator), Xgraph, or Gnuplot to visualize the network behavior and the performance metrics.
- To simulate the congestion control algorithms using NS, refer to the examples given in the NS documentation or the online tutorials. Modify the script according to your requirements and observe the effects of different parameters and scenarios on the network performance.



## Experiment 11 - Perform a case study about the different routing algorithms to select the network path with its optimum and economical during data transfer

- Routing algorithms are the methods that routers use to determine the best path for sending packets in a network.
- Routing algorithms can be classified into two main categories: adaptive and non-adaptive.
- Adaptive algorithms change their routing decisions based on the current network status, such as topology, traffic load, link failures, etc. They can adapt to dynamic network conditions and improve the performance and reliability of data transfer. However, they also incur more overhead and complexity than non-adaptive algorithms.
- Non-adaptive algorithms do not change their routing decisions once they are initialized. They are based on a fixed network topology and do not consider the current network status. They are simpler and faster than adaptive algorithms, but they may not be able to cope with network changes and may result in suboptimal or inefficient data transfer.
- Some examples of adaptive algorithms are distance vector, link state, and multipath routing. Some examples of non-adaptive algorithms are shortest path, flooding, and random walk routing.
- A case study of the evolution of routing algorithms in a network planning tool is presented in   . The authors used Dijkstra's algorithm, a shortest path algorithm, to solve different routing problems encountered in transmission network planning. They modified the basic algorithm to incorporate various factors, such as link capacity, link cost, link reliability, traffic demand, etc. They showed that the modified algorithm was useful and practical in solving real-life problems, and that it could handle different network scenarios, such as single-path, multi-path, and multi-layer routing. They also compared the performance of their algorithm with other routing algorithms, such as minimum spanning tree, maximum flow, and genetic algorithm, and found that their algorithm was superior in terms of speed, accuracy, and robustness.



# Experiment 11.1 - Link State Routing

- Link state routing is a type of routing algorithm that uses the information about the state of each link (such as bandwidth, delay, cost, etc.) to calculate the shortest path from one node to every other node in the network.
- Link state routing is also known as Dijkstra's algorithm, which is an iterative algorithm that finds the least cost path for a given destination node after each iteration.
- Link state routing requires each node to construct a map of the network topology, in the form of a graph, by exchanging messages with other nodes. Each node then independently computes the best next hop for each destination using the graph.
- Link state routing protocols are one of the two main classes of routing protocols used in packet switching networks, the other being distance-vector routing protocols. Examples of link state routing protocols include Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).
- Link state routing has some advantages over distance-vector routing, such as faster convergence, lower bandwidth consumption, and more accurate routing decisions. However, link state routing also has some disadvantages, such as higher memory and CPU requirements, more complex configuration, and vulnerability to flooding attacks.



### Experiment 11.2 - Flooding

- Flooding is a natural phenomenon that occurs when a large amount of water overflows onto land that is normally dry.
- Flooding can be caused by various factors, such as heavy rainfall, snowmelt, storm surges, dam failures, or river overflow.
- Flooding can have positive and negative impacts on the environment, society, and economy.
- Positive impacts of flooding include:
  - Replenishing soil nutrients and groundwater resources.
  - Creating habitats for aquatic and wetland species.
  - Providing opportunities for recreation and tourism.
- Negative impacts of flooding include:
  - Damaging infrastructure, property, and crops.
  - Displacing people and animals.
  - Spreading diseases and pollutants.
  - Increasing the risk of landslides and erosion.
- To measure the extent and severity of flooding, some indicators are used, such as:
  - Flood frequency: how often a flood of a given magnitude occurs in a given area.
  - Flood duration: how long a flood lasts in a given area.
  - Flood depth: how high the water level rises above the normal level in a given area.
  - Flood area: how much land is covered by water in a given area.
- To reduce the negative impacts of flooding, some strategies are used, such as:
  - Structural measures: building dams, levees, reservoirs, or drainage systems to control the flow of water.
  - Non-structural measures: implementing land use planning, flood forecasting, flood insurance, or public education to increase the awareness and preparedness of people.
  - Ecological measures: restoring natural wetlands, forests, or grasslands to enhance the water retention and infiltration capacity of the land.



# Experiment 11.3 - Distance vector

- Distance vector is a routing protocol that calculates the best route for a packet based on the distance and direction to the destination.
- Distance vector routers exchange information about their routing tables with their neighbors periodically or when there is a change in the network topology.
- Distance vector routers use the Bellman-Ford algorithm to update their routing tables and find the shortest path to the destination.
- Distance vector routers have the following characteristics:
  - They only know the distance and direction to the destination, not the entire path.
  - They use hop count as the metric to measure the distance to the destination.
  - They are prone to routing loops, count-to-infinity problems, and slow convergence.
  - They use split horizon, poison reverse, and triggered updates to prevent or mitigate these problems.
  - They are simple, easy to implement, and suitable for small networks with low traffic and stable topology.
- Distance vector routers perform the following steps to update their routing tables:
  1. Initialize the routing table with the directly connected networks and assign a hop count of zero to them.
  2. Send the routing table to all the neighboring routers and receive their routing tables.
  3. For each destination in the received routing table, compare the hop count with the existing hop count in the local routing table.
  4. If the received hop count is smaller than the existing hop count, update the local routing table with the new hop count and the next hop router.
  5. If the received hop count is equal to the existing hop count, check if the next hop router is different. If yes, add the alternative route to the local routing table.
  6. If the received hop count is larger than the existing hop count, ignore the update.
  7. Repeat steps 2 to 6 until no more updates are received or the routing table stabilizes.



# Experiment 12 - To learn handling and configuration of networking hardware like RJ-45 connector, CAT-6 cable, crimping tool, etc

## Objective
- To understand the basic components and functions of a wired network.
- To learn how to make a network cable using RJ-45 connectors, CAT-6 cable, and a crimping tool.
- To test the network cable for connectivity and performance.

## Theory
- A wired network is a network that uses cables to connect devices such as computers, routers, switches, and printers.
- A network cable is a cable that carries data signals between devices on a network.
- A network cable consists of a core of twisted pairs of wires, a protective jacket, and connectors at both ends.
- The most common type of network cable is the Ethernet cable, which follows the standards of the Institute of Electrical and Electronics Engineers (IEEE).
- The Ethernet cable can be classified into different categories based on the speed and bandwidth it can support, such as CAT-5, CAT-5e, CAT-6, CAT-6a, etc.
- The CAT-6 cable is a type of Ethernet cable that can support up to 10 gigabits per second (Gbps) of data transfer and a bandwidth of up to 250 megahertz (MHz).
- The CAT-6 cable has four pairs of twisted wires, each with a different color code: orange, green, blue, and brown.
- The RJ-45 connector is a type of connector that is used to terminate the Ethernet cable and connect it to a device.
- The RJ-45 connector has eight pins that correspond to the eight wires in the Ethernet cable.
- The RJ-45 connector can be attached to the Ethernet cable using a crimping tool, which is a device that applies pressure to the connector and the cable to create a secure connection.
- The crimping tool can also cut and strip the cable to expose the wires and align them with the pins of the connector.
- The crimping tool can be used for different types of connectors, such as RJ-11, RJ-12, and RJ-45, depending on the size and shape of the connector.
- The crimping tool can also be used for different types of cables, such as CAT-5, CAT-5e, CAT-6, etc, depending on the diameter and thickness of the cable.
- The network cable can be tested for connectivity and performance using a network cable tester, which is a device that sends and receives signals through the cable and displays the results on a screen or a LED indicator.
- The network cable tester can detect if the cable is properly terminated, if the wires are correctly aligned, if the cable is damaged or broken, and if the cable can support the desired speed and bandwidth.

## Procedure
- To make a network cable using RJ-45 connectors, CAT-6 cable, and a crimping tool, follow these steps:
  - Step 1: Cut a length of CAT-6 cable using the crimping tool or a wire cutter.
  - Step 2: Strip about 2 cm of the jacket from both ends of the cable using the crimping tool or a wire stripper.
  - Step 3: Untwist the pairs of wires and arrange them according to the color code and the wiring scheme. There are two common wiring schemes for RJ-45 connectors: T568A and T568B. The wiring scheme determines the order of the wires in the connector and affects the compatibility of the cable with different devices. The T568A wiring scheme follows this order: green-white, green, orange-white, blue, blue-white, orange, brown-white, brown. The T568B wiring scheme follows this order: orange-white, orange, green-white, blue, blue-white, green, brown-white, brown. Choose one wiring scheme and use it for both ends of the cable.
  - Step 4: Flatten the wires and trim them to the same length using the crimping tool or a wire cutter. The wires should be about 1.3 cm long from the edge of the jacket.
  - Step 5: Insert the wires into the RJ-45 connector, making sure that they are aligned with the pins and that the jacket is inside the connector. The connector should have a clip on the top and a slot on the bottom. The wires should enter the connector from the bottom and face the clip.
  - Step 6: Place the connector with the cable into the crimping tool, making sure that the connector is in the right position and that the cable is



## Experiment 13 - Configuration of router, hub, switch etc. (using real devices or simulators)

- A router is a device that routes data packets based on their IP addresses. It can connect different networks, such as LANs and WANs, and perform functions such as assigning IP addresses, acting as a switch, and protecting the network .
- A hub is a device that connects multiple computers to create a LAN. It broadcasts all the data it receives to all the connected devices, regardless of the destination.
- A switch is a device that also connects multiple computers to create a LAN, but unlike a hub, it knows which device the information is intended for and sends it there. This reduces network congestion and improves security.
- To configure a router, you need to enter the Router Configuration mode, using the `configure terminal` command on Cisco devices, and then the Interface Configuration mode, using the `interface <interface name>` command. You can then set various parameters for the interface, such as IP address, subnet mask, speed, duplex mode, etc. You can also configure routing protocols, such as RIP, OSPF, EIGRP, etc., to enable the router to exchange routing information with other routers.
- To configure a switch, you need to enter the Switch Configuration mode, using the `configure terminal` command on Cisco devices, and then the Interface Configuration mode, using the `interface <interface name>` command. You can then set various parameters for the interface, such as speed, duplex mode, VLAN membership, port security, etc. You can also configure spanning tree protocol, trunking, etherchannel, etc., to optimize the performance and reliability of the switch.
- To configure a hub, you do not need to do anything, as it is a plug-and-play device that does not have any configuration options.
- To practice the configuration of router and switch, you can use a simulator or an emulator. A simulator is a software that mimics the behavior of a device, but does not run the actual IOS (the operating system of Cisco devices). A simulator may have missing commands and programming errors, and it can never be as complete as the real IOS. An emulator is a software that runs the actual IOS image, and can provide a more realistic and accurate experience. However, an emulator may require more resources and licenses to run. Some examples of simulators are Packet Tracer, Boson NetSim, GNS3, etc. Some examples of emulators are Dynamips, Cisco VIRL, EVE-NG, etc.



## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

- The objective of this experiment is to learn how to use some common network utilities for troubleshooting and information gathering.
- The network utilities are programs that run on a host computer and interact with the network or other hosts.
- Some of the network utilities that will be covered in this experiment are:

  - **ping**: A program that sends a packet to a destination IP address and waits for a reply. It is used to test the connectivity and latency between two hosts. The ping command can also display statistics such as packet loss, round-trip time, and time to live (TTL)  .
  - **traceroute**: A program that traces the path of a packet from the source to the destination. It shows the IP addresses and hostnames of the routers that the packet passes through. It is used to diagnose routing problems and network congestion. The traceroute command can also display the time it takes for each hop  .
  - **nslookup**: A program that queries the Domain Name System (DNS) to obtain information about a domain name or an IP address. It is used to verify the DNS configuration and resolve domain names to IP addresses or vice versa. The nslookup command can also display other DNS records such as MX, NS, SOA, etc  .
  - **arp**: A program that displays or modifies the Address Resolution Protocol (ARP) cache. The ARP cache is a table that maps IP addresses to MAC addresses on the local network. It is used to find the MAC address of a host with a known IP address or vice versa. The arp command can also add or delete entries from the ARP cache  .
  - **telnet**: A program that establishes a remote connection to another host using the Telnet protocol. It is used to access and control a host that runs a Telnet server. The telnet command can also send commands and receive output from the remote host  .
  - **ftp**: A program that transfers files between two hosts using the File Transfer Protocol (FTP). It is used to upload and download files from a host that runs an FTP server. The ftp command can also list, create, delete, and rename files and directories on the remote host  .

- To run these network utilities, you need to open a command prompt or a terminal window on your host computer and type the name of the utility followed by the parameters or options. For example, to ping the IP address 8.8.8.8, you would type:

  ```
  ping 8.8.8.8
  ```

- To see the available parameters or options for each utility, you can type the name of the utility followed by a question mark (?) or a slash and a question mark (/?) on Windows, or a hyphen and a letter h (-h) on Linux or Mac OS X. For example, to see the options for the traceroute command on Linux, you would type:

  ```
  traceroute -h
  ```

- To exit from a network utility, you can type Ctrl+C on Windows or Linux, or Ctrl+D on Mac OS X. For some utilities, such as telnet and ftp, you can also type quit or bye to end the session.



## Experiment 15 - Network packet analysis using tools like Wireshark, tcpdump, etc

- Network packet analysis is the process of capturing, inspecting, and interpreting the data packets that are exchanged between devices on a network.
- Network packet analysis tools are software applications that can perform packet capture and analysis functions, such as filtering, decoding, reassembling, and displaying the packet data.
- Network packet analysis tools can be used for various purposes, such as network troubleshooting, performance monitoring, security auditing, and forensics.
- Some of the common network packet analysis tools are:

  - Wireshark: A free and open-source tool that can capture and analyze packets on various network protocols and interfaces. It has a graphical user interface (GUI) that allows users to view the packet details, statistics, and graphs. It also supports plugins and extensions for additional functionality.
  - tcpdump: A command-line tool that can capture and display packets on various network protocols and interfaces. It can also filter packets based on expressions and save them to files for later analysis. It is widely available on Unix-like systems and can be used with other tools, such as Wireshark.
  - Colasoft Capsa: A commercial tool that can capture and analyze packets on both wired and wireless networks. It has a GUI that allows users to view the packet details, statistics, and graphs. It also supports network diagnosis, alerting, and reporting features.
  - Paessler PRTG: A commercial tool that can capture and analyze packets on various network protocols and interfaces. It has a web-based interface that allows users to view the packet details, statistics, and graphs. It also supports network monitoring, alerting, and reporting features.
  - Arkime: A free and open-source tool that can capture and analyze packets on various network protocols and interfaces. It has a web-based interface that allows users to view the packet details, statistics, and graphs. It also supports network security, alerting, and reporting features.

- To perform network packet analysis using these tools, the following steps are typically involved:

  - Select a network interface or device to capture packets from, such as Ethernet, Wi-Fi, or USB.
  - Optionally, apply a filter or expression to capture only the packets of interest, such as by protocol, port, address, or content.
  - Start the packet capture and wait for the packets to be collected.
  - Stop the packet capture and save the packets to a file or database for later analysis.
  - Analyze the packets using the tool's features, such as decoding, reassembling, searching, filtering, sorting, and exporting the packet data.
  - Optionally, generate reports or graphs based on the packet analysis results, such as by throughput, latency, errors, or anomalies.



## Experiment 16 - Network simulation using tools like Cisco Packet Tracer, NetSim, OMNeT++, NS2, NS3, etc

- Network simulation is the process of modeling the behavior and performance of a network using software tools.
- Network simulation tools can help students, researchers, and professionals to learn, design, test, and troubleshoot networks without using physical hardware.
- Network simulation tools can support various types of networks, such as wired, wireless, mobile, sensor, software-defined, hybrid, etc.
- Network simulation tools can vary in their features, capabilities, complexity, and licensing. Some of the most popular network simulation tools are:

  - Cisco Packet Tracer: A network simulation and visualization tool developed by Cisco for its Networking Academy courses. It allows users to create, configure, and troubleshoot network scenarios using Cisco devices and protocols. It also supports IoT and cybersecurity features. It is free to download for students and instructors enrolled in Cisco courses.
  - NetSim: A network simulation and emulation tool developed by Tetcos. It supports a wide range of network technologies, such as LAN, WAN, MANET, LTE, Wi-Fi, WiMAX, ZigBee, etc. It also supports network design, protocol analysis, and performance evaluation. It is a licensed software with a free trial version available.
  - OMNeT++: An open-source, modular, and component-based network simulation framework. It allows users to create and customize network models using C++ and a graphical user interface. It supports various network domains, such as wireless, optical, sensor, vehicular, etc. It also supports parallel and distributed simulation.
  - NS2: An open-source, discrete-event network simulator. It is widely used for academic research and education. It supports various network protocols, such as TCP, UDP, IP, MPLS, etc. It also supports wireless and mobile networks, such as ad hoc, sensor, cellular, etc. It uses two languages: C++ for the core simulation engine and OTcl for the network configuration .
  - NS3: An open-source, discrete-event network simulator. It is a successor of NS2 with improved features and performance. It supports various network technologies, such as Wi-Fi, WiMAX, LTE, 5G, etc. It also supports software-defined networks, hybrid networks, and network emulation. It uses C++ and Python as the main programming languages .



# Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

## Introduction

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A socket is an endpoint of a communication channel that can send and receive data using a protocol.
- There are two main types of sockets: stream sockets and datagram sockets.
- Stream sockets use TCP (Transmission Control Protocol) as the transport layer protocol, which provides reliable, ordered and error-free data delivery .
- Datagram sockets use UDP (User Datagram Protocol) as the transport layer protocol, which provides fast, connectionless and unreliable data delivery .
- TCP sockets are suited for applications that require high reliability and transmission time is less critical, such as web browsing, file transfer, email, etc.
- UDP sockets are suited for applications that require low latency and transmission time is more critical, such as video streaming, online gaming, voice over IP, etc.

## Objectives

- To learn how to create and use TCP and UDP sockets in Python.
- To implement simple client-server applications using TCP and UDP sockets, such as:
  - Simple DNS: A client sends a domain name to a server and the server replies with the corresponding IP address.
  - Data & time client/server: A client requests the current date and time from a server and the server replies with the requested information.
  - Echo client/server: A client sends a message to a server and the server echoes back the same message to the client.
  - Iterative & concurrent servers: A server can handle multiple client requests either sequentially (iterative) or simultaneously (concurrent) using different techniques, such as threading, multiprocessing, select, etc.

## Procedure

- To create a TCP socket in Python, use the following code:

```python
import socket
# Create a TCP socket object
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- To create a UDP socket in Python, use the following code:

```python
import socket
# Create a UDP socket object
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

- To bind a socket to a port and listen for incoming connections, use the following code:

```python
# Bind the socket to a port
tcp_socket.bind((host, port))
# Listen for incoming connections
tcp_socket.listen()
```

- To accept a connection from a client and create a new socket for communication, use the following code:

```python
# Accept a connection from a client
client_socket, client_address = tcp_socket.accept()
```

- To connect to a server using a socket, use the following code:

```python
# Connect to a server
tcp_socket.connect((host, port))
```

- To send and receive data using a TCP socket, use the following code:

```python
# Send data to the server
tcp_socket.send(data.encode())
# Receive data from the server
data = tcp_socket.recv(buffer_size).decode()
```

- To send and receive data using a UDP socket, use the following code:

```python
# Send data to the server
udp_socket.sendto(data.encode(), (host, port))
# Receive data from the server
data, server_address = udp_socket.recvfrom(buffer_size).decode()
```

- To close a socket, use the following code:

```python
# Close the socket
tcp_socket.close()
```

- To implement the simple client-server applications using TCP and UDP sockets, follow the steps below:

  - Simple DNS:
    - Create a TCP or UDP socket for the client and the server.
    - The client sends a domain name to the server using the socket.
    - The server receives the domain name and performs a DNS lookup using the socket module's gethostbyname function.
    - The server sends the IP address of the domain name back to the client using the socket.
    - The client receives the IP address and prints it.
    - The client and the server close the socket.

  - Data & time client/server:
    - Create a TCP or UDP socket for the client and the server.
    - The client sends a request to the server using the socket.
    - The server

