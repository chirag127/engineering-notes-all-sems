

## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

- Stop and wait protocol is a data link layer protocol that provides unidirectional data transmission over a noiseless channel.
- In this protocol, the sender sends one packet at a time and waits for an acknowledgment from the receiver before sending the next packet.
- The sender and the receiver use only two sequence numbers, 0 and 1, to identify the packets and avoid duplication.
- The efficiency of stop and wait protocol is low, as it depends on the ratio of propagation delay to transmission time.
- Sliding window protocol is a data link layer protocol that provides bidirectional data transmission over a noisy channel.
- In this protocol, the sender can send multiple packets without waiting for an acknowledgment, as long as the number of packets does not exceed the window size.
- The sender and the receiver use a sliding window to keep track of the sequence numbers of the packets that are sent, received, and acknowledged.
- The efficiency of sliding window protocol is high, as it utilizes the channel bandwidth more effectively.

: https://www.geeksforgeeks.org/stop-and-wait-arq/
: https://www.javatpoint.com/stop-and-wait-protocol
: https://www.scaler.com/topics/computer-network/stop-and-wait-protocol/
: https://www.geeksforgeeks.org/stop-and-wait-protocol-its-problems-and-solutions/
: https://www.javatpoint.com/sliding-window-protocol



### Experiment 1.1 - Implementation of Stop and Wait Protocol

The stop and wait protocol is a flow control protocol that belongs to the data link layer. It is used for transmitting data over noiseless channels. It provides unidirectional data transmission, which means that either sending or receiving of data will take place at a time.

The main idea of the stop and wait protocol is that the sender will not send the next packet to the receiver until the acknowledgment of the previous packet is received. This ensures that the packets are delivered in order and without errors.

The steps involved in the implementation of the stop and wait protocol are:

- The sender sends a data packet to the receiver and starts a timer.
- The receiver receives the data packet and sends an acknowledgment (ACK) packet back to the sender.
- The sender receives the ACK packet and stops the timer. Then it sends the next data packet and repeats the process.
- If the sender does not receive the ACK packet within the timeout period, it assumes that the data packet or the ACK packet was lost and retransmits the data packet.

The stop and wait protocol has some advantages and disadvantages. Some of the advantages are:

- It is simple and easy to implement.
- It avoids the problem of buffer overflow at the receiver side, as the receiver can process one packet at a time.
- It ensures reliable and in-order delivery of data packets.

Some of the disadvantages are:

- It has low efficiency, as the sender has to wait for the ACK packet before sending the next packet. The efficiency of the stop and wait protocol is given by:

  Efficiency = Useful time / Total cycle time = Tt / (Tt + 2Tp) = 1 / (1 + 2a) [a = Tp/Tt]

  where Tt is the transmission time of a packet, Tp is the propagation delay of the channel, and a is the ratio of Tp to Tt.

- It does not utilize the full bandwidth of the channel, as the channel is idle during the waiting time of the sender.
- It is vulnerable to errors and delays in the channel, as a single lost or corrupted packet can cause retransmission of the same packet.



### Experiment 1.2 - Implementation of Sliding Window Protocol

- Sliding window protocol is a feature of packet-based data transmission protocols that ensures reliable and sequential delivery of data frames .
- The protocol uses a window size that determines how many frames can be sent by the sender before receiving an acknowledgment from the receiver .
- The window slides along the sequence of frames as the sender transmits and the receiver acknowledges them .
- The protocol requires the receiver to acknowledge the receipt of each data packet, and it allows the receiver to use a single acknowledgment (ACK) to confirm the delivery of multiple packets.
- The protocol also handles the cases of lost, corrupted, or duplicated frames by using timers, sequence numbers, and retransmission mechanisms .
- There are different variants of sliding window protocol, such as stop-and-wait, go-back-N, and selective repeat  .
- Stop-and-wait is the simplest sliding window protocol, where the sender sends one frame at a time and waits for an ACK before sending the next frame .
- Go-back-N is the sliding window protocol where the sender can send multiple frames (up to the window size) without waiting for ACKs, but the receiver can only send a cumulative ACK for the last in-order frame received  .
- Selective repeat is the sliding window protocol where the sender can send multiple frames (up to the window size) without waiting for ACKs, and the receiver can send individual ACKs for each frame received, regardless of the order  .
- The implementation of sliding window protocol involves the following steps:
  - Define the window size, the sequence number range, and the frame structure for the sender and the receiver  .
  - Initialize the window and the sequence numbers for the sender and the receiver  .
  - Implement the logic for sending and receiving frames, including the acknowledgment, timer, and retransmission mechanisms  .
  - Simulate the cases of frame loss, corruption, or duplication and observe the behavior of the protocol  .
  - Compare the performance of different variants of sliding window protocol in terms of throughput, efficiency, and reliability  .



## Experiment 2 - Study of Socket Programming and Client – Server model

- Socket programming is a way of enabling communication between two processes over a network.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol.
- A client is a process that initiates a connection to a server, which is another process that listens for and accepts incoming connections from clients.
- The client and server communicate by exchanging data through the socket connection, following the rules of the protocol they use.
- There are two types of sockets: stream sockets and datagram sockets.
  - Stream sockets are connection-oriented, meaning they establish a reliable and ordered data transfer between the client and server. They use the Transmission Control Protocol (TCP) as the underlying protocol.
  - Datagram sockets are connectionless, meaning they do not require a connection before sending or receiving data. They are unreliable and unordered, meaning data may be lost, duplicated, or arrive out of order. They use the User Datagram Protocol (UDP) as the underlying protocol.
