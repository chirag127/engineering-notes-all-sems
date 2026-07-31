

## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

### Stop and Wait Protocol
- Stop and Wait Protocol is a flow control protocol.
- It is used in data communication to prevent the sender from overwhelming the receiver with data.
- In this protocol, the sender sends a single data frame and waits for an acknowledgment from the receiver before sending the next frame.
- If the acknowledgment is not received within a specified time, the sender retransmits the frame.
- This protocol is simple to implement but has low efficiency due to the time spent waiting for acknowledgments.

### Sliding Window Protocol
- Sliding Window Protocol is another flow control protocol.
- It is an improvement over the Stop and Wait Protocol as it allows the sender to transmit multiple frames before waiting for an acknowledgment.
- The sender maintains a window of frames that can be sent without waiting for an acknowledgment.
- The receiver also maintains a window of frames that it can receive.
- As the receiver acknowledges the receipt of frames, the sender's window slides forward, allowing the transmission of more frames.
- This protocol is more efficient than the Stop and Wait Protocol as it reduces the time spent waiting for acknowledgments.



### Experiment 1.1 - Implementation of Stop and Wait Protocol

Stop and Wait Protocol is a flow control protocol that is used in data communication. It is a simple protocol that is used to ensure that the sender does not overwhelm the receiver with data. The sender sends a single data packet and then waits for an acknowledgment from the receiver before sending the next packet. This protocol is used in situations where the transmission time is much larger than the propagation delay.

The steps involved in the implementation of the Stop and Wait Protocol are as follows:

1. The sender sends a data packet to the receiver.
2. The sender starts a timer and waits for an acknowledgment from the receiver.
3. If the acknowledgment is received before the timer expires, the sender sends the next data packet.
4. If the acknowledgment is not received before the timer expires, the sender retransmits the data packet.
5. The process is repeated until all the data packets have been transmitted.

This protocol is simple to implement but has some drawbacks. The main drawback is that the sender has to wait for an acknowledgment before sending the next packet, which can result in low throughput. Additionally, if the acknowledgment is lost, the sender will retransmit the data packet, which can result in duplicate packets being received by the receiver.

Overall, the Stop and Wait Protocol is a simple and effective flow control protocol that is used in data communication. However, it may not be the most efficient protocol in all situations.



### Experiment 1.2 - Implementation of Sliding Window Protocol

The Sliding Window Protocol is a method used in computer networks to manage the flow of data between two devices. It is used to ensure that data is transmitted reliably and efficiently, without overwhelming the receiver or causing congestion in the network.

Here are the key points to remember when implementing the Sliding Window Protocol:

1. The sender maintains a window of data packets that it is allowed to send at any given time. The size of the window is determined by the receiver, based on its current capacity to process incoming data.

2. The receiver acknowledges the receipt of each packet by sending an acknowledgement (ACK) message back to the sender. The sender uses these ACK messages to update its window and determine which packets have been successfully received.

3. If a packet is lost or corrupted during transmission, the receiver will not send an ACK for that packet. The sender will eventually retransmit the lost packet, based on a timeout mechanism or the receipt of duplicate ACKs for other packets.

4. The sender may also use a technique called selective repeat, where it retransmits only the lost or corrupted packets, rather than retransmitting the entire window of data.

5. The Sliding Window Protocol can be implemented using either a go-back-N or a selective repeat mechanism. In a go-back-N implementation, the sender retransmits all packets in the window after a lost or corrupted packet is detected. In a selective repeat implementation, the sender retransmits only the lost or corrupted packets.

6. The Sliding Window Protocol is widely used in computer networks, including in the Transmission Control Protocol (TCP), which is the primary protocol used for transmitting data over the Internet. It is an effective way to manage the flow of data and ensure reliable transmission, even in the presence of network congestion or packet loss.



## Experiment 2 - Study of Socket Programming and Client – Server model

