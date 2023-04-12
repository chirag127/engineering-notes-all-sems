



## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

- Stop and Wait Protocol is a type of flow control protocol used for reliable transmission of data over a network. It is a sender-receiver protocol, where the sender sends a packet to the receiver, and then waits for an acknowledgement from the receiver before sending the next packet.

- Sliding Window Protocol is a type of flow control protocol used for reliable transmission of data over a network. It is a sender-receiver protocol, in which the sender can send multiple packets to the receiver, and the receiver can acknowledge the packets in any order.

- In Stop and Wait Protocol, the sender sends a single packet of data to the receiver, and then waits for an acknowledgement from the receiver before sending the next packet. This makes it a simple and reliable protocol, but it is not very efficient since it requires the sender to wait for an acknowledgement before sending the next packet.

- In Sliding Window Protocol, the sender can send multiple packets of data to the receiver, and the receiver can acknowledge the packets in any order. This makes it a more efficient protocol than Stop and Wait Protocol, as it allows the sender to send multiple packets before waiting for an acknowledgement.

- Stop and Wait Protocol is a simpler protocol than Sliding Window Protocol, but it is not as efficient. Sliding Window Protocol is more efficient, but it is more complex than Stop and Wait Protocol.




### Experiment 1.1 - Implementation of Stop and Wait Protocol

1. Stop and wait protocol is a data link layer protocol that is used to ensure reliable communication between two nodes over a network. 
2. The protocol requires that each node wait for an acknowledgement from the other node before sending the next packet of data. 
3. This ensures that the data is received by the intended recipient and that no data is lost in transmission.
4. The protocol also ensures that the data is received in the order it was sent, so that the data is not corrupted.
5. The protocol works by having the sender send a packet of data to the receiver, which is then acknowledged by the receiver. 
6. The sender then waits for the acknowledgement before sending the next packet. 
7. If the acknowledgement is not received, the sender will resend the packet until it is acknowledged.
8. This protocol is used in a variety of applications, such as file transfer, email, web browsing, and streaming video.




### Experiment 1.2 - Implementation of Sliding Window Protocol

1. The Sliding Window Protocol is a data link layer protocol that is used to ensure reliable communication between two devices. 
2. It is a type of stop-and-wait protocol, which means that the sender will wait for an acknowledgement from the receiver before sending the next packet. 
3. The protocol works by having the sender and receiver maintain a window of packets, where the sender can only send packets within the window and the receiver can only receive packets within the window. 
4. The sender will start by sending a packet and the receiver will send an acknowledgement for that packet. 
5. The sender will then send the next packet and the receiver will send an acknowledgement for that packet. 
6. This process continues until the window is full. 
7. The sender will then wait for the receiver to send an acknowledgement for the last packet, before sending the next packet. 
8. The receiver will send an acknowledgement for each packet received, and the sender will adjust the window size accordingly. 
9. The protocol ensures reliable communication by using acknowledgements and adjusting the window size.




## Experiment 2 - Study of Socket Programming and Client – Server model

1. Socket programming is a type of network communication that enables two or more processes to communicate with each other over a network. It is a way of establishing a connection between two computers in order to exchange data.

2. Socket programming is based on the client–server model. In this model, one process acts as a server that waits for connections from other processes (clients).

3. A socket is an endpoint of a two-way communication link between two programs running on the network. A socket is bound to a port number so that the TCP layer can identify the application that data is destined to be sent.

4. Socket programming is used in many applications such as web servers, email servers, file transfer protocol (FTP) servers, instant messaging applications, and more.

5. Socket programming supports both connection-oriented and connectionless communication. In connection-oriented communication, both the client and the server must establish a connection before any data can be exchanged. In connectionless communication, the client can send data without first establishing a connection.

6. Socket programming can be implemented in different programming languages such as C, Java, Python, and more. Each language has its own set of functions and libraries that are used to create socket programs.




### Experiment 2.1 - Study of Socket Programming

1. Socket programming is a form of inter-process communication (IPC) that enables different processes running on the same or different computers to communicate with each other. 
2. It is based on the concept of ports and sockets, which are endpoints of communication between two processes.
3. Socket programming enables the exchange of data between two processes in a networked environment. It is a technique used for establishing communication between two processes, which can be on the same computer or on different computers connected through a network.
4. Socket programming is used to create a connection between two or more processes, which can be used to exchange data between them.
5. Socket programming is used in many applications, such as web servers, file transfer protocols, instant messaging, and more.
6. Socket programming is based on the client-server model, where a client process requests a service from a server process.
7. Socket programming involves creating a socket, connecting it to a port, and then sending and receiving data over the socket.
8. The socket programming API provides a set of functions and data structures that can be used to create and manage sockets.
9. Socket programming is an important concept in computer networks, and is used in many applications such as web servers, file transfer protocols, instant messaging, and more.