- Socket programming involves the following steps:
  - Socket creation: The client and server create a socket object using the socket() function, which takes the domain, type, and protocol as parameters. The domain specifies the address family, such as IPv4 or IPv6. The type specifies the socket type, such as stream or datagram. The protocol specifies the protocol to be used, such as TCP or UDP. The socket() function returns a socket descriptor, which is an integer that identifies the socket.
  - Socket binding: The server binds the socket to a specific address and port using the bind() function, which takes the socket descriptor and a sockaddr structure as parameters. The sockaddr structure contains the address family, the IP address, and the port number. The bind() function assigns the address and port to the socket, so that the server can listen for incoming connections from clients on that address and port.
  - Socket listening: The server calls the listen() function, which takes the socket descriptor and a backlog as parameters. The backlog specifies the maximum number of pending connections that the server can queue up. The listen() function marks the socket as a passive socket, meaning it can accept incoming connections from clients.
  - Socket connection: The client calls the connect() function, which takes the socket descriptor and a sockaddr structure as parameters. The sockaddr structure contains the address family, the IP address, and the port number of the server. The connect() function attempts to establish a connection to the server by sending a connection request to the server's address and port. If the server accepts the connection, the connect() function returns successfully and the client and server can communicate through the socket. If the server rejects the connection, the connect() function returns an error and the client has to try again or abort.
  - Socket acceptance: The server calls the accept() function, which takes the socket descriptor and a sockaddr structure as parameters. The sockaddr structure is used to store the address and port of the client that is connecting to the server. The accept() function blocks until a connection request arrives from a client. When a connection request arrives, the accept() function creates a new socket for the connection and returns a new socket descriptor for that socket. The server can then communicate with the client through the new socket, while the original socket remains listening for more connections.
  - Socket communication: The client and server can exchange data through the socket using the send() and recv() functions, which take the socket descriptor, a buffer, and a length as parameters. The buffer is used to store the data to be sent or received, and the length specifies the size of the buffer. The send() function sends the data in the buffer to the other end of the socket, and the recv() function receives the data from the other end of the socket and stores it in the buffer. The send() and recv() functions return the number of bytes sent or received, or an error if the communication fails.
  - Socket closure: The client and server can close the socket connection when they are done communicating using the close() function, which takes the socket descriptor as a parameter. The close() function terminates the connection and frees the socket resources. The client and server should close the socket gracefully, by sending a termination message or a special flag to indicate the end of communication.



### Experiment 2.1 - Study of Socket Programming

- Socket programming is a way of enabling communication between different processes or machines using network protocols.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol, such as TCP or UDP.
- Socket programming involves creating, configuring, and using sockets to establish connections and exchange data.
- Socket programming can be done in various programming languages, such as C, Python, Java, etc.
- Socket programming can be used for various applications, such as web servers, chat applications, file transfer, etc.

Some basic steps involved in socket programming are:

- Create a socket using the socket() function, specifying the address family, socket type, and protocol.
- Bind the socket to a local address and port using the bind() function.
- Listen for incoming connections using the listen() function (for server sockets) or connect to a remote address and port using the connect() function (for client sockets).
- Accept a connection request from a client using the accept() function (for server sockets) or send and receive data using the send() and recv() functions (for client sockets).
- Close the socket using the close() function when the communication is over.



### Experiment 2.2 - Study of Client – Server model

- The client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.
- Often clients and servers communicate over a computer network on separate hardware, but both client and server may reside in the same system.
- The client-server model describes a specific way devices access the information you store in servers.
- The client-server connection is established through a network or the Internet.
- The client initiates a request to the server, and the server responds with the desired service or resource.
- The server can provide different types of services, such as web, email, file transfer, database, etc.
- The client can be any device that can send and receive data, such as a computer, a smartphone, a tablet, etc.
- The client-server model has some advantages, such as:
  - Centralized system with all data in a single place.
  - Cost efficient, requires less maintenance cost and data recovery is possible.
  - The capacity of the client and server can be changed separately.
  - The server can handle multiple clients simultaneously.
  - The client can access the server from anywhere using the network.
- The client-server model also has some disadvantages, such as:
  - The server can become a bottleneck if it is overloaded with requests.
  - The server can be a single point of failure if it malfunctions or crashes.
  - The client-server communication can be vulnerable to security threats, such as hacking, eavesdropping, spoofing, etc.
  - The client-server model can be less scalable and flexible than other models, such as peer-to-peer or cloud computing.



## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is a network protocol that maps an IP address to a MAC address of a device on the same network.
- RARP stands for Reverse Address Resolution Protocol. It is a network protocol that maps a MAC address to an IP address of a device on the same network.
- Both ARP and RARP use broadcast messages to request and reply the address mappings.
- The following is a pseudocode for simulating ARP /RARP protocols:

```
# Define a class for a device on the network
class Device:
  # Initialize the device with its IP and MAC addresses
  def __init__(self, ip, mac):
    self.ip = ip
    self.mac = mac
    self.arp_table = {} # A dictionary to store the ARP cache
    self.rarp_table = {} # A dictionary to store the RARP cache

  # A method to send an ARP request to the network
  def arp_request(self, target_ip):
    # Broadcast a message to the network with the target IP and the sender's IP and MAC addresses
    broadcast_message = f"ARP request: Who has {target_ip}? Tell {self.ip}, {self.mac}"
    print(f"{self.ip} sends {broadcast_message}")
    # Return the broadcast message
    return broadcast_message

  # A method to receive an ARP request from the network
  def arp_receive(self, message):
    # Parse the message and extract the target IP, the sender IP and the sender MAC addresses
    message_parts = message.split()
    target_ip = message_parts[2]
    sender_ip = message_parts[4][:-1]
    sender_mac = message_parts[5]
    # Check if the target IP matches the device's IP
    if target_ip == self.ip:
      # Send an ARP reply to the sender with the device's IP and MAC addresses
      self.arp_reply(sender_ip, sender_mac)
    # Update the ARP cache with the sender's IP and MAC addresses
    self.arp_table[sender_ip] = sender_mac

  # A method to send an ARP reply to the sender
  def arp_reply(self, sender_ip, sender_mac):
    # Send a message to the sender with the device's IP and MAC addresses and the sender's IP and MAC addresses
    reply_message = f"ARP reply: {self.ip}, {self.mac} is at {target_ip}, {target_mac}"
    print(f"{self.ip} sends {reply_message} to {sender_ip}")
    # Return the reply message
    return reply_message

  # A method to receive an ARP reply from the sender
  def arp_receive_reply(self, message):
    # Parse the message and extract the sender IP, the sender MAC, the target IP and the target MAC addresses
    message_parts = message.split()
    sender_ip = message_parts[1][:-1]
    sender_mac = message_parts[2]
    target_ip = message_parts[4][:-1]
    target_mac = message_parts[5]
    # Check if the target IP matches the device's IP
    if target_ip == self.ip:
      # Update the ARP cache with the sender's IP and MAC addresses
      self.arp_table[sender_ip] = sender_mac

  # A method to send a RARP request to the network
  def rarp_request(self, target_mac):
    # Broadcast a message to the network with the target MAC and the sender's IP and MAC addresses
    broadcast_message = f"RARP request: Who has {target_mac}? Tell {self.ip}, {self.mac}"
    print(f"{self.ip} sends {broadcast_message}")
    # Return the broadcast message
    return broadcast_message

  # A method to receive a RARP request from the network
  def rarp_receive(self, message):
    # Parse the message and extract the target MAC, the sender IP and the sender MAC addresses
    message_parts = message.split()
    target_mac = message_parts[2]
    sender_ip = message_parts[4][:-1]
    sender_mac = message_parts[5]
    # Check if the target MAC matches the device's MAC
    if target_mac == self.mac:
      # Send a RARP reply to the sender with the device's IP and MAC addresses
      self.rarp_reply(sender_ip, sender_mac)
    # Update the RARP cache with the sender's IP and MAC addresses
    self.rarp_table[sender_mac] = sender_ip

  # A method to send a RARP reply to the sender
  def rarp_reply(self, sender_ip, sender_mac):
    # Send a

```




## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- PING and TRACEROUTE are common commands you can use to troubleshoot network problems  .
- PING is a simple command that can test the reachability of a device on the network by sending and receiving ICMP packets  .
- TRACEROUTE is a command you use to 'trace' the route that a packet takes when traveling to its destination by sending and receiving ICMP packets with varying TTL values   .
- To write a code simulating PING and TRACEROUTE commands, you need to follow these steps:

  - Import the necessary modules, such as socket, struct, time, sys, etc.
  - Define a function to calculate the checksum of an ICMP packet.
  - Define a function to create an ICMP packet with a given type, code, ID, sequence number, and payload.
  - Define a function to send an ICMP packet to a given destination address and port, and receive the response packet or timeout.
  - Define a function to perform the PING operation by sending and receiving ICMP packets with type 8 (echo request) and type 0 (echo reply), and printing the statistics such as RTT, packet loss, etc.
  - Define a function to perform the TRACEROUTE operation by sending and receiving ICMP packets with type 8 (echo request) and varying TTL values, and printing the intermediate hops and their RTT .
  - Use the main function to parse the command-line arguments and call the appropriate function based on the user input.

- Here is an example code in Python that simulates the PING and TRACEROUTE commands:

```python
# Import the necessary modules
import socket
import struct
import time
import sys

# Define a function to calculate the checksum of an ICMP packet
def checksum(data):
    # Initialize the sum to zero
    sum = 0
    # Loop through the data in 16-bit chunks
    for i in range(0, len(data), 2):
        # Add the 16-bit chunk to the sum
        if i + 1 < len(data):
            sum += (data[i] << 8) + data[i + 1]
        else:
            sum += data[i]
        # Add the carry bits to the sum
        sum = (sum & 0xffff) + (sum >> 16)
    # Return the one's complement of the sum
    return ~sum & 0xffff

# Define a function to create an ICMP packet with a given type, code, ID, sequence number, and payload
def create_packet(type, code, id, seq, payload):
    # Pack the header fields into a binary format
    header = struct.pack('!BBHHH', type, code, 0, id, seq)
    # Calculate the checksum of the header and payload
    chksum = checksum(header + payload)
    # Repack the header with the checksum
    header = struct.pack('!BBHHH', type, code, chksum, id, seq)
    # Return the header and payload as a packet
    return header + payload

# Define a function to send an ICMP packet to a given destination address and port, and receive the response packet or timeout
def send_packet(sock, dest_addr, port, packet, timeout):
    # Send the packet to the destination address and port
    sock.sendto(packet, (dest_addr, port))
    # Set the socket timeout
    sock.settimeout(timeout)
    # Try to receive the response packet
    try:
        response, addr = sock.recvfrom(1024)
        # Return the response packet and the address
        return response, addr
    # Handle the socket timeout exception
    except socket.timeout:
        # Return None and None
        return None, None

# Define a function to perform the PING operation by sending and receiving ICMP packets with type 8 (echo request) and type 0 (echo reply), and printing the statistics such as RTT, packet loss, etc
def ping(dest_addr, count, interval, timeout, payload_size):
    # Create a raw socket for ICMP protocol
    sock = socket.socket

```




## Experiment 5 - Create a socket for HTTP for web page upload and download