1. **Socket Programming** refers to the process of creating a network communication endpoint using the Berkeley sockets API.
2. A **socket** is an endpoint for sending or receiving data across a computer network.
3. Socket programming is used to facilitate communication between different processes on the same or different machines.
4. The **Client-Server model** is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.
5. In the Client-Server model, the client sends a request to the server, which processes the request and returns a response.
6. The server listens for incoming connections and handles them accordingly, while the client initiates a connection to the server.
7. Socket programming and the Client-Server model are commonly used in the development of web applications, email systems, and other network-based services.



### Experiment 2.1 - Study of Socket Programming

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.

Here are some key points to remember when studying socket programming:

1. Sockets are the endpoints of a bidirectional communications channel.
2. Sockets may communicate within a process, between processes on the same machine, or between processes on different machines.
3. Socket programming is the core API for interprocess communication.
4. Socket programming can be used to implement client-server architecture.
5. The two most common types of sockets are stream sockets and datagram sockets.
6. Stream sockets use TCP (Transmission Control Protocol) for data transmission.
7. Datagram sockets use UDP (User Datagram Protocol) for data transmission.
8. Socket programming can be implemented in various programming languages, including C, C++, Python, and Java.




### Experiment 2.2 - Study of Client – Server model

The client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients. Here are some key points to understand about the client-server model:

1. The server is a computer program or a device that provides a service to another computer program and its user, also known as the client.
2. The client is a computer program that requests a service from the server.
3. The client and server communicate with each other through a computer network.
4. The client sends a request to the server, and the server responds with the requested information or service.
5. The server can serve multiple clients simultaneously.
6. The client-server model is used in many applications, including email, file sharing, and web browsing.

This model is useful for understanding how different components of a distributed system interact with each other. It is also useful for designing and implementing distributed systems. In this experiment, we will study the client-server model and its applications.



## Experiment 3 - Write a code simulating ARP /RARP protocols

ARP (Address Resolution Protocol) and RARP (Reverse Address Resolution Protocol) are two important protocols used in computer networks. ARP is used to map a network address (such as an IP address) to a physical address (such as a MAC address), while RARP is used to map a physical address to a network address.

Here are the steps to write a code simulating ARP/RARP protocols:

1. Define the data structures for the ARP and RARP packets.
2. Create a function to generate ARP request packets.
3. Create a function to generate RARP request packets.
4. Create a function to process ARP request packets and generate ARP reply packets.
5. Create a function to process RARP request packets and generate RARP reply packets.
6. Create a function to send and receive packets over the network.
7. Create a function to update the ARP and RARP cache tables.
8. Create a main function to simulate the ARP and RARP protocols by sending and receiving packets and updating the cache tables.

This is a high-level overview of the steps involved in writing a code to simulate ARP/RARP protocols. Each step can be further broken down into smaller sub-steps and implemented using the programming language of your choice. It is important to test the code thoroughly to ensure that it correctly simulates the behavior of the ARP and RARP protocols.



## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

1. **PING** is a computer network administration software utility used to test the reachability of a host on an Internet Protocol (IP) network. It measures the round-trip time for messages sent from the originating host to a destination computer that are echoed back to the source.

2. **TRACEROUTE** is a computer network diagnostic tool for displaying the route (path) and measuring transit delays of packets across an Internet Protocol (IP) network.

3. To simulate the PING command, you can write a program that sends an Internet Control Message Protocol (ICMP) echo request to a specified host and waits for a response. The program can measure the time it takes for the response to arrive and display it to the user.

4. To simulate the TRACEROUTE command, you can write a program that sends a series of ICMP echo requests with increasing Time to Live (TTL) values. The program can record the IP addresses of the routers that respond with ICMP Time Exceeded messages and display the route to the user.

5. Here is an example of a Python program that simulates the PING command:

```python
import os
hostname = "google.com"
response = os.system("ping -c 1 " + hostname)
if response == 0:
    print(hostname + ' is up!')
else:
    print(hostname + ' is down!')
```

