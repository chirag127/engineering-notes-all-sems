

## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

### Objective
- To understand the basic concepts of flow control and error control in data link layer.
- To implement and compare the performance of stop and wait protocol and sliding window protocol.

### Theory
- Flow control is a mechanism that regulates the amount of data that can be sent by the sender to the receiver, to avoid congestion and buffer overflow.
- Error control is a mechanism that detects and corrects the errors that may occur during data transmission, such as bit errors, frame loss, or duplication.
- Stop and wait protocol is a simple flow control and error control protocol that uses a single buffer at both sender and receiver. The sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. The receiver sends an acknowledgment after receiving and processing the frame. The sender and receiver use alternating sequence numbers (0 and 1) to distinguish between different frames and acknowledgments.
- Sliding window protocol is an advanced flow control and error control protocol that uses multiple buffers at both sender and receiver. The sender can send multiple frames without waiting for acknowledgments, as long as the number of unacknowledged frames does not exceed the window size. The receiver can receive and process multiple frames out of order, as long as the number of frames in the buffer does not exceed the window size. The sender and receiver use a range of sequence numbers to identify different frames and acknowledgments.

### Procedure
- To implement the stop and wait protocol, follow these steps:
  - Initialize the sender and receiver buffers with sequence number 0.
  - Generate a random frame and send it to the receiver with sequence number 0.
  - Start a timer and wait for an acknowledgment from the receiver with sequence number 0.
  - If the acknowledgment is received before the timer expires, stop the timer and update the sender buffer with sequence number 1. Go to step 2.
  - If the acknowledgment is not received before the timer expires, resend the frame with sequence number 0. Go to step 3.
  - Repeat steps 2 to 5 until all frames are sent and acknowledged.
  - Initialize the receiver buffer with sequence number 0.
  - Receive a frame from the sender with sequence number 0.
  - Check for errors in the frame. If the frame is error-free, process the frame and send an acknowledgment to the sender with sequence number 0. Update the receiver buffer with sequence number 1. Go to step 9.
  - If the frame is corrupted or lost, discard the frame and do not send any acknowledgment. Go to step 8.
  - Receive a frame from the sender with sequence number 1.
  - Check for errors in the frame. If the frame is error-free, process the frame and send an acknowledgment to the sender with sequence number 1. Update the receiver buffer with sequence number 0. Go to step 8.
  - If the frame is corrupted or lost, discard the frame and do not send any acknowledgment. Go to step 10.
  - Repeat steps 8 to 11 until all frames are received and processed.
- To implement the sliding window protocol, follow these steps:
  - Initialize the sender and receiver buffers with sequence numbers 0 to N-1, where N is the window size.
  - Generate a random frame and send it to the receiver with the next available sequence number in the sender buffer.
  - Start a timer for the frame and update the sender buffer by removing the sequence number of the frame.
  - Repeat steps 2 and 3 until the sender buffer is empty or the window size is reached.
  - Wait for an acknowledgment from the receiver with the sequence number of the oldest frame in the window.
  - If the acknowledgment is received before the timer expires, stop the timer and update the sender buffer by adding the sequence number of the acknowledgment. Go to step 2.
  - If the acknowledgment is not received before the timer expires, resend the frame with the sequence number of the oldest frame in the window. Go to step 5.
  - Repeat steps 2 to 7 until all frames are sent and acknowledged.
  - Initialize the receiver buffer with sequence numbers 0 to N-1, where N is the window size.
  - Receive a frame from the sender with a sequence number within the range of the receiver buffer.
  - Check for errors in the frame. If the frame is error-free, process the frame and send an acknowledgment to the sender with the sequence number of the frame. Update the receiver buffer by removing the sequence number



### Experiment 1.1 - Implementation of Stop and Wait Protocol

The stop and wait protocol is a flow control protocol that ensures reliable data transmission over a noisy channel. It works as follows:

- The sender sends one data packet at a time and waits for an acknowledgment from the receiver before sending the next packet.
- The receiver sends an acknowledgment after receiving a data packet without any error. If the packet is corrupted or lost, the receiver does not send any acknowledgment.
- The sender uses a timer to detect the timeout of an acknowledgment. If the timer expires, the sender assumes that the packet or the acknowledgment was lost and retransmits the same packet.
- The sender and the receiver use sequence numbers to distinguish between new and retransmitted packets. The sequence numbers alternate between 0 and 1.

The following diagram shows the implementation of the stop and wait protocol:

stop and wait protocol diagram

The following are the steps to perform the experiment:

- Set up a network simulator such as NS2 or OPNET to create a sender node, a receiver node, and a channel with some error rate and propagation delay.
- Write a program for the sender node that implements the stop and wait protocol. The program should send data packets with sequence numbers and wait for acknowledgments with timers. The program should also handle timeout and retransmission events.
- Write a program for the receiver node that implements the stop and wait protocol. The program should receive data packets and check for errors. The program should also send acknowledgments with sequence numbers and discard duplicate packets.
- Run the simulation and observe the data transmission and reception. Measure the throughput, efficiency, and delay of the protocol. Compare the results with the theoretical values. Analyze the effect of error rate and propagation delay on the performance of the protocol.



### Experiment 1.2 - Implementation of Sliding Window Protocol

The sliding window protocol is a feature of packet-based data transmission protocols that ensures reliable and sequential delivery of data frames. The protocol uses a window size that determines how many frames can be sent by the sender before receiving an acknowledgment from the receiver. The window slides along the sequence of frames as the sender and receiver exchange data and acknowledgments.

The sliding window protocol can be implemented in different ways, such as:

- Stop-and-wait: The simplest sliding window protocol, where the sender sends one frame at a time and waits for an acknowledgment before sending the next frame. The window size is one for both the sender and the receiver.
- Go-back-N: The sender can send up to N frames at a time, where N is the window size, but the receiver can only acknowledge the last correctly received frame. If the receiver detects an error in a frame, it discards that frame and all the subsequent frames until it receives the correct frame. The sender then retransmits all the frames from the last acknowledged frame.
- Selective repeat: The sender can send up to N frames at a time, where N is the window size, and the receiver can acknowledge any correctly received frame. The receiver also buffers the out-of-order frames until the missing frames are received. The sender only retransmits the frames that are not acknowledged within a certain time limit.

To implement the sliding window protocol, the following steps are required:

- Define the data frame structure, which should include a sequence number, a data field, and an error detection code (such as checksum or CRC).
- Define the window size for the sender and the receiver, which should be less than or equal to the maximum sequence number.
- Define the timeout value for the sender, which should be longer than the maximum round-trip time between the sender and the receiver.
- Implement the sender logic, which should include the following functions:
  - Send a frame with the next sequence number and start a timer.
  - Wait for an acknowledgment or a timeout event.
  - If an acknowledgment is received, slide the window forward and send the next frame if the window is not empty.
  - If a timeout occurs, retransmit the frame and restart the timer.
- Implement the receiver logic, which should include the following functions:
  - Receive a frame and check for errors using the error detection code.
  - If the frame is error-free and has the expected sequence number, send an acknowledgment and deliver the data to the upper layer.
  - If the frame is error-free but has an unexpected sequence number, send an acknowledgment with the expected sequence number and discard the frame (or buffer it for selective repeat).
  - If the frame has an error, discard it and do not send an acknowledgment (or send a negative acknowledgment for selective repeat).

The following diagram illustrates the sliding window protocol with a window size of 4 for both the sender and the receiver, using the go-back-N method.

Sliding window protocol diagram

: Sliding window protocol - Wikipedia
: Sliding Window Protocol - tutorialspoint.com
: What is the sliding window technique and how does it work?
: Sliding Window Protocol | Set 1 (Sender Side) - GeeksforGeeks



## Experiment 2 - Study of Socket Programming and Client – Server model