### Experiment 2.2 - Study of Client – Server model

1. The client-server model is a distributed computing architecture where two or more computers communicate with each other in order to share resources and exchange data.

2. The client-server model consists of two components: the client and the server. The client is responsible for making requests to the server and the server is responsible for responding to the requests.

3. The client-server model is used in many types of applications, such as web applications, database applications, file sharing applications, and more.

4. In a client-server model, the server is responsible for providing the resources and services requested by the client. The server also handles the security of the data being transferred between the client and the server.

5. The client-server model is a popular model for distributed computing because it allows for scalability, reliability, and flexibility. It also provides a level of security for the data being transferred.




## Experiment 3 - Write a Code Simulating ARP /RARP Protocols

1. ARP (Address Resolution Protocol): This protocol is used to find a host's physical (MAC) address when only its IP address is known. It is used in a broadcast type of communication, where an ARP request is sent out from one host to all other hosts on the same network. 
2. RARP (Reverse Address Resolution Protocol): This protocol is used to find a host's IP address when only its MAC address is known. It is used in a broadcast type of communication, where a RARP request is sent out from one host to all other hosts on the same network. 
3. Writing a Code Simulating ARP /RARP Protocols: The code should be written in a language such as C or C++, and should include the following components: 
    * A function to create an ARP request packet 
    * A function to create a RARP request packet 
    * A function to send the ARP request packet 
    * A function to send the RARP request packet 
    * A function to receive the ARP response packet 
    * A function to receive the RARP response packet 
    * A function to parse the ARP response packet 
    * A function to parse the RARP response packet 
    * A function to process the ARP response packet 
    * A function to process the RARP response packet 
    * A function to display the results of the ARP /RARP request 
4. Testing the Code: Once the code is written, it should be tested to ensure that it works correctly. A test environment should be created to simulate a network, and the code should be tested with multiple different hosts to ensure that it is working correctly.




## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

1. PING (Packet Internet Groper) is a basic network utility used to check if a device is reachable over a network. It is used to measure the round-trip time for messages sent from the local host to a destination computer. 
2. TRACEROUTE (also known as tracert) is a network utility used to trace the route packets take from a local host to a destination computer. It is used to measure the time taken for packets to reach the destination computer. 
3. In order to simulate a PING or TRACEROUTE command, a code can be written in any programming language. The code should include the following steps: 
    - Establish a connection with the destination computer. 
    - Send out a PING or TRACEROUTE request. 
    - Receive the response from the destination computer. 
    - Calculate the round-trip time for the request. 
    - Display the results. 
4. The code should also include error-handling mechanisms to handle any potential errors that may occur while sending or receiving the request.




## Experiment 5 - Create a Socket for HTTP for Web Page Upload and Download

1. A socket is an endpoint in a network connection between two programs running on the same or different devices.
2. In order to create a socket for HTTP, a client program must first establish a connection with a server program.
3. The client program will send an HTTP request to the server program, which will then respond with an HTTP response.
4. The client program can then use the socket to upload and download web pages from the server.
5. When uploading a web page, the client program will send the web page to the server, which will then store the web page in its database.
6. When downloading a web page, the client program will request the web page from the server, which will then send the web page to the client program.
7. The socket can also be used for other types of communication between the client and server, such as sending and receiving data.




## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

1. RPC (Remote Procedure Call) is a protocol that allows a program to request a service from a program located in another computer on a network without having to understand the network's details. 
2. It is a form of inter-process communication (IPC) that allows different processes to communicate with each other.
3. RPC is a client-server architecture, meaning that one program (the client) requests a service from another program (the server).
4. The client sends a request message to the server, which then executes the requested operation and sends back a response message.
5. The client and server must be written in the same programming language for the RPC to work.
6. The server program must be written to accept and respond to requests from clients.
7. The client program must be written to make requests to the server.
8. To implement RPC, the client and server must have a common interface. This interface defines the operations that the server can perform.
9. The client sends a request message to the server, which then executes the requested operation and sends back a response message.
10. The client and server communicate using a protocol, such as TCP/IP or UDP.
11. The client and server must also agree on a data format for sending and receiving messages. This could be a binary format or a text-based format such as JSON or XML.
12. Security is an important aspect of RPC. Authentication and encryption are used to ensure that only authorized clients can access the server and that messages are not intercepted or modified in transit.




