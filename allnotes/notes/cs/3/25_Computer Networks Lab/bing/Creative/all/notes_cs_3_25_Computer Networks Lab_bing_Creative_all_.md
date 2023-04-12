

# Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

## Stop and Wait Protocol

- Stop and wait protocol is a data link layer protocol that provides unidirectional data transmission over a noiseless channel.
- In this protocol, the sender sends one packet at a time and waits for an acknowledgment from the receiver before sending the next packet.
- The sender and the receiver use a sliding window of size 1, which means they can only send or receive one packet at a time.
- The sender and the receiver use two sequence numbers, 0 and 1, to identify the packets and avoid duplication.
- The efficiency of stop and wait protocol is low, as the sender has to wait for the round trip time (RTT) of each packet, which is the time taken for a packet to travel from the sender to the receiver and back.
- The efficiency of stop and wait protocol is given by:

  Efficiency = Useful time / Total cycle time = Tt / (Tt + 2Tp) = 1 / (1 + 2a) [a = Tp/Tt]

  where Tt is the transmission time of a packet, Tp is the propagation delay of the channel, and a is the ratio of Tp to Tt.

## Sliding Window Protocol

- Sliding window protocol is a data link layer protocol that provides bidirectional data transmission over a noisy channel.
- In this protocol, the sender can send multiple packets without waiting for an acknowledgment from the receiver, as long as the number of packets does not exceed the window size.
- The window size is the maximum number of packets that can be sent or received at a time, and it is determined by the bandwidth-delay product of the channel.
- The sender and the receiver use sequence numbers to identify the packets and acknowledge them, and they use a sliding window to keep track of the packets that are in transit or have been received.
- The efficiency of sliding window protocol is high, as the sender can utilize the channel capacity by sending multiple packets in a single RTT.
- The efficiency of sliding window protocol is given by:

  Efficiency = Window size / (1 + 2a) [a = Tp/Tt]

  where window size is the number of packets that can be sent or received at a time, and a is the ratio of Tp to Tt.

## References

: https://www.geeksforgeeks.org/stop-and-wait-arq/
: https://www.javatpoint.com/stop-and-wait-protocol
: https://www.scaler.com/topics/computer-network/stop-and-wait-protocol/
: https://www.geeksforgeeks.org/stop-and-wait-arq/
: https://www.geeksforgeeks.org/stop-and-wait-protocol-its-problems-and-solutions/
: https://www.javatpoint.com/sliding-window-protocol



# Experiment 1.1 - Implementation of Stop and Wait Protocol

## Objective
The objective of this experiment is to implement the stop and wait protocol, which is a flow control protocol that ensures reliable data transmission over a noiseless channel.

## Theory
- The stop and wait protocol is a data-link layer protocol that uses a half-duplex link between the sender and the receiver. This means that only one direction of data transmission is possible at a time.
- The sender sends one data packet or frame at a time and waits for an acknowledgment (ACK) from the receiver before sending the next packet. The receiver sends an ACK after receiving a packet and checking its validity.
- The sender and the receiver use sequence numbers to identify the packets and avoid duplication. The sequence numbers alternate between 0 and 1, as the window size of the protocol is 1.
- The stop and wait protocol is simple and easy to implement, but it has low efficiency and throughput. The efficiency is the ratio of the useful time to the total cycle time, and the throughput is the rate of data transmission. The efficiency and the throughput depend on the propagation delay, which is the time taken by a packet to travel from the sender to the receiver, and the transmission time, which is the time taken by a packet to be transmitted on the channel.
- The efficiency of the stop and wait protocol is given by:

  `Efficiency = Tt / (Tt + 2Tp)`

  where Tt is the transmission time and Tp is the propagation delay.

  The throughput of the stop and wait protocol is given by:

  `Throughput = L / (Tt + 2Tp)`

  where L is the length of the packet.

## Procedure
- To implement the stop and wait protocol, we need two programs: one for the sender and one for the receiver. We can use any programming language, such as C, Java, Python, etc., to write the programs.
- The sender program should perform the following steps:

  1. Create a socket and bind it to a port number.
  2. Initialize the sequence number to 0 and the buffer to store the data to be sent.
  3. Read the data from a file or the user input and store it in the buffer.
  4. Create a packet with the data and the sequence number and send it to the receiver using the socket.
  5. Start a timer and wait for an ACK from the receiver.
  6. If the ACK is received and matches the sequence number, stop the timer and increment the sequence number. Go to step 3 and repeat until all the data is sent.
  7. If the ACK is not received or does not match the sequence number, resend the packet and restart the timer. Go to step 5 and repeat until the ACK is received or the maximum number of retries is reached.
  8. Close the socket and exit the program.

- The receiver program should perform the following steps:

  1. Create a socket and bind it to a port number.
  2. Initialize the sequence number to 0 and the buffer to store the received data.
  3. Receive a packet from the sender using the socket and check its validity.
  4. If the packet is valid and matches the sequence number, store the data in the buffer and send an ACK with the same sequence number to the sender using the socket. Increment the sequence number.
  5. If the packet is invalid or does not match the sequence number, discard the packet and send a negative acknowledgment (NAK) with the same sequence number to the sender using the socket. Do not increment the sequence number.
  6. Go to step 3 and repeat until all the data is received.
  7. Write the data from the buffer to a file or the user output.
  8. Close the socket and exit the program.

## Results and Observations
- After running the sender and the receiver programs, we can observe the data transmission and the ACK/NAK exchange between them. We can also measure the efficiency and the throughput of the protocol using the formulae given in the theory section.
- We can observe that the stop and wait protocol works correctly for a noiseless channel, but it has low efficiency and throughput due to the waiting time and the overhead of the ACK/NAK packets. We can also observe that the protocol can handle packet loss and duplication by resending the packets and using the sequence numbers.



# Experiment 1.2 - Implementation of Sliding Window Protocol

## Objective
The objective of this experiment is to implement and simulate the sliding window protocol, which is a feature of packet-based data transmission protocols. The sliding window protocol is used to ensure reliable and sequential delivery of data frames between a sender and a receiver, as well as to optimize the packet flow and avoid congestion.

## Theory
The sliding window protocol works as follows:

- The sender maintains a window of size `ws` that indicates how many frames it can send before receiving an acknowledgment from the receiver. The window slides forward as the sender receives acknowledgments for the sent frames.
- The receiver maintains a window of size `wr` that indicates how many frames it can receive and buffer before sending an acknowledgment to the sender. The window slides forward as the receiver sends acknowledgments for the received frames.
- Each frame has a sequence number that identifies its position in the data stream. The sequence numbers are modulo `n`, where `n` is the maximum number of frames that can be sent or received without wrapping around. The sequence numbers are used to detect and handle lost, duplicated, or out-of-order frames.
- The sender and the receiver use timers to detect and recover from frame losses. The sender sets a timer for each frame it sends and retransmits the frame if the timer expires before receiving an acknowledgment. The receiver sets a timer for each frame it expects and sends a negative acknowledgment (NAK) if the timer expires before receiving the frame.

There are different variants of the sliding window protocol, such as stop-and-wait, go-back-N, and selective repeat, that differ in how they handle frame losses and acknowledgments.

- Stop-and-wait: This is the simplest sliding window protocol, where `ws = wr = 1`. The sender sends one frame at a time and waits for an acknowledgment before sending the next frame. The receiver sends an acknowledgment for each frame it receives. This protocol is inefficient as it does not utilize the full bandwidth of the channel.
- Go-back-N: This is a sliding window protocol where `ws > 1` and `wr = 1`. The sender can send multiple frames at a time without waiting for acknowledgments, but it must keep a copy of each frame in case of retransmission. The receiver sends an acknowledgment for the last correctly received frame in sequence, and discards any out-of-order frames. The sender retransmits all the frames from the last acknowledged frame to the current frame if it receives a NAK or a timeout. This protocol is more efficient than stop-and-wait, but it may waste bandwidth by retransmitting frames that have already been received by the receiver.
- Selective repeat: This is a sliding window protocol where `ws > 1` and `wr > 1`. The sender can send multiple frames at a time without waiting for acknowledgments, but it must keep a copy of each frame in case of retransmission. The receiver can receive and buffer multiple frames out of order, and sends an acknowledgment for each frame it receives. The sender retransmits only the frames that have not been acknowledged by the receiver. This protocol is the most efficient among the sliding window protocols, but it requires more buffer space and complexity at both the sender and the receiver.

## Procedure
The procedure for implementing the sliding window protocol is as follows:

- Define the parameters of the protocol, such as `ws`, `wr`, `n`, and the frame size.
- Create a sender and a receiver process that communicate through a shared channel.
- Implement the sender process as follows:
  - Initialize a variable `sn` to store the sequence number of the next frame to be sent.
  - Initialize a variable `sf` to store the sequence number of the first frame in the window.
  - Initialize a variable `sl` to store the sequence number of the last frame in the window.
  - Initialize an array `buffer` to store the frames to be sent.
  - Initialize an array `timer` to store the timers for each frame in the window.
  - Repeat the following steps until all the data is sent:
    - If the window is not full and there is data to be sent, generate a frame with the sequence number `sn` and the data, and store it in the `buffer`.
    - Send the frame in the `buffer` with the sequence number `sn` to the channel, and start the timer for that frame.
    - Increment `sn` by 1 modulo `n`, and update `sl` accordingly.
    - Wait for an acknowledgment or a timeout from the channel.
    -