- Socket programming is a way of enabling two programs to communicate over a network using a well-established protocol.
- A socket is a simple communication channel that supports two-way communication between a client and a server.
- A client is a program that requests a service or resource from a server.
- A server is a program that provides a service or resource to a client.
- The client and the server must follow the same protocol to establish a connection and exchange data.
- A protocol is a set of rules and behavior that both the client and the server must follow in order to communicate.
- There are two types of sockets: stream sockets and datagram sockets.
- Stream sockets, also known as connection-oriented sockets, establish a connection before transferring data.
- Stream sockets are reliable and in-order, meaning that the data is guaranteed to arrive at the destination without errors or duplication, and in the same order as it was sent.
- Stream sockets use Transmission Control Protocol (TCP) as the underlying protocol.
- Datagram sockets, also known as connectionless sockets, do not establish a connection before transferring data.
- Datagram sockets are unreliable and out-of-order, meaning that the data may be lost, corrupted, duplicated, or arrive in a different order than it was sent.
- Datagram sockets use User Datagram Protocol (UDP) as the underlying protocol.
- A socket has a typical flow of events in the client-server model:
  - The server creates a socket and binds it to an address that clients can use to find the server.
  - The server listens for incoming connection requests from clients on the socket.
  - The client creates a socket and connects it to the server's address.
  - The server accepts the connection request from the client and creates a new socket for the communication.
  - The client and the server exchange data using read and write operations on the sockets.
  - The client and the server close the sockets when the communication is over.
- Socket programming can be done in various programming languages, such as C, C++, Python, Java, etc .
- Socket programming can be used for various applications, such as web browsing, email, file transfer, chat, etc .



### Experiment 2.1 - Study of Socket Programming

- Socket programming is a way of enabling communication between different processes or machines using network protocols.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol, such as TCP or UDP.
- Socket programming involves creating, configuring, connecting, sending and receiving data through sockets using a programming language, such as C, Python, or Java.
- Socket programming can be used for various applications, such as web servers, chat applications, file transfer, remote control, etc.
- Socket programming can be classified into two types: stream sockets and datagram sockets.
  - Stream sockets use TCP as the transport protocol and provide reliable, ordered, and error-free data transmission. Stream sockets are suitable for applications that require a continuous flow of data, such as web browsing, email, etc.
  - Datagram sockets use UDP as the transport protocol and provide fast, unordered, and unreliable data transmission. Datagram sockets are suitable for applications that require low latency, such as video streaming, online gaming, etc.
- Socket programming can be done using different APIs, such as BSD sockets, Winsock, Java sockets, etc. Each API provides a set of functions or methods to create, manipulate, and use sockets.
- Socket programming can be done using different models, such as blocking, non-blocking, multiplexing, asynchronous, etc. Each model defines how the program handles the input and output operations on sockets.
  - Blocking model: The program waits for the socket operation to complete before proceeding to the next statement. This model is simple but inefficient, as the program cannot perform other tasks while waiting for the socket operation.
  - Non-blocking model: The program does not wait for the socket operation to complete and proceeds to the next statement. This model is efficient but complex, as the program has to check the status of the socket operation and handle errors or exceptions.
  - Multiplexing model: The program uses a single thread or process to monitor multiple sockets and perform the appropriate socket operation when an event occurs. This model is efficient and scalable, as the program can handle multiple sockets without creating multiple threads or processes.
  - Asynchronous model: The program registers a callback function or handler to be executed when a socket operation is completed. This model is efficient and simple, as the program does not have to wait or check the status of the socket operation.



### Experiment 2.2 - Study of Client – Server model

#### Objective
To understand the basic concepts and functions of the client-server model in network computing.

#### Theory
- The client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.
- Often clients and servers communicate over a computer network on separate hardware, but both client and server may reside in the same system.
- A server is a powerful computer that provides one or more services to other computers or devices on a network.
- A client is a computer or device that requests and receives services or resources from a server.
- The client-server connection is established through a network or the Internet.
- The client initiates a request to the server, and the server responds with the desired service or resource.
- The client and server can communicate using various protocols, such as HTTP, FTP, SMTP, etc.
- The client-server model has many advantages, such as:
  - Centralized system with all data in a single place.
  - Cost efficient, requires less maintenance cost and data recovery is possible.
  - The capacity of the client and server can be changed separately.
  - Scalable and flexible, can accommodate more clients and servers as needed.
  - Secure and reliable, can implement authentication and encryption mechanisms.

#### Procedure
- To study the client-server model, you will need a network of computers or devices that can act as clients and servers.
- You will also need a software application that can implement the client-server communication using a specific protocol.
- For example, you can use a web browser as a client and a web server as a server, and use HTTP as the protocol.
- To set up the web server, you will need to install and configure a software such as Apache, Nginx, or IIS on a computer that has a static IP address or a domain name.
- To set up the web browser, you will need to install and configure a software such as Chrome, Firefox, or Edge on another computer or device that can access the network or the Internet.
- To test the client-server communication, you will need to create and host some web pages on the web server, and access them from the web browser using the web server's IP address or domain name.
- You can use a tool such as Wireshark to capture and analyze the network packets exchanged between the client and the server, and observe the structure and content of the HTTP request and response messages.



## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is a network protocol that maps an IP address to a MAC address of a device on the same network.
- RARP stands for Reverse Address Resolution Protocol. It is a network protocol that maps a MAC address to an IP address of a device on the same network.
- Both ARP and RARP use broadcast messages to request and reply the address mappings.
- The following is a pseudocode that simulates the basic functions of ARP and RARP protocols.

```
# Define a class for a device on the network
class Device:
  # Initialize the device with an IP address and a MAC address
  def __init__(self, ip, mac):
    self.ip = ip
    self.mac = mac
    self.arp_table = {} # A dictionary to store the ARP cache
    self.rarp_table = {} # A dictionary to store the RARP cache

  # Define a method to send an ARP request to the network
  def arp_request(self, target_ip):
    # Broadcast a message to the network with the target IP address and the sender's IP and MAC addresses
    broadcast_message = "ARP request: Who has " + target_ip + "? Tell " + self.ip + " (" + self.mac + ")"
    print(self.ip + " (" + self.mac + ") sends " + broadcast_message)

    # Return the broadcast message
    return broadcast_message

  # Define a method to receive an ARP request from another device
  def arp_receive(self, message):
    # Parse the message to get the target IP address and the sender's IP and MAC addresses
    message_parts = message.split()
    target_ip = message_parts[2]
    sender_ip = message_parts[5]
    sender_mac = message_parts[6]

    # Check if the target IP address matches the device's IP address
    if target_ip == self.ip:
      # Send an ARP reply to the sender with the device's IP and MAC addresses
      self.arp_reply(sender_ip, sender_mac)
    else:
      # Update the ARP cache with the sender's IP and MAC addresses
      self.arp_table[sender_ip] = sender_mac
      print(self.ip + " (" + self.mac + ") updates its ARP cache with " + sender_ip + " (" + sender_mac + ")")

  # Define a method to send an ARP reply to another device
  def arp_reply(self, target_ip, target_mac):
    # Send a message to the target device with the device's IP and MAC addresses and the target's IP and MAC addresses
    message = "ARP reply: " + self.ip + " is at " + self.mac + " for " + target_ip + " (" + target_mac + ")"
    print(self.ip + " (" + self.mac + ") sends " + message)

    # Return the message
    return message

  # Define a method to receive an ARP reply from another device
  def arp_receive_reply(self, message):
    # Parse the message to get the sender's IP and MAC addresses and the target's IP and MAC addresses
    message_parts = message.split()
    sender_ip = message_parts[1]
    sender_mac = message_parts[4]
    target_ip = message_parts[6]
    target_mac = message_parts[7]

    # Check if the target IP address matches the device's IP address
    if target_ip == self.ip:
      # Update the ARP cache with the sender's IP and MAC addresses
      self.arp_table[sender_ip] = sender_mac
      print(self.ip + " (" + self.mac + ") updates its ARP cache with " + sender_ip + " (" + sender_mac + ")")
    else:
      # Ignore the message
      print(self.ip + " (" + self.mac + ") ignores the message")

  # Define a method to send a RARP request to the network
  def rarp_request(self, target_mac):
    # Broadcast a message to the network with the target MAC address and the sender's IP and MAC addresses
    broadcast_message = "RARP request: Who has " + target_mac + "? Tell " + self.ip + " (" + self.mac + ")"
    print(self.ip + " (" + self.mac + ") sends " + broadcast_message)

    # Return the broadcast message
    return broadcast_message

  # Define a method to receive a RARP request from another device
  def rarp_receive(self, message):
    # Parse the message to get the target MAC address and the sender's IP and MAC addresses
    message_parts = message.split()
    target_mac = message_parts[2]
    sender_ip = message_parts[5

```




## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- PING and TRACEROUTE are common commands you can use to troubleshoot network problems .
- PING is a simple command that can test the reachability of a device on the network by sending and receiving ICMP packets   .
- TRACEROUTE is a command you use to 'trace' the route that a packet takes when traveling to its destination by sending and receiving ICMP packets with varying TTL values  .
- The code for simulating PING and TRACEROUTE commands can be written in Python using the socket and struct modules.
- The code should perform the following steps:
  - Import the socket and struct modules
  - Define a function to calculate the checksum of an ICMP packet
  - Define a function to create an ICMP echo request packet
  - Define a function to send and receive an ICMP packet using a socket
  - Define a function to perform a PING operation by sending and receiving one ICMP packet and measuring the round-trip time
  - Define a function to perform a TRACEROUTE operation by sending and receiving multiple ICMP packets with increasing TTL values and recording the intermediate hops
  - Define a main function to take the destination address as an argument and call the PING and TRACEROUTE functions
  - Run the main function with a sample destination address
- The code should handle any exceptions or errors that may occur during the socket operations
- The code should print the results of the PING and TRACEROUTE operations in a readable format
- The code should follow the Python coding style and conventions
- The code should be commented and documented
- The code should be tested and verified



## Experiment 5 - Create a socket for HTTP for web page upload and download

- A socket is an endpoint of a communication channel between two processes or devices over a network.
- HTTP (Hypertext Transfer Protocol) is a protocol that defines how messages are formatted and transmitted over the web, and how servers and browsers should respond to various commands.
- To create a socket for HTTP, we need to use the socket module in Python, which provides a low-level interface to the network layer.
- The steps to create a socket for HTTP are:

  1. Import the socket module: `import socket`
  2. Create a socket object: `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  3. Specify the host and port of the server: `host = 'www.example.com'` and `port = 80`
  4. Connect the socket to the server: `s.connect((host, port))`
  5. Send an HTTP request to the server: `s.send(b'GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n')`
  6. Receive the HTTP response from the server: `data = s.recv(1024)`
  7. Print the data: `print(data.decode())`
  8. Close the socket: `s.close()`

- To upload and download a web page using the socket, we need to use the following methods:

  - To upload a web page, we need to send an HTTP POST request to the server with the content of the web page in the body of the request. For example: `s.send(b'POST /upload.html HTTP/1.1\r\nHost: www.example.com\r\nContent-Type: text/html\r\nContent-Length: 20\r\n\r\n<html>Hello</html>')`
  - To download a web page, we need to send an HTTP GET request to the server with the name of the web page in the request line. For example: `s.send(b'GET /download.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n')`
  - To receive the web page, we need to read the data from the socket until the end of the response. For example: `data = b''` and `while True: chunk = s.recv(1024) if not chunk: break data += chunk`
  - To save the web page, we need to write the data to a file. For example: `with open('download.html', 'wb') as f: f.write(data)`



## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

- RPC is a technique that allows a program to invoke a procedure or a function on a different machine or process as if it were a local call.
- RPC hides the details of the network communication, such as the message formats, protocols, and data marshalling, from the application programmer.
- RPC consists of two components: a client and a server.
- The client is the program that initiates the request for a remote procedure call, and the server is the program that executes the requested procedure and returns the result to the client.
- The client and the server communicate through a stub, which is a piece of code that acts as an interface between the application and the network layer.
- The client stub prepares the parameters for the remote procedure call, encodes them into a message, and sends it to the server stub over the network.
- The server stub receives the message, decodes the parameters, invokes the appropriate procedure on the server, encodes the result into a message, and sends it back to the client stub.
- The client stub then decodes the result and returns it to the client application.

### Steps to write a program to implement RPC

- To write a program to implement RPC, we need to use a tool that can generate the stubs for the client and the server based on a common interface definition.
- One such tool is RPCGEN, which is a compiler that takes an input file containing the definitions of the remote procedures and their parameters, and produces the following files:
  - A header file that contains the declarations of the data types and the constants used by the remote procedures.
  - A client stub file that contains the code for the client stub.
  - A server stub file that contains the code for the server stub.
  - A client main file that contains the code for the client application.
  - A server main file that contains the code for the server application.
- The input file for RPCGEN has a .x extension and follows a specific syntax. It consists of three sections: definitions, declarations, and programs.
  - The definitions section contains the definitions of the data types and the constants used by the remote procedures. It uses the C syntax for defining structures, unions, enumerations, and typedefs.
  - The declarations section contains the declarations of the remote procedures and their parameters. It uses the following syntax: `return_type procedure_name(parameter_type parameter_name, ...);`
  - The programs section contains the definitions of the programs that provide the remote procedures. It uses the following syntax: `program program_name { version version_name { procedure_declaration; ... } = version_number; ... } = program_number;`
- The program_number and the version_number are unique identifiers that are used to locate and invoke the remote procedures on the server.
- The RPCGEN tool can be invoked by using the following command: `rpcgen -a input_file.x`
- This command will generate the following files: input_file.h, input_file_clnt.c, input_file_svc.c, input_file_client.c, and input_file_server.c.
- The input_file_client.c and input_file_server.c files contain the skeleton code for the client and the server applications, respectively. They need to be modified by the programmer to implement the desired functionality.
- The input_file_clnt.c and input_file_svc.c files contain the code for the client and the server stubs, respectively. They do not need to be modified by the programmer.
- The input_file.h file contains the declarations of the data types and the constants used by the remote procedures. It is included by both the client and the server applications.
- To compile and run the program, we need to use the following commands:
  - `gcc -o input_file_client input_file_client.c input_file_clnt.c -lnsl`
  - `gcc -o input_file_server input_file_server.c input_file_svc.c -lnsl`
  - `./input_file_server &`
  - `./input_file_client server_host_name`
- The -lnsl flag is used to link the network services library, which is required by the RPC library.
- The server_host_name is the name or the IP address of the machine where the server is running.
- The server program runs in the background and waits for the client requests.
- The client program takes the server host name as an argument and invokes the remote procedures on the server.

### Example of a program to implement RPC

- Suppose we want to write a program to implement RPC that provides two remote procedures: add and subtract, which take two integers as parameters and return their sum and difference, respectively.
- The input file for RPCGEN would look like this:

```c
// input_file.x
// definitions section
typedef int