## Experiment 7 - Implementation of Subnetting

1. Subnetting is the process of dividing a single network into multiple smaller networks. 
2. Subnetting is used to improve the efficiency of network traffic by segmenting the network into smaller, more manageable pieces. 
3. Subnetting is also used to provide better security by isolating network segments from each other. 
4. To create a subnet, a network administrator must first determine the number of subnets that are needed, the size of each subnet, and the IP address range for each subnet. 
5. The IP address range for each subnet is determined by the subnet mask. The subnet mask is a 32-bit number that defines which parts of an IP address should be used to identify the network and which parts should be used to identify the host. 
6. The subnet mask is written in the form of four octets, each containing 8 bits. The bits that are set to 1 indicate which part of the IP address should be used for the network, and the bits that are set to 0 indicate which part of the IP address should be used for the host. 
7. Once the subnet mask has been determined, the IP address range for each subnet can be determined by using the subnet mask and the IP address of the network. 
8. Subnetting can also be used to create virtual LANs (VLANs). VLANs are used to separate network segments from each other and to provide better security. 
9. Subnetting is an important tool for network administrators and is used to improve the efficiency and security of networks.




## Experiment 8 - Applications using TCP Sockets 

1. TCP sockets are the most commonly used type of network connection. They are used to establish connections between two computers, allowing them to communicate with each other over the internet.

2. TCP sockets are used for a variety of applications, such as web browsing, file sharing, remote desktop access, and online gaming. 

3. When using TCP sockets, the two computers must first establish a connection before they can send and receive data. This is done through a three-way handshake process.

4. Once the connection is established, data can be sent in both directions. The data is broken into packets and sent over the network.

5. The receiving computer will acknowledge the receipt of each packet and the sending computer will resend any packets that are not acknowledged.

6. TCP sockets are reliable and secure, as the data is guaranteed to arrive in the correct order and is encrypted.

7. TCP sockets are also used for streaming applications, such as streaming audio and video. They are also used for Voice over IP (VoIP) applications, such as Skype.




### Experiment 8.1 - Echo client and echo server

1. An **echo server** is a type of network service that sends back data that it receives. It is commonly used for testing network connections and for diagnosing network problems.

2. An **echo client** is a type of network service that sends data to an echo server and receives the same data back. It is commonly used for testing network connections and for diagnosing network problems.

3. The **echo protocol** is a simple protocol that is used to send and receive data between two network nodes. It works by sending a packet of data from the client to the server, and then the server sends the same packet back to the client.

4. The **echo test** is a procedure used to test the performance of a network connection. It involves sending a packet of data from the client to the server, and then measuring the amount of time it takes for the server to send the same packet back to the client.

5. The **echo request** is a special type of packet that is sent by the client to the server in order to initiate an echo test.

6. The **echo reply** is a special type of packet that is sent by the server to the client in response to an echo request.




### Experiment 8.2 - Chat
- Chatbots are computer programs that simulate conversation with human users.
- They are designed to provide a conversational interface for users to access information or services.
- Chatbots can be used for customer service, marketing, or providing information about products and services.
- Chatbots can be deployed on websites, social media, or messaging applications.
- Chatbots use natural language processing (NLP) to understand user input and generate an appropriate response.
- Chatbots can be programmed to respond to user input in a variety of ways, such as providing answers to questions, providing recommendations, or completing tasks.
- Chatbots can be used to automate tasks such as scheduling appointments, ordering food, or booking flights.
- Chatbot design and development requires knowledge of computer programming, artificial intelligence, and natural language processing.




### Experiment 8.3 - File Transfer

1. File transfer is the process of moving files from one computer to another.
2. It can be done over a network or via a direct connection.
3. There are several different protocols used for file transfer, including FTP, SFTP, and SCP.
4. FTP (File Transfer Protocol) is the most commonly used protocol for file transfer. It is used to transfer files between two computers over a network.
5. SFTP (Secure File Transfer Protocol) is an extension of FTP that adds security features such as encryption and authentication.
6. SCP (Secure Copy Protocol) is another secure file transfer protocol that is used to securely copy files between two computers.
7. File transfer can also be done using direct connections, such as USB or Firewire.
8. The speed of file transfer depends on the network connection and the size of the file being transferred.