- A socket is an endpoint of a communication channel between two processes or devices over a network.
- HTTP (Hypertext Transfer Protocol) is an application layer protocol that defines how web pages are requested and transferred over the internet.
- To create a socket for HTTP, we need to use the socket module in Python, which provides a low-level interface to access network services.
- The steps to create a socket for HTTP are:

  1. Import the socket module: `import socket`
  2. Create a socket object: `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  3. Specify the host and port of the web server: `host = "www.example.com"` and `port = 80`
  4. Connect the socket to the server: `s.connect((host, port))`
  5. Send an HTTP request to the server: `s.send(b"GET /index.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n")`
  6. Receive the HTTP response from the server: `data = s.recv(1024)`
  7. Print the response data: `print(data.decode())`
  8. Close the socket: `s.close()`

- To upload and download web pages using the socket, we need to use the following methods:

  - To upload a web page, we need to send an HTTP POST request to the server with the content of the web page in the request body. For example: `s.send(b"POST /upload.html HTTP/1.1\r\nHost: www.example.com\r\nContent-Type: text/html\r\nContent-Length: 20\r\n\r\n<html>Hello</html>")`
  - To download a web page, we need to send an HTTP GET request to the server with the name of the web page in the request line. For example: `s.send(b"GET /download.html HTTP/1.1\r\nHost: www.example.com\r\n\r\n")`
  - To receive the uploaded or downloaded web page, we need to read the response data from the socket and parse the HTTP headers and the body. For example: `data = s.recv(1024)` and `headers, body = data.split(b"\r\n\r\n", 1)`



## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

- RPC (Remote Procedure Call) is a technique that allows a program to execute a procedure or a function on a different machine, as if it was a local call.
- RPC involves two components: a client and a server. The client sends a request to the server, specifying the name and parameters of the procedure to be executed. The server receives the request, invokes the procedure, and sends back the result to the client.
- RPC can be implemented using different protocols, such as TCP/IP, UDP, HTTP, etc. In this experiment, we will use TCP/IP as the underlying protocol.
- To implement RPC, we need to define the interface of the remote procedure, using a language-independent format, such as IDL (Interface Definition Language). The IDL compiler generates the stubs and skeletons for the client and server, respectively. The stubs and skeletons are the code that handles the communication and marshalling of the parameters and results between the client and server.
- The steps to implement RPC are as follows:

  1. Define the interface of the remote procedure in IDL. For example, suppose we want to implement a remote procedure that calculates the factorial of a given number. The IDL file can be written as:

  ```
  // factorial.idl
  interface Factorial {
    int factorial (in int n);
  };
  ```

  2. Compile the IDL file using the IDL compiler. This will generate the stubs and skeletons for the client and server in the chosen programming language. For example, if we use C as the programming language, the IDL compiler will generate the following files:

  ```
  // factorial_c.h
  // This file contains the declarations of the stubs and skeletons
  #ifndef FACTORIAL_C_H
  #define FACTORIAL_C_H

  #include <rpc/rpc.h>

  #define FACTORIAL_PROG 0x12345678 // A unique identifier for the program
  #define FACTORIAL_VERS 1 // The version number of the program
  #define FACTORIAL_PROC 1 // The procedure number of the factorial function

  // The data structure that represents the input parameter
  typedef struct {
    int n;
  } factorial_in;

  // The data structure that represents the output result
  typedef struct {
    int res;
  } factorial_out;

  // The declaration of the client stub
  factorial_out *factorial_1(factorial_in *argp, CLIENT *clnt);

  // The declaration of the server skeleton
  void *factorial_1_svc(factorial_in *argp, struct svc_req *rqstp);

  #endif
  ```

  ```
  // factorial_clnt.c
  // This file contains the definition of the client stub
  #include "factorial_c.h"

  // The definition of the client stub
  factorial_out *factorial_1(factorial_in *argp, CLIENT *clnt) {
    static factorial_out res;

    // Clear the result
    memset((char *)&res, 0, sizeof(res));

    // Call the remote procedure using TCP
    if (clnt_call(clnt, FACTORIAL_PROC, xdr_factorial_in, argp, xdr_factorial_out, &res, TIMEOUT) != RPC_SUCCESS) {
      return NULL;
    }

    // Return the result
    return &res;
  }
  ```

  ```
  // factorial_svc.c
  // This file contains the definition of the server skeleton
  #include "factorial_c.h"

  // The definition of the server skeleton
  void *factorial_1_svc(factorial_in *argp, struct svc_req *rqstp) {
    static factorial_out res;

    // Clear the result
    memset((char *)&res, 0, sizeof(res));

    // Call the local procedure that implements the factorial logic
    res.res = factorial(argp->n);

    // Return the result
    return &res;
  }
  ```

  3. Write the client and server programs that use the stubs and skeletons. For example, the client program can be written as:

  ```
  // factorial_client.c
  // This file contains the main function of the client program
  #include "factorial_c.h"

  // The main function of the client program
  int main(int argc, char *argv[]) {
    CLIENT *clnt; // The client handle
    factorial_in in; // The input parameter
    factorial_out *out; // The output result

    // Check the number of arguments
    if (argc != 3) {

```




## Experiment 7 - Implementation of Subnetting

- Subnetting is a technique of dividing a network into smaller logical subnetworks, each with its own range of IP addresses and network prefix.
- Subnetting can improve network performance, security, and scalability by reducing the size of the broadcast domain and the routing table.
- Subnetting requires a network mask, which is a binary number that indicates which bits of the IP address belong to the network prefix and which bits belong to the host identifier.
- The network mask can be expressed in dotted decimal notation (e.g., 255.255.255.0) or in slash notation (e.g., /24).
- To perform subnetting, the network administrator can borrow some bits from the host identifier and use them to create subnetwork identifiers. The number of subnets and hosts per subnet depends on how many bits are borrowed.
- The formula for calculating the number of subnets is 2^n, where n is the number of borrowed bits. The formula for calculating the number of hosts per subnet is 2^(32-n-m)-2, where n is the number of borrowed bits and m is the number of network prefix bits.
- To find the subnet address, the network mask is bitwise ANDed with the IP address. To find the broadcast address, the network mask is bitwise inverted and then bitwise ORed with the IP address.
- To find the valid host range, the subnet address is incremented by one and the broadcast address is decremented by one. The first and last addresses in the range are the valid host addresses.
- An example of subnetting is given below:

  - Given a network address of 192.168.1.0/24 and a requirement of 4 subnets, the network mask can be changed to 255.255.255.192 or /26 by borrowing 2 bits from the host identifier.
  - The number of subnets is 2^2 = 4 and the number of hosts per subnet is 2^(32-26-8)-2 = 62.
  - The subnet addresses are 192.168.1.0, 192.168.1.64, 192.168.1.128, and 192.168.1.192.
  - The broadcast addresses are 192.168.1.63, 192.168.1.127, 192.168.1.191, and 192.168.1.255.
  - The valid host ranges are 192.168.1.1-192.168.1.62, 192.168.1.65-192.168.1.126, 192.168.1.129-192.168.1.190, and 192.168.1.193-192.168.1.254.



## Experiment 8 - Applications using TCP Sockets

- TCP sockets are a type of network communication that uses the Transmission Control Protocol (TCP) to establish reliable and ordered data exchange between applications.
- TCP sockets are connection-oriented, meaning that they require a three-way handshake (SYN, SYN-ACK, ACK) to establish a connection before sending or receiving data.
- TCP sockets are identified by a combination of IP address and port number, which form a socket address.
- TCP sockets can be used for various applications, such as web servers, email clients, file transfer, chat, remote access, etc.
- TCP sockets can be programmed using various languages and platforms, such as C, Java, Python, .NET, etc .
- TCP sockets can be classified into two types: server sockets and client sockets.
  - Server sockets are used to listen for incoming connection requests from client sockets and accept them.
  - Client sockets are used to initiate connection requests to server sockets and send or receive data after the connection is established.
- TCP sockets can be implemented using various socket APIs, such as BSD sockets, Winsock, Java sockets, etc.
- TCP sockets can be tested using various tools, such as telnet, netcat, curl, etc.



### Experiment 8.1 - Echo client and echo server

- An echo client and echo server are applications that communicate over a network using sockets.
- An echo client sends a message to an echo server, and the echo server receives the message and sends back an identical copy of the message to the echo client.
- The purpose of this experiment is to demonstrate the basic concepts of socket programming in Java, such as creating, binding, listening, accepting, reading, and writing sockets.
- The steps of this experiment are as follows:

  1. Create a single-threaded TCP echo server that listens on a specific port and prints out the received messages on the standard output.
  2. Create a TCP echo client that connects to the echo server, reads a line of input from the keyboard, and sends it to the echo server.
  3. Run the echo server and the echo client on the same or different machines, and observe the communication between them.
  4. Modify the echo server and the echo client to handle multiple messages and close the connection gracefully.
  5. Experiment with different types of messages, such as empty, long, or binary messages, and see how the echo server and the echo client handle them.
  6. Optionally, create a UDP echo server and a UDP echo client, and compare the differences between TCP and UDP sockets.



### Experiment 8.2 - Chat

- The objective of this experiment is to learn how to create a simple chat application using HTML, CSS, and JavaScript.
- The chat application allows users to send and receive text messages in real time using a web browser.
- The chat application consists of three main components: a client, a server, and a database.
- The client is the user interface that displays the chat messages and allows the user to input and send messages.
- The server is the program that handles the communication between the clients and the database.
- The database is the storage system that stores the chat messages and other information.
- The steps to create the chat application are as follows:

  1. Create the HTML file that defines the structure and layout of the chat interface.
  2. Create the CSS file that styles the chat interface and makes it responsive and attractive.
  3. Create the JavaScript file that adds interactivity and functionality to the chat interface, such as validating the user input, sending and receiving messages, and updating the chat history.
  4. Create the server file that uses Node.js and Express.js to create a web server that listens for requests from the clients and responds with appropriate data.
  5. Create the database file that uses MongoDB and Mongoose to create a database that stores the chat messages and other information, such as the user name and the timestamp.
  6. Test the chat application by running the server and opening the HTML file in multiple web browsers. Try to send and receive messages and observe the chat history.



### Experiment 8.3 - File Transfer

- The objective of this experiment is to learn how to transfer files between different devices using various methods and protocols.
- The devices involved in this experiment are a PC, a laptop, a smartphone, and a USB flash drive.
- The methods and protocols used for file transfer are:
  - USB cable: This is a physical connection that allows data transfer between a device and a USB port on another device. The USB cable can support different standards, such as USB 2.0, USB 3.0, or USB-C, which have different speeds and features.
  - Bluetooth: This is a wireless technology that allows data transfer between devices that are within a short range of each other. Bluetooth can support different profiles, such as FTP (File Transfer Profile), OPP (Object Push Profile), or MAP (Message Access Profile), which have different functions and capabilities.
  - Wi-Fi: This is a wireless technology that allows data transfer between devices that are connected to the same local area network (LAN) or the internet. Wi-Fi can support different protocols, such as FTP (File Transfer Protocol), HTTP (Hypertext Transfer Protocol), or SMB (Server Message Block), which have different rules and formats for data exchange.
  - Cloud: This is a service that allows data storage and access on remote servers over the internet. Cloud can support different platforms, such as Google Drive, Dropbox, or OneDrive, which have different features and security options.
- The steps for file transfer using each method and protocol are:
  - USB cable: Connect the device to the USB port on the PC or laptop using the appropriate cable. Open the file explorer on the PC or laptop and locate the device. Drag and drop the files to or from the device.
  - Bluetooth: Turn on the Bluetooth on both devices and pair them. Open the file explorer on the PC or laptop and locate the device. Right-click on the file and select Send to > Bluetooth device. Alternatively, open the file manager on the smartphone and locate the file. Tap on the file and select Share > Bluetooth. Choose the destination device and accept the file transfer request.
  - Wi-Fi: Connect both devices to the same Wi-Fi network. Open the file explorer on the PC or laptop and locate the device. Alternatively, open the file manager on the smartphone and locate the file. Drag and drop the files to or from the device. Alternatively, use a web browser on either device and enter the IP address or hostname of the other device. Enter the username and password if required and access the files. Alternatively, use a third-party app on either device that supports Wi-Fi file transfer, such as Shareit, Xender, or Zapya, and follow the instructions.
  - Cloud: Create an account on the cloud platform of your choice and install the app on both devices. Log in to the app on both devices and access the files. Drag and drop the files to or from the cloud folder. Alternatively, use a web browser on either device and log in to the cloud website. Upload or download the files as needed.



## Experiment 9 - Applications using TCP and UDP Sockets

- TCP and UDP are two protocols that provide reliable and unreliable data transmission over the Internet Protocol (IP) network.
- TCP stands for Transmission Control Protocol and it guarantees that the data sent by one end is received by the other end in the same order and without any loss or corruption.
- UDP stands for User Datagram Protocol and it does not guarantee any reliability or ordering of the data. It is faster and more efficient than TCP for some applications that do not require reliability.
- Sockets are the endpoints of a bidirectional communication channel between two processes running on different machines over a network.
- A socket is identified by a combination of an IP address and a port number. An IP address is a unique identifier for a machine on the network and a port number is a logical identifier for a specific process or service on that machine.
- A socket can be either a TCP socket or a UDP socket, depending on the protocol used for data transmission.
- Some common applications that use TCP and UDP sockets are:

  - Web browsers and web servers use TCP sockets to exchange HTTP requests and responses over the World Wide Web.
  - Email clients and servers use TCP sockets to send and receive emails using SMTP, POP3 or IMAP protocols.
  - File transfer applications use TCP sockets to transfer files between machines using FTP or SCP protocols.
  - Streaming media applications use UDP sockets to deliver audio and video data over the Internet using RTP or RTSP protocols.
  - Online games use UDP sockets to exchange real-time information between players using custom protocols.
  - Voice over IP applications use UDP sockets to transmit voice data over the Internet using SIP or H.323 protocols.



### Experiment 9.1 - DNS

- DNS stands for Domain Name System, which is a distributed database that maps domain names to IP addresses and other information.
- DNS allows users to access websites and other resources using human-readable names instead of numerical addresses.
- DNS consists of a hierarchical structure of name servers, which store and resolve domain names to IP addresses and other records.
- DNS uses a client-server model, where a DNS client (also called a resolver) sends queries to a DNS server, which responds with the requested information or a referral to another server.
- DNS queries and responses use the UDP protocol by default, but can also use TCP if the message size exceeds 512 bytes or for zone transfers.
- DNS supports various types of records, such as A (address), AAAA (IPv6 address), CNAME (canonical name), MX (mail exchange), NS (name server), PTR (pointer), SOA (start of authority), and TXT (text).
- DNS also supports various features, such as caching, recursion, forwarding, load balancing, security, and dynamic updates.



### Experiment 9.2 - SNMP

- SNMP stands for Simple Network Management Protocol. It is a way for different devices on a network to share information about their current state, and also a channel through which an administrator can modify pre-defined values .
- SNMP is widely used in network management for network monitoring. SNMP exposes management data in the form of variables on the managed systems organized in a management information base (MIB) which describe the system status and configuration.
- SNMP is a component of the Internet Protocol Suite as defined by the Internet Engineering Task Force (IETF). It consists of a set of standards for network management, including an application layer protocol, a database schema, and a set of data objects.
- SNMP operates on a client-server model, where the client is called a manager and the server is called an agent. The manager can request information from the agent, or instruct the agent to perform some action. The agent can also send unsolicited notifications to the manager, called traps or informs, to report events or errors .
- SNMP uses four basic operations: GET, SET, GETNEXT, and GETBULK. GET is used to retrieve the value of a variable from the agent. SET is used to assign a new value to a variable on the agent. GETNEXT is used to retrieve the next variable in the MIB. GETBULK is used to retrieve multiple variables in a single request .
- SNMP has three versions: SNMPv1, SNMPv2c, and SNMPv3. SNMPv1 is the original version, which only supports simple authentication based on community strings. SNMPv2c is an extension of SNMPv1, which adds support for GETBULK and informs, and uses a common community string for both authentication and encryption. SNMPv3 is the latest version, which adds support for user-based security, encryption, and access control  .
- SNMP can be used to monitor and manage various aspects of a network, such as bandwidth usage, device availability, performance, configuration, security, and more. SNMP can also be integrated with other network management tools, such as syslog, NetFlow, and RMON, to provide a comprehensive view of the network .



### Experiment 9.3 - File Transfer

- The objective of this experiment is to learn how to transfer files between different devices using various methods and protocols.
- The prerequisites for this experiment are:
  - Basic knowledge of computer networks and file systems.
  - Access to at least two devices that can communicate with each other, such as computers, smartphones, tablets, etc.
  - A USB cable, a Bluetooth adapter, or a Wi-Fi connection to enable file transfer.
- The steps for this experiment are:
  - Identify the source device and the destination device for the file transfer. For example, you may want to transfer a file from your computer to your smartphone, or vice versa.
  - Choose a method and a protocol for the file transfer. For example, you may use a USB cable, a Bluetooth connection, or a Wi-Fi network to transfer the file. You may also use different protocols, such as FTP, HTTP, or SMB, to transfer the file over a network.
  - Connect the devices using the chosen method and protocol. For example, you may plug in the USB cable, pair the Bluetooth devices, or join the Wi-Fi network.
  - Locate the file that you want to transfer on the source device. For example, you may use a file manager, a web browser, or a command line to find the file.
  - Initiate the file transfer from the source device to the destination device. For example, you may use a drag-and-drop, a copy-and-paste, or a send-to option to transfer the file.
  - Verify that the file transfer is successful and that the file is intact on the destination device. For example, you may use a checksum, a file size, or a file type to check the file.
- The expected outcomes of this experiment are:
  - You will learn how to transfer files between different devices using various methods and protocols.
  - You will understand the advantages and disadvantages of different methods and protocols for file transfer.
  - You will be able to troubleshoot common problems and errors that may occur during file transfer.



## Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

- Network simulator (NS) is a name for a series of discrete event network simulators, specifically ns-1, ns-2, and ns-3  .
- NS is used for simulation of TCP, routing, and multicast protocols over wired and wireless (local and satellite) networks .
- NS is free, open-source software, licensed under the GNU GPLv2 license, and maintained by a worldwide community.
- NS is written in C++ and uses Tcl as a scripting language .
- NS provides a modular library of network components and models, such as nodes, links, queues, protocols, applications, etc .
- NS allows users to create and run network simulations using a graphical user interface (GUI) or a command-line interface (CLI) .
- NS supports various congestion control algorithms, such as TCP Reno, TCP New Reno, TCP Vegas, TCP SACK, etc .
- To simulate congestion control algorithms using NS, the following steps are required:
  - Install NS on your system and verify its functionality .
  - Create a network topology using NS components and models .
  - Configure the parameters of the congestion control algorithm, such as window size, timeout, retransmission, etc .
  - Define the traffic sources and sinks, such as FTP, HTTP, CBR, etc .
  - Specify the output format and metrics, such as trace files, graphs, throughput, delay, etc .
  - Run the simulation and analyze the results .



## Experiment 11 - Perform a case study about the different routing algorithms to select the network path with its optimum and economical during data transfer

- Routing algorithms are the methods used by routers to determine the best path for sending packets in a network.
- Routing algorithms can be classified into two main categories: adaptive and non-adaptive.
- Adaptive algorithms change their routing decisions whenever network topology or traffic load changes. They can adapt to network conditions and optimize performance, but they require more computation and communication overhead.
- Non-adaptive algorithms do not change their routing decisions once they are initialized. They are simpler and faster, but they may not perform well under dynamic network conditions.
- Some examples of adaptive algorithms are distance vector, link state, and multipath routing. Some examples of non-adaptive algorithms are shortest path, flooding, and random walk routing.
- A case study of the evolution of routing algorithms in a network planning tool is presented in   . The authors describe how they developed and improved different routing algorithms for a software system that helps design transmission networks for telecommunication operators.
- The authors compare the performance of different routing algorithms in terms of network cost, reliability, and scalability. They also discuss the challenges and trade-offs involved in developing and maintaining routing algorithms for a complex and dynamic network planning problem.



### Experiment 11.1 - Link State Routing

- Link state routing is a type of routing algorithm that uses the information about the state of each link (such as bandwidth, delay, cost, etc.) to calculate the shortest path from one node to every other node in the network .
- Link state routing is also known as Dijkstra's algorithm, which is an iterative algorithm that finds the least cost path for a given destination node after each iteration.
- Link state routing requires each node to construct a map of the network topology, in the form of a graph, by exchanging messages with all the other nodes in the network. These messages are called link state advertisements (LSAs).
- Link state routing protocols are more scalable and robust than distance-vector routing protocols, as they have a global view of the network and can detect and avoid loops and broken links .
- Examples of link state routing protocols are Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).
- The steps involved in link state routing are:
  - Each node broadcasts its LSAs to all its neighbors periodically or when there is a change in the link state.
  - Each node receives the LSAs from its neighbors and stores them in a link state database (LSDB).
  - Each node uses the LSDB to construct a graph of the network topology, where the nodes are routers and the edges are links with their costs.
  - Each node applies Dijkstra's algorithm to the graph to find the shortest path tree for itself, which contains the shortest path to every other node in the network.
  - Each node updates its routing table based on the shortest path tree, where the next hop for each destination is the first node on the shortest path.



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
  - Building levees, dams, or floodwalls to control water flow and divert excess water.
  - Restoring natural wetlands and vegetation to absorb water and reduce runoff.
  - Implementing early warning systems and evacuation plans to alert and protect people and property.
  - Adopting flood insurance and disaster relief programs to compensate and support affected communities.



### Experiment 11.3 - Distance vector

- A distance vector is a data structure that contains the distance and direction from a source node to a destination node in a network.
- A distance vector routing algorithm is a distributed algorithm that uses distance vectors to compute the shortest paths between nodes in a network.
- A distance vector routing algorithm works as follows:
  - Each node maintains a distance vector table that contains the distance and next hop to every other node in the network.
  - Each node periodically exchanges its distance vector table with its direct neighbors.
  - Each node updates its distance vector table based on the information received from its neighbors, using the Bellman-Ford equation: `d(x,y) = min{c(x,v) + d(v,y)}` where `d(x,y)` is the distance from node `x` to node `y`, `c(x,v)` is the cost of the link from node `x` to node `v`, and `d(v,y)` is the distance from node `v` to node `y` as reported by node `v`.
  - The algorithm converges when no node changes its distance vector table in an iteration.
- A distance vector routing algorithm has the following advantages and disadvantages:
  - Advantages:
    - It is simple and easy to implement.
    - It does not require global knowledge of the network topology.
    - It can adapt to dynamic changes in the network, such as link failures or additions.
  - Disadvantages:
    - It may take a long time to converge, especially in large networks.
    - It may suffer from the count-to-infinity problem, where a node increases its distance to a destination indefinitely due to a loop in the network.
    - It may generate a lot of traffic due to periodic updates, which may consume bandwidth and energy.



## Experiment 12 - To learn handling and configuration of networking hardware like RJ-45 connector, CAT-6 cable, crimping tool, etc

- The objective of this experiment is to learn how to make your own network cables using RJ-45 connectors, CAT-6 cables, and crimping tools.
- RJ-45 connectors are the standard plugs used for Ethernet cables. They have eight pins that correspond to the eight wires inside the cable. RJ-45 connectors come in different types, such as shielded or unshielded, and pass-through or non-pass-through. Pass-through connectors allow the wires to go through the connector and be trimmed after crimping, while non-pass-through connectors require the wires to be cut before inserting them into the connector .
- CAT-6 cables are the most common type of Ethernet cables used for network installations. They have four twisted pairs of wires that can support data transfer speeds up to 10 Gbps. CAT-6 cables are backward compatible with CAT-5 and CAT-5e cables, but have better performance and less crosstalk. CAT-6 cables have different categories, such as UTP (unshielded twisted pair), STP (shielded twisted pair), and FTP (foiled twisted pair), depending on the level of shielding and interference protection .
- Crimping tools are the devices used to attach RJ-45 connectors to CAT-6 cables. They have different sections for cutting, stripping, and crimping the wires. Crimping tools can be manual or automatic, and can have different features, such as rubber grips, ratchet mechanisms, and wire testers. Crimping tools must be compatible with the type and size of the RJ-45 connectors and CAT-6 cables used  .

- The steps for making your own network cable are as follows:

  1. Choose the type and length of CAT-6 cable you need for your network installation. Cut the cable using the cutting section of the crimping tool or a pair of scissors.
  2. Strip about 2 cm of the outer sheath of the cable using the stripping section of the crimping tool or a knife. Be careful not to damage the inner wires.
  3. Untwist the four pairs of wires and arrange them in the correct order according to the wiring standard you are using. The most common standards are T568A and T568B, which differ in the position of the green and orange pairs. The order of the wires from left to right when looking at the end of the cable is as follows:

     - T568A: white-green, green, white-orange, blue, white-blue, orange, white-brown, brown
     - T568B: white-orange, orange, white-green, blue, white-blue, green, white-brown, brown

  4. Hold the wires with your thumb and index finger to keep them in order. Then, use the cutting section of the crimping tool to cut them into an even line. The wires must be in an even line to be crimped into the RJ-45 connector properly.
  5. Choose the type of RJ-45 connector you want to use for your cable. If you are using a pass-through connector, insert the wires through the connector until they reach the end. If you are using a non-pass-through connector, insert the wires into the slots of the connector until they are fully seated. Make sure the wires are in the same order as before and match the color-coded pins of the connector.
  6. Place the connector with the wires into the crimping section of the crimping tool. Squeeze the handle firmly until you hear a click. This will push the pins of the connector into the wires and secure them. If you are using a pass-through connector, use the cutting section of the crimping tool to trim the excess wires after crimping.
  7. Repeat the same steps for the other end of the cable, using the same or a different wiring standard depending on your network configuration. You can use a cable tester to check if the cable is working properly and has no short circuits or open circuits.
  8. Label the cable and use cable ties or clips to organize it. You can now use the cable to connect your network devices.



## Experiment 13 - Configuration of router, hub, switch etc. (using real devices or simulators)

- A router is a device that routes data packets based on their IP addresses. It can connect different networks, such as LANs and WANs, and perform functions such as assigning IP addresses, acting as a switch, and protecting the network.  
- A hub is a device that connects multiple computers to create a LAN. It broadcasts all the data it receives to all the connected devices, regardless of the destination. It operates at the physical layer of the OSI model. 
- A switch is a device that connects multiple computers to create a LAN. It learns the MAC addresses of the connected devices and sends the data only to the intended destination. It operates at the data link layer of the OSI model. 
- To configure a router, you need to enter the router configuration mode, using the `configure terminal` command on Cisco devices, and then the interface configuration mode, using the `interface <interface name>` command. You can then set various parameters for the interface, such as IP address, subnet mask, speed, duplex, and description. You can also enable or disable the interface, using the `no shutdown` or `shutdown` command, respectively. 
- To configure a switch, you need to enter the switch configuration mode, using the `configure terminal` command on Cisco devices, and then the interface configuration mode, using the `interface <interface name>` command. You can then set various parameters for the interface, such as speed, duplex, and description. You can also assign the interface to a VLAN, using the `switchport mode access` and `switchport access vlan <vlan number>` commands.
- To configure a hub, you do not need to do anything, as it is a plug-and-play device that does not have any configuration options.
- To use a simulator for router and switch configuration, you can use a free emulator such as Packet Tracer, GNS3, or Boson NetSim. These tools allow you to create virtual networks with different devices and practice various commands and scenarios.



## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

- The objective of this experiment is to learn how to use some common network services and commands that can help in troubleshooting, testing, and transferring data over the network.
- The following are the main services and commands that will be covered in this experiment:
  - ping: A command that sends packets of data to a specified destination and measures the round-trip time and packet loss rate.
  - traceroute: A command that traces the route of packets from the source to the destination and displays the IP addresses and names of the intermediate routers and hosts.
  - nslookup: A command that queries the Domain Name System (DNS) and resolves hostnames to IP addresses or vice versa.
  - arp: A command that displays or modifies the Address Resolution Protocol (ARP) cache, which maps IP addresses to MAC addresses on the local network.
  - telnet: A service that allows remote login and command execution on a host using the Telnet protocol.
  - ftp: A service that allows file transfer between hosts using the File Transfer Protocol (FTP).
- The following are the steps to perform the experiment:
  - Step 1: Open a terminal window on your computer and type `ping www.google.com` to test the connectivity to Google's website. Observe the output and note down the IP address of the destination, the number of packets sent and received, the round-trip time, and the packet loss rate.
  - Step 2: Type `traceroute www.google.com` to trace the route of packets to Google's website. Observe the output and note down the number of hops, the IP addresses and names of the intermediate routers and hosts, and the time taken for each hop.
  - Step 3: Type `nslookup www.google.com` to query the DNS and resolve the hostname to an IP address. Observe the output and note down the name and address of the DNS server, the name and address of the destination, and any aliases or other records associated with the destination.
  - Step 4: Type `arp -a` to display the ARP cache on your computer. Observe the output and note down the IP addresses and MAC addresses of the hosts on your local network.
  - Step 5: Type `telnet towel.blinkenlights.nl` to connect to a remote host using the Telnet protocol. Observe the output and enjoy the ASCII art animation of Star Wars. To exit, press Ctrl + ] and then type `quit`.
  - Step 6: Type `ftp ftp.gnu.org` to connect to a remote host using the FTP protocol. Observe the output and enter `anonymous` as the username and your email address as the password. To list the files and directories on the remote host, type `ls`. To download a file, type `get filename`. To upload a file, type `put filename`. To exit, type `bye`.
- The following are some questions to test your understanding of the experiment:
  - Q1: What is the purpose of ping command and what are the parameters that can be used to modify its behavior?
  - Q2: What is the difference between traceroute and ping commands and how can they be used to diagnose network problems?
  - Q3: What is the role of DNS and how can nslookup command be used to query different types of DNS records?
  - Q4: What is the function of ARP and how can arp command be used to add, delete, or modify ARP entries?
  - Q5: What are the advantages and disadvantages of telnet service and what are some alternatives to it?



## Experiment 15 - Network packet analysis using tools like Wireshark, tcpdump, etc

- Network packet analysis is the process of capturing, inspecting, and interpreting the data packets that are exchanged between devices on a network.
- Network packet analysis tools are software applications that can capture, filter, decode, and analyze the packet data, as well as provide various statistics and visualizations of the network traffic.
- Some of the benefits of network packet analysis are:
  - Troubleshooting network problems and performance issues
  - Detecting and preventing network attacks and intrusions
  - Monitoring and enforcing network policies and compliance
  - Understanding network behavior and usage patterns
  - Optimizing network resources and bandwidth
- Some of the challenges of network packet analysis are:
  - Handling large volumes and high speeds of network traffic
  - Protecting the privacy and security of the packet data
  - Selecting the appropriate tools and techniques for different network scenarios
  - Interpreting the packet data correctly and accurately
- Some of the common network packet analysis tools are:
  - Wireshark: a free and open-source packet analyzer that allows you to examine network data transmissions in real-time . It supports hundreds of protocols and has a graphical user interface (GUI) as well as a command-line interface (CLI).
  - tcpdump: an open-source and powerful command-line packet analyzer tool that captures protocols such as TCP, UDP, and ICMP (Internet Control Message Protocol). It can run on various operating systems and can filter and save the packet data to a file.
  - Colasoft Capsa: a real-time portable network analyzer, monitoring, and diagnostics tool for both wired and wireless networks. It has a GUI that can display network traffic information according to category and provide an estimate of the risk level associated with this traffic.
  - Paessler PRTG: a network monitoring and analysis tool that can capture and store network packets for later analysis. It has a web-based interface that can show various metrics and graphs of the network performance and health.
  - Arkime: a web-based packet capture and analysis tool that can store and index large amounts of network data. It has a powerful search and filtering functionality that can help you find and analyze the relevant packets.



## Experiment 16 - Network simulation using tools like Cisco Packet Tracer, NetSim, OMNeT++, NS2, NS3, etc

- Network simulation is the process of modeling the behavior and performance of a network using software tools.
- Network simulation tools can help students, researchers, and professionals to design, test, and analyze various network scenarios and protocols.
- Network simulation tools can also support network emulation, which is the integration of real and simulated network components.
- Some of the benefits of network simulation tools are:
  - They can reduce the cost and complexity of building physical network labs.
  - They can support a wide range of network technologies and topologies.
  - They can provide accurate and reproducible results.
  - They can enable rapid prototyping and experimentation.
- Some of the challenges of network simulation tools are:
  - They may have limitations in scalability, realism, and validation.
  - They may require high computational resources and expertise.
  - They may have compatibility and interoperability issues with different platforms and tools.
- Some of the popular network simulation tools are:
  - Cisco Packet Tracer: A network simulation and visualization tool that can be used for teaching and learning networking concepts and skills. It supports Cisco devices and protocols, as well as IoT and cybersecurity features. It is available for free for Cisco Networking Academy students and instructors. 
  - NetSim: A network simulation and emulation tool that can be used for research and development of network protocols and applications. It supports a variety of network technologies, such as wireless, mobile, optical, satellite, and sensor networks. It is a commercial product developed by Tetcos. 
  - OMNeT++: An open source, modular, and component-based network simulation framework that can be used for modeling and simulating various network systems and protocols. It supports C++ as the programming language and has a graphical user interface and a network editor. It can be extended with various simulation models and libraries, such as INET, VEINS, and SimuLTE.  
  - NS2: An open source, discrete-event network simulator that can be used for studying the behavior and performance of wired and wireless networks. It supports Tcl and C++ as the programming languages and has a network animator (NAM) for visualization. It can be extended with various simulation models and libraries, such as Mobile IP, TCP, and DSR.  
  - NS3: An open source, discrete-event network simulator that can be used for research and education in networking. It supports C++ and Python as the programming languages and has a graphical user interface (PyViz) for visualization. It can be integrated with various simulation models and tools, such as Wireshark, Click, and OpenFlow.



## Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol.
- There are three types of sockets: stream sockets, datagram sockets and raw sockets.
- Stream sockets use TCP (Transmission Control Protocol) as the transport layer protocol, which provides a reliable, connection-oriented and byte-stream service .
- Datagram sockets use UDP (User Datagram Protocol) as the transport layer protocol, which provides an unreliable, connectionless and message-oriented service .
- Raw sockets can use any protocol, but they require the programmer to handle the headers and checksums of the packets.
- TCP and UDP have different characteristics and trade-offs, and they are suited for different applications.
- TCP ensures that the data is delivered in order and without errors, but it has more overhead and latency than UDP.
- UDP is faster and more efficient than TCP, but it does not guarantee the delivery, order or integrity of the data.
- Some examples of applications that use TCP are web browsing, email, file transfer and remote login.
- Some examples of applications that use UDP are video streaming, online gaming, voice over IP and DNS.
- To program sockets in C/C++, the socket.h header file is required, which provides the functions and structures for creating, binding, listening, connecting, sending and receiving sockets.
- To program sockets in Python, the socket module is required, which provides the functions and classes for creating, binding, listening, connecting, sending and receiving sockets .
- The main difference between working with TCP and UDP in Python is that, when creating the socket, you have to use SOCK_DGRAM for UDP and SOCK_STREAM for TCP.
- A simple DNS (Domain Name System) client/server application can use UDP sockets to exchange queries and responses between the client and the server.
- A simple data & time client/server application can use TCP sockets to establish a connection between the client and the server, and then send and receive the current date and time as a string.
- A simple echo client/server application can use either TCP or UDP sockets to send and receive the same message between the client and the server .
- An iterative server is a server that handles one client request at a time, and then waits for the next request.
- A concurrent server is a server that can handle multiple client requests simultaneously, using either processes or threads.
- An iterative server is simpler to implement than a concurrent server, but it has lower performance and scalability.
- A concurrent server is more complex to implement than an iterative server, but it has higher performance and scalability.