```




## Experiment 7 - Implementation of Subnetting

### Objective
- To understand the concept of subnetting and its benefits.
- To learn how to divide a network into smaller subnets using subnet masks.
- To practice subnetting calculations and address assignments.

### Theory
- Subnetting is a technique of dividing a large network into smaller subnets, each with its own range of IP addresses and network parameters.
- Subnetting reduces network congestion, improves security, and simplifies network management.
- Subnetting involves applying a subnet mask to an IP address, which determines how many bits are used for the network ID and how many bits are used for the host ID.
- The subnet mask is a 32-bit binary number that has 1s in the network ID portion and 0s in the host ID portion. For example, 255.255.255.0 is a subnet mask that divides an IP address into 24 bits for the network ID and 8 bits for the host ID.
- The subnet mask can also be written in dotted decimal notation or in slash notation. For example, 255.255.255.0 is equivalent to /24.
- To calculate the number of subnets and hosts per subnet, the following formulas can be used:

  - Number of subnets = 2^n, where n is the number of bits borrowed from the host ID portion of the subnet mask.
  - Number of hosts per subnet = 2^m - 2, where m is the number of bits remaining in the host ID portion of the subnet mask. The -2 is to account for the network address and the broadcast address, which cannot be assigned to hosts.

- To assign IP addresses to subnets, the following steps can be followed:

  - Identify the network address and the broadcast address of the original network. The network address is the lowest IP address in the range, and the broadcast address is the highest IP address in the range. For example, if the original network is 192.168.1.0/24, then the network address is 192.168.1.0 and the broadcast address is 192.168.1.255.
  - Determine the subnet mask and the number of subnets and hosts per subnet. For example, if the subnet mask is 255.255.255.192, then the number of subnets is 2^2 = 4 and the number of hosts per subnet is 2^6 - 2 = 62.
  - Divide the original network into subnets by incrementing the network address by the number of hosts per subnet. For example, the first subnet will have the network address 192.168.1.0 and the broadcast address 192.168.1.63, the second subnet will have the network address 192.168.1.64 and the broadcast address 192.168.1.127, and so on.
  - Assign IP addresses to hosts within each subnet. For example, the first host in the first subnet can have the IP address 192.168.1.1, the second host can have the IP address 192.168.1.2, and so on. The last host in the first subnet can have the IP address 192.168.1.62. The same logic applies to the other subnets.

### Procedure
- To implement subnetting in a network, the following steps can be followed:

  - Design a network topology that consists of routers, switches, and hosts. For example, a network topology can have two routers, four switches, and eight hosts.
  - Configure the routers with the appropriate IP addresses and subnet masks for their interfaces. For example, the first router can have the IP address 192.168.1.1/26 for its first interface and 192.168.1.65/26 for its second interface. The second router can have the IP address 192.168.1.129/26 for its first interface and 192.168.1.193/26 for its second interface.
  - Configure the switches with the appropriate IP addresses and subnet masks for their management interfaces. For example, the first switch can have the IP address 192.168.1.2/26, the second switch can have the IP address 192.168.1.66/26, and so on.
  - Configure the hosts with the appropriate IP addresses and subnet masks for their network interfaces. For example, the first host can have the IP address 192.168.1.3/26, the second host can have the IP address 192.168.1.4/26, and so on.
  - Verify the connectivity between the hosts and the routers using ping commands



## Experiment 8 - Applications using TCP Sockets

TCP sockets are a type of network communication mechanism that allows two processes to exchange data using the Transmission Control Protocol (TCP). TCP is a reliable, connection-oriented protocol that ensures the delivery and ordering of data packets. TCP sockets can be used to implement various network applications, such as:

- File transfer: TCP sockets can be used to send and receive files between a client and a server. The client can request a file from the server by sending the file name, and the server can send the file contents in chunks until the end of file is reached. The client can acknowledge each chunk and request the next one until the file transfer is complete. An example of a file transfer application using TCP sockets is the File Transfer Protocol (FTP).
- Remote command execution: TCP sockets can be used to execute commands on a remote machine and get the output. The client can send a command to the server, and the server can execute the command and send the output back to the client. The client can send multiple commands and receive multiple outputs until the connection is closed. An example of a remote command execution application using TCP sockets is the Secure Shell (SSH).
- Chat: TCP sockets can be used to implement a chat application that allows multiple users to communicate with each other. The client can send messages to the server, and the server can broadcast the messages to all the connected clients. The clients can receive the messages and display them on the screen. The clients can also send private messages to specific users by specifying their usernames. An example of a chat application using TCP sockets is the Internet Relay Chat (IRC).
- Web: TCP sockets can be used to implement a web application that allows a client to request and receive web pages from a server. The client can send a request to the server using the Hypertext Transfer Protocol (HTTP), and the server can send the response back to the client. The response can contain the web page content, such as HTML, CSS, JavaScript, images, etc. The client can render the web page on the browser and interact with it. An example of a web application using TCP sockets is the World Wide Web (WWW).



### Experiment 8.1 - Echo client and echo server

- An echo client and echo server are applications that allow a client and a server to communicate over a network using sockets.
- A socket is an endpoint of a bidirectional communication channel between two processes running on different machines.
- An echo server is a server that receives data from a client and sends back an identical copy of the data to the client.
- An echo client is a client that sends data to an echo server and receives the same data back from the server.
- The purpose of this experiment is to demonstrate the basic concepts of socket programming in Java, such as creating, binding, listening, accepting, sending and receiving sockets.
- The steps of this experiment are as follows:

  1. Create a single-threaded TCP echo server that listens on a specific port for incoming connections from clients.
  2. Create a TCP echo client that connects to the echo server on the same port and sends a message to the server.
  3. The echo server receives the message from the client and echoes it back to the client.
  4. The echo client receives the echoed message from the server and prints it on the standard output.
  5. The echo client and server close their sockets and terminate.

- The code for the echo server and client can be found in the following sources  .



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content in markdown format on the topic of Experiment 8.2 - Chat. Here is what I have written:

# Experiment 8.2 - Chat

## Objective
- To create a chatbot that can communicate with a human user in natural language.
- To use a neural network model to generate responses based on the user input and the chat history.
- To evaluate the chatbot's performance using metrics such as perplexity, coherence, and engagement.

## Requirements
- A computer with Python 3.7 or higher installed.
- A text editor or an IDE to write and run the code.
- A dataset of conversational pairs or a pre-trained model to fine-tune.
- A library such as PyTorch, TensorFlow, or HuggingFace Transformers to implement the neural network model.
- A library such as NLTK, spaCy, or Gensim to preprocess the text data.
- A library such as nltk-chat or ChatterBot to create a simple chat interface.

## Procedure
- Import the required libraries and modules.
- Load the dataset of conversational pairs or the pre-trained model and split it into training and validation sets.
- Preprocess the text data by tokenizing, lowercasing, removing punctuation, and padding the sequences.
- Define the neural network model architecture, such as a sequence-to-sequence model with attention, a transformer model, or a GPT-3 model.
- Train the model on the training set using an optimizer, a loss function, and a learning rate scheduler.
- Evaluate the model on the validation set using metrics such as perplexity, coherence, and engagement.
- Save the model and its parameters for future use.
- Create a chat interface using a library such as nltk-chat or ChatterBot and load the model.
- Test the chatbot by interacting with it and providing feedback.

## Expected Output
- A chatbot that can generate relevant, coherent, and engaging responses to the user input and the chat history.
- A report that summarizes the model architecture, the training and evaluation process, and the chatbot performance.



### Experiment 8.3 - File Transfer

- File transfer is the process of copying or moving a file from one computer to another over a network or the Internet.
- File transfer can be done using different protocols, such as FTP, HTTP, SCP, SFTP, etc.
- File transfer can be done in different modes, such as binary, ASCII, or auto.
- File transfer can be done using different tools, such as command-line utilities, graphical user interfaces, or web browsers.
- File transfer can be done for different purposes, such as backup, synchronization, sharing, or distribution.

#### Objectives

- To learn how to use FTP to transfer files between two computers.
- To learn how to use SCP and SFTP to securely transfer files between two computers.
- To learn how to use HTTP to transfer files using a web browser.

#### Requirements

- Two computers connected to the same network or the Internet.
- FTP server and client software installed on both computers.
- SSH server and client software installed on both computers.
- Web server and browser software installed on both computers.
- A text editor and a binary file (such as an image or a video) to transfer.

#### Procedure

- FTP
  - On the computer that will act as the FTP server, create a folder named ftp and copy the text and binary files into it.
  - On the same computer, start the FTP server software and configure it to allow anonymous access to the ftp folder.
  - On the computer that will act as the FTP client, start the FTP client software and connect to the FTP server using the IP address and the anonymous username and password.
  - On the FTP client, use the ls or dir command to list the files in the ftp folder on the FTP server.
  - On the FTP client, use the get or mget command to download the text and binary files from the FTP server to the local folder.
  - On the FTP client, use the put or mput command to upload the text and binary files from the local folder to the FTP server.
  - On the FTP client, use the quit or bye command to disconnect from the FTP server.
  - On the FTP server, verify that the files have been transferred correctly by comparing the file sizes and contents.
- SCP and SFTP
  - On the computer that will act as the SSH server, create a folder named ssh and copy the text and binary files into it.
  - On the same computer, start the SSH server software and configure it to allow password authentication and public key authentication.
  - On the computer that will act as the SSH client, start the SSH client software and generate a public and private key pair using the ssh-keygen command.
  - On the SSH client, use the ssh-copy-id command to copy the public key to the SSH server.
  - On the SSH client, use the scp command to securely copy the text and binary files from the SSH server to the local folder using the IP address and the username and password or the public key.
  - On the SSH client, use the scp command to securely copy the text and binary files from the local folder to the SSH server using the IP address and the username and password or the public key.
  - On the SSH client, use the sftp command to securely connect to the SSH server using the IP address and the username and password or the public key.
  - On the SFTP client, use the ls or dir command to list the files in the ssh folder on the SSH server.
  - On the SFTP client, use the get or mget command to download the text and binary files from the SSH server to the local folder.
  - On the SFTP client, use the put or mput command to upload the text and binary files from the local folder to the SSH server.
  - On the SFTP client, use the quit or bye command to disconnect from the SSH server.
  - On the SSH server, verify that the files have been transferred correctly by comparing the file sizes and contents.
- HTTP
  - On the computer that will act as the web server, create a folder named www and copy the text and binary files into it.
  - On the same computer, start the web server software and configure it to allow access to the www folder.
  - On the computer that will act as the web client, start the web browser software and enter the URL of the web server using the IP address and the www folder name.
  - On the web browser, view the text and binary files by clicking on the links or the icons.
  - On the web browser, download the text and binary files by right-clicking on the links or the icons and choosing the save option.
  - On the web browser, upload the text and binary



## Experiment 9 - Applications using TCP and UDP Sockets

TCP and UDP are two protocols that provide different ways of sending and receiving data over a network. TCP stands for Transmission Control Protocol and UDP stands for User Datagram Protocol. Both protocols use sockets, which are endpoints of communication between two devices.

Some of the applications that use TCP and UDP sockets are:

- **Web browsing**: Web browsers use TCP sockets to request and receive web pages from web servers. TCP ensures reliable and ordered delivery of data, which is important for web pages that contain text, images, and other elements. TCP also allows the browser and the server to establish a persistent connection, which can improve the performance and efficiency of web browsing.

- **Email**: Email clients use TCP sockets to send and receive email messages from email servers. TCP ensures reliable and ordered delivery of data, which is important for email messages that contain text, attachments, and other elements. TCP also allows the client and the server to authenticate each other and encrypt the data, which can enhance the security and privacy of email communication.

- **File transfer**: File transfer applications use TCP sockets to send and receive files from other devices. TCP ensures reliable and ordered delivery of data, which is important for files that contain binary, text, or other data. TCP also allows the sender and the receiver to resume the file transfer in case of interruption, which can improve the robustness and efficiency of file transfer.

- **Streaming media**: Streaming media applications use UDP sockets to send and receive audio and video data from other devices. UDP provides fast and low-latency delivery of data, which is important for streaming media that require real-time and smooth playback. UDP also allows the sender and the receiver to adjust the quality and rate of the data, which can improve the adaptability and scalability of streaming media.

- **Online gaming**: Online gaming applications use UDP sockets to send and receive game data from other players. UDP provides fast and low-latency delivery of data, which is important for online gaming that require real-time and interactive gameplay. UDP also allows the players to exchange data without establishing a connection, which can improve the flexibility and responsiveness of online gaming.

- **Voice over IP (VoIP)**: VoIP applications use UDP sockets to send and receive voice data from other devices. UDP provides fast and low-latency delivery of data, which is important for VoIP that require real-time and clear communication. UDP also allows the devices to use different codecs and protocols, which can improve the compatibility and quality of VoIP.



Hello, I am Sydney, your AI assistant. I can help you with your topic of Experiment 9.1 - DNS. Here is some content that you can use for your study material:

### Experiment 9.1 - DNS

- DNS stands for Domain Name System, which is a distributed database that maps domain names to IP addresses and other information.
- DNS allows users to access websites and other resources using human-readable names instead of numerical addresses, which are easier to remember and type.
- DNS also provides other services, such as email routing, load balancing, and security.
- DNS consists of a hierarchical structure of name servers, which store and update the records for different domains and subdomains.
- The root name servers are the top-level name servers that manage the root zone, which contains the information about the top-level domains (TLDs), such as .com, .org, .edu, etc.
- The authoritative name servers are the name servers that have the definitive information about a specific domain or subdomain, such as google.com, wikipedia.org, etc.
- The recursive name servers are the name servers that act as intermediaries between the users and the authoritative name servers, by resolving the queries and caching the results for future use.
- The resolver is the software component that runs on the user's device and initiates the DNS queries to the recursive name servers.
- The DNS protocol uses UDP as the transport layer protocol for most queries and responses, and TCP for larger messages or zone transfers.
- The DNS message format consists of a header, a question section, an answer section, an authority section, and an additional section.
- The header contains the identification, flags, and counts of the sections.
- The question section contains the name and type of the query, such as A, AAAA, MX, NS, etc.
- The answer section contains the resource records (RRs) that match the query, such as the IP address, the mail server, the name server, etc.
- The authority section contains the RRs that point to the authoritative name servers for the queried domain or subdomain.
- The additional section contains the RRs that provide additional information, such as the IP addresses of the name servers in the authority section.
- The DNS resolution process involves the following steps:
  - The user types a domain name in the browser, such as www.example.com.
  - The resolver sends a DNS query to the recursive name server, asking for the IP address of www.example.com.
  - The recursive name server checks its cache for the answer. If it does not have it, it sends a query to the root name server, asking for the name server of the .com TLD.
  - The root name server responds with the name and IP address of the .com name server.
  - The recursive name server sends a query to the .com name server, asking for the name server of the example.com domain.
  - The .com name server responds with the name and IP address of the example.com name server.
  - The recursive name server sends a query to the example.com name server, asking for the IP address of www.example.com.
  - The example.com name server responds with the IP address of www.example.com.
  - The recursive name server caches the answer and sends it back to the resolver.
  - The resolver passes the IP address to the browser, which can then establish a connection to the web server.



### Experiment 9.2 - SNMP

- SNMP stands for Simple Network Management Protocol  .
- It is a way for different devices on a network to share information about their current state, and also a channel through which an administrator can modify pre-defined values.
- It allows devices to communicate even if the devices are different hardware and run different software.
- It is a component of the Internet Protocol Suite as defined by the Internet Engineering Task Force (IETF).
- It consists of a set of standards for network management, including an application layer protocol, a database schema, and a set of data objects.
- SNMP exposes management data in the form of variables on the managed systems organized in a management information base (MIB) which describe the system status and configuration.
- SNMP is widely used in network management for network monitoring.
- Devices that typically support SNMP include cable modems, routers, switches, servers, workstations, printers, and more.



### Experiment 9.3 - File Transfer

- File transfer is the process of copying or moving a file from one computer to another over a network or the Internet.
- File transfer can be done using different protocols, such as FTP, HTTP, SCP, SFTP, etc.
- File transfer can be done for different purposes, such as backup, synchronization, sharing, distribution, etc.
- File transfer can be done in different modes, such as binary, ASCII, or auto.
- File transfer can be done using different tools, such as command-line utilities, graphical user interfaces, web browsers, etc.

#### Objectives

- To learn how to use FTP and SCP commands to transfer files between computers.
- To compare the advantages and disadvantages of FTP and SCP protocols.
- To understand the difference between binary and ASCII modes of file transfer.
- To learn how to use SFTP and a graphical user interface to transfer files securely and conveniently.

#### Procedure

1. Connect to a remote computer using SSH or Telnet.
2. Use the FTP command to start an FTP session with another remote computer.
3. Use the `help` command to see the list of available FTP commands.
4. Use the `ls` command to list the files and directories on the remote computer.
5. Use the `cd` command to change the current directory on the remote computer.
6. Use the `lcd` command to change the current directory on the local computer.
7. Use the `get` command to download a file from the remote computer to the local computer.
8. Use the `put` command to upload a file from the local computer to the remote computer.
9. Use the `mget` and `mput` commands to download and upload multiple files at once.
10. Use the `type` command to change the mode of file transfer between binary and ASCII.
11. Use the `quit` command to end the FTP session.
12. Use the SCP command to copy a file from the local computer to the remote computer using SSH.
13. Use the SCP command to copy a file from the remote computer to the local computer using SSH.
14. Use the `-r` option to copy a directory and its contents recursively using SCP.
15. Use the `-p` option to preserve the file attributes such as permissions, timestamps, etc. using SCP.
16. Use the SFTP command to start an SFTP session with another remote computer using SSH.
17. Use the same commands as FTP to list, change, and transfer files and directories using SFTP.
18. Use the `quit` command to end the SFTP session.
19. Use a graphical user interface such as FileZilla or WinSCP to connect to a remote computer using FTP or SFTP.
20. Use the drag-and-drop feature to transfer files and directories between the local and remote computers using the graphical user interface.

#### Observations

- FTP is a simple and widely used protocol for file transfer, but it is not secure as it sends the data and credentials in plain text over the network.
- SCP is a secure protocol for file transfer, as it encrypts the data and credentials using SSH, but it is not as flexible as FTP as it does not support interactive commands or multiple file transfers.
- SFTP is a secure and flexible protocol for file transfer, as it combines the features of FTP and SCP using SSH, but it may not be supported by all servers or clients.
- Binary mode is used to transfer files that are not text-based, such as images, audio, video, etc. ASCII mode is used to transfer files that are text-based, such as documents, scripts, etc. Auto mode is used to detect the file type and choose the appropriate mode automatically.
- Graphical user interfaces are user-friendly and convenient tools for file transfer, but they may not be as fast or reliable as command-line utilities.



## Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

- Network simulator (NS) is a name for a series of discrete event network simulators, specifically ns-1, ns-2, and ns-3  .
- NS is used for simulation of TCP, routing, and multicast protocols over wired and wireless (local and satellite) networks .
- NS is free, open-source software, licensed under the GNU GPLv2 license, and maintained by a worldwide community.
- NS is written in C++ and uses Tcl as a scripting language .
- NS provides a modular library of network components and models, such as nodes, links, queues, protocols, applications, etc .
- NS allows users to create and run network simulations using a graphical user interface (GUI) or a command-line interface (CLI) .
- NS can also be integrated with other tools, such as network animator (NAM), Xgraph, Gnuplot, etc., for visualization and analysis of simulation results .

- Congestion control algorithms are mechanisms that aim to regulate the amount of traffic sent into a network, in order to avoid congestion and improve network performance.
- Congestion control algorithms can be classified into two categories: end-to-end and network-assisted.
- End-to-end congestion control algorithms rely on the feedback from the receivers or the network to adjust the sending rate of the sources, such as TCP.
- Network-assisted congestion control algorithms involve the cooperation of the network devices, such as routers, to signal the sources about the network conditions, such as Explicit Congestion Notification (ECN).
- Congestion control algorithms can also be designed for different types of networks, such as wired, wireless, or satellite networks, with different characteristics and challenges.
- Congestion control algorithms can be evaluated using various metrics, such as throughput, delay, packet loss, fairness, etc.

- Simulation of congestion control algorithms using NS involves the following steps:
  - Install and configure NS on your system.
  - Create a network topology using NS components and models, such as nodes, links, queues, etc.
  - Specify the traffic sources and sinks, such as TCP, UDP, FTP, etc., and assign them to the nodes.
  - Choose the congestion control algorithm to be simulated, such as TCP Reno, TCP Vegas, TCP NewReno, etc., and set the parameters accordingly.
  - Run the simulation using the NS command ns or the GUI tool NsTclsh.
  - Collect and analyze the simulation results using NS tools, such as NAM, Xgraph, Gnuplot, etc., or external tools, such as Excel, Matlab, etc.
  - Compare and contrast the performance of different congestion control algorithms using the metrics mentioned above.



## Experiment 11 - Perform a case study about the different routing algorithms to select the network path with its optimum and economical during data transfer

- Routing is the process of selecting a path for traffic in a network or between or across multiple networks.
- Routing algorithms are the methods that determine the best path for a packet to reach its destination.
- Routing algorithms can be classified into two types: static and dynamic.
  - Static routing algorithms use fixed routes that do not change with network conditions. They are simple, fast, and easy to implement, but they cannot adapt to network failures or congestion.
  - Dynamic routing algorithms use current network information to update routes periodically or on demand. They are more flexible, robust, and efficient, but they require more computation, communication, and memory resources.
- Routing algorithms can also be categorized based on their scope: global or decentralized.
  - Global routing algorithms use complete information about the network topology and state to compute optimal routes. They are also called link-state algorithms. Examples are Dijkstra's algorithm and Open Shortest Path First (OSPF) protocol.
  - Decentralized routing algorithms use partial or local information about the network to compute routes. They are also called distance-vector algorithms. Examples are Bellman-Ford algorithm and Routing Information Protocol (RIP).
- Routing algorithms can also be distinguished based on their adaptiveness: non-adaptive or adaptive.
  - Non-adaptive routing algorithms use fixed routes that do not change with network conditions. They are also called deterministic algorithms. Examples are shortest path routing and flooding.
  - Adaptive routing algorithms use dynamic routes that change with network conditions. They are also called stochastic algorithms. Examples are congestion-aware routing and load balancing.
- Path selection involves applying a routing metric to multiple routes to select (or predict) the best route.
  - A routing metric is a numerical value that represents the desirability of a route. It can be based on various factors, such as hop count, bandwidth, delay, cost, reliability, etc.
  - A routing metric can be additive, multiplicative, or concave. An additive metric is the sum of the values of each link in the route. A multiplicative metric is the product of the values of each link in the route. A concave metric is the minimum of the values of each link in the route.
  - A routing metric can also be static or dynamic. A static metric is fixed and does not change with network conditions. A dynamic metric is variable and changes with network conditions.
- Path selection can be performed by different methods, such as shortest path, least cost, highest bandwidth, lowest delay, etc.
  - Shortest path selects the route with the minimum number of hops. It is simple and fast, but it does not consider other factors, such as link capacity, traffic load, etc.
  - Least cost selects the route with the minimum total cost. It is economical and efficient, but it requires a common cost function for all links and nodes.
  - Highest bandwidth selects the route with the maximum available bandwidth. It is optimal for high-throughput applications, but it may cause congestion and waste of resources.
  - Lowest delay selects the route with the minimum total delay. It is suitable for real-time applications, but it may ignore other factors, such as reliability, security, etc.
- Path selection can also be performed by using multiple paths, such as multipath routing, equal-cost multipath routing, or load balancing.
  - Multipath routing uses more than one path for a packet to reach its destination. It can improve reliability, performance, and fault tolerance, but it may cause routing loops, out-of-order delivery, or increased overhead.
  - Equal-cost multipath routing uses multiple paths that have the same routing metric value. It can balance the load among the paths, but it may cause packet reordering or synchronization issues.
  - Load balancing distributes the traffic among multiple paths based on their current load or utilization. It can optimize the network performance and avoid congestion, but it may require frequent updates and coordination among the routers.



### Experiment 11.1 - Link State Routing

- Link state routing is a type of routing algorithm that uses the information about the state of each link (such as bandwidth, delay, cost, etc.) to calculate the best path from one node to every other node in the network.
- Link state routing is also known as Dijkstra's algorithm, which is an iterative algorithm that finds the shortest path from a source node to all other nodes by using a priority queue to store the nodes with the least cost paths.
- Link state routing requires each node to construct a map of the network topology, which is a graph that shows the nodes and the links between them. Each node exchanges messages with its neighbors to learn the state of each link, and then broadcasts this information to all other nodes in the network.
- Link state routing has some advantages over distance-vector routing, such as faster convergence, less routing loops, and more accurate routing information. However, link state routing also has some disadvantages, such as higher memory and CPU usage, more bandwidth consumption, and more complexity.
- Link state routing protocols are widely used in packet switching networks for computer communications, such as the Internet. Some examples of link state routing protocols are Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).
- Link state routing protocols have some common features, such as:
  - Hello protocol: A mechanism to establish and maintain neighbor relationships between nodes.
  - Link state advertisement (LSA): A message that contains the information about the state of a link or a group of links.
  - Link state database (LSDB): A data structure that stores the LSAs received from all other nodes in the network.
  - Link state request (LSR): A message that requests a specific LSA from another node.
  - Link state update (LSU): A message that contains one or more LSAs to be sent to another node.
  - Link state acknowledgment (LSAck): A message that confirms the receipt of an LSU from another node.
  - Shortest path first (SPF) algorithm: A procedure that calculates the best path from a node to all other nodes in the network by using the LSDB as the input.



### Experiment 11.2 - Flooding

- Flooding is a natural phenomenon that occurs when a large amount of water overflows onto land that is normally dry.
- Flooding can be caused by various factors, such as heavy rainfall, snowmelt, storm surges, dam failures, or river overflow.
- Flooding can have positive and negative impacts on the environment, society, and economy.
- Positive impacts include:
  - Replenishing soil nutrients and groundwater resources.
  - Providing habitats and food sources for aquatic and terrestrial wildlife.
  - Supporting agriculture and fisheries.
- Negative impacts include:
  - Damaging infrastructure and property.
  - Disrupting transportation and communication networks.
  - Causing injuries, deaths, and diseases among humans and animals.
  - Increasing the risk of soil erosion, landslides, and water pollution.
- To measure the extent and severity of flooding, some indicators are used, such as:
  - Flood frequency: how often a flood of a given magnitude occurs in a given area.
  - Flood duration: how long a flood lasts in a given area.
  - Flood depth: how high the water level rises above the normal level in a given area.
  - Flood area: how much land is covered by water in a given area.
- To prevent or reduce the negative impacts of flooding, some strategies are used, such as:
  - Structural measures: building physical barriers or structures to control the flow of water, such as dams, levees, or floodwalls.
  - Non-structural measures: implementing policies or practices to reduce the exposure or vulnerability of people and property to flooding, such as land use planning, flood insurance, or evacuation plans.



### Experiment 11.3 - Distance vector

- A distance vector is a data structure that contains the distance and direction from a source node to a destination node in a network.
- A distance vector routing protocol is a type of routing protocol that uses distance vectors to exchange routing information between neighboring nodes.
- The main advantage of distance vector routing is its simplicity and low overhead. The main disadvantage is its slow convergence and susceptibility to routing loops.
- An example of a distance vector routing protocol is the Routing Information Protocol (RIP), which uses hop count as the distance metric and sends updates every 30 seconds.
- The algorithm for distance vector routing is as follows:

  - Each node maintains a distance vector table that contains the distance and next hop to every other node in the network.
  - Each node periodically broadcasts its distance vector table to its neighbors.
  - Upon receiving a distance vector table from a neighbor, a node updates its own table by applying the Bellman-Ford equation: 
    - For each destination d, if the distance to d through the neighbor n is smaller than the current distance to d, then update the distance to d as the sum of the distance to n and the distance from n to d, and update the next hop to d as n.
  - The algorithm terminates when there are no more updates to any distance vector table.



## Experiment 12 - To learn handling and configuration of networking hardware like RJ-45 connector, CAT-6 cable, crimping tool, etc

### Aim
To learn how to handle and configure common networking hardware such as RJ-45 connector, CAT-6 cable, crimping tool, etc.

### Theory
- RJ-45 connector: A standard type of connector for Ethernet cables. It has eight pins that are arranged in a specific order to transmit and receive data signals. The connector is usually attached to the end of a cable by crimping, which is the process of securing the connector to the cable using a crimping tool.
- CAT-6 cable: A category of twisted pair cable that is used for Ethernet networks. It has four pairs of wires that are twisted together to reduce crosstalk and interference. It can support data rates up to 10 Gbps and frequencies up to 250 MHz. It is backward compatible with CAT-5 and CAT-5e cables.
- Crimping tool: A device that is used to attach RJ-45 connectors to CAT-6 cables. It has a pair of jaws that can cut, strip, and crimp the cable and the connector. It also has a ratchet mechanism that ensures a proper and secure crimp.

### Procedure
1. Cut a desired length of CAT-6 cable using the cutting blade of the crimping tool.
2. Strip about 2 cm of the outer insulation of the cable using the stripping blade of the crimping tool.
3. Untwist the four pairs of wires and arrange them in the following order from left to right: orange-white, orange, green-white, blue, blue-white, green, brown-white, brown. This is the T568B standard for RJ-45 wiring.
4. Trim the wires to make them even and insert them into the RJ-45 connector. Make sure that the wires are fully inserted and that the insulation of each wire is in contact with the end of the connector.
5. Place the connector with the cable into the crimping slot of the crimping tool and squeeze the handle firmly until the ratchet clicks. This will secure the connector to the cable.
6. Repeat steps 1 to 5 for the other end of the cable.
7. Test the cable using a cable tester or by connecting it to a network device and checking the link status.



## Experiment 13 - Configuration of router, hub, switch etc. (using real devices or simulators)

- The objective of this experiment is to learn how to configure and connect different network devices, such as routers, hubs, switches, etc., using real devices or simulators.
- The network devices are used to create and manage networks of computers and other devices that communicate with each other using protocols such as TCP/IP, Ethernet, etc.
- The configuration of network devices involves setting up parameters such as IP addresses, subnet masks, default gateways, routing tables, etc., that enable the devices to send and receive data packets across the network.
- The connection of network devices involves using cables, connectors, ports, etc., that physically link the devices together and allow the transmission of electrical signals between them.
- The experiment can be performed using real devices or simulators. Real devices are actual hardware components that can be connected and configured using physical tools and software. Simulators are software applications that emulate the behavior and functionality of real devices using graphical user interfaces and virtual tools.
- The advantages of using real devices are that they provide a realistic and hands-on experience of network configuration and connection, and that they can be used to test and troubleshoot real network scenarios and problems. The disadvantages of using real devices are that they are expensive, require physical space and maintenance, and may not be available or accessible for all students.
- The advantages of using simulators are that they are cheaper, require less space and resources, and can be easily accessed and modified by students. The disadvantages of using simulators are that they may not accurately reflect the performance and limitations of real devices, and that they may not support all the features and functions of real devices.
- Some examples of real devices that can be used for this experiment are Cisco routers, switches, and hubs, which are widely used in the industry and have standard interfaces and commands. Some examples of simulators that can be used for this experiment are Cisco Packet Tracer, GNS3, and NetSim, which are popular and user-friendly software applications that can simulate Cisco devices and networks.



## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

- In this experiment, you will learn how to use some common network services and commands that can help you troubleshoot, test, and communicate with other devices on a network.
- These services and commands are:
  - ping: a tool that sends packets of data to a specified destination and measures the round-trip time and packet loss rate.
  - traceroute: a tool that traces the path of packets from the source to the destination and displays the routers and hosts along the way.
  - nslookup: a tool that queries the Domain Name System (DNS) and resolves hostnames to IP addresses or vice versa.
  - arp: a tool that displays and manipulates the Address Resolution Protocol (ARP) cache, which maps IP addresses to MAC addresses on a local network.
  - telnet: a protocol that allows remote login and command execution on a host using a text-based interface.
  - ftp: a protocol that allows file transfer between hosts using a client-server model.
- To run these services and commands, you will need a terminal or command prompt application on your device, and access to a network with other devices that support these protocols.
- The syntax and output of these commands may vary depending on the operating system and network configuration of your device and the destination device.
- The following are some examples of how to use these services and commands on a Windows device. You can replace the IP addresses or hostnames with the ones that are relevant to your network.

### ping
- To ping a destination, type `ping <destination>` in the terminal, where `<destination>` can be an IP address or a hostname.
- For example, to ping the IP address 8.8.8.8, which is a public DNS server provided by Google, type `ping 8.8.8.8` and press Enter.
- You should see something like this:

```
Pinging 8.8.8.8 with 32 bytes of data:
Reply from 8.8.8.8: bytes=32 time=14ms TTL=117
Reply from 8.8.8.8: bytes=32 time=13ms TTL=117
Reply from 8.8.8.8: bytes=32 time=13ms TTL=117
Reply from 8.8.8.8: bytes=32 time=13ms TTL=117