## Experiment 9 - Applications using TCP and UDP Sockets

* Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) are two of the most commonly used protocols for communication between applications.
* TCP is a connection-oriented protocol, which means that it establishes a connection between two applications before data can be exchanged. It provides reliable data transfer, as it guarantees that all data sent is received and in the same order as it was sent.
* UDP is a connectionless protocol, which means that it does not establish a connection before data is exchanged. It is often used for streaming media, as it can send data faster than TCP. It does not guarantee that data is received in the same order as it was sent, or that it is received at all.
* Both TCP and UDP can be used for applications such as web browsing, email, file transfers, and streaming media.
* TCP is often used for web browsing and email, as these applications require reliable data transfer.
* UDP is often used for streaming media, such as video and audio, as it can send data faster than TCP.
* Both TCP and UDP can also be used for file transfers, though UDP is not as reliable as TCP and is therefore not recommended for large file transfers.




### Experiment 9.1 - DNS

1. DNS stands for Domain Name System. It is a distributed hierarchical database that is used to translate domain names (e.g. www.example.com) into IP addresses.

2. DNS is a client-server system. Clients query DNS servers to resolve domain names into IP addresses.

3. DNS servers are organized in a hierarchical structure. At the top of the hierarchy is the root DNS server, which is responsible for resolving the top-level domains (e.g. .com, .org, .net).

4. DNS servers can be configured to provide different types of information, such as mail exchangers (MX records) and text records (TXT records).

5. DNS is an essential part of the internet infrastructure, as it allows users to access websites and services by typing in an easy-to-remember domain name.




### Experiment 9.2 - SNMP

1. Simple Network Management Protocol (SNMP) is a network management protocol used for monitoring and managing network devices, such as routers, switches, servers, and other networked devices. 
2. SNMP is a standard protocol for network management, defined in RFC 1157 and RFC 3411. 
3. SNMP uses a manager-agent architecture, where the manager is responsible for sending queries to the agent and the agent is responsible for responding to them. 
4. SNMP uses a UDP port 161 for communication between the manager and agent, and a UDP port 162 for traps (notifications of events) sent from the agent to the manager. 
5. SNMP messages are structured into five main types: GetRequest, GetNextRequest, GetBulkRequest, SetRequest, and Trap. 
6. SNMP uses a hierarchical structure of managed objects, called the Management Information Base (MIB), to define the data that can be monitored and managed. 
7. SNMP allows for the monitoring and management of network devices from a centralized console, making it easier to manage large networks.





### Experiment 9.3 - File Transfer

1. File transfer is the process of copying or moving files from one computer to another over a network or the Internet.

2. File transfer can be done manually, by downloading and uploading files, or automatically, with a program that performs the transfer.

3. File transfer protocols are the rules and standards used to transfer files. Common protocols include FTP, SFTP, and HTTP.

4. File transfer requires a connection between the two computers. This connection can be established through a local area network (LAN) or a wide area network (WAN).

5. Security is an important factor when transferring files. Encryption, authentication, and authorization are all important measures to ensure the security of the file transfer.




## Experiment 10 - Study of Network Simulator (NS) and Simulation of Congestion Control Algorithms using NS

1. Network Simulator (NS) is a software package for simulating computer networks and is used to study the behaviour of various network protocols.
2. NS is an open source and freely available software package.
3. It is used to simulate a variety of protocols, such as TCP, UDP, IP, and others.
4. It is also used to simulate congestion control algorithms, such as RED, DropTail, and others.
5. NS is written in the C++ programming language and is highly portable.
6. It is capable of simulating large networks with thousands of nodes.
7. NS provides a variety of tools for analyzing the performance of various protocols and algorithms.
8. It also provides a graphical user interface for visualizing network topology and performance.
9. NS is widely used in academia for research and teaching purposes.
10. It is also used in industry for network design and analysis.




## Experiment 11 - Perform a case study about the different routing algorithms to select the network path with its optimum and economical during data transfer