# Experiment 2 - Study of Socket Programming and Client – Server model

## Objective
To understand the concept of socket programming and client-server model in network communication.

## Theory
- A socket is a simple communication channel through which two programs communicate over a network.
- A socket supports two-way communication between a client and a server, using a well-established protocol.
- A protocol is a set of rules and behavior that both the server and client must follow in order to establish two-way communication.
- A common protocol for socket communication is the Transmission Control Protocol (TCP), which provides reliable, in-order and error-free delivery of data .
- A socket is identified by a combination of an IP address and a port number.
- An IP address is a unique identifier for a device on a network, and a port number is a logical identifier for a specific process or service on that device.
- A socket on the server process waits for requests from a client, and binds an address that clients can use to find the server.
- A socket on the client process initiates a connection request to the server, and sends or receives data through the established connection.
- A socket can be either stream-oriented or datagram-oriented.
- A stream-oriented socket, also known as a connection-oriented socket, establishes a connection before transferring data, and ensures that the data is delivered reliably and in order.
- A datagram-oriented socket, also known as a connectionless socket, does not require a connection, and each packet sent or received on a datagram socket is individually addressed and routed.
- Socket programming is the process of creating and using sockets to enable communication between processes.
- Socket programming can be done in various programming languages, such as C, C++, Java, Python, etc .
- Socket programming involves the following steps :
  - Socket creation: A socket is created using the socket() function, which takes the domain, type and protocol as parameters, and returns a socket descriptor, an integer that identifies the socket.
  - Socket options: The socket options can be manipulated using the setsockopt() function, which takes the socket descriptor, the level, the option name and the option value as parameters, and allows changing the behavior of the socket.
  - Socket binding: The socket is bound to an address using the bind() function, which takes the socket descriptor and the address structure as parameters, and assigns a local protocol address to the socket.
  - Socket listening: The socket is set to listen for incoming connection requests using the listen() function, which takes the socket descriptor and the backlog as parameters, and marks the socket as a passive socket that can accept connections.
  - Socket connection: The socket is connected to a remote address using the connect() function, which takes the socket descriptor and the address structure as parameters, and initiates a connection to the specified address.
  - Socket acceptance: The socket accepts a connection request from a client using the accept() function, which takes the socket descriptor and the address structure as parameters, and returns a new socket descriptor for the accepted connection.
  - Socket communication: The socket can send or receive data using the send() and recv() functions, which take the socket descriptor, the buffer, the length and the flags as parameters, and transfer data between the connected sockets.
  - Socket closure: The socket is closed using the close() function, which takes the socket descriptor as a parameter, and releases the resources associated with the socket.

## References
: http://www.csce.uark.edu/~mqhuang/courses/3613/s2023/lectures/Lecture_3_socket.pdf
: https://eng.libretexts.org/Bookshelves/Computer_Science/Programming_Languages/Java_Java_Java_-_Object-Oriented_Programming_(Morelli_and_Walde)/15%3A_Sockets_and_Networking/15.06%3A_Client_Server_Communication_via_Sockets
: https://www.ibm.com/docs/en/i/7.3?topic=programming-how-sockets-work
: http://www.csce.uark.edu/~mqhuang/courses/3613/s2022/lectures/Lecture_3_socket.pdf
:



# Experiment 2.1 - Study of Socket Programming

## Objective
To learn the basics of socket programming and how to write client/server applications using sockets.

## Theory
- A socket is an endpoint of communication between two processes or machines on a network.
- Socket programming is the process of creating and using sockets to send and receive data over a network.
- Sockets can be classified into two types: stream sockets and datagram sockets.
- Stream sockets use TCP as the transport protocol and provide reliable, ordered, and error-free communication.
- Datagram sockets use UDP as the transport protocol and provide unreliable, unordered, and error-prone communication.
- Sockets can also be classified into two domains: Internet domain and Unix domain.
- Internet domain sockets use IP addresses and port numbers to identify the endpoints of communication.
- Unix domain sockets use file system paths to identify the endpoints of communication.
- Sockets are supported by various operating systems, such as Unix, Windows, Mac, etc.
- Sockets can be created and manipulated using various programming languages, such as C, Python, Java, etc.

## Steps
- To create a socket, we need to specify the domain, the type, and the protocol of the socket.
- To use a socket, we need to perform the following steps:
  - Bind the socket to a local address and port using the bind() function.
  - Listen for incoming connections using the listen() function (for server sockets only).
  - Accept a connection from a remote socket using the accept() function (for server sockets only).
  - Connect to a remote socket using the connect() function (for client sockets only).
  - Send and receive data using the send() and recv() functions (for stream sockets) or the sendto() and recvfrom() functions (for datagram sockets).
  - Close the socket using the close() function.
- To use sockets in different programming languages, we need to import the socket library and use the appropriate functions and methods provided by the library.



# Experiment 2.2 - Study of Client – Server model

## Objective
To understand the basic concepts and functions of the client-server model in network computing.

## Theory
- The client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.
- Often clients and servers communicate over a computer network on separate hardware, but both client and server may reside in the same system.
- A server is a powerful centralized computer that hosts one or more services or resources that are shared with the clients.
- A client is a computer or a software program that requests and receives services or resources from the server.
- The client-server connection is established through a network or the Internet.
- The client-server model is based on the principle of request-response, where the client initiates a request to the server and the server responds with the desired service or resource.
- The client-server model can support different types of services, such as web, email, file transfer, database, printing, etc.
- The client-server model has some advantages, such as:
  - Centralized system with all data in a single place.
  - Cost efficient, requires less maintenance cost and data recovery is possible.
  - The capacity of the client and server can be changed separately.
  - Scalable and flexible, can support multiple clients and servers.
  - Secure, can implement authentication and encryption mechanisms.
- The client-server model also has some disadvantages, such as:
  - Server dependency, if the server fails or is overloaded, the clients cannot access the services or resources.
  - Network dependency, if the network is slow or unreliable, the communication between the client and server is affected.
  - Security risks, if the server is compromised or attacked, the data and services can be exposed or corrupted.

## Procedure
- To study the client-server model, we need to set up a network environment with at least one server and one client computer.
- The server computer should have a server operating system and the required software to provide the services or resources that we want to study, such as web server, email server, file server, etc.
- The client computer should have a client operating system and the required software to request and receive the services or resources from the server, such as web browser, email client, file explorer, etc.
- The server and client computers should be connected to the same network or the Internet, either through wired or wireless connections.
- To test the client-server model, we need to perform the following steps:
  - On the server computer, start the server software and configure the settings, such as the port number, the service name, the access permissions, etc.
  - On the client computer, start the client software and enter the address or the name of the server, such as the IP address, the domain name, the URL, etc.
  - On the client software, send a request to the server for the desired service or resource, such as a web page, an email, a file, etc.
  - On the server software, receive the request from the client and process it according to the server settings and the service logic.
  - On the server software, send a response to the client with the requested service or resource, or an error message if the request cannot be fulfilled.
  - On the client software, receive the response from the server and display or use the service or resource, or handle the error message if the response is unsuccessful.
  - Repeat the above steps for different types of services or resources and observe the results.

## References
: https://en.wikipedia.org/wiki/Client%E2%80%93server_model
: https://www.indeed.com/career-advice/career-development/what-is-client-server-model
: https://www.techopedia.com/definition/18321/client-server-model
: https://www.geeksforgeeks.org/client-server-model/
: https://www.serverwatch.com/guides/client-server-model/



## Experiment 3 - Write a code simulating ARP /RARP protocols

- ARP stands for Address Resolution Protocol. It is a network protocol that maps an IP address to a MAC address in a local area network (LAN).
- RARP stands for Reverse Address Resolution Protocol. It is a network protocol that maps a MAC address to an IP address in a LAN.
- Both ARP and RARP use the same packet format, which consists of the following fields:
  - Hardware type: specifies the type of network hardware, such as Ethernet or Token Ring.
  - Protocol type: specifies the type of network protocol, such as IPv4 or IPv6.
  - Hardware length: specifies the length of the hardware address in bytes, such as 6 for Ethernet MAC address.
  - Protocol length: specifies the length of the protocol address in bytes, such as 4 for IPv4 address.
  - Operation: specifies the type of operation, such as 1 for ARP request, 2 for ARP reply, 3 for RARP request, or 4 for RARP reply.
  - Sender hardware address: specifies the MAC address of the sender of the packet.
  - Sender protocol address: specifies the IP address of the sender of the packet.
  - Target hardware address: specifies the MAC address of the target of the packet.
  - Target protocol address: specifies the IP address of the target of the packet.
- The following is a pseudocode for simulating ARP /RARP protocols:

```python
# Define a class for ARP /RARP packet
class ARPPacket:
  def __init__(self, hw_type, pr_type, hw_len, pr_len, op, sha, spa, tha, tpa):
    self.hw_type = hw_type # Hardware type
    self.pr_type = pr_type # Protocol type
    self.hw_len = hw_len # Hardware length
    self.pr_len = pr_len # Protocol length
    self.op = op # Operation
    self.sha = sha # Sender hardware address
    self.spa = spa # Sender protocol address
    self.tha = tha # Target hardware address
    self.tpa = tpa # Target protocol address

# Define a function for sending an ARP /RARP packet
def send_packet(packet):
  # Check the operation field of the packet
  if packet.op == 1: # ARP request
    # Broadcast the packet to all nodes in the LAN
    broadcast(packet)
    # Wait for an ARP reply from the target node
    reply = receive_packet()
    # Check if the reply matches the request
    if reply.op == 2 and reply.spa == packet.tpa and reply.tpa == packet.spa:
      # Print the MAC address of the target node
      print("The MAC address of " + packet.tpa + " is " + reply.sha)
    else:
      # Print an error message
      print("No ARP reply received")
  elif packet.op == 2: # ARP reply
    # Send the packet to the node that sent the ARP request
    send(packet, packet.tha)
  elif packet.op == 3: # RARP request
    # Broadcast the packet to all nodes in the LAN
    broadcast(packet)
    # Wait for a RARP reply from the gateway router
    reply = receive_packet()
    # Check if the reply matches the request
    if reply.op == 4 and reply.sha == packet.tha and reply.tha == packet.sha:
      # Print the IP address of the sender node
      print("The IP address of " + packet.sha + " is " + reply.spa)
    else:
      # Print an error message
      print("No RARP reply received")
  elif packet.op == 4: # RARP reply
    # Send the packet to the node that sent the RARP request
    send(packet, packet.tha)
  else:
    # Print an error message
    print("Invalid operation")
```



## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

- Ping and traceroute are common commands you can use to troubleshoot network problems  .
- Ping is a simple command that can test the reachability of a device on the network by sending an ICMP echo request and waiting for an ICMP echo reply   .
- Traceroute is a command you use to 'trace' the route that a packet takes when traveling to its destination by sending a series of ICMP echo requests with increasing TTL values and recording the ICMP time exceeded responses from the intermediate routers    .
- To write a code simulating ping and traceroute commands, you need to use a programming language that can send and receive raw network packets, such as Python, C, or Java.
- You also need to use a library or a module that can handle ICMP messages, such as scapy for Python, libnet for C, or jpcap for Java.
- The basic steps for writing a code simulating ping and traceroute commands are:

  - Import the necessary libraries or modules for network programming and ICMP handling.
  - Define a function for sending an ICMP echo request to a given destination address and port number, and returning the ICMP echo reply or an error message if any.
  - Define a function for sending a series of ICMP echo requests to a given destination address and port number, with increasing TTL values from 1 to a maximum limit, and returning the ICMP time exceeded responses or the ICMP echo reply from the destination if any.
  - Define a function for calculating the round-trip time (RTT) between sending and receiving an ICMP message, and formatting the output in a readable way.
  - Define a function for validating the user input, such as checking if the destination address is valid and reachable, and handling any exceptions or errors.
  - Define a main function for taking the user input, such as the destination address and port number, and the command to execute (ping or traceroute), and calling the appropriate functions to perform the network test and display the results.
  - Run the main function and test the code with different destination addresses and port numbers, and compare the results with the actual ping and traceroute commands.

- The following is an example of a code simulating ping and traceroute commands in Python, using the scapy module:

```python
# Import the scapy module
from scapy.all import *

# Define a function for sending an ICMP echo request and returning the ICMP echo reply or an error message
def send_ping(dst, port):
  # Create an ICMP echo request packet with the destination address and port number
  packet = IP(dst=dst)/ICMP()/UDP(dport=port)
  # Send the packet and wait for a response, with a timeout of 2 seconds
  response = sr1(packet, timeout=2, verbose=0)
  # If there is a response, return it
  if response:
    return response
  # If there is no response, return an error message
  else:
    return "Request timed out"

# Define a function for sending a series of ICMP echo requests with increasing TTL values and returning the ICMP time exceeded responses or the ICMP echo reply
def send_traceroute(dst, port):
  # Initialize an empty list for storing the responses
  responses = []
  # Initialize the TTL value to 1
  ttl = 1
  # Initialize a flag to indicate if the destination is reached
  reached = False
  # Loop until the destination is reached or the TTL value exceeds the maximum limit of 30
  while not reached and ttl <= 30:
    # Create an ICMP echo request packet with the destination address, port number, and TTL value
    packet = IP(dst=dst, ttl=ttl)/ICMP()/UDP(dport=port)
    # Send the packet and wait for a response, with a timeout of 2 seconds
    response = sr1(packet, timeout=2, verbose=0)
    # If there is a response, append it to the list of responses
    if response:
      responses.append(response)
      # If the response is an ICMP echo reply, set the flag to True and break the loop
      if response[ICMP].type == 0:
        reached = True
        break
    # If there is no response,

```




## Experiment 5 - Create a socket for HTTP for web page upload and download

- A socket is an endpoint of a communication between two processes or machines on a network.
- HTTP (Hypertext Transfer Protocol) is a protocol that defines how messages are formatted and transmitted over the web, and how servers and browsers should respond to various commands.
- To create a socket for HTTP, we need to use the socket module in Python, which provides a low-level interface to the network layer.
- The steps to create a socket for HTTP are:

  - Import the socket module: `import socket`
  - Create a socket object: `s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
  - The first argument `socket.AF_INET` specifies the address family, which is IPv4 in this case. The second argument `socket.SOCK_STREAM` specifies the socket type, which is TCP in this case.
  - Connect the socket to a server address and port: `s.connect((host, port))`
  - The host can be a domain name or an IP address. The port is usually 80 for HTTP.
  - Send an HTTP request to the server: `s.send(request.encode())`
  - The request should follow the HTTP protocol format, which consists of a request line, headers, and an optional body. For example, a GET request to retrieve a web page could look like this:

    ```
    GET /index.html HTTP/1.1
    Host: www.example.com
    User-Agent: Python-socket
    Connection: close
    ```
  - The request should be encoded as bytes before sending.
  - Receive the HTTP response from the server: `response = s.recv(buffer_size)`
  - The response should also follow the HTTP protocol format, which consists of a status line, headers, and an optional body. For example, a 200 OK response could look like this:

    ```
    HTTP/1.1 200 OK
    Date: Wed, 15 Mar 2023 22:10:34 GMT
    Server: Apache
    Content-Type: text/html
    Content-Length: 1234
    Connection: close

    <html>
    <head>
    <title>Example Page</title>
    </head>
    <body>
    <h1>Hello, World!</h1>
    </body>
    </html>
    ```
  - The response should be decoded as a string after receiving.
  - Close the socket: `s.close()`
  - This will terminate the connection and free up the resources.

- To upload and download a web page using the socket, we need to modify the request and response accordingly.
- To upload a web page, we need to use a POST request instead of a GET request, and include the content of the web page in the body of the request. For example, a POST request to upload a web page could look like this:

    ```
    POST /upload.html HTTP/1.1
    Host: www.example.com
    User-Agent: Python-socket
    Content-Type: text/html
    Content-Length: 5678
    Connection: close

    <html>
    <head>
    <title>Uploaded Page</title>
    </head>
    <body>
    <h1>This is a page uploaded by socket</h1>
    </body>
    </html>
    ```
  - The server should respond with a status code indicating the success or failure of the upload, and optionally a message or a redirect to the uploaded page.
- To download a web page, we need to use a GET request as before, but save the content of the response body to a file. For example, to download a web page and save it as download.html, we could do something like this:

    ```
    request = "GET /download.html HTTP/1.1\r\nHost: www.example.com\r\nUser-Agent: Python-socket\r\nConnection: close\r\n\r\n"
    s.send(request.encode())
    response = s.recv(4096)
    response = response.decode()
    headers, body = response.split("\r\n\r\n", 1)
    with open("download.html", "w") as f:
        f.write(body)
    s.close()
    ```



## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

- RPC is a mechanism that enables data exchange and invocation of functionality residing in a different process.
- RPC can be used to create distributed client/server programs that can communicate across the network or the Internet.
- RPC uses an Interface Definition Language (IDL) to describe the parameters, functions and interfaces of the remote procedure.
- RPC also uses a stub compiler to generate the client and server stubs that handle the marshalling and unmarshalling of data.
- RPC supports both synchronous and asynchronous calls, and various methods of notification of the call's completion.
- RPC can be implemented using C or C++ programming languages, and various libraries and frameworks are available for this purpose  .

The following steps can be followed to write a program to implement RPC:

1. Define the interface of the remote procedure using IDL. The interface should specify the name, parameters, return type and attributes of the remote procedure. For example, the following IDL defines a simple interface for adding two integers:

```
interface Adder
{
  [idempotent] int Add(int a, int b);
};
```

2. Compile the IDL file using the stub compiler. This will generate the client and server stubs, as well as the header file that contains the interface definition. For example, using the Microsoft RPC framework, the following command can be used to compile the IDL file:

```
midl Adder.idl
```

3. Write the client program that invokes the remote procedure. The client program should include the header file generated by the stub compiler, and use the RPC API functions to bind to the server, make the remote procedure call, and unbind from the server. For example, the following code snippet shows a possible client program for the Adder interface:

```
#include <windows.h>
#include <stdio.h>
#include "Adder.h" // the header file generated by the stub compiler