6. Here is an example of a Python program that simulates the TRACEROUTE command:

```python
import os
hostname = "google.com"
for i in range(1, 30):
    response = os.system("traceroute -m " + str(i) + " " + hostname)
    if response == 0:
        break
```

7. These programs can be modified and expanded to include additional features and functionality, such as displaying the round-trip time for each hop in the route or allowing the user to specify the maximum number of hops to trace.



## Experiment 5 - Create a socket for HTTP for web page upload and download

1. **Objective:** The objective of this experiment is to create a socket for HTTP to enable the upload and download of web pages.

2. **Background:** HTTP (Hypertext Transfer Protocol) is the protocol used for transmitting web pages over the internet. A socket is an endpoint for sending or receiving data across a computer network.

3. **Procedure:**
    1. Create a socket using the `socket()` function.
    2. Connect the socket to a server using the `connect()` function.
    3. Send an HTTP request to the server using the `send()` function.
    4. Receive the server's response using the `recv()` function.
    5. Close the socket using the `close()` function.

4. **Expected Outcome:** After completing this experiment, you should be able to create a socket for HTTP and use it to upload and download web pages.

5. **Further Reading:** For more information on sockets and HTTP, you can refer to the following resources:
    - [Python Socket Programming](https://docs.python.org/3/library/socket.html)
    - [HTTP Made Really Easy](https://www.jmarshall.com/easy/http/)



## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

Remote Procedure Call (RPC) is a protocol that allows a program to request a service from a program located on another computer in a network without having to understand the network's details. RPC is used to call other processes on the remote systems like a local system.

Here are the steps to implement RPC:

1. Define the remote procedure and the data structures required to pass the arguments.
2. Generate the client and server stubs using the RPC compiler.
3. Write the client program that calls the remote procedure.
4. Write the server program that implements the remote procedure.
5. Compile the client and server programs and link them with the respective stubs.
6. Start the RPC server.
7. Run the client program to call the remote procedure on the server.

This is a basic overview of how to implement RPC. It is important to note that the specific details and implementation may vary depending on the programming language and platform being used. It is recommended to consult the documentation and resources specific to your environment for more detailed information.



## Experiment 7 - Implementation of Subnetting

Subnetting is the process of dividing a network into smaller, more manageable subnetworks, or subnets. This can be useful for a variety of reasons, including improving network performance, simplifying network administration, and enhancing network security.

Here are the steps to implement subnetting:

1. Determine the number of subnets required: The first step in subnetting is to determine how many subnets are needed. This will depend on the size and structure of the network.

2. Determine the subnet mask: The subnet mask is used to determine which part of an IP address represents the network and which part represents the host. The subnet mask is determined based on the number of subnets required.

3. Assign IP addresses: Once the subnet mask has been determined, IP addresses can be assigned to the devices on the network. Each device on a subnet must have a unique IP address.

4. Configure routing: Routing must be configured to ensure that traffic can flow between the different subnets. This may involve configuring routing protocols or static routes.

5. Test and verify: Finally, it is important to test and verify that the subnetting has been implemented correctly. This can be done by pinging devices on different subnets to ensure that they can communicate with each other.

Subnetting can be a complex process, but it is an essential skill for network administrators. By following these steps, you can successfully implement subnetting on your network.



## Experiment 8 - Applications using TCP Sockets
TCP (Transmission Control Protocol) is one of the main protocols in the Internet protocol suite. It is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of data between applications running on different devices.

Some common applications that use TCP sockets include:
1. **Web Browsers:** Web browsers use TCP sockets to communicate with web servers and retrieve web pages and other resources.
2. **Email Clients:** Email clients use TCP sockets to communicate with email servers and send and receive emails.
3. **File Transfer:** File transfer applications such as FTP (File Transfer Protocol) use TCP sockets to transfer files between devices.
4. **Instant Messaging:** Instant messaging applications use TCP sockets to send and receive messages in real-time.
5. **Online Gaming:** Many online games use TCP sockets to communicate game data between players and game servers.

TCP sockets provide a reliable and efficient way for applications to communicate over the Internet. They are widely used in many different types of applications and are an essential part of the Internet's infrastructure.



### Experiment 8.1 - Echo client and echo server

1. **Objective:** The objective of this experiment is to understand the basic concepts of client-server communication using the echo protocol.
2. **Introduction:** The echo protocol is a simple communication protocol that sends data from a client to a server, and the server sends the same data back to the client. This is useful for testing the communication between the client and the server.
3. **Procedure:**
    1. **Setting up the server:** The first step is to set up the echo server. This can be done using a programming language such as Python or Java. The server listens on a specific port for incoming connections from clients.
    2. **Setting up the client:** The next step is to set up the echo client. This can also be done using a programming language such as Python or Java. The client connects to the server using the server's IP address and port number.
    3. **Sending data:** Once the client is connected to the server, it can send data to the server. The server receives the data and sends it back to the client.
    4. **Receiving data:** The client receives the data sent back by the server and can display it to the user.
4. **Conclusion:** This experiment demonstrates the basic concepts of client-server communication using the echo protocol. It shows how data can be sent from a client to a server and back to the client.



### Experiment 8.2 - Chat

1. Chat is a form of communication that allows two or more people to exchange messages in real-time.
2. Chat can take place through various mediums, including text, voice, and video.
3. Chat can be used for personal, social, or business purposes.
4. Chat can be facilitated through various platforms, including social media, messaging apps, and chat rooms.
5. Chat can be synchronous, where all participants are present at the same time, or asynchronous, where messages are sent and received at different times.
6. Chat can be public, where anyone can join, or private, where only invited participants can join.
7. Chat can be moderated, where a designated person or group of people oversee the conversation and enforce rules, or unmoderated, where there are no rules or oversight.
8. Chat can be used for various purposes, including socializing, networking, collaborating, and problem-solving.
9. Chat can have various benefits, including increased social connection, improved communication, and enhanced productivity.
10. Chat can also have various challenges, including misunderstandings, distractions, and privacy concerns. It is important to use chat responsibly and respectfully.



### Experiment 8.3 - File Transfer

File transfer refers to the process of transmitting files over a computer network from one device to another. There are several methods and protocols used for file transfer, including:

1. **File Transfer Protocol (FTP):** A standard network protocol used to transfer files from one host to another over a TCP-based network, such as the Internet.
2. **Secure File Transfer Protocol (SFTP):** A secure version of FTP that uses SSH to encrypt data during transfer.
3. **Trivial File Transfer Protocol (TFTP):** A simple, lockstep, file transfer protocol which allows a client to get a file from or put a file onto a remote host.
4. **Hypertext Transfer Protocol (HTTP):** A protocol used for transferring files, such as text, graphic images, sound, video, and other multimedia files, on the World Wide Web.
5. **Email:** Files can also be transferred as attachments to email messages.

Each method has its own advantages and disadvantages, and the choice of method depends on factors such as the size of the file, the level of security required, and the network infrastructure. It is important to understand the different methods and protocols in order to choose the most appropriate one for a given file transfer task.



## Experiment 9 - Applications using TCP and UDP Sockets

TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two of the core protocols in the Internet Protocol Suite. Both protocols are used to send data over the internet, but they have different characteristics and use cases.

1. **TCP** is a connection-oriented protocol, which means that it establishes a connection between the sender and receiver before transmitting data. This connection ensures that data is transmitted reliably and in the correct order. TCP is used by applications that require reliable data transmission, such as web browsing, email, and file transfers.

2. **UDP** is a connectionless protocol, which means that it does not establish a connection before transmitting data. Instead, it sends data in individual packets, called datagrams, without checking if they are received correctly or in the correct order. UDP is used by applications that require fast data transmission and can tolerate some data loss, such as online gaming, video streaming, and voice over IP (VoIP).

Some common applications that use TCP and UDP sockets include:

- **Web browsing:** Web browsers use TCP to establish a connection to a web server and request web pages.

- **Email:** Email clients use TCP to send and receive emails from an email server.

- **File transfers:** File transfer protocols such as FTP and SFTP use TCP to reliably transfer files between computers.

- **Online gaming:** Online games often use UDP to send fast, real-time updates between players.

- **Video streaming:** Video streaming services such as YouTube and Netflix use UDP to quickly transmit video data.

- **Voice over IP (VoIP):** VoIP applications such as Skype and WhatsApp use UDP to transmit voice data in real-time.

In summary, TCP and UDP are two core protocols in the Internet Protocol Suite, used by various applications to transmit data over the internet. TCP is used by applications that require reliable data transmission, while UDP is used by applications that require fast data transmission and can tolerate some data loss. Some common applications that use TCP and UDP sockets include web browsing, email, file transfers, online gaming, video streaming, and VoIP.



### Experiment 9.1 - DNS

1. **Objective:** To understand the Domain Name System (DNS) and its role in the internet infrastructure.
2. **Background:** DNS is a hierarchical and decentralized naming system for computers, services, or other resources connected to the internet or a private network. It associates various information with domain names assigned to each of the participating entities.
3. **Procedure:** 
    - Open a command prompt or terminal window.
    - Use the `nslookup` command to query the DNS server for the IP address of a domain name. For example, `nslookup www.example.com`.
    - Observe the response from the DNS server, which should include the IP address of the domain name.
4. **Observations:** Record the response from the DNS server, including the IP address of the domain name.
5. **Conclusion:** DNS plays a crucial role in the internet infrastructure by translating human-readable domain names into IP addresses that can be understood by computers and network devices.



### Experiment 9.2 - SNMP

SNMP stands for Simple Network Management Protocol. It is a standard protocol used for managing devices on IP networks. Some of the key features of SNMP are:

1. It is used to monitor network-attached devices for conditions that require administrative attention.
2. SNMP provides a standardized framework and a common language used for the monitoring and management of devices in a network.
3. SNMP uses a client-server architecture where the client is the Network Management System (NMS) and the server is the managed device.
4. SNMP uses a hierarchical namespace called the Management Information Base (MIB) to organize and represent the information of the managed devices.
5. SNMP has three versions: SNMPv1, SNMPv2c, and SNMPv3. SNMPv3 is the most secure version as it provides authentication and encryption.




### Experiment 9.3 - File Transfer

File transfer refers to the process of transmitting files over a computer network from one device to another. There are several methods and protocols used for file transfer, including:

1. **File Transfer Protocol (FTP):** A standard network protocol used to transfer files from one host to another over a TCP-based network, such as the Internet.

2. **Secure File Transfer Protocol (SFTP):** A secure version of FTP that uses SSH to encrypt data during transmission.

3. **Trivial File Transfer Protocol (TFTP):** A simple, lock-step, file transfer protocol that allows a client to get or put a file onto a remote host.

4. **Hypertext Transfer Protocol (HTTP):** A protocol used for transferring files over the World Wide Web.

5. **Email:** Files can be attached to an email and sent to the recipient for download.

Each method has its own advantages and disadvantages, and the choice of method depends on factors such as the size of the file, the level of security required, and the network infrastructure. It is important to choose the appropriate method for the specific file transfer needs.



## Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

1. **Introduction:** Network Simulator (NS) is a discrete event simulator targeted at networking research. It provides substantial support for simulation of TCP, routing, and multicast protocols over wired and wireless (local and satellite) networks.

2. **Objective:** The objective of this experiment is to study the NS and simulate congestion control algorithms using NS.

3. **Procedure:**
    - Install NS on your system.
    - Create a simple network topology using NS.
    - Simulate the network and observe the behavior of different congestion control algorithms.
    - Analyze the results and compare the performance of different algorithms.

4. **Conclusion:** By performing this experiment, you will gain an understanding of how NS can be used to simulate and study the behavior of different congestion control algorithms in a network. You will also learn how to analyze and compare the performance of different algorithms.



## Experiment 11 - Perform a case study about the different routing algorithms to select the network path with its optimum and economical during data transfer

Routing algorithms are used to determine the best path for data transfer in a network. There are several different algorithms that can be used, each with its own advantages and disadvantages. In this case study, we will examine some of the most commonly used routing algorithms and evaluate their effectiveness in selecting the optimum and economical network path during data transfer.

1. **Shortest Path First (SPF)**: This algorithm calculates the shortest path between two nodes in a network. It is commonly used in link-state routing protocols such as OSPF and IS-IS.

2. **Distance Vector**: This algorithm calculates the best path based on the distance between nodes. It is commonly used in distance-vector routing protocols such as RIP and IGRP.

3. **Bellman-Ford**: This algorithm calculates the best path based on the cost of each link. It is commonly used in distance-vector routing protocols such as RIP and IGRP.

4. **Dijkstra's Algorithm**: This algorithm calculates the shortest path between two nodes in a network. It is commonly used in link-state routing protocols such as OSPF and IS-IS.

Each of these algorithms has its own strengths and weaknesses. For example, SPF and Dijkstra's algorithms are effective at finding the shortest path, but they can be computationally intensive. Distance Vector and Bellman-Ford algorithms are less computationally intensive, but they may not always find the shortest path.

In conclusion, the choice of routing algorithm depends on the specific requirements of the network. Factors such as network size, topology, and traffic patterns should be considered when selecting the most appropriate algorithm for a given network. It is important to regularly evaluate the effectiveness of the chosen algorithm and make adjustments as necessary to ensure optimum and economical data transfer.



### Experiment 11.1 - Link State routing

Link State routing is a type of routing protocol used in computer networks. It is based on the concept of each router in the network maintaining a map of the entire network topology. This map is used to calculate the shortest path to each destination in the network.

The steps involved in Link State routing are as follows:

1. Each router in the network sends a "hello" message to its directly connected neighbors to discover their presence.
2. Each router then sends a Link State Packet (LSP) to all other routers in the network, containing information about its directly connected neighbors and the cost of reaching them.
3. Each router receives the LSPs from all other routers and uses this information to construct a complete map of the network topology.
4. Each router then uses a shortest path algorithm, such as Dijkstra's algorithm, to calculate the shortest path to each destination in the network.
5. The router updates its routing table with the calculated shortest paths and uses this information to forward packets to their destination.

Link State routing protocols are commonly used in large networks due to their ability to quickly adapt to changes in the network topology. Some examples of Link State routing protocols include OSPF and IS-IS.



### Experiment 11.2 - Flooding

Flooding is a computer networking technique used to transmit information to all nodes in a network. It is a simple and effective method of disseminating information, but it can also lead to network congestion and inefficiency.

In this experiment, we will explore the concept of flooding and its effects on a network. The following points will be covered:

1. Definition and explanation of flooding.
2. Advantages and disadvantages of flooding.
3. Examples of flooding in real-world scenarios.
4. Techniques to mitigate the negative effects of flooding.

By the end of this experiment, you should have a clear understanding of the concept of flooding and its implications in computer networking. This knowledge will be useful in designing and managing efficient and effective networks.



### Experiment 11.3 - Distance vector

Distance vector routing is a routing protocol used in computer networks to determine the best path for data packets to travel from one node to another. It is based on the Bellman-Ford algorithm and calculates the shortest path between nodes by exchanging information about the distances between them.

Some key points to remember about distance vector routing are:

1. Distance vector routing protocols use the Bellman-Ford algorithm to calculate the shortest path between nodes.
2. Each router maintains a routing table that contains information about the distances to other nodes in the network.
3. Routers exchange information about the distances to other nodes with their neighboring routers.
4. The routing table is updated based on the information received from neighboring routers.
5. Distance vector routing protocols are simple to implement and are suitable for small networks.
6. However, they do not scale well to large networks and can suffer from the "count to infinity" problem.

In summary, distance vector routing is a simple and effective routing protocol for small networks, but may not be suitable for larger networks due to scalability issues. It is important to understand the principles of distance vector routing when studying computer networks.



## Experiment 12 - To learn handling and configuration of networking hardware like RJ-45 connector, CAT-6 cable, crimping tool, etc

1. **RJ-45 connector**: This is a type of connector commonly used for Ethernet networking. It is an 8-position, 8-contact (8P8C) modular plug and jack, which is commonly used to connect computers to a local area network (LAN).
2. **CAT-6 cable**: This is a type of twisted pair cable used for Ethernet and other networking standards. It is designed to support data transfer rates of up to 10 Gbps (gigabits per second) and is backward compatible with CAT-5 and CAT-5e cables.
3. **Crimping tool**: This is a tool used to attach connectors to cables. It is used to crimp, or compress, the metal contacts of the connector onto the individual wires of the cable, creating a secure connection.
4. To configure these networking hardware, first, strip the outer insulation of the CAT-6 cable to expose the individual wires. Then, untwist the wires and arrange them in the correct order according to the wiring standard being used (T568A or T568B). Next, insert the wires into the RJ-45 connector, making sure that each wire is fully inserted into its corresponding pin. Finally, use the crimping tool to crimp the connector onto the cable, securing the wires in place.




## Experiment 13 - Configuration of router, hub, switch etc. (using real devices or simulators)

1. **Objective**: The objective of this experiment is to learn how to configure a router, hub, switch, and other networking devices using real devices or simulators.

2. **Equipment**: For this experiment, you will need a router, hub, switch, and other networking devices. If you do not have access to real devices, you can use a network simulator such as Cisco Packet Tracer or GNS3.

3. **Procedure**:
    - Connect the devices according to the network topology you want to create.
    - Configure the router by accessing its command line interface (CLI) and entering the necessary commands.
    - Configure the switch by accessing its CLI and entering the necessary commands.
    - Configure the hub by accessing its CLI and entering the necessary commands.
    - Test the network by sending packets between devices and verifying that they are correctly forwarded.

4. **Observations**: Record your observations during the experiment, such as the commands you entered and the output you received.

5. **Conclusion**: Summarize your findings and what you learned from the experiment.



## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

1. **Ping**: Ping is a command used to test the reachability of a host on an IP network. It measures the round-trip time for messages sent from the originating host to a destination computer that are echoed back to the source.

2. **Traceroute**: Traceroute is a command used to display the route and measure transit delays of packets across an IP network. It shows the path that a packet takes from the source to the destination.

3. **Nslookup**: Nslookup is a command used to query the Domain Name System (DNS) to obtain domain name or IP address mapping or for any other specific DNS record.

4. **Arp**: Arp is a command used to view and manipulate the Address Resolution Protocol (ARP) cache. The ARP cache is used to store mappings between IP addresses and MAC addresses.

5. **Telnet**: Telnet is a command used to connect to a remote computer over a network using the Telnet protocol. It is used for remote command line access to a computer.

6. **Ftp**: Ftp is a command used to transfer files between computers on a network using the File Transfer Protocol (FTP). It is used to upload and download files from a remote computer.

These are some of the commonly used services and commands in networking. They are used for various purposes such as testing connectivity, transferring files, and querying DNS records. It is important to have a basic understanding of these commands when working with networks.



## Experiment 15 - Network packet analysis using tools like Wireshark, tcpdump, etc

1. **Introduction:** Network packet analysis involves capturing and analyzing the packets of data that are transmitted over a network. This can be useful for troubleshooting network issues, monitoring network traffic, and detecting security threats.

2. **Tools:** There are several tools available for network packet analysis, including Wireshark, tcpdump, and others. These tools allow users to capture and analyze packets in real-time, providing detailed information about the data being transmitted over the network.

3. **Wireshark:** Wireshark is a popular, open-source network protocol analyzer. It allows users to capture and interactively browse the traffic running on a computer network. Wireshark has a user-friendly interface and provides detailed information about network protocols, allowing users to easily analyze network traffic.

4. **tcpdump:** tcpdump is a command-line tool for capturing and analyzing network traffic. It is available on many operating systems, including Linux, macOS, and Windows. tcpdump provides a wide range of options for capturing and filtering network traffic, making it a powerful tool for network analysis.

5. **Usage:** Network packet analysis tools can be used for a variety of purposes, including troubleshooting network issues, monitoring network traffic, and detecting security threats. By capturing and analyzing network traffic, users can gain insight into the data being transmitted over the network and identify potential issues or threats.

6. **Conclusion:** Network packet analysis is an important tool for network administrators and security professionals. Tools like Wireshark and tcpdump provide detailed information about network traffic, allowing users to monitor, troubleshoot, and secure their networks.



## Experiment 16 - Network simulation using tools like Cisco Packet Tracer, NetSim, OMNeT++, NS2, NS3, etc

- Network simulation is the technique of modeling the behavior of a network by calculating the interaction between the different network entities using mathematical formulas.
- Network simulation tools are software applications that allow network administrators and researchers to study the behavior of a network under different conditions.
- Some popular network simulation tools include Cisco Packet Tracer, NetSim, OMNeT++, NS2, and NS3.
- Cisco Packet Tracer is a network simulation tool developed by Cisco Systems that allows users to create network topologies and simulate the behavior of Cisco devices.
- NetSim is a network simulation tool developed by Tetcos that supports a wide range of protocols and technologies, including routing, switching, and wireless.
- OMNeT++ is a modular, component-based C++ simulation library and framework primarily used for building network simulators.
- NS2 and NS3 are open-source network simulation tools that support a wide range of network protocols and technologies.
- These tools allow users to design and test network topologies, protocols, and configurations before deploying them in a real-world environment.
- Network simulation tools are widely used in research and education to study the behavior of networks and to develop new networking technologies.



## Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.

There are two widely used socket types, stream sockets, and datagram sockets. Stream sockets use TCP (Transmission Control Protocol), which is a reliable, stream-oriented protocol, and datagram sockets use UDP (User Datagram Protocol), which is unreliable and message-oriented.

- **TCP** is a connection-oriented protocol, which means that a connection is established and maintained until the application programs at each end have finished exchanging messages. It determines how to break application data into packets that networks can deliver, sends packets to and accepts packets from the network layer, manages flow control, and handles retransmission of dropped or garbled packets as well as acknowledgment of all packets that arrive.

- **UDP** is a simpler message-based connectionless protocol. Connectionless protocols do not set up a dedicated end-to-end connection. Communication is achieved by transmitting information in one direction from source to destination without verifying the readiness or state of the receiver.

Some common applications of socket programming are:

- **Simple DNS:** Domain Name System (DNS) is a distributed database that translates domain names to IP addresses. A simple DNS server can be implemented using socket programming to listen for DNS queries and respond with the corresponding IP address.

- **Data & Time Client/Server:** A time server can be implemented using socket programming to listen for time requests and respond with the current date and time. A time client can also be implemented to send time requests to the server and display the received date and time.

- **Echo Client/Server:** An echo server is a server that simply sends back any data it receives. An echo client can be implemented to send data to the server and display the received echoed data.

- **Iterative & Concurrent Servers:** An iterative server handles one client at a time, processing each request before moving on to the next. A concurrent server, on the other hand, can handle multiple clients simultaneously, processing each request concurrently using threads or processes.

In summary, socket programming using UDP and TCP allows for the implementation of various network applications, including simple DNS, data & time client/server, echo client/server, and iterative & concurrent servers. These applications can be implemented using either the reliable, connection-oriented TCP or the simpler, connectionless UDP, depending on the requirements of the application.

