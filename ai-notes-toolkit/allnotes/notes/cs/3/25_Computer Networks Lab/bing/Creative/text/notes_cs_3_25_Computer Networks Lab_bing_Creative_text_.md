

## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

- Stop and Wait Protocol is a flow control protocol that ensures reliable data transmission over a noiseless channel.
- Sliding Window Protocol is a flow control protocol that allows multiple packets to be sent and received concurrently over a noisy channel.
- Both protocols use sequence numbers and acknowledgments to coordinate the sender and receiver.
- The main difference between the two protocols is the window size, which is the number of packets that can be sent or received without waiting for an acknowledgment.
- In Stop and Wait Protocol, the window size is 1, which means the sender has to wait for an acknowledgment after sending each packet, and the receiver has to send an acknowledgment after receiving each packet.
- In Sliding Window Protocol, the window size can be larger than 1, which means the sender can send multiple packets without waiting for acknowledgments, and the receiver can receive multiple packets without sending acknowledgments for each one.
- The advantage of Sliding Window Protocol over Stop and Wait Protocol is that it can utilize the channel bandwidth more efficiently and achieve higher throughput.
- The disadvantage of Sliding Window Protocol over Stop and Wait Protocol is that it is more complex to implement and requires more buffer space at the sender and receiver.



### Experiment 1.1 - Implementation of Stop and Wait Protocol

- The stop and wait protocol is a flow control protocol that is used for transmitting data over noiseless channels.
- It provides unidirectional data transmission, which means that either sending or receiving of data will take place at a time.
- It is a special category of sliding window protocol where the window size is 1 .
- It requires only two sequence numbers, 0 and 1, to distinguish between the packets.
- The sender sends a data packet and waits for an acknowledgment from the receiver before sending the next packet.
- The receiver sends an acknowledgment after receiving a data packet and waits for the next packet.
- The sender and the receiver use timers to detect and handle lost or corrupted packets .
- The efficiency of the stop and wait protocol is low, as the sender remains idle for most of the time.
- The efficiency can be calculated as: Efficiency = Tt / (Tt + 2Tp), where Tt is the transmission time and Tp is the propagation time.



### Experiment 1.2 - Implementation of Sliding Window Protocol

- Sliding window protocol is a feature of packet-based data transmission protocols that ensures reliable and sequential delivery of data frames  .
- Sliding window protocol uses a window size that determines how many frames can be sent by the sender before receiving an acknowledgment from the receiver  .
- Sliding window protocol can improve the efficiency of data transmission by sending more than one frame at a time with a larger sequence number, which is similar to pipelining in architecture.
- Sliding window protocol can handle errors and losses by using different techniques, such as stop-and-wait, go-back-N, and selective repeat   .
- Sliding window protocol can also be used in the Transmission Control Protocol (TCP) to control the flow and congestion of data packets .

The steps to implement the sliding window protocol are:

1. The sender and the receiver agree on the window size, which is the maximum number of frames that can be sent or received at a time.
2. The sender assigns a sequence number to each frame and sends them to the receiver within the window size.
3. The receiver sends an acknowledgment (ACK) to the sender for each frame it receives, indicating the next expected sequence number.
4. The sender slides the window forward by the number of frames that have been acknowledged by the receiver, and sends more frames if available.
5. The receiver slides the window forward by the number of frames that have been received and processed, and expects more frames from the sender.
6. If the sender does not receive an ACK from the receiver within a certain time, it assumes that the frame has been lost or corrupted, and retransmits the frame.
7. If the receiver receives a frame that is out of order or has an incorrect sequence number, it discards the frame and sends a negative acknowledgment (NAK) to the sender, indicating the expected sequence number.
8. The sender and the receiver repeat the steps until all the frames have been transmitted and received successfully.



## Experiment 2 - Study of Socket Programming and Client – Server model

- Socket programming is a way of enabling two programs to communicate over a network using a well-established protocol.
- A socket is a communication channel that connects a client and a server, allowing them to exchange data in both directions.
- A client is a program that requests a service or resource from a server, which is a program that provides the service or resource.
- The client-server model is a distributed application structure that partitions tasks between the providers of a service (servers) and the requesters of a service (clients).
- There are two types of sockets: stream sockets and datagram sockets.
  - Stream sockets, also known as connection-oriented sockets, establish a connection before transferring data. They are reliable, in-order, and use Transmission Control Protocol (TCP).
  - Datagram sockets, also known as connectionless sockets, do not require a connection before transferring data. They are unreliable, out-of-order, and use User Datagram Protocol (UDP).
- To create a socket, we need to specify the domain, the type, and the protocol of the socket.
  - The domain specifies the address family of the socket, such as IPv4, IPv6, or Unix domain.
  - The type specifies the communication semantics of the socket, such as stream or datagram.
  - The protocol specifies the protocol to be used by the socket, such as TCP or UDP.
- To use a socket, we need to perform some steps to establish a connection between the client and the server.
  - The server needs to bind the socket to an address that clients can use to find the server.
  - The server needs to listen for incoming connection requests from clients on the socket.
  - The server needs to accept a connection request from a client and create a new socket for the communication.
  - The client needs to connect to the server's socket using the server's address.
  - The client and the server can then send and receive data using the socket.
  - The client and the server need to close the socket when the communication is finished.



### Experiment 2.1 - Study of Socket Programming

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A node represents a computer or a physical device with an internet connection.
- A socket is the endpoint used for connecting to a node. It is created by the combination of the IP address and port number of the software.
- Socket programming tells us how we can use socket API for creating communication between local and remote processes.
- Socket programming can be done in different languages, such as C, C++, Python, Java, etc. Each language has its own socket library and functions .
- Socket programming can be classified into two types: TCP and UDP. TCP stands for Transmission Control Protocol and UDP stands for User Datagram Protocol. TCP is reliable, ordered and error-checked, while UDP is unreliable, unordered and not error-checked.
- Socket programming can be used for various applications, such as web browsing, email, chat, file transfer, remote login, etc.
- Socket programming can be learned by following some steps, such as:
  - Understanding the basic concepts of network communication, such as IP addresses, ports, protocols, etc.
  - Choosing a programming language and a socket library to work with.
  - Creating a socket using the socket function and specifying the domain, type and protocol.
  - Setting the socket options using the setsockopt function to manipulate the socket behavior.
  - Binding the socket to a specific address and port using the bind function.
  - Listening for incoming connections using the listen function (for server sockets) or connecting to a remote socket using the connect function (for client sockets).
  - Accepting a connection from a client socket using the accept function (for server sockets) or sending and receiving data using the send and recv functions (for client sockets).
  - Closing the socket using the close function when the communication is over.



### Experiment 2.2 - Study of Client – Server model