int main()
{
  RPC_STATUS status;
  int a, b, c;
  printf("Enter two numbers: ");
  scanf("%d %d", &a, &b);

  // bind to the server using the interface UUID and the protocol sequence
  status = RpcStringBindingCompose(NULL, "ncacn_ip_tcp", NULL, "1234", NULL, &szStringBinding);
  if (status)
  {
    printf("RpcStringBindingCompose failed: %d\n", status);
    exit(status);
  }

  status = RpcBindingFromStringBinding(szStringBinding, &hAdderBinding);
  if (status)
  {
    printf("RpcBindingFromStringBinding failed: %d\n", status);
    exit(status);
  }

  // make the remote procedure call
  RpcTryExcept
  {
    c = Add(a, b); // the stub function generated by the stub compiler
    printf("The sum is: %d\n", c);
  }
  RpcExcept(1)
  {
    printf("Runtime reported exception: %d\n", RpcExceptionCode());
  }
  RpcEndExcept

  // unbind from the server
  status = RpcBindingFree(&hAdderBinding);
  if (status)
  {
    printf("RpcBindingFree failed: %d\n", status);
    exit(status);
  }

  return 0;
}
```

4. Write the server program that implements the remote procedure. The server program should also include the header file generated by the stub compiler, and use the RPC API functions to register the interface, listen for client requests, and unregister the interface. For example, the following code snippet shows a possible server program for the Adder interface:

```
#include <windows.h>
#include <stdio.h>
#include "Adder.h" // the header file generated by the stub compiler

// the implementation of the remote procedure
int Add(int a, int b)
{
  return a + b;
}