1. Routing algorithms are used to select the network path with the best performance and cost efficiency when transferring data.
2. The main types of routing algorithms are distance vector, link state, and hybrid.
3. Distance vector routing algorithms use the Bellman-Ford equation to determine the shortest path from the source to the destination.
4. Link state routing algorithms use a flooding algorithm to share information about the network topology with all nodes in the network.
5. Hybrid routing algorithms combine the features of distance vector and link state routing algorithms to provide more efficient routing.
6. The selection of the best routing algorithm depends on the network size, traffic patterns, and link costs.
7. The performance of the routing algorithm can be evaluated by metrics such as throughput, delay, and jitter.
8. The cost of the routing algorithm can be evaluated by metrics such as link costs, energy consumption, and hardware costs.
9. The optimal routing algorithm should be chosen based on the network requirements and performance objectives.




### Experiment 11.1 - Link State routing

1. Link State routing is a type of routing protocol used in computer networks. It is also known as shortest path first (SPF) routing protocol.

2. Link State routing protocol works by discovering a network topology and creating a routing table based on the topology.

3. The routers in the network exchange information about their links and the cost associated with each link.

4. The routers then use this information to calculate the shortest path to each destination in the network.

5. Link State routing protocols are generally faster than distance vector routing protocols, as they don't require periodic updates of the entire routing table.

6. Link State routing protocols are more complex than distance vector routing protocols, as they require more processing power to calculate the shortest paths.

7. Examples of Link State routing protocols include Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).




### Experiment 11.2 - Flooding

- Flooding is a type of psychotherapy that involves having a patient repeatedly and vividly recall a traumatic event in order to reduce its emotional impact.
- The goal of flooding is to desensitize the patient to the traumatic event by repeatedly having them confront the associated memories and emotions.
- Flooding is typically done in a controlled setting with the guidance of a trained therapist.
- The therapist will usually start by having the patient describe the traumatic event in detail, and then gradually increase their exposure to the memories and emotions associated with the event.
- The therapist will also provide support and guidance to help the patient process the emotions associated with the trauma.
- Flooding has been shown to be effective in reducing the symptoms of post-traumatic stress disorder (PTSD), but it is not without risks.
- Flooding can cause a great deal of emotional distress, and should only be used with the guidance of a trained mental health professional.




### Experiment 11.3 - Distance Vector

1. Distance vector routing is a type of routing protocol used in computer networks. It is based on the Bellman-Ford algorithm, which calculates the shortest path between two nodes in a network.

2. Distance vector routing works by having each node in the network maintain a table of the shortest paths to all other nodes in the network. This table is referred to as the routing table.

3. Each node in the network sends its routing table to its neighbors. The neighbors then compare their routing tables with the one they received from the node. If the neighbor finds a shorter path to any node in the network, it updates its routing table accordingly.

4. The process of exchanging routing tables is known as the distance vector algorithm. It is an iterative process, meaning that the nodes keep exchanging routing tables until the tables converge to their final form.

5. The distance vector algorithm is used in a variety of different routing protocols, including RIP, IGRP, and EIGRP. It is also used in some link-state routing protocols, such as OSPF.




## Experiment 12 - To learn handling and configuration of networking hardware like RJ-45 connector, CAT-6 cable, crimping tool, etc.

1. RJ-45 Connector: An RJ-45 connector is the most common type of connector used for computer networking. It is a type of 8P8C connector used for connecting computers and other devices to a local area network (LAN).

2. CAT-6 Cable: CAT-6 cable is a type of network cable used for Ethernet networks. It is a shielded twisted pair cable that supports gigabit Ethernet, and is backward-compatible with CAT-5 and CAT-5e cables.

3. Crimping Tool: A crimping tool is a tool used for connecting RJ-45 connectors to CAT-6 cables. It is used to crimp the metal pins of the RJ-45 connector onto the wires of the CAT-6 cable.

4. Connecting the RJ-45 Connector: To connect an RJ-45 connector to a CAT-6 cable, the wires of the cable must be arranged in the correct order. The wires must then be inserted into the RJ-45 connector and crimped using a crimping tool.

5. Testing the Connection: Once the RJ-45 connector is connected to the CAT-6 cable, it can be tested to make sure it is working properly. This can be done using a network tester, which will check for continuity and any other errors in the connection.




## Experiment 13 - Configuration of router, hub, switch etc. (using real devices or simulators)