- The client-server model is a distributed computing paradigm that divides tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.
- The clients and servers communicate over a computer network or, in some cases, on the same machine.
- A client does not share any of its resources, but requests a server's content or service function. Clients therefore initiate communication sessions with servers, which await incoming requests.
- Examples of computer applications that use the client-server model are email, network printing, and the World Wide Web.
- The client-server model can be classified into two types: thin client and thick client.
- A thin client is a client that relies heavily on the server for processing and data management. For example, a web browser is a thin client that requests web pages from web servers.
- A thick client is a client that performs most or all of the processing and data management itself, and uses the server mainly for storage or backup. For example, an email client is a thick client that can compose and read emails without a server, but uses a server to send and receive emails.
- The advantages of the client-server model are:
  - It allows for centralized management and control of data and resources.
  - It reduces network traffic by sending only the requested data or service to the client.
  - It improves scalability and performance by distributing the workload among multiple servers.
  - It supports interoperability and compatibility among different platforms and devices.
- The disadvantages of the client-server model are:
  - It creates a single point of failure if the server goes down or is overloaded.
  - It increases the security risks and vulnerabilities of the server and the data stored on it.
  - It requires more maintenance and administration costs for the server.



## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is used to map a network layer address (such as an IP address) to a data link layer address (such as a MAC address).
- RARP stands for Reverse Address Resolution Protocol. It is used to map a data link layer address to a network layer address.
- Both ARP and RARP use the same packet format, which consists of the following fields:
  - Hardware type: specifies the type of hardware used for the local network, such as Ethernet or Token Ring.
  - Protocol type: specifies the type of protocol used for the network layer, such as IP or IPX.
  - Hardware length: specifies the length of the hardware address in bytes.
  - Protocol length: specifies the length of the protocol address in bytes.
  - Operation: specifies the type of operation, such as ARP request, ARP reply, RARP request, or RARP reply.
  - Sender hardware address: specifies the hardware address of the sender of the packet.
  - Sender protocol address: specifies the protocol address of the sender of the packet.
  - Target hardware address: specifies the hardware address of the target of the packet.
  - Target protocol address: specifies the protocol address of the target of the packet.
- The following is a pseudocode for simulating ARP /RARP protocols:

  ```
  # Define a class for ARP /RARP packets
  class ARPPacket:
    # Initialize the packet with the given fields
    def __init__(self, htype, ptype, hlen, plen, op, sha, spa, tha, tpa):
      self.htype = htype # Hardware type
      self.ptype = ptype # Protocol type
      self.hlen = hlen # Hardware length
      self.plen = plen # Protocol length
      self.op = op # Operation
      self.sha = sha # Sender hardware address
      self.spa = spa # Sender protocol address
      self.tha = tha # Target hardware address
      self.tpa = tpa # Target protocol address

    # Display the packet fields
    def show(self):
      print("Hardware type:", self.htype)
      print("Protocol type:", self.ptype)
      print("Hardware length:", self.hlen)
      print("Protocol length:", self.plen)
      print("Operation:", self.op)
      print("Sender hardware address:", self.sha)
      print("Sender protocol address:", self.spa)
      print("Target hardware address:", self.tha)
      print("Target protocol address:", self.tpa)

  # Define a list of hosts with their hardware and protocol addresses
  hosts = [
    {"ha": "00:0a:95:9d:68:16", "pa": "192.168.0.1"},
    {"ha": "00:0a:95:9d:68:17", "pa": "192.168.0.2"},
    {"ha": "00:0a:95:9d:68:18", "pa": "192.168.0.3"},
    {"ha": "00:0a:95:9d:68:19", "pa": "192.168.0.4"},
    {"ha": "00:0a:95:9d:68:20", "pa": "192.168.0.5"}
  ]

  # Define a function to simulate ARP /RARP
  def arp_rarp(packet):
    # Check the operation field of the packet
    if packet.op == 1: # ARP request
      # Loop through the hosts list
      for host in hosts:
        # Check if the target protocol address matches the host's protocol address
        if packet.tpa == host["pa"]:
          # Create an ARP reply packet with the host's hardware and protocol addresses
          reply = ARPPacket(packet.htype, packet.ptype, packet.hlen, packet.plen, 2, host["ha"], host["pa"], packet.sha, packet.spa)
          # Display the reply packet
          print("ARP reply:")
          reply.show()
          # Return the reply packet
          return reply
      # If no match is found, display an error message
      print("No host with the target protocol address found.")
    elif packet.op == 2: # ARP reply
      # Display the packet
      print("ARP reply:")
      packet.show()
    elif packet.op == 3: # RARP request
      # Loop through the hosts list
      for host in hosts:
        # Check if the target hardware address matches the host's hardware address

```




## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- PING and TRACEROUTE are two network diagnostic tools that can be used to test the connectivity and latency between two hosts on a network.
- PING sends a series of packets to a destination host and measures the time it takes for each packet to be echoed back. It also reports the packet loss rate and the round-trip time (RTT) statistics.
- TRACEROUTE traces the route that packets take from the source host to the destination host. It sends packets with increasing time-to-live (TTL) values and records the IP addresses of the routers that send back time-exceeded messages. It also measures the RTT for each hop along the path.
- To write a code simulating PING and TRACEROUTE commands, we need to use the socket module in Python, which provides low-level access to network interfaces. We also need to use the struct module to pack and unpack binary data, and the time module to measure the elapsed time.
- The following steps outline the basic algorithm for the code:

  - Create a raw socket with the ICMP protocol (Internet Control Message Protocol), which is used to send and receive error and control messages on the network.
  - Generate a unique identifier and a sequence number for each packet. The identifier and sequence number are used to match the echo request and echo reply packets.
  - Construct the ICMP header with the type, code, checksum, identifier, and sequence number fields. The type and code fields indicate the type of message, such as echo request or echo reply. The checksum field is used to verify the integrity of the packet. The identifier and sequence number fields are the same as the ones generated earlier.
  - Construct the ICMP payload with some arbitrary data. The payload can be any data, but it is usually a timestamp or a sequence of bytes.
  - Calculate the checksum of the ICMP header and payload and insert it into the header.
  - Pack the ICMP header and payload into a binary format using the struct module.
  - Send the packet to the destination host using the socket.sendto() method. Record the current time as the send time.
  - Wait for a response from the destination host using the socket.recvfrom() method. Record the current time as the receive time. If no response is received within a timeout period, report a timeout error and exit.
  - Unpack the response packet into the IP header and the ICMP header and payload using the struct module.
  - Check the type, code, identifier, and sequence number fields of the ICMP header to verify that it is a valid echo reply packet. If not, report an invalid packet error and exit.
  - Calculate the RTT by subtracting the send time from the receive time. Report the RTT, the packet size, and the destination IP address.
  - Repeat the above steps for a specified number of packets or until the user interrupts the program. Report the summary statistics, such as the minimum, maximum, average, and standard deviation of the RTT, and the packet loss rate.