int main()
{
  RPC_STATUS status;

  // register the interface using the interface UUID and the protocol sequence
  status = RpcServerUseProtseq("ncacn_ip_tcp", RPC_C_PROTSEQ_MAX_REQS_DEFAULT, NULL);
  if (status)
  {
    printf("RpcServerUseProtseq failed: %d\n", status);
    exit(status);
  }

  status = RpcServerRegisterIf(Adder_v1_0_s_ifspec, NULL, NULL);
  if (status)
  {
    printf("RpcServerRegister

```




# Experiment 7 - Implementation of Subnetting

## Objective
- To understand the concept of subnetting and its benefits.
- To learn how to divide a network into smaller subnets using subnet masks.
- To practice subnetting calculations and address assignments.

## Theory
- Subnetting is a technique of dividing a large network into smaller subnets, each with its own range of IP addresses and network parameters.
- Subnetting allows efficient use of IP address space, reduces network congestion, improves security and performance, and simplifies network administration and troubleshooting.
- Subnetting involves applying a subnet mask to an IP address, which determines how many bits are used for the network ID and how many bits are used for the host ID.
- The subnet mask is a 32-bit binary number that has 1s in the network ID portion and 0s in the host ID portion. For example, 255.255.255.0 is a subnet mask that indicates that the first 24 bits are used for the network ID and the last 8 bits are used for the host ID.
- The subnet mask can also be written in slash notation, which indicates the number of 1s in the subnet mask. For example, /24 is equivalent to 255.255.255.0.
- To subnet a network, the network administrator borrows some bits from the host ID portion and assigns them to the subnet ID portion. This creates more subnets, but reduces the number of hosts per subnet.
- The number of subnets and hosts per subnet can be calculated using the following formulas:

  - Number of subnets = 2^n, where n is the number of borrowed bits.
  - Number of hosts per subnet = 2^m - 2, where m is the number of remaining bits in the host ID portion. The -2 accounts for the network address and the broadcast address, which cannot be assigned to hosts.

- To assign IP addresses to subnets, the network administrator follows these steps:

  - Choose a subnet mask that meets the requirements of the network.
  - Identify the network address of the original network by performing a bitwise AND operation between the IP address and the subnet mask.
  - Identify the subnet addresses by incrementing the subnet ID portion of the network address by one for each subnet.
  - Identify the host addresses by assigning any value between 1 and 254 to the host ID portion of the subnet address. The value 0 is reserved for the network address and the value 255 is reserved for the broadcast address.
  - Identify the broadcast address of each subnet by replacing the host ID portion of the subnet address with all 1s.

## Example
- Suppose a network has an IP address of 192.168.1.0/24 and needs to be divided into four subnets, each with at least 50 hosts. How can this be done?

  - Step 1: Choose a subnet mask that meets the requirements of the network. Since we need four subnets, we need to borrow two bits from the host ID portion. This gives us a subnet mask of 255.255.255.192 or /26.
  - Step 2: Identify the network address of the original network by performing a bitwise AND operation between the IP address and the subnet mask. This gives us 192.168.1.0 as the network address.
  - Step 3: Identify the subnet addresses by incrementing the subnet ID portion of the network address by one for each subnet. This gives us the following subnet addresses:

    - Subnet 1: 192.168.1.0
    - Subnet 2: 192.168.1.64
    - Subnet 3: 192.168.1.128
    - Subnet 4: 192.168.1.192

  - Step 4: Identify the host addresses by assigning any value between 1 and 254 to the host ID portion of the subnet address. The value 0 is reserved for the network address and the value 255 is reserved for the broadcast address. This gives us the following host address ranges for each subnet:

    - Subnet 1: 192.168.1.1 to 192.168.1.62
    - Subnet 2: 192.168.1.65 to 192.168.1.126
    - Subnet 3: 192.168.1.129 to 192.168.1.190
    - Subnet 4: 192.168.1.193 to 192.168.1.254

  - Step 5: Identify the broadcast address of each subnet by replacing the host ID portion of



## Experiment 8 - Applications using TCP Sockets

TCP sockets are a type of network communication mechanism that allows two processes to exchange data using the Transmission Control Protocol (TCP). TCP is a reliable, connection-oriented protocol that ensures the data is delivered in order and without errors. TCP sockets can be used to implement various network applications, such as:

- **File transfer**: TCP sockets can be used to send and receive files between a client and a server. The client can request a file from the server by sending its name, and the server can send the file contents in chunks until the end of file is reached. The client can save the file locally and acknowledge each chunk received. An example of a file transfer application using TCP sockets is the File Transfer Protocol (FTP).
- **Remote command execution**: TCP sockets can be used to execute commands on a remote machine by sending the command as a string and receiving the output as a stream of bytes. The client can send a command to the server, and the server can execute the command using a system call and send the output back to the client. The client can display the output on the console or save it to a file. An example of a remote command execution application using TCP sockets is the Secure Shell (SSH).
- **Chat**: TCP sockets can be used to implement a chat application that allows multiple users to communicate with each other in real time. The client can send a message to the server, and the server can broadcast the message to all the other connected clients. The client can also receive messages from the server and display them on the screen. An example of a chat application using TCP sockets is the Internet Relay Chat (IRC).
- **Web**: TCP sockets can be used to implement a web application that allows a client to request and receive web pages from a server. The client can send a request to the server using the Hypertext Transfer Protocol (HTTP), and the server can send the response containing the web page contents in the HyperText Markup Language (HTML) format. The client can render the web page on the browser and display the images, links, and other elements. An example of a web application using TCP sockets is the World Wide Web (WWW).



# Experiment 8.1 - Echo client and echo server

- An echo client and echo server are applications that allow a client and a server to communicate over a network using sockets     .
- An echo client sends a message to the echo server and waits for a response. The echo server receives the message and sends back an identical copy of the message to the echo client. The echo client displays the received message on the standard output     .
- The purpose of an echo client and echo server is to test the connectivity and functionality of the network and the sockets. They can also be used to measure the latency and throughput of the network     .
- An echo client and echo server can be implemented using different protocols, such as TCP or UDP. TCP is a reliable and connection-oriented protocol that ensures the delivery and order of the messages. UDP is an unreliable and connectionless protocol that does not guarantee the delivery and order of the messages     .
- An echo client and echo server can be implemented using different programming languages, such as Java, Python, or C. The programming language should provide a socket API that allows the creation and manipulation of sockets. The socket API should also support the protocol of choice, such as TCP or UDP     .
- An echo client and echo server can be implemented using different architectures, such as single-threaded or multi-threaded. A single-threaded server can handle only one client connection at a time. A multi-threaded server can handle multiple client connections concurrently by creating a new thread for each client     .



# Experiment 8.2 - Chat

- The objective of this experiment is to learn how to create a simple chat application using Python and sockets.
- A chat application allows two or more users to communicate with each other over a network using text messages.
- A chat application consists of two main components: a server and a client.
- The server is a program that listens for incoming connections from clients and relays messages between them.
- The client is a program that connects to the server and sends and receives messages from other clients.
- To create a chat application, we need to use the socket module in Python, which provides low-level access to network communication.
- A socket is an endpoint of a communication channel between two processes or machines.
- A socket has an address, which consists of an IP address and a port number.
- An IP address is a unique identifier for a machine on a network, and a port number is a number between 0 and 65535 that identifies a specific service or application on that machine.
- To create a socket in Python, we use the socket.socket() function, which takes two arguments: the address family and the socket type.
- The address family specifies the protocol used for communication, such as IPv4 or IPv6.
- The socket type specifies the mode of communication, such as TCP or UDP.
- TCP stands for Transmission Control Protocol, which is a reliable and ordered way of sending and receiving data.
- UDP stands for User Datagram Protocol, which is a fast and unreliable way of sending and receiving data.
- For this experiment, we will use TCP sockets, which are suitable for chat applications.
- To create a TCP socket in Python, we use the following code:

```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

- The first argument, socket.AF_INET, specifies the IPv4 address family.
- The second argument, socket.SOCK_STREAM, specifies the TCP socket type.
- The variable s is a socket object that we can use to perform various operations, such as binding, listening, connecting, sending and receiving data.



# Experiment 8.3 - File Transfer

- The objective of this experiment is to learn how to transfer files between different devices using various protocols and methods.
- The prerequisites for this experiment are:
  - Basic knowledge of networking concepts and terminology.
  - Access to at least two devices that can communicate over a network, such as computers, smartphones, tablets, etc.
  - A common file format that can be transferred and opened by both devices, such as a text file, an image file, a PDF file, etc.
- The steps for this experiment are:
  - Choose a file that you want to transfer from one device to another. Make sure the file is not too large or too sensitive for the purpose of this experiment.
  - Decide which protocol or method you want to use for the file transfer. Some common options are:
    - FTP (File Transfer Protocol): A standard network protocol for transferring files between a client and a server over a TCP/IP network. You will need an FTP client software on the device that initiates the transfer, and an FTP server software on the device that receives the transfer. You will also need to know the IP address, username, and password of the FTP server.
    - HTTP (Hypertext Transfer Protocol): A standard network protocol for transferring files between a web browser and a web server over a TCP/IP network. You will need a web browser on the device that initiates the transfer, and a web server software on the device that receives the transfer. You will also need to know the URL (Uniform Resource Locator) of the file on the web server.
    - Bluetooth: A wireless technology for transferring files between devices that are in close proximity to each other. You will need to enable Bluetooth on both devices, and pair them with each other. You will also need to select the file on the device that initiates the transfer, and accept the file on the device that receives the transfer.
    - Email: A method of transferring files by attaching them to an email message and sending them to a recipient. You will need an email account and an email client software on the device that initiates the transfer, and an email account and an email client software on the device that receives the transfer. You will also need to know the email address of the recipient, and the size limit of the email attachment.
  - Follow the instructions of the chosen protocol or method to transfer the file from one device to another. Verify that the file has been transferred successfully and that it can be opened by the receiving device.
  - Repeat the steps with different files, protocols, and methods to compare their advantages and disadvantages. Some factors to consider are:
    - Speed: How fast is the file transfer?
    - Reliability: How likely is the file transfer to fail or be interrupted?
    - Security: How secure is the file transfer from unauthorized access or modification?
    - Ease of use: How easy is the file transfer to set up and perform?
    - Compatibility: How compatible is the file transfer with different devices and file formats?
- The expected outcomes of this experiment are:
  - You will gain practical experience in transferring files between different devices using various protocols and methods.
  - You will understand the benefits and drawbacks of different file transfer options.
  - You will be able to choose the most suitable file transfer option for different scenarios and purposes.



# Experiment 9 - Applications using TCP and UDP Sockets

## Introduction

TCP and UDP are two of the most common transport layer protocols used for sending and receiving data over the Internet. They are both based on the IP protocol, which provides the basic mechanism for delivering packets from one node to another. However, they have different characteristics and features that make them suitable for different types of applications.

## TCP Sockets

TCP stands for Transmission Control Protocol. It is a connection-oriented protocol, which means that it establishes a reliable and ordered communication channel between two nodes before exchanging data. TCP sockets are the endpoints of a TCP connection, identified by a combination of IP address and port number. A TCP socket can only send and receive data to and from the remote node that it is connected to.

Some of the features of TCP sockets are:

- They use a three-way handshake to establish a connection, which involves sending and acknowledging SYN, SYN-ACK, and ACK packets.
- They use sequence numbers and acknowledgments to ensure that all data is delivered correctly and in order.
- They use flow control and congestion control mechanisms to adjust the sending rate and window size according to the network conditions.
- They use a four-way handshake to terminate a connection, which involves sending and acknowledging FIN, FIN-ACK, ACK, and RST packets.

Some of the applications that use TCP sockets are:

- Web browsers and servers, which use HTTP over TCP to exchange web pages and other resources.
- Email clients and servers, which use SMTP over TCP to send and receive emails.
- File transfer clients and servers, which use FTP over TCP to upload and download files.
- Remote login clients and servers, which use SSH or Telnet over TCP to execute commands on remote machines.

## UDP Sockets

UDP stands for User Datagram Protocol. It is a connectionless protocol, which means that it does not establish or maintain a communication channel between two nodes. UDP sockets are the endpoints of a UDP communication, identified by a combination of IP address and port number. A UDP socket can send and receive data to and from any node at any time with the same socket.

Some of the features of UDP sockets are:

- They do not use any handshake to establish or terminate a communication, which makes them faster and simpler than TCP sockets.
- They do not use any sequence numbers or acknowledgments to ensure that data is delivered correctly and in order. They rely on the application layer to handle any errors or losses.
- They do not use any flow control or congestion control mechanisms to adjust the sending rate or window size. They send data as fast as possible, regardless of the network conditions.
- They do not guarantee any ordering or reliability of data. They may deliver data out of order, duplicate, or drop data.

Some of the applications that use UDP sockets are:

- Streaming media clients and servers, which use RTP over UDP to transmit audio and video data in real time.
- Online gaming clients and servers, which use UDP to exchange game state and events with low latency and high responsiveness.
- Voice over IP clients and servers, which use SIP over UDP to establish and manage voice calls over the Internet.
- Domain name system clients and servers, which use DNS over UDP to resolve domain names to IP addresses.



# Experiment 9.1 - DNS

DNS stands for Domain Name System. It is a system that maps domain names to IP addresses. Domain names are human-readable names that identify websites, such as www.google.com. IP addresses are numerical identifiers that computers use to communicate over the Internet, such as 142.250.74.196.

The purpose of DNS is to allow users to access websites using domain names instead of IP addresses, which are easier to remember and type. DNS also provides other services, such as email delivery, load balancing, and security.

The main components of DNS are:

- DNS servers: These are computers that store and update the mappings between domain names and IP addresses. There are different types of DNS servers, such as root servers, authoritative servers, and recursive servers.
- DNS resolvers: These are programs that run on the user's device and query DNS servers to find the IP address of a domain name. The resolver may cache the results of previous queries to speed up the process.
- DNS records: These are data entries that store the information about a domain name and its IP address. There are different types of DNS records, such as A records, CNAME records, MX records, and NS records.

The process of resolving a domain name to an IP address involves the following steps:

- The user types a domain name in the browser, such as www.example.com.
- The browser sends a DNS query to the resolver, asking for the IP address of www.example.com.
- The resolver checks its cache to see if it already has the answer. If not, it sends a query to a root server, which is one of the 13 servers that manage the top-level domains, such as .com, .org, .net, etc.
- The root server responds with a referral to an authoritative server for the .com domain, which is responsible for managing the subdomains under .com, such as example.com, google.com, etc.
- The resolver sends a query to the authoritative server for the .com domain, asking for the IP address of www.example.com.
- The authoritative server responds with a referral to another authoritative server for the example.com domain, which is responsible for managing the subdomains under example.com, such as www.example.com, mail.example.com, etc.
- The resolver sends a query to the authoritative server for the example.com domain, asking for the IP address of www.example.com.
- The authoritative server responds with the IP address of www.example.com, which is stored in an A record.
- The resolver returns the IP address of www.example.com to the browser, and caches the result for future use.
- The browser uses the IP address of www.example.com to establish a connection with the web server and request the web page.



# Experiment 9.2 - SNMP

## Objective
- To learn about the Simple Network Management Protocol (SNMP) and its components.
- To use SNMP commands to monitor and manage network devices.

## Theory
- SNMP is an application layer protocol that allows network administrators to remotely monitor and manage network devices such as routers, switches, servers, printers, etc.
- SNMP uses a client-server model, where the client is called a manager and the server is called an agent.
- The manager sends requests to the agent using SNMP messages, and the agent responds with the requested information or performs the requested action.
- The agent also sends unsolicited messages to the manager, called traps or notifications, to report significant events or errors.
- SNMP messages are encoded using the Abstract Syntax Notation One (ASN.1) and transmitted using the User Datagram Protocol (UDP).
- SNMP has three versions: SNMPv1, SNMPv2c, and SNMPv3. The main differences among them are the security and authentication mechanisms.
- SNMP uses a hierarchical data structure called the Management Information Base (MIB), which defines the variables that can be accessed by the manager and the agent.
- The MIB consists of a collection of objects, each identified by a unique name called an Object Identifier (OID).
- The OID follows a tree-like structure, where each node represents a specific organization, standard, or vendor.
- The MIB objects can be either scalar (single-valued) or tabular (multi-valued), and can have different data types, such as integer, string, counter, gauge, etc.
- The MIB objects can be read-only or read-write, depending on the access rights assigned to them.
- The MIB objects can be accessed using four basic SNMP operations: GET, GETNEXT, SET, and TRAP.
- The GET operation is used to retrieve the value of a specific MIB object, identified by its OID.
- The GETNEXT operation is used to retrieve the value of the next MIB object in the OID tree, starting from a given OID.
- The SET operation is used to modify the value of a writable MIB object, identified by its OID.
- The TRAP operation is used by the agent to send a notification to the manager, containing the OID and the value of the MIB object that triggered the event.

## Procedure
- To perform this experiment, you will need a network simulator software, such as Packet Tracer, GNS3, or NetSim, and a SNMP manager software, such as SNMPc, Net-SNMP, or SNMP Tester.
- You will also need to configure the network devices (routers, switches, etc.) with the appropriate IP addresses, SNMP agent settings, and MIB files.
- The following steps are an example of how to use SNMP commands to monitor and manage network devices, using Packet Tracer and SNMP Tester as the tools.

1. Launch Packet Tracer and create a simple network topology, consisting of a PC, a router, and a switch, as shown in the figure below.

network topology

2. Assign IP addresses to the PC and the router interfaces, as shown in the table below.

| Device | Interface | IP Address | Subnet Mask |
|--------|-----------|------------|-------------|
| PC     | FastEthernet0 | 192.168.1.2 | 255.255.255.0 |
| Router | FastEthernet0/0 | 192.168.1.1 | 255.255.255.0 |
| Router | FastEthernet0/1 | 192.168.2.1 | 255.255.255.0 |
| Switch | N/A | N/A | N/A |

3. Configure the router with the following SNMP agent settings, using the command-line interface (CLI).

- Enable SNMP service with the command `snmp-server enable`.
- Set the SNMP read-only community string to `public` with the command `snmp-server community public RO`.
- Set the SNMP read-write community string to `private` with the command `snmp-server community private RW`.
- Set the SNMP trap destination to the PC's IP address with the command `snmp-server host 192.168.1.2 public`.
- Save the configuration with the command `copy running-config startup-config`.

4. Launch SNMP Tester and enter the following settings in the main window.

- Set the IP address to `192.168.1.1`, the port to `161`, and the community string to `public`.
- Select the `Read Device Uptime` option from the drop-down menu and click the `Run Test` button.
- Observe the output in the lower window,



# Experiment 9.3 - File Transfer

## Objective
- To learn how to transfer files between different devices using various methods and protocols.

## Requirements
- Two or more devices (such as computers, smartphones, tablets, etc.) that can connect to each other via a network (such as Wi-Fi, Bluetooth, USB, etc.).
- A file (such as a document, image, video, etc.) that you want to transfer from one device to another.
- A file transfer application or tool (such as FTP, SCP, AirDrop, ShareIt, etc.) that supports the chosen method and protocol.

## Procedure
- Choose a file that you want to transfer from one device to another. Note the file name, size, type, and location on the source device.
- Choose a method and protocol for transferring the file. For example, you can use Wi-Fi and FTP, or Bluetooth and OBEX, or USB and MTP, etc. Note the advantages and disadvantages of each method and protocol.
- Install and configure the file transfer application or tool on both the source and destination devices. Make sure they are compatible with each other and with the chosen method and protocol.
- Establish a connection between the source and destination devices using the chosen method and protocol. For example, you can connect them to the same Wi-Fi network, or pair them via Bluetooth, or plug them into the same USB port, etc.
- Initiate the file transfer from the source device to the destination device using the file transfer application or tool. For example, you can select the file and click on the send or upload button, or drag and drop the file to the destination device, etc.
- Monitor the progress and status of the file transfer. Note the transfer speed, time, and errors (if any).
- Verify that the file transfer is complete and successful. Check the file name, size, type, and location on the destination device. Compare it with the source device and make sure they are identical.
- Disconnect the connection between the source and destination devices using the chosen method and protocol. For example, you can disconnect from the Wi-Fi network, or unpair from Bluetooth, or unplug from USB, etc.

## Observations
- Record your observations and findings from the experiment. For example, you can note the following:
  - Which method and protocol did you use and why?
  - How easy or difficult was it to install and configure the file transfer application or tool on both devices?
  - How fast or slow was the file transfer speed and time?
  - Did you encounter any errors or issues during the file transfer?
  - How reliable or secure was the file transfer method and protocol?
  - What are the benefits and drawbacks of the file transfer method and protocol?

## Conclusion
- Summarize your conclusion from the experiment. For example, you can state the following:
  - What did you learn from the experiment?
  - How did the experiment meet the objective?
  - What are the implications and applications of the file transfer method and protocol?
  - What are the limitations and challenges of the file transfer method and protocol?



## Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

- Network simulator (NS) is a discrete event simulator that can be used to model and analyze the performance of various network protocols and architectures.
- NS is written in C++ and Tcl (Tool Command Language), and provides a modular framework for creating and configuring network components such as nodes, links, queues, agents, applications, etc.
- NS supports various network technologies such as wired, wireless, satellite, mobile, ad hoc, sensor, optical, etc., and can simulate different aspects of network behavior such as routing, congestion control, traffic generation, error models, etc.
- NS also provides graphical tools for visualizing and animating the network simulation, such as NAM (Network Animator) and Xgraph.
- Congestion control algorithms are mechanisms that aim to regulate the flow of packets in a network, in order to avoid congestion and ensure fair and efficient utilization of network resources.
- Congestion occurs when the demand for network bandwidth exceeds the available capacity, resulting in packet loss, delay, and reduced throughput.
- Congestion control algorithms can be classified into two categories: end-to-end and network-assisted.
- End-to-end congestion control algorithms rely on the feedback from the receivers or the network to adjust the sending rate of the sources, such as TCP (Transmission Control Protocol), which uses acknowledgments and timeouts to detect and recover from packet loss.
- Network-assisted congestion control algorithms involve the cooperation of the network routers or switches to monitor and regulate the traffic flow, such as RED (Random Early Detection), which uses queue length and packet drop probability to signal congestion to the sources.
- NS can be used to simulate and compare the performance of different congestion control algorithms, by varying the network parameters such as link capacity, propagation delay, buffer size, packet size, number of sources, etc., and measuring the metrics such as throughput, delay, packet loss, fairness, etc.



# Experiment 11 - Perform a case study about the different routing algorithms to select the network path with its optimum and economical during data transfer

## Objective
The objective of this experiment is to understand the concept and working of different routing algorithms and to compare their performance in terms of network efficiency and cost.

## Introduction
Routing is the process of finding the best path for sending data packets from a source node to a destination node in a network. Routing algorithms are the rules or methods that routers use to determine the optimal path for each packet. Routing algorithms can be classified into two main categories: adaptive and non-adaptive.

- Adaptive algorithms are the algorithms that change their routing decisions whenever network topology or traffic load changes. The changes in routing decisions are reflected in the topology as well as the traffic of the network. Adaptive algorithms can be further divided into centralized, distributed, and isolated algorithms.

- Non-adaptive algorithms are the algorithms that do not change their routing decisions once the network is established. They are also called static algorithms. Non-adaptive algorithms are simpler and faster than adaptive algorithms, but they may not be able to cope with dynamic network conditions.

## Case Study
In this case study, we will compare four different routing algorithms: shortest path, flooding, distance vector, and link state. We will use a hypothetical network topology as shown in the figure below. The numbers on the links represent the cost or distance of each link. The cost can be measured in terms of hop count, delay, bandwidth, or any other metric.

Network Topology

We will assume that each node in the network is a router that can run any of the four routing algorithms. We will also assume that each router has a routing table that stores the best path and cost to reach every other node in the network. The routing table is updated periodically or whenever there is a change in the network.

We will analyze the performance of each routing algorithm in terms of the following criteria:

- Completeness: The ability of the algorithm to find a path to every destination in the network.
- Correctness: The ability of the algorithm to find the optimal path to every destination in the network.
- Robustness: The ability of the algorithm to adapt to changes in the network topology or traffic load.
- Efficiency: The amount of resources (such as bandwidth, memory, or processing power) consumed by the algorithm.
- Scalability: The ability of the algorithm to handle large and complex networks.

## Shortest Path Algorithm
The shortest path algorithm is a non-adaptive algorithm that finds the path with the minimum cost to every destination in the network. The algorithm uses a global view of the network, which means that every router knows the cost of every link in the network. The algorithm can be implemented using Dijkstra's algorithm or Bellman-Ford algorithm.

The shortest path algorithm is complete and correct, as it always finds the optimal path to every destination in the network. However, the algorithm is not robust, as it does not react to changes in the network topology or traffic load. The algorithm is also not efficient, as it requires a lot of communication and computation to maintain a global view of the network. The algorithm is not scalable, as it becomes impractical for large and complex networks.

## Flooding Algorithm
The flooding algorithm is a non-adaptive algorithm that sends every packet to every link in the network. The algorithm does not use any routing table or cost information. The algorithm relies on the destination node to recognize and accept the packet, and on the source node to stop sending the packet after a certain number of hops or a certain time.

The flooding algorithm is complete, as it guarantees that every packet will reach the destination node. However, the algorithm is not correct, as it does not find the optimal path to the destination node. The algorithm is robust, as it can cope with any changes in the network topology or traffic load. However, the algorithm is very inefficient, as it consumes a lot of bandwidth and creates a lot of redundancy and congestion in the network. The algorithm is not scalable, as it becomes unmanageable for large and complex networks.

## Distance Vector Algorithm
The distance vector algorithm is an adaptive algorithm that finds the best path to every destination in the network based on the distance or cost information from the neighboring routers. The algorithm uses a distributed view of the network, which means that every router only knows the cost of the links to its neighbors. The algorithm can be implemented using the Bellman-Ford algorithm or the RIP protocol.

The distance vector algorithm is complete and correct, as it eventually converges to the optimal path to every destination in



# Experiment 11.1 - Link State routing

- Link state routing is a type of routing algorithm that computes the shortest path between a source and a destination in a network.
- Link state routing requires each router to maintain a complete and consistent view of the network topology, called the link state database (LSDB).
- Link state routing uses a distributed algorithm called the link state update protocol to exchange link state information among routers and to keep the LSDBs synchronized.
- Link state routing uses a local algorithm called the shortest path first (SPF) algorithm to calculate the shortest path tree for each router based on the LSDB.
- Link state routing has several advantages over distance vector routing, such as faster convergence, loop-free routing, and support for hierarchical routing.
- Link state routing also has some disadvantages, such as higher memory and CPU requirements, more bandwidth consumption, and vulnerability to link state flooding attacks.



# Experiment 11.2 - Flooding

- Flooding is a natural phenomenon that occurs when a large amount of water overflows onto land that is normally dry.
- Flooding can be caused by various factors, such as heavy rainfall, snowmelt, storm surges, dam failures, or river overflow.
- Flooding can have positive and negative impacts on the environment, society, and economy.
- Positive impacts of flooding include:
  - Replenishing soil nutrients and groundwater resources.
  - Creating habitats for aquatic and wetland species.
  - Providing opportunities for recreation and tourism.
- Negative impacts of flooding include:
  - Damaging infrastructure, property, and crops.
  - Disrupting transportation, communication, and electricity services.
  - Causing injuries, deaths, and diseases among humans and animals.
  - Increasing the risk of soil erosion, landslides, and water pollution.
- To reduce the negative impacts of flooding, various measures can be taken, such as:
  - Building flood defenses, such as levees, dams, or barriers.
  - Implementing flood warning and evacuation systems.
  - Adopting flood insurance and compensation schemes.
  - Promoting flood awareness and preparedness among the public.
  - Restoring natural floodplains and wetlands.



# Experiment 11.3 - Distance vector routing algorithm

- Distance vector routing is a dynamic routing protocol that uses the Bellman-Ford algorithm or the shortest path algorithm to find the best routes between nodes in a network .
- Distance vector routing algorithm works by exchanging information about the distances and directions to the destination nodes with the neighboring nodes that have a direct link .
- Each node maintains a distance vector table that contains the distance and the next hop for each possible destination in the network .
- The distance vector table is updated periodically by sending and receiving the distance vectors from the neighboring nodes .
- The distance vector routing algorithm can handle changes in the network topology by propagating the updates to all the nodes in the network .
- The distance vector routing algorithm has some advantages and disadvantages, such as:
  - Advantages:
    - It is simple and easy to implement .
    - It does not require much computational power or memory .
    - It can adapt to different network sizes and topologies .
  - Disadvantages:
    - It can cause routing loops and count-to-infinity problems .
    - It can have slow convergence and high bandwidth consumption .
    - It can be vulnerable to malicious attacks and false information .



## Experiment 12 - To learn handling and configuration of networking hardware like RJ-45 connector, CAT-6 cable, crimping tool, etc

- The objective of this experiment is to learn how to handle and configure some common networking hardware devices, such as RJ-45 connector, CAT-6 cable, crimping tool, etc.
- The RJ-45 connector is a standard type of connector for Ethernet cables, which are used to connect computers and other devices to a network. The RJ-45 connector has eight pins that correspond to the eight wires in the cable.
- The CAT-6 cable is a type of twisted pair cable that can support data transmission speeds up to 10 Gbps. The CAT-6 cable has four pairs of wires, each with a different color code. The wires are twisted together to reduce interference and crosstalk.
- The crimping tool is a device that is used to attach the RJ-45 connector to the CAT-6 cable. The crimping tool has a blade that cuts the cable to the desired length, a stripper that removes the insulation from the wires, and a crimper that presses the pins of the connector into the wires.
- The steps to handle and configure the networking hardware are as follows:

  1. Cut the CAT-6 cable to the desired length using the blade of the crimping tool.
  2. Strip about 2 cm of the insulation from both ends of the cable using the stripper of the crimping tool.
  3. Untwist the wires and arrange them according to the color code of the RJ-45 connector. The standard color code is: orange-white, orange, green-white, blue, blue-white, green, brown-white, brown.
  4. Insert the wires into the RJ-45 connector, making sure that they are aligned with the pins and that they reach the end of the connector.
  5. Place the connector into the crimper of the crimping tool and squeeze the handle firmly to crimp the connector to the cable.
  6. Repeat the steps 1 to 5 for the other end of the cable.
  7. Test the cable by connecting it to two devices and checking the network connectivity.

- The expected outcome of this experiment is to have a functional Ethernet cable that can be used to connect two devices to a network.
- The possible sources of error or difficulty in this experiment are:

  - Cutting the cable too short or too long, which can affect the signal quality and the flexibility of the cable.
  - Stripping too much or too little insulation from the wires, which can expose the wires to damage or interference, or prevent them from reaching the end of the connector.
  - Mixing up the color code of the wires, which can result in a wrong or faulty connection.
  - Inserting the wires into the wrong pins of the connector, which can damage the connector or the cable.
  - Crimping the connector too loosely or too tightly, which can affect the contact between the pins and the wires, or damage the connector or the cable.
  - Using a defective or incompatible connector, cable, or crimping tool, which can cause malfunction or failure of the cable.



## Experiment 13 - Configuration of router, hub, switch etc. (using real devices or simulators)

- A router is a device that routes data packets based on their IP addresses. It can connect different networks, such as LANs and WANs, and perform functions such as assigning IP addresses, acting as a switch, and protecting the network .
- A hub is a device that connects multiple computers to create a LAN. It broadcasts all the data it receives to all the connected devices, regardless of the destination. It operates at the physical layer of the OSI model.
- A switch is a device that connects multiple computers to create a LAN. It forwards the data it receives to the specific device that matches the destination MAC address. It operates at the data link layer of the OSI model.
- To configure a router, you need to enter the router configuration mode, using the `configure terminal` command on Cisco devices, and then the interface configuration mode, using the `interface <interface name>` command. You can then set various parameters for the interface, such as IP address, subnet mask, speed, duplex mode, etc. You can also configure routing protocols, such as RIP, OSPF, EIGRP, etc., to enable the router to exchange routing information with other routers.
- To configure a switch, you need to enter the switch configuration mode, using the `configure terminal` command on Cisco devices, and then the interface configuration mode, using the `interface <interface name>` command. You can then set various parameters for the interface, such as speed, duplex mode, VLAN membership, port security, etc. You can also configure spanning tree protocol, trunking protocol, and inter-VLAN routing to optimize the performance and security of the switch.
- To configure a hub, you do not need to do anything, as it is a plug-and-play device that does not have any configurable settings.
- To practice the configuration of router and switch, you can use a simulator or an emulator. A simulator is a software that mimics the behavior of a device, but does not run the actual IOS. A simulator may have missing commands and programming errors, and it cannot fully replicate the real device. An emulator is a software that runs the actual IOS image of a device, and can provide a more realistic and complete experience. An example of a simulator is Packet Tracer, and an example of an emulator is GNS3.



## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

- The objective of this experiment is to learn how to use some common network services and commands that can help in troubleshooting, testing, and managing network connectivity and performance.
- The following are some of the services and commands that will be covered in this experiment:

  - **ping**: A command that sends packets of data to a specified destination and measures the round-trip time and packet loss rate. It can be used to test the reachability and latency of a host or a network.
  - **traceroute**: A command that traces the route of packets from the source to the destination and displays the IP addresses and hostnames of the intermediate routers and switches. It can be used to identify the network path and possible bottleneecs or failures along the way.
  - **nslookup**: A command that queries the Domain Name System (DNS) and resolves a hostname to an IP address or vice versa. It can be used to verify the DNS configuration and records of a domain or a host.
  - **arp**: A command that displays or manipulates the Address Resolution Protocol (ARP) cache, which maps IP addresses to MAC addresses on a local network. It can be used to view or modify the ARP entries or detect ARP spoofing attacks.
  - **telnet**: A service that allows remote login and access to a host using the Telnet protocol, which is a plain-text and unencrypted communication protocol. It can be used to test the connectivity and functionality of a service or a port on a host, but it is not secure and should be avoided for sensitive data transmission.
  - **ftp**: A service that allows file transfer between hosts using the File Transfer Protocol (FTP), which is a standard and widely used protocol for uploading and downloading files. It can be used to transfer files between hosts, but it is also not secure and should be replaced by more secure protocols such as SFTP or SCP.

- The following are some of the steps and procedures to run and use these services and commands:

  - To run the ping command, open a terminal or a command prompt and type `ping <destination>` where `<destination>` can be an IP address or a hostname of the target host or network. For example, `ping 8.8.8.8` or `ping www.google.com`. The command will send a series of packets and display the results for each packet, such as the size, the time, and the status. To stop the ping command, press Ctrl+C. Some of the options that can be used with the ping command are:

    - `-c <count>`: Specifies the number of packets to send. For example, `ping -c 5 8.8.8.8` will send 5 packets and then stop.
    - `-i <interval>`: Specifies the interval in seconds between each packet. For example, `ping -i 2 8.8.8.8` will send a packet every 2 seconds.
    - `-t <ttl>`: Specifies the Time to Live (TTL) value for the packets, which is the maximum number of hops that the packets can traverse before being discarded. For example, `ping -t 10 8.8.8.8` will send packets with a TTL of 10.
    - `-s <size>`: Specifies the size in bytes of the packets to send. For example, `ping -s 100 8.8.8.8` will send packets with a size of 100 bytes.

  - To run the traceroute command, open a terminal or a command prompt and type `traceroute <destination>` where `<destination>` can be an IP address or a hostname of the target host or network. For example, `traceroute 8.8.8.8` or `traceroute www.google.com`. The command will send a series of packets with increasing TTL values and display the results for each hop, such as the IP address, the hostname, and the time. Some of the options that can be used with the traceroute command are:

    - `-n`: Suppresses the hostname resolution and displays only the IP addresses of the hops. For example, `traceroute -n 8.8.8.8`.
    - `-I`: Uses ICMP packets instead of UDP packets for the traceroute. For example, `traceroute -I 8.8.8.8`.
    - `-T`: Uses TCP packets instead of UDP packets for the traceroute. For example, `traceroute -T 8.8.8.8`.
    - `-p <port>`: Specifies the destination



# Experiment 15 - Network packet analysis using tools like Wireshark, tcpdump, etc

## Objective
The objective of this experiment is to learn how to capture, analyze, and interpret network packets using various tools such as Wireshark, tcpdump, etc.

## Theory
- A network packet is a unit of data that is transmitted over a network. It consists of a header and a payload. The header contains information such as the source and destination addresses, the protocol type, the length, and the checksum. The payload contains the actual data being sent.
- Network packet analysis is the process of examining the network packets to understand the network traffic, troubleshoot problems, identify security threats, optimize performance, etc.
- Network packet analysis tools are software applications that can capture, filter, decode, and display network packets. Some of the common tools are:
  - Wireshark: A free and open-source graphical user interface (GUI) tool that supports many protocols and features. It can capture packets from live or offline sources, apply filters, display statistics, export data, etc. 
  - tcpdump: A command-line tool that can capture and print network packets. It can also save packets to a file for later analysis. It supports many filters and options. 
  - Colasoft Capsa: A commercial GUI tool that can capture and analyze network packets in real-time. It can also monitor and diagnose network issues, generate reports, etc. 
  - Paessler PRTG: A commercial network monitoring tool that can capture and analyze network packets. It can also classify network traffic, measure bandwidth, alert on issues, etc. 
  - Arkime: A free and open-source web-based tool that can capture and index network packets. It can also search, visualize, and export data, etc. 

## Procedure
The procedure for network packet analysis using tools like Wireshark, tcpdump, etc. may vary depending on the tool, the platform, the network interface, the capture filter, the display filter, the analysis task, etc. However, a general procedure can be outlined as follows:

1. Install and launch the network packet analysis tool of your choice on your system.
2. Select the network interface from which you want to capture packets. You may need to configure the interface settings, such as the promiscuous mode, the snap length, the buffer size, etc.
3. Optionally, apply a capture filter to limit the packets that are captured based on certain criteria, such as the protocol, the port, the address, etc. For example, `tcp port 80` will capture only TCP packets with port 80 as the source or destination.
4. Start the packet capture and observe the packets that are displayed on the tool. You may need to stop the capture manually or set a capture duration or size limit.
5. Optionally, apply a display filter to limit the packets that are displayed based on certain criteria, such as the protocol, the field, the value, etc. For example, `http.request.method == "GET"` will display only HTTP packets with the GET method.
6. Select a packet that you want to analyze and view its details. You may need to expand the packet header and payload sections, decode the packet data, follow the packet stream, etc.
7. Repeat steps 5 and 6 for other packets that you want to analyze.
8. Optionally, save the captured packets to a file for later analysis or export the packet data to another format, such as CSV, XML, JSON, etc.
9. Optionally, generate statistics, graphs, reports, etc. based on the captured packets or the analysis results.



# Experiment 16 - Network simulation using tools like Cisco Packet Tracer, NetSim, OMNeT++, NS2, NS3, etc

## Introduction

- Network simulation is the process of modeling the behavior and performance of a network using software tools.
- Network simulation tools can help students, researchers, and professionals to design, test, and troubleshoot networks without using physical hardware.
- Network simulation tools can support various types of networks, such as wired, wireless, mobile, ad hoc, sensor, software-defined, etc.
- Network simulation tools can also provide graphical user interfaces, visualization, animation, debugging, and analysis features.

## Objectives

- To learn the basic concepts and features of network simulation tools.
- To compare and contrast different network simulation tools based on their characteristics and capabilities.
- To use network simulation tools to create and configure network topologies, protocols, and scenarios.
- To use network simulation tools to measure and evaluate network performance metrics, such as throughput, delay, packet loss, etc.
- To use network simulation tools to analyze and troubleshoot network problems and issues.

## Network simulation tools

- There are many network simulation tools available, both open source and commercial, that have different advantages and disadvantages.
- Some of the most popular and widely used network simulation tools are:

  - Cisco Packet Tracer: A network simulation and visualization tool developed by Cisco Systems for teaching and learning networking concepts and skills. It supports Cisco devices and protocols, as well as basic IoT and cybersecurity features. It is available for free for Cisco Networking Academy students and instructors. 
  - NetSim: A network simulation and emulation tool developed by Tetcos for academic and research purposes. It supports a wide range of network technologies, such as wireless, mobile, ad hoc, sensor, cognitive, satellite, etc. It also supports network design, testing, and optimization features. It is a commercial tool that offers a free trial version. 
  - OMNeT++: A network simulation framework based on C++ and discrete event simulation. It is an open source and modular tool that can be extended with various libraries and models for different network domains, such as software-defined networks, all types of wireless networks, etc. It also provides graphical user interfaces, visualization, and analysis tools.  
  - NS2: A network simulator based on Tcl and C++ that supports discrete event simulation. It is an open source and widely used tool for network research and education. It supports various network protocols and models, such as mobile ad hoc networks, sensor networks, etc. It also provides graphical user interfaces, visualization, and analysis tools.  
  - NS3: A network simulator based on C++ and Python that supports discrete event simulation. It is an open source and successor of NS2 that aims to provide more realistic and accurate network simulation. It supports various network protocols and models, such as software-defined networks, hybrid networks, etc. It also provides graphical user interfaces, visualization, and analysis tools.  

## Procedure

- The procedure for using network simulation tools may vary depending on the specific tool and the network scenario. However, some common steps are:

  - Select and install the network simulation tool of your choice on your computer or server.
  - Create and configure the network topology, devices, and parameters using the graphical user interface or the scripting language of the tool.
  - Define and implement the network protocols, algorithms, and applications using the programming language or the library of the tool.
  - Run the network simulation and observe the network behavior and performance using the visualization, animation, and debugging features of the tool.
  - Collect and analyze the network data and statistics using the output files, graphs, and tables of the tool.
  - Evaluate and compare the network performance metrics, such as throughput, delay, packet loss, etc., using the analysis tools of the tool.
  - Identify and troubleshoot the network problems and issues using the error messages, logs, and traces of the tool.

## Conclusion

- Network simulation is a useful and powerful technique for learning and experimenting with network concepts and technologies.
- Network simulation tools can help network students, researchers, and professionals to design, test, and troubleshoot networks without using physical hardware.
- Network simulation tools can support various types of networks, protocols, and scenarios, and provide various features and capabilities for network simulation and analysis.
- Network simulation tools can also help network students, researchers, and professionals to measure and evaluate network performance metrics, such as throughput, delay, packet loss, etc



# Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

## Introduction

- Socket programming is a way of connecting two nodes on a network to communicate with each other.
- A socket is an endpoint of a communication channel that can send and receive data using a specific protocol.
- There are three types of sockets: stream sockets, datagram sockets and raw sockets.
- Stream sockets use TCP (Transmission Control Protocol) as the transport layer protocol, which provides reliable, ordered and error-free data delivery .
- Datagram sockets use UDP (User Datagram Protocol) as the transport layer protocol, which provides fast, connectionless and unreliable data delivery .
- Raw sockets can use any protocol at the network layer or lower, and allow direct access to the network interface.
- In this experiment, we will learn how to program sockets using UDP and TCP in Python, and implement some simple applications such as DNS, data & time client/server, echo client/server, and iterative & concurrent servers.

## UDP Socket Programming

- UDP sockets are created using the socket.SOCK_DGRAM parameter in the socket.socket() function.
- UDP sockets do not need to establish a connection before sending or receiving data, so they do not use the listen(), accept() or connect() methods that TCP sockets use.
- UDP sockets can send and receive data using the sendto() and recvfrom() methods, which take the data and the destination address as arguments.
- UDP sockets can also use the bind() method to associate a socket with a specific address and port, and the close() method to close the socket.
- UDP sockets are suitable for applications that require low latency, high throughput and multicast or broadcast capabilities, but do not care much about reliability, ordering or error correction.
- An example of UDP socket programming in Python is given below:

```python
# UDP client
import socket
# create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# send a message to the server
message = b"Hello, server!"
server_address = ("127.0.0.1", 5000) # server IP and port
client_socket.sendto(message, server_address)
# receive a response from the server
response, address = client_socket.recvfrom(1024) # buffer size
print("Received from server:", response.decode())
# close the socket
client_socket.close()
```

```python
# UDP server
import socket
# create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# bind the socket to a specific address and port
server_address = ("127.0.0.1", 5000) # server IP and port
server_socket.bind(server_address)
# receive a message from a client
message, address = server_socket.recvfrom(1024) # buffer size
print("Received from client:", message.decode())
# send a response to the client
response = b"Hello, client!"
server_socket.sendto(response, address)
# close the socket
server_socket.close()
```

## TCP Socket Programming

- TCP sockets are created using the socket.SOCK_STREAM parameter in the socket.socket() function.
- TCP sockets need to establish a connection before sending or receiving data, so they use the listen(), accept() and connect() methods that UDP sockets do not use .
- TCP sockets can send and receive data using the send() and recv() methods, which take the data and the buffer size as arguments.
- TCP sockets can also use the bind() method to associate a socket with a specific address and port, the close() method to close the socket, and the gethostname() method to get the host name of the machine.
- TCP sockets are suitable for applications that require high reliability, ordering and error correction, but do not care much about latency, throughput or multicast or broadcast capabilities.
- An example of TCP socket programming in Python is given below:

```python
# TCP client
import socket
# create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the server
server_address = ("127.0.0.1", 5000) # server IP and port
client_socket.connect(server_address)
# send a message to the server
message = b

```