* Routers are network devices that link two or more networks together. They act as a gateway between networks and can be used to connect computers, printers, and other devices to each other.
* Hubs are network devices that connect multiple computers together. They are used to create a local area network (LAN) and allow for data to be transferred between computers.
* Switches are network devices that allow for data to be transferred between two or more computers. They are used to create a local area network (LAN) and allow for data to be transferred between computers.
* Real devices are physical devices that are used to connect to a network. They can be routers, hubs, switches, or other network devices.
* Simulators are computer programs that are used to simulate real devices. They can be used to test and configure a network before deploying it.




## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

1. **Ping**: Ping is a network utility used to check if a host is reachable on a network. It sends an ICMP echo request packet to a specified host and waits for an ICMP echo reply.

2. **Traceroute**: Traceroute is a network utility that shows the route taken by packets from the source to the destination. It displays the IP addresses of the routers in the path, as well as the time taken for the packets to reach each router.

3. **Nslookup**: Nslookup is a network utility used to query DNS records. It can be used to query the IP address of a host, as well as other DNS records such as MX records.

4. **Arp**: Arp is a network utility used to view and modify the local arp cache. It can be used to view the IP address and MAC address of hosts on the local network.

5. **Telnet**: Telnet is a network protocol used to connect to remote hosts. It can be used to connect to a remote host and execute commands on it.

6. **FTP**: FTP (File Transfer Protocol) is a network protocol used to transfer files between hosts. It can be used to upload and download files from a remote host.




## Experiment 15 - Network Packet Analysis using Tools like Wireshark, tcpdump, etc.

1. Network packet analysis is the process of examining the data that is sent and received over a computer network. 
2. Network packet analysis can be used to troubleshoot network issues, detect malicious activity, and monitor network performance. 
3. Wireshark is a popular network packet analysis tool that is used to capture, analyze, and interpret network traffic. 
4. tcpdump is another network packet analysis tool that is used to capture and analyze network traffic. 
5. Both Wireshark and tcpdump can be used to capture, filter, and analyze network traffic. 
6. To use Wireshark or tcpdump, you must have access to the network traffic that you want to analyze. 
7. The captured network traffic can then be analyzed to determine the source, destination, and type of traffic. 
8. Network packet analysis can also be used to detect malicious activity, such as port scans, denial of service attacks, and other malicious activity. 
9. Network packet analysis can also be used to monitor network performance, such as latency and throughput. 
10. Network packet analysis can also be used to troubleshoot network issues, such as packet loss, latency, and throughput.




## Experiment 16 - Network Simulation

* Network simulation is the process of creating a virtual model of a networked system in order to study the behavior of the system. 
* Network simulation tools such as Cisco Packet Tracer, NetSim, OMNeT++, NS2, and NS3 can be used to simulate and analyze the behavior of a networked system.
* Network simulation tools allow users to create and modify network topologies, configure network devices, and analyze the performance of the network.
* Network simulation tools can be used to simulate various network scenarios such as network congestion, network security threats, and network performance issues.
* Network simulation tools can also be used to evaluate the performance of new network protocols and services before they are deployed in real-world networks.
* Network simulation tools can be used to create virtual networks for educational and research purposes, as well as for testing and troubleshooting in production networks.




## Experiment 17 - Socket programming using UDP and TCP

Socket programming is a form of inter-process communication (IPC) that allows two or more processes to communicate with each other. It is a powerful way to exchange data between different processes on the same machine or on different machines connected by a network.

**UDP**

UDP (User Datagram Protocol) is a connectionless protocol which allows applications to send and receive data without establishing a connection. It is a simple, fast and reliable protocol. It is suitable for applications that require low latency and low overhead.

**TCP**

TCP (Transmission Control Protocol) is a connection-oriented protocol which requires both processes to establish a connection before sending or receiving data. It is a reliable protocol which ensures that all the data sent from one process is received by the other process in the same order it was sent.

**Simple DNS**

Simple DNS (Domain Name System) is a distributed database which is used to map domain names to IP addresses. It is used to resolve domain names to IP addresses so that applications can connect to the correct server.

**Data & Time Client/Server**

Data & Time Client/Server is a network application which allows two processes to exchange data and time information. The client sends a request to the server and the server responds with the current date and time.

**Echo Client/Server**

Echo Client/Server is a network application which allows two processes to exchange data. The client sends a request to the server and the server responds with the same data that was sent by the client.

**Iterative & Concurrent Servers**

Iterative and concurrent servers are types of server applications which allow multiple clients to connect and send requests. An iterative server handles one request at a time while a concurrent server can handle multiple requests simultaneously.