- The following steps outline the basic algorithm for the TRACEROUTE code:

  - Create a raw socket with the ICMP protocol and another raw socket with the UDP protocol (User Datagram Protocol), which is used to send and receive datagrams on the network.
  - Generate a unique identifier and a sequence number for each packet. The identifier and sequence number are used to match the UDP datagram and the ICMP time-exceeded message.
  - Construct the UDP header with the source port, destination port, length, and checksum fields. The source port and destination port fields indicate the endpoints of the communication. The length field indicates the size of the UDP header and payload. The checksum field is used to verify the integrity of the packet. The source port can be any unused port, and the destination port can be any port that is unlikely to be open on the destination host, such as 33434.
  - Construct the UDP payload with some arbitrary data. The payload can be any data, but it is usually a timestamp or a sequence of bytes.
  - Calculate the checksum of the UDP header and payload and insert it into the header.
  - Pack the UDP header and payload into a binary format using the struct module.
  - Set the TTL value of the packet to 1 using the socket.setsockopt() method. The TTL value indicates how many hops the packet can traverse before being discarded by a router. By setting it to 1, we ensure that the packet will be discarded by the first router on the path and generate a time-exceeded message.
  - Send the packet to the destination host using the socket.sendto() method. Record the current time as the



## Experiment 5 - Create a socket for HTTP for web page upload and download

- A socket is an endpoint of a communication channel between two processes or devices over a network.
- HTTP (Hypertext Transfer Protocol) is a protocol that defines how messages are formatted and transmitted over the web, and how servers and clients should respond to various commands.
- To create a socket for HTTP, we need to use the socket module in Python, which provides a low-level interface to access network services.
- The steps to create a socket for HTTP are:

  - Import the socket module: `import socket`
  - Create a socket object: `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  - Specify the address and port of the server: `host = 'www.example.com'` and `port = 80`
  - Connect the socket to the server: `s.connect((host, port))`
  - Send an HTTP request to the server: `s.send(b'GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n')`
  - Receive the HTTP response from the server: `data = s.recv(1024)`
  - Print the response data: `print(data.decode())`
  - Close the socket: `s.close()`

- To upload and download web pages using the socket, we need to modify the HTTP request and response accordingly.
- For example, to upload a web page, we need to use the POST method instead of the GET method, and include the content of the web page in the request body.
- To download a web page, we need to parse the response data and extract the content of the web page from the response body.



## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

- Remote Procedure Call (RPC) is a mechanism that allows a program to invoke a function or a procedure in another process, possibly on a different machine, as if it were a local call.
- RPC enables data exchange and invocation of functionality residing in a different process.
- RPC can be implemented using various languages, such as C, C++, Java, etc. In this experiment, we will use C as the programming language.
- To implement RPC in C, we need to use some tools and libraries, such as:
  - Interface Definition Language (IDL) - a language that describes the parameters, functions and interfaces of the RPC application.
  - IDL Compiler - a tool that generates stubs and headers from the IDL file.
  - RPC Runtime Library - a library that provides the functions and data structures for RPC communication.
  - RPC Protocol Modules - modules that implement the underlying transport protocols for RPC, such as TCP, UDP, HTTP, etc.
- The steps to write a program to implement RPC in C are as follows:
  - Define the interface of the RPC application using IDL. The interface should specify the name, parameters and return type of the remote procedure, as well as any attributes or options.
  - Compile the IDL file using the IDL compiler. This will generate the stubs and headers for the client and the server.
  - Write the client program that invokes the remote procedure using the stubs and headers generated by the IDL compiler. The client program should link with the RPC runtime library and the appropriate RPC protocol module .
  - Write the server program that implements the remote procedure using the stubs and headers generated by the IDL compiler. The server program should also link with the RPC runtime library and the appropriate RPC protocol module .
  - Compile and run the client and the server programs on the same or different machines, depending on the RPC protocol used .
- For example, suppose we want to implement a simple RPC application that calculates the sum of two integers. The IDL file, the client program and the server program are shown below:

```c
// sum.idl - the interface definition file for the RPC application
[ uuid(12345678-1234-abcd-ef00-0123456789ab), version(1.0) ]
interface sum
{
    // The remote procedure declaration
    [idempotent] int add([in] int a, [in] int b);
}
```

```c
// sum_client.c - the client program for the RPC application
#include <stdio.h>
#include <windows.h>
#include "sum.h" // the header file generated by the IDL compiler

int main()
{
    RPC_STATUS status; // the status of the RPC operation
    int a, b, c; // the input and output parameters
    unsigned char* szStringBinding = NULL; // the string binding

    // Create a string binding handle.
    status = RpcStringBindingCompose(
        NULL, // UUID to bind to
        (unsigned char*) "ncacn_ip_tcp", // use TCP/IP protocol
        (unsigned char*) "localhost", // network address to use
        (unsigned char*) "4747", // endpoint to use
        NULL, // protocol dependent network options to use
        &szStringBinding); // output string binding

    if (status)
        exit(status);

    // Set the binding handle that will be used to bind to the server.
    status = RpcBindingFromStringBinding(
        szStringBinding, // the string binding to validate
        &sum_IfHandle); // output binding handle

    if (status)
        exit(status);

    // Free the memory allocated by a string.
    status = RpcStringFree(
        &szStringBinding); // string to be freed

    if (status)
        exit(status);

    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);

    // Call the remote procedure "add" with the parameters a and b.
    c = add(a, b);

    printf("The sum is %d\n", c);

    // Free the binding handle
    status = RpcBindingFree(
        &sum_IfHandle); // binding handle to be freed

    if (status)
        exit(status);

    return 0