Ping statistics for 8.8.8.8:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 13ms, Maximum = 14ms, Average = 13ms
```
- This output shows that four packets of 32 bytes each were sent to 8.8.8.8, and all of them were received back with a time of 13 or 14 milliseconds and a Time To Live (TTL) of 117. The TTL is a value that indicates how many hops (routers) the packet can pass through before it expires. The ping statistics show the number of packets sent, received, and lost, and the minimum, maximum, and average round-trip times.
- To ping a hostname, such as www.google.com, type `ping www.google.com` and press Enter. You should see something like this:

```
Pinging www.google.com [142.250.74.196] with 32 bytes of data:
Reply from 142.250.74.196: bytes=32 time=14ms TTL=117
Reply from 142.250.74.196: bytes=32 time=13ms TTL=117
Reply from 142.250.74.196: bytes=32 time=13ms TTL=117
Reply from 142.250.74.196: bytes=32 time=13ms TTL=117

Ping statistics for 142.250.74.196:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 13ms, Maximum = 14ms, Average = 13ms
```
- This output shows that the hostname www.google.com was resolved to the IP address 142.250.74.196, and the rest of the output is similar to the previous example.
- To stop the ping command, press Ctrl+C. You can also use some options to modify the ping behavior, such as `-n` to specify the number of packets to send, `-l` to specify the



## Experiment 15 - Network packet analysis using tools like Wireshark, tcpdump, etc

- Network packet analysis is the process of capturing, inspecting, and interpreting the data packets that are exchanged between devices on a network.
- Network packet analysis tools are software applications that can capture, filter, decode, and analyze the packets on a network.
- Network packet analysis tools can help network administrators and security analysts to troubleshoot network problems, monitor network performance, detect network anomalies, and investigate network attacks.
- Some of the popular network packet analysis tools are:

  - Wireshark: A free and open-source tool that can capture and analyze packets on various network protocols and display them in a graphical user interface .
  - tcpdump: A command-line tool that can capture and display packets on various network protocols and filter them based on various criteria.
  - Colasoft Capsa: A commercial tool that can capture and analyze packets on both wired and wireless networks and provide real-time network monitoring and diagnostics.
  - Paessler PRTG: A commercial tool that can capture and analyze packets on various network protocols and provide network performance monitoring and alerting.
  - Arkime: A free and open-source tool that can capture and store packets on various network protocols and provide web-based analysis and visualization.

- To perform network packet analysis using these tools, the following steps are usually involved:

  - Selecting a network interface or a capture file to capture packets from.
  - Applying capture filters to limit the amount of packets captured based on network addresses, protocols, ports, etc.
  - Starting the packet capture and stopping it when enough packets are collected.
  - Applying display filters to narrow down the packets of interest based on various criteria.
  - Examining the packet details, such as the packet headers, payload, and checksums, and decoding the packet data according to the protocol specifications.
  - Analyzing the packet statistics, such as the packet rates, sizes, types, and flows, and identifying the network trends, patterns, and anomalies.
  - Saving the packet capture and analysis results for future reference or sharing.



## Experiment 16 - Network simulation using tools like Cisco Packet Tracer, NetSim, OMNeT++, NS2, NS3, etc

- Network simulation is the process of modeling the behavior and performance of a network using software tools.
- Network simulation tools can help students, researchers, and professionals to learn, design, test, and troubleshoot networks without using physical hardware.
- Network simulation tools can support various types of networks, such as wired, wireless, mobile, sensor, software-defined, hybrid, etc.
- Network simulation tools can vary in their features, capabilities, complexity, and cost. Some are open source and free, while others are licensed and commercial.
- Some of the most popular network simulation tools are:

  - Cisco Packet Tracer: A network simulation and visualization tool developed by Cisco for teaching and learning networking concepts. It supports basic and advanced networking devices, protocols, and scenarios. It is available for free for Cisco Networking Academy students and instructors. 
  - NetSim: A network simulation and emulation tool developed by Tetcos for research and education. It supports a wide range of protocols and technologies, such as TCP/IP, LTE, WiMAX, MANET, VANET, IoT, etc. It also supports interfacing with real networks and hardware devices. It is a licensed and commercial product. 
  - OMNeT++: An open source, modular, and component-based network simulation framework. It supports discrete event simulation, graphical user interface, and network animation. It can be extended with various libraries and models, such as INET, VEINS, SimuLTE, etc. It can run on Linux, Windows, and Mac OS.  
  - NS2: An open source, discrete event network simulator. It supports various network protocols and applications, such as TCP, UDP, HTTP, FTP, etc. It also supports wireless and mobile networks, such as ad hoc and sensor networks. It can run on Linux, Unix, Windows, and Ubuntu. It uses OTcl and C++ as programming languages.  
  - NS3: An open source, discrete event network simulator. It is a successor of NS2, but not backward compatible. It supports more advanced and realistic network models and scenarios, such as software-defined networks, hybrid networks, LTE, Wi-Fi, etc. It can run on Linux, Unix, Windows, and Ubuntu. It uses C++ and Python as programming languages.



## Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol.
- There are three types of sockets: stream sockets, datagram sockets and raw sockets.
- Stream sockets use TCP (Transmission Control Protocol) as the transport layer protocol, which provides a reliable, connection-oriented and byte-stream service .
- Datagram sockets use UDP (User Datagram Protocol) as the transport layer protocol, which provides an unreliable, connectionless and message-oriented service .
- Raw sockets can use any protocol, but they require the programmer to handle the headers and checksums of the packets.
- TCP and UDP have different characteristics and trade-offs, and they are suited for different applications .
- TCP ensures that the data is delivered in order and without errors, but it also adds overhead and latency to the communication.
- UDP is faster and simpler than TCP, but it does not guarantee the delivery, order or integrity of the data .
- Some examples of applications that use TCP are web browsing, email, file transfer and remote login.
- Some examples of applications that use UDP are video streaming, online gaming, voice over IP and DNS (Domain Name System)  .
- To program sockets using TCP or UDP in Python, the socket module provides the necessary functions and constants .
- To create a socket object, the socket function takes two arguments: the address family and the socket type .
- The address family can be AF_INET (for IPv4) or AF_INET6 (for IPv6)  .
- The socket type can be SOCK_STREAM (for TCP) or SOCK_DGRAM (for UDP)  .
- To establish a connection between a client and a server using TCP, the server socket needs to bind to a port, listen for incoming requests and accept a connection from a client socket  .
- The client socket needs to connect to the server socket using its IP address and port number  .
- To send and receive data using TCP, the send and recv methods can be used on the socket objects  .
- To close the connection, the close method can be used on the socket objects  .
- To communicate between a client and a server using UDP, there is no need to establish a connection or listen for requests .
- The server socket only needs to bind to a port, and the client socket can send data to the server socket using its IP address and port number .
- To send and receive data using UDP, the sendto and recvfrom methods can be used on the socket objects .
- These methods also return the address of the sender or receiver, which can be used for further communication .
- To close the socket, the close method can be used on the socket objects .
- Some examples of socket programming using UDP and TCP are:
  - Simple DNS: A client socket sends a domain name to a server socket using UDP, and the server socket returns the corresponding IP address using UDP.
  - Data and time client/server: A client socket requests the current date and time from a server socket using TCP, and the server socket sends the date and time using TCP.
  - Echo client/server: A client socket sends a message to a server socket using TCP or UDP, and the server socket echoes back the same message using TCP or UDP .
  - Iterative server: A server socket handles one client request at a time using TCP or UDP, and then waits for the next request .
  - Concurrent server: A server socket spawns a new process or