```




## Experiment 7 - Implementation of Subnetting

- Subnetting is a technique of dividing a network into smaller subnetworks, each with its own range of IP addresses and subnet mask.
- Subnetting can improve network performance, security, and scalability by reducing the size of the broadcast domain and the routing table.
- Subnetting can be done by borrowing bits from the host portion of an IP address and using them to create subnets.
- The number of subnets and hosts per subnet depends on the subnet mask, which is a 32-bit binary number that indicates which bits of the IP address belong to the network and which belong to the host.
- The subnet mask can be written in dotted decimal notation, such as 255.255.255.0, or in slash notation, such as /24, which indicates the number of network bits.
- To calculate the number of subnets and hosts per subnet, the following formulas can be used:

  - Number of subnets = 2^n, where n is the number of borrowed bits
  - Number of hosts per subnet = 2^m - 2, where m is the number of remaining host bits
  - For example, if the subnet mask is 255.255.255.192 or /26, then n = 2 and m = 6, so the number of subnets is 2^2 = 4 and the number of hosts per subnet is 2^6 - 2 = 62.

- To find the subnet address, host address, and broadcast address of a given IP address and subnet mask, the following steps can be followed:

  - Convert the IP address and subnet mask to binary
  - Perform a bitwise AND operation between the IP address and subnet mask to get the subnet address
  - To get the host address, replace the network bits with zeros and the host bits with the binary value of the IP address
  - To get the broadcast address, replace the network bits with ones and the host bits with the binary value of the IP address
  - Convert the subnet address, host address, and broadcast address back to dotted decimal notation
  - For example, if the IP address is 192.168.1.100 and the subnet mask is 255.255.255.192 or /26, then the subnet address, host address, and broadcast address are:

    - Subnet address: 192.168.1.64
    - Host address: 192.168.1.100
    - Broadcast address: 192.168.1.127



## Experiment 8 - Applications using TCP Sockets

TCP sockets are a type of network communication mechanism that allows two processes to exchange data using the Transmission Control Protocol (TCP). TCP is a reliable, connection-oriented protocol that ensures the data is delivered in order and without errors. TCP sockets can be used to implement various network applications, such as:

- **File transfer**: TCP sockets can be used to send and receive files between a client and a server. The client can request a file from the server by sending its name, and the server can send the file contents in chunks until the end of file is reached. The client can acknowledge each chunk and request the next one until the file transfer is complete. An example of a file transfer application using TCP sockets is the File Transfer Protocol (FTP).
- **Remote command execution**: TCP sockets can be used to execute commands on a remote machine by sending the command as a string and receiving the output as a stream of bytes. The client can send a command to the server, and the server can execute the command using a system call and send the output back to the client. An example of a remote command execution application using TCP sockets is the Secure Shell (SSH).
- **Chat**: TCP sockets can be used to implement a chat application that allows multiple users to communicate with each other in real time. The client can send a message to the server, and the server can broadcast the message to all the other connected clients. The client can also receive messages from the server and display them on the screen. An example of a chat application using TCP sockets is the Internet Relay Chat (IRC).
- **Web**: TCP sockets can be used to implement a web application that allows a client to request and receive web pages from a server. The client can send a request to the server using the Hypertext Transfer Protocol (HTTP), and the server can send the response back to the client using the same protocol. The response can contain text, images, videos, or other types of media. An example of a web application using TCP sockets is the World Wide Web (WWW).



### Experiment 8.1 - Echo client and echo server

- An echo client and echo server are applications that allow a client and a server to communicate over a network using sockets     .
- The client sends a message to the server and the server receives the message and sends, or echoes, it back to the client     .
- The echo functionality is useful for testing the connectivity and performance of the network and the applications .
- The echo client and server can be implemented using different protocols, such as TCP or UDP   .
- TCP is a reliable, connection-oriented protocol that ensures the delivery and order of the messages   .
- UDP is an unreliable, connectionless protocol that does not guarantee the delivery and order of the messages   .
- The echo client and server can be implemented using different programming languages, such as Java, Python, or C   .
- The echo client and server can be implemented using different threading models, such as single-threaded or multi-threaded  .
- A single-threaded server means that it accepts only one client connection at a time  .
- A multi-threaded server means that it can handle multiple client connections concurrently using threads  .
- The echo client and server can be implemented using different socket APIs, such as BSD sockets or Java sockets   .
- A socket API is a set of functions and data structures that allow applications to create and manipulate sockets   .
- A socket is an endpoint of communication between two processes on a network   .
- A socket has an address, which consists of an IP address and a port number   .
- An IP address is a numerical identifier that uniquely identifies a host on a network   .
- A port number is a numerical identifier that uniquely identifies a process on a host   .
- The echo client and server can be implemented using different message formats, such as text or binary   .
- A text message is a sequence of characters that can be encoded and decoded using a character set, such as ASCII or UTF-8   .
- A binary message is a sequence of bytes that can be interpreted according to a specific protocol or format, such as JPEG or MP3   .
- The echo client and server can be implemented using different message delimiters, such as newline or length-prefix   .
- A message delimiter is a special character or sequence of characters that indicates the end or the length of a message   .
- A newline delimiter is a character or sequence of characters that represents a line break, such as \n or \r\n   .
- A length-prefix delimiter is a sequence of characters that represents the length of the message, such as 4HELLO or 10HELLO WORLD   .
- The echo client and server can be implemented using different message buffers, such as fixed-size or dynamic-size



### Experiment 8.2 - Chat

- The objective of this experiment is to learn how to create a simple chat application using HTML, CSS and JavaScript.
- The chat application will allow two or more users to communicate with each other in real time over the internet.
- The chat application will consist of the following components:
  - A web server that will host the chat application and handle the requests from the clients.
  - A web socket that will enable bidirectional communication between the server and the clients.
  - A web page that will display the chat interface and allow the user to send and receive messages.
  - A database that will store the chat history and the user information.
- The steps involved in creating the chat application are as follows:
  - Set up the web server using Node.js and Express.js.
  - Set up the web socket using Socket.io.
  - Set up the database using MongoDB and Mongoose.
  - Create the web page using HTML, CSS and Bootstrap.
  - Create the chat interface using JavaScript and jQuery.
  - Add the functionality to send and receive messages using Socket.io and jQuery.
  - Add the functionality to register and login users using MongoDB and Passport.js.
  - Add the functionality to display the chat history and the online users using MongoDB and jQuery.
  - Test and debug the chat application using Chrome DevTools and Postman.



### Experiment 8.3 - File Transfer

- The objective of this experiment is to learn how to transfer files between different devices using various protocols and tools.
- The prerequisites for this experiment are:
  - Basic knowledge of networking concepts and protocols such as TCP/IP, FTP, HTTP, SCP, etc.
  - Access to at least two devices (such as computers, smartphones, tablets, etc.) that can connect to the same network or the internet.
  - Familiarity with the operating systems and command-line interfaces of the devices.
- The steps for this experiment are:
  1. Identify the source and destination devices and the files to be transferred.
  2. Choose an appropriate protocol and tool for the file transfer, depending on the type, size, and security of the files and the devices.
  3. Install and configure the necessary software or applications on the devices, if required.
  4. Establish a connection between the devices using the protocol and tool.
  5. Initiate the file transfer and monitor the progress and status of the operation.
  6. Verify the integrity and availability of the transferred files on the destination device.
  7. Terminate the connection and close the software or applications on the devices.
- The expected outcomes of this experiment are:
  - The ability to transfer files between different devices using various protocols and tools.
  - The understanding of the advantages and disadvantages of different protocols and tools for file transfer.
  - The awareness of the security and ethical issues related to file transfer.



## Experiment 9 - Applications using TCP and UDP Sockets

- A socket is an endpoint of communication between two processes or devices over a network.
- A socket is identified by a combination of an IP address and a port number.
- A port is a logical number that identifies a specific application or service on a device.
- There are two types of sockets: stream sockets and datagram sockets.
- Stream sockets use TCP (Transmission Control Protocol), which is a reliable, stream-oriented protocol that ensures that all data is delivered in order and without errors.
- Datagram sockets use UDP (User Datagram Protocol), which is an unreliable, message-oriented protocol that does not guarantee delivery, order, or error detection.
- TCP and UDP are both protocols that operate on top of the IP protocol, which is responsible for routing packets across the Internet.
- TCP and UDP sockets can use the same port number, but they are not related to each other. TCP ports are interpreted by the TCP stack, while the UDP stack interprets UDP ports.
- TCP and UDP sockets have different characteristics and applications, depending on the requirements of the communication.
- TCP sockets are suitable for applications that need reliable and ordered data transfer, such as web browsing, file transfer, email, etc.
- UDP sockets are suitable for applications that need fast and lightweight data transfer, such as video streaming, online gaming, voice over IP, etc.

Some examples of applications using TCP and UDP sockets are:

- A web browser uses a TCP socket to connect to a web server and request a web page. The web server uses another TCP socket to send the web page back to the browser.
- A video conferencing application uses a UDP socket to send and receive audio and video data between the participants. The UDP socket allows for low latency and high bandwidth communication, but some packets may be lost or out of order.
- A chat application uses a TCP socket to establish a connection between the sender and the receiver, and then uses another TCP socket to send and receive text messages. The TCP socket ensures that the messages are delivered reliably and in order.
- A DNS (Domain Name System) client uses a UDP socket to send a query to a DNS server, asking for the IP address of a domain name. The DNS server uses another UDP socket to send the response back to the client. The UDP socket allows for fast and simple communication, but the query or the response may be lost or corrupted.



### Experiment 9.1 - DNS

- DNS stands for Domain Name System. It is a distributed database that maps domain names to IP addresses and other information.
- DNS allows users to access websites and other resources using human-readable names instead of numerical addresses.
- DNS consists of a hierarchical structure of name servers that store and resolve domain names.
- The root name servers are the top-level name servers that manage the root zone of the DNS namespace. They delegate authority to lower-level name servers for different top-level domains (TLDs) such as .com, .org, .edu, etc.
- The authoritative name servers are the name servers that have the definitive information about a specific domain name and its subdomains. They are responsible for answering queries from other name servers or clients.
- The recursive name servers are the name servers that act as intermediaries between clients and authoritative name servers. They cache the results of previous queries to improve performance and reduce network traffic.
- The DNS resolver is the software component that runs on the client side and initiates DNS queries to resolve domain names to IP addresses. It may use a local cache or a configured recursive name server to perform the resolution.
- The DNS protocol is the set of rules and formats that define how DNS messages are exchanged between name servers and clients. It uses UDP as the transport layer protocol for most queries and TCP for zone transfers and some large responses.
- The DNS message consists of a header and four sections: question, answer, authority, and additional. The header contains fields such as identification, flags, and counts. The question section contains the domain name and the type of record to be queried. The answer section contains the resource records that match the query. The authority section contains the name servers that are authoritative for the domain name. The additional section contains other resource records that may be useful for the query.
- The DNS resource record is the basic unit of information in the DNS database. It consists of a name, a type, a class, a time-to-live, and a data field. The type specifies the kind of information stored in the data field, such as A (address), NS (name server), MX (mail exchange), CNAME (canonical name), etc. The class specifies the protocol family, such as IN (Internet). The time-to-live specifies how long the record can be cached by other name servers or clients. The data field contains the actual information, such as an IP address, a domain name, a preference value, etc.



### Experiment 9.2 - SNMP

- SNMP stands for Simple Network Management Protocol. It is a standard protocol for managing devices on a network, such as routers, switches, servers, printers, etc.
- SNMP operates on the application layer of the OSI model. It uses UDP as the transport protocol and port 161 for requests and port 162 for notifications.
- SNMP consists of three components: SNMP managers, SNMP agents, and management information base (MIB).
  - SNMP managers are software applications that run on network management systems (NMS). They initiate queries and receive responses from SNMP agents. They can also receive unsolicited notifications (traps or informs) from SNMP agents.
  - SNMP agents are software modules that run on managed devices. They collect and store information about the device's status and configuration in the MIB. They respond to queries and send notifications to SNMP managers.
  - MIB is a hierarchical database that defines the variables (objects) that can be accessed by SNMP. Each object has a unique identifier (OID) and a data type. MIB is divided into two parts: standard MIB and vendor-specific MIB. Standard MIB defines common objects for all devices, such as system name, uptime, interface statistics, etc. Vendor-specific MIB defines additional objects for specific devices, such as CPU temperature, fan speed, etc.
- SNMP has four basic operations: GET, GETNEXT, SET, and TRAP (or INFORM).
  - GET is used by SNMP managers to request the value of one or more objects from SNMP agents.
  - GETNEXT is used by SNMP managers to request the value of the next object in the MIB from SNMP agents.
  - SET is used by SNMP managers to modify the value of one or more objects on SNMP agents.
  - TRAP (or INFORM) is used by SNMP agents to send unsolicited notifications to SNMP managers about significant events or changes on the device.
- SNMP has three versions: SNMPv1, SNMPv2c, and SNMPv3.
  - SNMPv1 is the original version of SNMP. It supports only GET, GETNEXT, and TRAP operations. It uses community strings as a simple form of authentication and authorization. Community strings are plain-text passwords that are sent along with SNMP messages. They determine the access level (read-only or read-write) of the SNMP manager to the SNMP agent. The default community strings are "public" for read-only access and "private" for read-write access.
  - SNMPv2c is an extension of SNMPv1. It adds support for GETBULK, INFORM, and RESPONSE operations. GETBULK is used by SNMP managers to request multiple objects in a single message from SNMP agents. INFORM is similar to TRAP, but it requires an acknowledgment from the SNMP manager. RESPONSE is used by SNMP agents to acknowledge INFORM messages. SNMPv2c also improves the performance and error handling of SNMP. It still uses community strings as the security mechanism.
  - SNMPv3 is the latest and most secure version of SNMP. It adds support for encryption, authentication, and authorization. It uses user-based security model (USM) and view-based access control model (VACM) as the security mechanisms. USM defines how SNMP messages are encrypted and authenticated using different algorithms and keys. VACM defines who can access which objects on the SNMP agent using different views and groups. SNMPv3 also supports SNMPv1 and SNMPv2c messages for backward compatibility.



### Experiment 9.3 - File Transfer

- File transfer is the process of copying or moving a file from one computer to another over a network or the Internet.
- File transfer can be done using different protocols, such as FTP, HTTP, SCP, SFTP, etc.
- File transfer can be used for various purposes, such as sharing data, backing up data, updating software, etc.
- File transfer can be performed in different modes, such as binary, ASCII, or auto.
- File transfer can be affected by various factors, such as network speed, file size, file type, encryption, compression, etc.
- File transfer can be monitored and controlled using various tools, such as progress bars, checksums, logs, etc.

- In this experiment, you will learn how to perform file transfer using FTP and SCP protocols.
- You will need two computers connected to the same network or the Internet, and a FTP server and a SCP server running on one of them.
- You will also need a FTP client and a SCP client software installed on both computers.
- You will use the FTP client and the SCP client to connect to the FTP server and the SCP server respectively, and transfer files between the computers.
- You will compare the speed, security, and reliability of the file transfer using FTP and SCP protocols.



## Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

- Network simulator (NS) is a discrete event simulator for network research and education.
- NS can model various network protocols, topologies, traffic patterns, and performance metrics.
- NS is written in C++ and Tcl, and uses an object-oriented approach to design and implement network components.
- NS has a graphical user interface called NAM (Network Animator) that can visualize network simulations and animations.
- NS can simulate various congestion control algorithms, such as TCP, UDP, Reno, NewReno, Vegas, SACK, etc.
- Congestion control algorithms are mechanisms to regulate the flow of data packets in a network and avoid congestion collapse.
- Congestion collapse occurs when the network becomes overloaded and the throughput drops significantly.
- Congestion control algorithms can be classified into two categories: window-based and rate-based.
- Window-based algorithms adjust the size of the sender's window, which is the number of packets that can be sent without receiving an acknowledgment.
- Rate-based algorithms adjust the sending rate of the sender, which is the number of packets that can be sent per unit time.
- Some of the factors that affect the performance of congestion control algorithms are: network bandwidth, delay, packet loss, queue size, etc.
- To simulate congestion control algorithms using NS, the following steps are required:
  - Define the network topology, such as the number and type of nodes, links, and queues.
  - Define the traffic sources and sinks, such as the type and parameters of the application layer protocols.
  - Define the transport layer protocols, such as the type and parameters of the congestion control algorithms.
  - Define the output files and variables, such as the trace files, NAM files, and performance metrics.
  - Run the simulation and analyze the results, such as the throughput, delay, packet loss, etc.



## Experiment 11 - Perform a case study about the different routing algorithms to select the network path with its optimum and economical during data transfer

- Routing is the process of finding a path for data packets to reach their destination in a network.
- Routing algorithms are the rules or methods that determine how routers choose the best path for data packets.
- Different routing algorithms have different objectives, such as minimizing delay, maximizing throughput, minimizing cost, or maximizing reliability.
- Some of the common routing algorithms are:

  - Shortest Path Routing: This algorithm chooses the path with the least number of hops or links between the source and the destination. It can use different metrics to measure the length of a path, such as distance, bandwidth, or delay. It is simple and efficient, but it may not consider the current traffic conditions or the quality of the links.
  - Flooding: This algorithm sends a copy of every data packet to every outgoing link, except the one it arrived on. It guarantees that the packet will reach the destination, but it generates a lot of redundant traffic and wastes network resources. It is usually used for broadcasting or multicasting purposes, or as a backup mechanism in case of link failures.
  - Distance Vector Routing: This algorithm maintains a table of distances to every other node in the network, and updates it periodically by exchanging information with its neighbors. It uses the Bellman-Ford algorithm to calculate the shortest path to each destination based on the distance vectors. It is easy to implement and scalable, but it may suffer from slow convergence, routing loops, or count-to-infinity problems.
  - Link State Routing: This algorithm maintains a map of the entire network topology, and updates it by sending link state packets to all other nodes whenever there is a change in the link status. It uses the Dijkstra's algorithm to calculate the shortest path to each destination based on the link state information. It is more accurate and robust than distance vector routing, but it requires more memory and bandwidth to store and transmit the link state packets.
  - Hierarchical Routing: This algorithm divides the network into smaller regions or domains, and assigns a level of hierarchy to each node. It uses different routing algorithms within and between the regions, depending on the level of hierarchy. It reduces the size and complexity of the routing tables, and allows for more flexibility and scalability, but it may increase the path length and delay.



### Experiment 11.1 - Link State Routing

- Link state routing is a type of routing algorithm that uses the information about the state of each link (such as bandwidth, delay, cost, etc.) to calculate the best path from one node to every other node in the network.
- Link state routing is also known as Dijkstra's algorithm, which is an iterative algorithm that finds the shortest path from a source node to all other nodes by using a priority queue to store the nodes with the least cost path so far.
- Link state routing requires each node to construct a map of the network topology, in the form of a graph, by exchanging messages with all other nodes in the network. These messages are called link state advertisements (LSAs) and they contain the information about the node's identity, its neighbors, and the cost of each link.
- Link state routing has some advantages over distance-vector routing, such as faster convergence, less routing loops, and more accurate routing information. However, it also has some disadvantages, such as higher memory and CPU usage, more bandwidth consumption, and more complexity.
- Link state routing protocols are widely used in packet switching networks for computer communications, such as Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).
- Link state routing protocols have some common features, such as hierarchical structure, flooding mechanism, reliable delivery, and authentication.



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
- Flooding can be measured by various indicators, such as flood frequency, flood duration, flood magnitude, and flood extent.
- Flood frequency is the average number of times a flood of a given size occurs in a given period of time.
- Flood duration is the length of time that a flood lasts.
- Flood magnitude is the amount of water that flows during a flood, usually expressed in cubic meters per second or cubic feet per second.
- Flood extent is the area that is covered by water during a flood, usually expressed in square kilometers or square miles.
- Flooding can be prevented or mitigated by various methods, such as:
  - Building levees, dams, or reservoirs to control water flow and storage.
  - Implementing flood warning systems and emergency plans to alert and evacuate people.
  - Restoring natural floodplains and wetlands to absorb excess water and reduce runoff.
  - Adopting sustainable land use and water management practices to reduce soil erosion and water pollution.



### Experiment 11.3 - Distance vector routing algorithm

- Distance vector routing is a dynamic routing protocol that uses the Bellman-Ford algorithm to find the shortest paths between nodes in a network  .
- Distance vector routing works by having each router maintain a routing table that contains the distance and direction (or vector) to each destination in the network .
- Each router periodically exchanges its routing table with its directly connected neighbors, and updates its own table based on the information received  .
- Distance vector routing is simple, easy to implement, and scalable for large networks . However, it also has some drawbacks, such as slow convergence, counting to infinity problem, and routing loops  .
- To improve the performance and reliability of distance vector routing, some enhancements have been proposed, such as split horizon, poison reverse, triggered updates, and hold-down timers  .
- Some examples of distance vector routing protocols are Routing Information Protocol (RIP), Interior Gateway Routing Protocol (IGRP), and Enhanced Interior Gateway Routing Protocol (EIGRP) .



## Experiment 12 - To learn handling and configuration of networking hardware like RJ-45 connector, CAT-6 cable, crimping tool, etc

- **Objective**: To understand the basic components and tools used for creating a wired network using Ethernet cables and connectors.
- **Theory**: A wired network is a type of network that uses cables to connect devices such as computers, routers, switches, etc. The most common type of cable used for wired networks is the twisted pair cable, which consists of four pairs of wires twisted together to reduce electromagnetic interference. The twisted pair cable can be classified into different categories based on the speed and bandwidth they support, such as CAT-5, CAT-5e, CAT-6, CAT-6a, etc. The higher the category, the better the performance and quality of the cable. The most widely used category for wired networks is CAT-6, which supports up to 10 Gbps of data transfer and up to 250 MHz of frequency.
- **Hardware**: The hardware required for this experiment are as follows:
  - RJ-45 connector: This is a type of connector that is used to terminate the twisted pair cable and connect it to a device. It has eight pins that correspond to the eight wires in the cable. The RJ-45 connector can be either male or female, depending on whether it has protruding pins or sockets. The male connector is usually attached to the cable, while the female connector is usually embedded in the device.
  - CAT-6 cable: This is a type of twisted pair cable that supports up to 10 Gbps of data transfer and up to 250 MHz of frequency. It has four pairs of wires, each with a different color code: orange, green, blue, and brown. Each pair consists of a solid-colored wire and a white wire with a stripe of the same color. The CAT-6 cable can be either straight-through or crossover, depending on how the wires are arranged in the RJ-45 connector. A straight-through cable has the same order of wires on both ends, while a crossover cable has the order of wires reversed on one end. A straight-through cable is used to connect devices of different types, such as a computer and a router, while a crossover cable is used to connect devices of the same type, such as two computers or two routers.
  - Crimping tool: This is a tool that is used to attach the RJ-45 connector to the CAT-6 cable. It has a slot that fits the RJ-45 connector and a lever that applies pressure to the pins and wires, creating a secure connection. The crimping tool also has a blade that can cut and strip the cable, exposing the wires inside.
- **Procedure**: The steps to create a wired network using the hardware are as follows:
  - Step 1: Cut a desired length of CAT-6 cable using the blade of the crimping tool. Be careful not to damage the wires inside the cable.
  - Step 2: Strip about 2 cm of the outer insulation of the cable using the blade of the crimping tool. Be careful not to cut the wires inside the cable.
  - Step 3: Untwist the four pairs of wires and arrange them in the correct order according to the type of cable you want to make. For a straight-through cable, the order is: orange-white, orange, green-white, blue, blue-white, green, brown-white, brown. For a crossover cable, the order is: green-white, green, orange-white, blue, blue-white, orange, brown-white, brown. Make sure the wires are aligned and parallel to each other.
  - Step 4: Cut the wires to the same length, leaving about 1.5 cm of exposed wire. Make sure the wires are straight and not bent or twisted.
  - Step 5: Insert the wires into the RJ-45 connector, making sure they match the pins. The pins are numbered from 1 to 8, from left to right when looking at the connector from the front. The wires should be inserted from the back of the connector, with the clip facing down. The wires should be fully inserted until they reach the end of the connector.
  - Step 6: Place the RJ-45 connector into the slot of the crimping tool, with the clip facing down. Squeeze the lever of the crimping tool firmly, applying pressure to the pins and wires. This will create a secure connection between the connector and the cable. Repeat steps 1 to 6 for the other end of the cable, using the same or opposite order of wires depending on the type of cable you want to make.
  - Step 7: Test the cable using a network tester



## Experiment 13 - Configuration of router, hub, switch etc. (using real devices or simulators)

- A router is a device that routes data packets based on their IP addresses. It can connect different networks, such as LANs and WANs, and perform functions such as assigning IP addresses, acting as a switch, and protecting the network .
- A hub is a device that connects multiple computers to create a LAN. It broadcasts all the data packets it receives to all the connected devices, regardless of their destination.
- A switch is a device that also connects multiple computers to create a LAN, but unlike a hub, it knows which device the data packet is intended for and sends it there. This reduces network congestion and improves security.
- To configure a router, you need to enter the Router Configuration mode, using the `configure terminal` command on Cisco devices, and then the Interface Configuration mode, using the `interface <interface name>` command. You can then set various parameters for the interface, such as IP address, subnet mask, speed, duplex mode, etc. You can also configure routing protocols, such as RIP, OSPF, EIGRP, etc., to enable the router to exchange routing information with other routers.
- To configure a switch, you need to enter the Switch Configuration mode, using the `configure terminal` command on Cisco devices, and then the Interface Configuration mode, using the `interface <interface name>` command. You can then set various parameters for the interface, such as speed, duplex mode, VLAN membership, port security, etc. You can also configure spanning tree protocol, trunking protocol, etc., to enable the switch to prevent loops, aggregate links, and carry traffic from multiple VLANs.
- To configure a hub, you do not need to do anything, as it is a plug-and-play device that does not have any intelligence or configuration options.
- To practice router and switch configuration, you can use a simulator or an emulator. A simulator is a software that mimics the behavior of a device, but does not run the actual IOS (the operating system of Cisco devices). A simulator may have missing commands or programming errors, and may not be as complete as the real IOS. An emulator is a software that runs the actual IOS image, and can provide a more realistic and accurate experience. However, an emulator may require more resources and may not be compatible with all IOS versions.
- Some examples of simulators are Packet Tracer, GNS3, and Boson NetSim. Some examples of emulators are Dynamips, Cisco VIRL, and EVE-NG.



## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

- The objective of this experiment is to learn how to use some common network services and commands that can help in troubleshooting, testing, and managing network connectivity and performance.
- The following are some of the services and commands that will be covered in this experiment:

  - **ping**: This command sends a series of packets to a destination host and measures the round-trip time and packet loss. It can be used to check if a host is reachable and responsive, and to test the network latency and reliability.
  - **traceroute**: This command traces the route that packets take from the source host to the destination host. It can be used to identify the intermediate routers and hops along the path, and to detect any network problems or bottleneecs that may affect the packet delivery.
  - **nslookup**: This command queries a domain name server (DNS) to obtain the IP address or the domain name of a host. It can be used to verify the DNS resolution and to diagnose any DNS issues.
  - **arp**: This command displays or modifies the address resolution protocol (ARP) cache, which maps IP addresses to MAC addresses. It can be used to view the MAC addresses of the hosts on the local network, and to add or delete ARP entries manually.
  - **telnet**: This command establishes a remote terminal session with a host using the telnet protocol. It can be used to access and manage a host remotely, and to test the connectivity and functionality of a service running on a specific port.
  - **ftp**: This command transfers files between hosts using the file transfer protocol (FTP). It can be used to upload or download files from a remote host, and to perform basic file operations such as listing, renaming, deleting, etc.

- The steps to run and use these services and commands are as follows:

  - **ping**: To ping a host, type `ping <host>` in the command prompt, where `<host>` can be an IP address or a domain name. For example, `ping 8.8.8.8` or `ping www.google.com`. To stop the ping, press Ctrl+C. To customize the ping parameters, such as the number of packets, the size of packets, the timeout, etc., use the appropriate options. For example, `ping -n 5 -l 100 -w 2000 8.8.8.8` will send 5 packets of 100 bytes each, with a timeout of 2000 milliseconds, to 8.8.8.8. To view the available options, type `ping /?`.
  - **traceroute**: To trace the route to a host, type `traceroute <host>` in the command prompt, where `<host>` can be an IP address or a domain name. For example, `traceroute 8.8.8.8` or `traceroute www.google.com`. The output will show the number of hops, the IP address and the hostname of each router, and the time taken for each hop. To customize the traceroute parameters, such as the maximum number of hops, the packet size, the timeout, etc., use the appropriate options. For example, `traceroute -m 10 -s 64 -w 1000 8.8.8.8` will trace the route to 8.8.8.8 with a maximum of 10 hops, a packet size of 64 bytes, and a timeout of 1000 milliseconds. To view the available options, type `traceroute /?`.
  - **nslookup**: To query a DNS server, type `nslookup <host>` in the command prompt, where `<host>` can be an IP address or a domain name. For example, `nslookup 8.8.8.8` or `nslookup www.google.com`. The output will show the name and the address of the DNS server, and the name and the address of the host. To specify a different DNS server, type `nslookup <host> <server>`, where `<server>` is the IP address or the domain name of the DNS server. For example, `nslookup www.google.com 8.8.4.4`. To enter the interactive mode, type `nslookup` without any arguments. In the interactive mode, you can type various commands to query different types of DNS records, such as A, CNAME, MX, NS, etc. To view the available commands, type `help` or `?`.
  - **arp**: To display the ARP cache, type `arp -a` in the command prompt.



## Experiment 15 - Network packet analysis using tools like Wireshark, tcpdump, etc

- Network packet analysis is the process of capturing, inspecting, and interpreting the data packets that are exchanged between devices on a network.
- Network packet analysis tools are software applications that can perform packet capture and analysis functions, such as filtering, decoding, reassembling, and displaying the packet data.
- Network packet analysis tools can help network administrators, security analysts, and forensic investigators to monitor network performance, troubleshoot network problems, detect network anomalies, and investigate network attacks.
- Some of the common network packet analysis tools are:

  - **Wireshark**: A free and open-source tool that can capture and analyze packets on various network protocols, such as TCP, UDP, ICMP, HTTP, DNS, etc. Wireshark has a graphical user interface (GUI) that allows users to view the packet data in different formats, such as hex dump, summary, detail, etc. Wireshark also has many features, such as filters, color codes, statistics, graphs, etc. that can help users to examine the packet data more easily .
  - **tcpdump**: A command-line tool that can capture and analyze packets on various network protocols, such as TCP, UDP, ICMP, etc. tcpdump can run on different operating systems, such as Linux, Windows, macOS, etc. tcpdump can display the packet data in a human-readable format, or save the packet data to a file for later analysis. tcpdump also supports filters, expressions, and options that can help users to specify the packets they want to capture and analyze.
  - **Colasoft Capsa**: A commercial tool that can capture and analyze packets on both wired and wireless networks. Colasoft Capsa has a GUI that allows users to view the packet data in different formats, such as dashboard, matrix, graph, etc. Colasoft Capsa also has many features, such as alerts, reports, diagnosis, etc. that can help users to monitor network performance, identify network problems, and detect network threats.
  - **Paessler PRTG**: A commercial tool that can capture and analyze packets on various network protocols, such as TCP, UDP, SNMP, etc. Paessler PRTG has a web-based interface that allows users to view the packet data in different formats, such as charts, tables, maps, etc. Paessler PRTG also has many features, such as sensors, notifications, dashboards, etc. that can help users to measure network bandwidth, optimize network usage, and troubleshoot network issues.
  - **Arkime**: A free and open-source tool that can capture and analyze packets on various network protocols, such as TCP, UDP, HTTP, DNS, etc. Arkime has a web-based interface that allows users to view the packet data in different formats, such as sessions, files, tags, etc. Arkime also has many features, such as queries, filters, plugins, etc. that can help users to search, analyze, and export the packet data.



## Experiment 16 - Network simulation using tools like Cisco Packet Tracer, NetSim, OMNeT++, NS2, NS3, etc

- Network simulation is the process of modeling the behavior and performance of a network using software tools.
- Network simulation tools can help students, researchers, and professionals to design, test, and analyze various network scenarios and protocols.
- Network simulation tools can also support network emulation, which is the integration of real and simulated network components.
- Some of the popular network simulation tools are:

  - Cisco Packet Tracer: A network simulation and visualization tool that allows users to create and configure network devices, protocols, and applications. It is mainly used for learning and teaching purposes. It supports Cisco devices and some IoT devices.
  - NetSim: A network simulation and emulation tool that supports a wide range of network technologies, such as wireless, mobile, LAN, WAN, IoT, etc. It also provides lab exercises and assignments for various network courses and certifications.
  - OMNeT++: An open source, modular, and component-based network simulation framework that can be extended with various libraries and models. It supports discrete event simulation, graphical user interface, and parallel simulation. It can be used to simulate various types of networks, such as software defined networks, sensor networks, vehicular networks, etc .
  - NS2: An open source, discrete event network simulator that can be used to simulate various network protocols and scenarios. It is written in C++ and OTcl. It supports mobile ad hoc networks, sensor networks, satellite networks, etc .
  - NS3: An open source, discrete event network simulator that is a successor of NS2. It is written in C++ and Python. It supports software defined networks, hybrid networks, LTE networks, etc .

- The objectives of this experiment are:

  - To learn the basic concepts and features of network simulation tools.
  - To compare and contrast the different network simulation tools and their capabilities.
  - To design and implement simple network scenarios using one or more network simulation tools.
  - To analyze and evaluate the network performance and behavior using various metrics and tools.



## Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A socket is an endpoint of a communication channel that can send and receive data using a protocol such as TCP or UDP.
- TCP (Transmission Control Protocol) is a connection-oriented, reliable, and stream-based protocol that ensures the delivery and ordering of data packets.
- UDP (User Datagram Protocol) is a connectionless, unreliable, and datagram-based protocol that does not guarantee the delivery and ordering of data packets.
- Stream sockets, datagram sockets, and raw sockets are the three types of socket programming interfaces.
- Stream sockets use TCP and provide a reliable and ordered stream of bytes between the nodes.
- Datagram sockets use UDP and provide an unreliable and unordered exchange of messages between the nodes.
- Raw sockets allow direct access to the network layer protocols and can be used to create custom protocols.
- Simple DNS (Domain Name System) is an application that translates domain names to IP addresses and vice versa using UDP sockets.
- Data and time client/server is an application that allows a client to request the current date and time from a server using TCP or UDP sockets.
- Echo client/server is an application that allows a client to send a message to a server and receive the same message back using TCP or UDP sockets.
- Iterative server is a server that handles one client request at a time in a sequential manner.
- Concurrent server is a server that handles multiple client requests at the same time using processes or threads.

