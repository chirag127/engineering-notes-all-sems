

## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

### Stop and Wait Protocol
- Stop and Wait Protocol is a flow control protocol.
- It is used in data communication to prevent the sender from overwhelming the receiver with data.
- In this protocol, the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame.
- If the sender does not receive an acknowledgment within a certain time period, it assumes that the frame was lost and retransmits it.

### Sliding Window Protocol
- Sliding Window Protocol is another flow control protocol.
- It is an improvement over the Stop and Wait Protocol as it allows the sender to send multiple frames before waiting for an acknowledgment.
- The sender maintains a window of frames that it can send without waiting for an acknowledgment.
- The size of the window determines the number of frames that can be sent at a time.
- The receiver also maintains a window of frames that it can receive.
- The receiver sends an acknowledgment for the frames it has received and the sender slides its window to send the next set of frames.

These protocols are used to ensure reliable data transmission in communication networks. They are implemented at the data link layer of the OSI model. They are important concepts to understand for anyone studying computer networks or data communication.



### Experiment 1.1 - Implementation of Stop and Wait Protocol

Stop and Wait Protocol is a flow control protocol in which the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. The receiver sends an acknowledgment after receiving a frame and checking it for errors.

The steps involved in the implementation of Stop and Wait Protocol are as follows:

1. The sender sends a frame to the receiver.
2. The receiver checks the frame for errors.
3. If the frame is error-free, the receiver sends an acknowledgment to the sender.
4. If the frame contains errors, the receiver discards the frame and does not send an acknowledgment.
5. The sender waits for an acknowledgment from the receiver before sending the next frame.
6. If the sender does not receive an acknowledgment within a specified time, it assumes that the frame was lost or corrupted and retransmits the frame.
7. This process continues until all frames have been transmitted and acknowledged.

This protocol is simple to implement but has a low efficiency due to the time spent waiting for acknowledgments. It is suitable for use in low error rate and low data rate communication channels.



### Experiment 1.2 - Implementation of Sliding Window Protocol

The Sliding Window Protocol is a method used in computer networks to manage the flow of data between two devices. It is used to ensure that data is transmitted reliably and efficiently.

1. The sender and receiver agree on a window size, which is the maximum number of packets that can be sent before an acknowledgment is received.
2. The sender sends packets within the window and waits for an acknowledgment from the receiver.
3. The receiver sends an acknowledgment for each packet received.
4. The sender moves the window forward by the number of acknowledged packets and sends more packets.
5. This process continues until all data has been transmitted.

The Sliding Window Protocol is an effective way to manage the flow of data and ensure reliable transmission. It is commonly used in computer networks and can be implemented in various ways, depending on the specific needs of the network.



## Experiment 2 - Study of Socket Programming and Client – Server model

1. **Socket Programming** refers to the process of creating a network communication between two or more devices using sockets. A socket is an endpoint of a two-way communication link between two programs running on a network.

2. **Client-Server Model** is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.

3. In this model, the client sends a request to the server, which processes the request and sends back a response.

4. The communication between the client and server is established using sockets.

5. The server creates a socket and binds it to a specific IP address and port number. The server then listens for incoming connections from clients.

6. The client creates a socket and connects it to the server's IP address and port number. Once the connection is established, the client and server can communicate by sending and receiving data through their respective sockets.

7. Socket programming is commonly used in the implementation of various network protocols, such as HTTP, FTP, and SMTP.

8. The study of socket programming and the client-server model is essential for understanding the fundamentals of network communication and the development of network applications.



### Experiment 2.1 - Study of Socket Programming

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.

Here are some key points to remember when studying socket programming:

1. Sockets are the endpoints of a bidirectional communication channel.
2. Sockets can communicate within a process, between processes on the same machine, or between processes on different machines.
3. Socket programming is supported by most popular operating systems, including Windows, Linux, and macOS.
4. There are two types of sockets: stream sockets and datagram sockets.
5. Stream sockets use TCP (Transmission Control Protocol) for data transmission, while datagram sockets use UDP (User Datagram Protocol).
6. Socket programming can be implemented in various programming languages, including C, C++, Python, and Java.




### Experiment 2.2 - Study of Client – Server model

1. **Overview:** The client-server model is a distributed application structure that partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients.
2. **How it works:** In a client-server model, the client sends a request to the server, which then processes the request and returns a response. This model is used in many different types of applications, including web browsing, email, and file sharing.
3. **Advantages:** Some advantages of the client-server model include centralized control, scalability, and ease of maintenance. Centralized control allows for easier management of resources and security. Scalability means that as the number of clients increases, the server can handle the increased workload. Ease of maintenance means that updates and changes can be made to the server without affecting the clients.
4. **Disadvantages:** Some disadvantages of the client-server model include the potential for a single point of failure, the need for a reliable network connection, and the potential for increased latency. A single point of failure means that if the server goes down, all clients are affected. A reliable network connection is necessary for the client and server to communicate. Increased latency can occur if the server is overloaded with requests.
5. **Examples:** Some examples of the client-server model in action include web browsing, where the client is a web browser and the server is a web server, and email, where the client is an email client and the server is an email server.




## Experiment 3 - Write a code simulating ARP /RARP protocols

The Address Resolution Protocol (ARP) and Reverse Address Resolution Protocol (RARP) are two important protocols used in computer networks. ARP is used to map an IP address to a physical address, such as a MAC address, while RARP is used to map a physical address to an IP address.

Here are the steps to write a code simulating ARP/RARP protocols:

1. Define the data structures for the ARP and RARP packets.
2. Create a function to generate ARP request packets.
3. Create a function to generate RARP request packets.
4. Create a function to process ARP request packets and generate ARP reply packets.
5. Create a function to process RARP request packets and generate RARP reply packets.
6. Create a function to send and receive packets over the network.
7. Implement the main function to simulate the ARP and RARP protocols.

This code can be written in a programming language such as C or Python. It is important to test the code thoroughly to ensure that it is working correctly and simulating the ARP and RARP protocols accurately.



## Experiment 4 - Write a code simulating PING and TRACEROUTE commands

1. **PING** is a computer network administration software utility used to test the reachability of a host on an Internet Protocol (IP) network. It measures the round-trip time for messages sent from the originating host to a destination computer that are echoed back to the source.

2. **TRACEROUTE** is a computer network diagnostic tool for displaying the route (path) and measuring transit delays of packets across an Internet Protocol (IP) network.

3. To simulate the PING command, you can write a code that sends an Internet Control Message Protocol (ICMP) echo request to the specified host and waits for a response. The code should measure the time it takes for the response to be received and display it to the user.

4. To simulate the TRACEROUTE command, you can write a code that sends a series of ICMP echo requests with increasing Time To Live (TTL) values. The code should record the IP addresses of the routers that respond with an ICMP Time Exceeded message and display the route to the user.

5. Both PING and TRACEROUTE can be implemented using various programming languages such as Python, C, or Java. It is important to choose a language that you are comfortable with and that has the necessary libraries and functions to support network programming.

6. When writing the code, it is important to consider error handling and to provide informative messages to the user in case of errors or unexpected behavior.

7. Testing and debugging the code is an important part of the development process. It is recommended to test the code on different networks and with different hosts to ensure that it is working correctly.

8. Once the code is complete, it can be used to simulate the PING and TRACEROUTE commands and provide useful information about the network connectivity and routing.



## Experiment 5 - Create a socket for HTTP for web page upload and download

1. **Objective:** The objective of this experiment is to create a socket for HTTP to enable the upload and download of web pages.

2. **Background:** HTTP (Hypertext Transfer Protocol) is the protocol used for transmitting web pages over the internet. It is a request-response protocol, where a client sends a request to a server and the server responds with the requested data.

3. **Procedure:**
    1. Create a socket using the `socket()` function.
    2. Connect the socket to the server using the `connect()` function.
    3. Send an HTTP request to the server using the `send()` function.
    4. Receive the server's response using the `recv()` function.
    5. Close the socket using the `close()` function.

4. **Expected Outcome:** After completing this experiment, you should be able to create a socket for HTTP and use it to upload and download web pages.

5. **Further Reading:** For more information on HTTP and socket programming, you can refer to the following resources:
    - [HTTP Made Really Easy](http://www.jmarshall.com/easy/http/)
    - [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/)
    - [Python Socket Programming Tutorial](https://realpython.com/python-sockets/)



## Experiment 6 - Write a program to implement RPC (Remote Procedure Call)

Remote Procedure Call (RPC) is a protocol that allows a program to request a service from a program located on another computer in a network without having to understand the network's details. RPC is used to call other processes on the remote systems like a local system.

Here are the steps to implement RPC:

1. Define the remote procedure and the data structures required to pass the data.
2. Generate the client and server stubs using the RPC compiler.
3. Write the client program that calls the remote procedure.
4. Write the server program that implements the remote procedure.
5. Compile and run the server and client programs.

The client program sends a message to the server with the name of the procedure to call, along with the required parameters. The server receives the message, unpacks the parameters, and calls the procedure. Once the procedure is completed, the server packs the result in a message and sends it back to the client.

Here is an example of a simple RPC program that adds two numbers on the server and returns the result to the client:

**Interface Definition File (add.x):**
```
program ADD_PROG {
    version ADD_VERS {
        int ADD(int, int) = 1;
    } = 1;
} = 0x20000001;
```

**Server Program (add_server.c):**
```
#include <stdio.h>
#include <rpc/rpc.h>
#include "add.h"

int *add_1_svc(int *num1, int *num2, struct svc_req *req) {
    static int result;
    result = *num1 + *num2;
    return &result;
}
```

**Client Program (add_client.c):**
```
#include <stdio.h>
#include <rpc/rpc.h>
#include "add.h"

int main(int argc, char *argv[]) {
    CLIENT *cl;
    int *result;
    int num1, num2;

    if (argc != 4) {
        fprintf(stderr, "Usage: %s hostname num1 num2\n", argv[0]);
        exit(1);
    }

    num1 = atoi(argv[2]);
    num2 = atoi(argv[3]);

    cl = clnt_create(argv[1], ADD_PROG, ADD_VERS, "tcp");
    if (cl == NULL) {
        clnt_pcreateerror(argv[1]);
        exit(1);
    }

    result = add_1(&num1, &num2, cl);
    if (result == NULL) {
        clnt_perror(cl, argv[1]);
        exit(1);
    }

    printf("%d + %d = %d\n", num1, num2, *result);

    return 0;
}
```

To compile and run the program, follow these steps:

1. Run the RPC compiler on the interface definition file to generate the client and server stubs: `rpcgen add.x`
2. Compile the server program: `cc -o add_server add_server.c add_svc.c`
3. Compile the client program: `cc -o add_client add_client.c add_clnt.c`
4. Run the server program: `./add_server`
5. Run the client program: `./add_client localhost 3 4`

The client program will send the numbers 3 and 4 to the server, the server will add them and return the result 7 to the client. The client will print the result on the screen.

This is a simple example of how to implement RPC. You can modify the program to implement more complex remote procedures and data structures.



## Experiment 7 - Implementation of Subnetting

Subnetting is the process of dividing a network into smaller subnetworks or subnets. This is done to improve network performance, security, and manageability. Here are the steps to implement subnetting:

1. Determine the number of subnets required: The first step in subnetting is to determine the number of subnets required. This can be done by considering the number of departments or locations that need to be separated on the network.

2. Determine the number of hosts per subnet: The next step is to determine the number of hosts required per subnet. This can be done by considering the number of devices that need to be connected to the network in each department or location.

3. Choose a subnet mask: The subnet mask is used to determine which part of an IP address represents the network and which part represents the host. The subnet mask should be chosen based on the number of subnets and hosts required.

4. Assign IP addresses: Once the subnet mask has been chosen, IP addresses can be assigned to the devices on the network. Each device on a subnet should have a unique IP address.

5. Configure routing: The final step in implementing subnetting is to configure routing. This involves setting up the network devices to route traffic between the different subnets.

Subnetting can be a complex process, but it is essential for managing large networks. By dividing a network into smaller subnets, network administrators can improve performance, security, and manageability.



## Experiment 8 - Applications using TCP Sockets

1. **Introduction:** Transmission Control Protocol (TCP) is a reliable, connection-oriented protocol used for transmitting data over the internet. TCP sockets provide a way for applications to communicate with each other using TCP.

2. **Examples of Applications using TCP Sockets:** Some common applications that use TCP sockets include:
    - Web browsers: Web browsers use TCP sockets to communicate with web servers and retrieve web pages.
    - Email clients: Email clients use TCP sockets to communicate with email servers and send/receive emails.
    - File transfer: Applications such as FTP (File Transfer Protocol) use TCP sockets to transfer files between computers.
    - Chat applications: Chat applications use TCP sockets to send messages between users in real-time.

3. **Advantages of using TCP Sockets:** Some advantages of using TCP sockets include:
    - Reliability: TCP ensures that data is transmitted reliably by retransmitting lost or corrupted packets.
    - Ordered delivery: TCP ensures that data is delivered in the order it was sent.
    - Flow control: TCP uses flow control to prevent the sender from overwhelming the receiver with data.

4. **Conclusion:** TCP sockets provide a reliable and efficient way for applications to communicate with each other over the internet. Many common applications, such as web browsers, email clients, and chat applications, use TCP sockets to transmit data.



### Experiment 8.1 - Echo client and echo server

1. **Objective:** The objective of this experiment is to understand the basic concepts of client-server communication using the echo protocol.
2. **Background:** The echo protocol is a simple communication protocol that sends data from a client to a server and then receives the same data back from the server. This is useful for testing the connectivity and latency of a network.
3. **Procedure:**
    1. **Setting up the server:** The first step is to set up the echo server. This can be done using a pre-existing echo server program or by writing your own using a programming language such as C or Python.
    2. **Setting up the client:** The next step is to set up the echo client. This can also be done using a pre-existing program or by writing your own.
    3. **Running the experiment:** Once the server and client are set up, the experiment can be run by sending data from the client to the server and observing the data that is returned.
4. **Expected results:** The expected result of this experiment is that the data sent from the client will be returned by the server unchanged.
5. **Conclusion:** This experiment demonstrates the basic principles of client-server communication using the echo protocol. It can be used as a starting point for more advanced experiments involving network communication.



### Experiment 8.2 - Chat

1. Chat is a form of communication that allows two or more people to exchange messages in real-time.
2. Chat can take place through various mediums, including text, voice, and video.
3. Chat can be used for personal, social, or business purposes.
4. Chat can be conducted through various platforms, including instant messaging applications, social media, and chat rooms.
5. Chat can be synchronous, where all participants are present at the same time, or asynchronous, where messages are sent and received at different times.
6. Chat can be moderated or unmoderated, with the former having rules and guidelines for participants to follow.
7. Chat can be public or private, with the former being accessible to anyone and the latter being accessible only to invited participants.
8. Chat can be used for various purposes, including sharing information, providing support, and building relationships.
9. Chat can have various features, including the ability to send and receive files, use emoticons, and format text.
10. Chat can have various benefits, including the ability to communicate in real-time, build relationships, and share information. However, it can also have drawbacks, including the potential for misunderstandings, distractions, and privacy concerns.



### Experiment 8.3 - File Transfer

File transfer refers to the process of transmitting files over a computer network from one device to another. There are several methods and protocols used for file transfer, including:

1. **File Transfer Protocol (FTP):** FTP is a standard network protocol used to transfer files from one host to another over a TCP-based network, such as the Internet. FTP is built on a client-server model architecture and uses separate control and data connections between the client and the server.

2. **Secure File Transfer Protocol (SFTP):** SFTP is a secure version of FTP that uses Secure Shell (SSH) to encrypt data during transmission. SFTP provides secure file transfer and management capabilities, including the ability to resume interrupted transfers, remotely delete files, and list directory contents.

3. **Hypertext Transfer Protocol (HTTP):** HTTP is the protocol used by the World Wide Web to transfer files, including text, images, and other multimedia content. HTTP is a request-response protocol, where the client sends a request to the server and the server responds with the requested file.

4. **Email:** Email can also be used to transfer files by attaching the file to an email message and sending it to the recipient. However, email is not designed for large file transfers and most email providers impose a limit on the size of attachments.

These are some of the common methods used for file transfer. Each method has its own advantages and disadvantages, and the choice of method depends on factors such as the size of the file, the level of security required, and the network infrastructure.



## Experiment 9 - Applications using TCP and UDP Sockets

1. **TCP (Transmission Control Protocol)** is a connection-oriented protocol that provides reliable data transfer between two devices. It is used by applications that require guaranteed delivery of data, such as email, file transfer, and web browsing.

2. **UDP (User Datagram Protocol)** is a connectionless protocol that provides fast, but unreliable data transfer between two devices. It is used by applications that can tolerate some data loss, such as online gaming, video streaming, and voice over IP (VoIP).

3. Some common applications that use **TCP** include:
    - **HTTP (HyperText Transfer Protocol)**: used by web browsers to retrieve web pages from web servers.
    - **FTP (File Transfer Protocol)**: used to transfer files between devices.
    - **SMTP (Simple Mail Transfer Protocol)**: used to send email messages between mail servers.

4. Some common applications that use **UDP** include:
    - **DNS (Domain Name System)**: used to resolve domain names to IP addresses.
    - **DHCP (Dynamic Host Configuration Protocol)**: used to automatically assign IP addresses to devices on a network.
    - **RTP (Real-time Transport Protocol)**: used to stream audio and video over the internet.

5. Both **TCP** and **UDP** use **sockets** to establish connections between devices. A socket is an endpoint for sending and receiving data, identified by an IP address and a port number.

6. In summary, **TCP** and **UDP** are two protocols used by applications to transfer data between devices. They have different characteristics and are used by different types of applications. Both protocols use sockets to establish connections between devices.



### Experiment 9.1 - DNS

1. **Objective:** To understand the Domain Name System (DNS) and its role in resolving domain names to IP addresses.
2. **Background:** DNS is a hierarchical and decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities.
3. **Procedure:** 
    - Open the command prompt or terminal on your computer.
    - Type `nslookup` followed by the domain name you want to resolve, for example `nslookup www.example.com`.
    - Press enter to execute the command.
    - The output will show the IP address associated with the domain name.
4. **Observations:** Note down the IP address returned by the `nslookup` command.
5. **Conclusion:** DNS plays a crucial role in resolving domain names to IP addresses, allowing us to access websites and other resources on the Internet using human-readable names instead of numerical IP addresses.



### Experiment 9.2 - SNMP

SNMP (Simple Network Management Protocol) is a protocol used for managing devices on IP networks. It is used to monitor and control network devices, and to manage configurations, statistics collection, performance, and security.

1. SNMP is an application layer protocol that facilitates the exchange of management information between network devices.
2. SNMP is part of the Internet Protocol Suite as defined by the Internet Engineering Task Force (IETF).
3. SNMP uses a simple request/response model for exchanging information between a manager and an agent.
4. SNMP messages are transported using User Datagram Protocol (UDP).
5. SNMP has three versions: SNMPv1, SNMPv2c, and SNMPv3.
6. SNMPv3 provides security enhancements such as authentication and encryption.
7. SNMP is widely used in network management systems to monitor network-attached devices for conditions that warrant administrative attention.




### Experiment 9.3 - File Transfer

1. **Objective:** The objective of this experiment is to learn how to transfer files between two computers or devices.

2. **Requirements:** Two computers or devices with the ability to connect to each other, either through a wired or wireless connection. A file to transfer.

3. **Procedure:**
    - Establish a connection between the two computers or devices.
    - Select the file to transfer on the source computer or device.
    - Initiate the file transfer using the appropriate method for the connection type and devices being used.
    - Monitor the progress of the file transfer until it is complete.
    - Verify that the file has been successfully transferred to the destination computer or device.

4. **Conclusion:** File transfer is a common task that is necessary for sharing data between computers or devices. There are many methods for transferring files, and the specific method used will depend on the connection type and devices being used. It is important to verify that the file has been successfully transferred to ensure that the data is not lost or corrupted during the transfer process.



## Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

1. **Introduction:** Network Simulator (NS) is a discrete event simulator targeted at networking research. It provides substantial support for simulation of TCP, routing, and multicast protocols over wired and wireless (local and satellite) networks.

2. **Objective:** The objective of this experiment is to study the NS and simulate congestion control algorithms using NS.

3. **Procedure:**
    - Install NS on your system.
    - Create a simple network topology using NS.
    - Simulate the network with different congestion control algorithms such as TCP Reno, TCP New Reno, and TCP Vegas.
    - Observe and analyze the results.

4. **Conclusion:** By performing this experiment, one can gain a better understanding of the NS and how it can be used to simulate congestion control algorithms. This can be useful in understanding the behavior of different algorithms in a network and how they can be used to improve network performance.



## Experiment 11 - Perform a case study about the different routing algorithms to select the network path with its optimum and economical during data transfer

Routing algorithms are used to determine the best path for data transfer in a network. There are several different routing algorithms that can be used to select the most optimal and economical path for data transfer. Some of the most commonly used routing algorithms include:

1. **Shortest Path First (SPF)**: This algorithm calculates the shortest path between two nodes in a network based on the distance or cost metric. It is commonly used in link-state routing protocols such as OSPF and IS-IS.

2. **Distance Vector**: This algorithm calculates the best path based on the distance or hop count metric. It is commonly used in distance-vector routing protocols such as RIP and IGRP.

3. **Path Vector**: This algorithm calculates the best path based on the path attributes such as AS path, origin, and local preference. It is commonly used in path-vector routing protocols such as BGP.

4. **Hybrid**: This algorithm combines the features of both link-state and distance-vector routing protocols. It is commonly used in hybrid routing protocols such as EIGRP.

Each of these routing algorithms has its own advantages and disadvantages, and the selection of the most optimal and economical routing algorithm depends on the specific requirements of the network. A case study can be performed to compare the performance of these different routing algorithms in a given network scenario. This can help network administrators to select the most appropriate routing algorithm for their network.



### Experiment 11.1 - Link State routing

Link State routing is a type of routing protocol used in computer networks. It is also known as shortest path first or Dijkstra's algorithm. The main features of Link State routing are:

1. Each router in the network maintains a complete map of the network topology, including the costs of each link.
2. Routers exchange information about the network topology with their neighbors using Link State packets (LSPs).
3. Each router uses the information it receives to calculate the shortest path to every other router in the network.
4. When a router detects a change in the network topology, it recalculates the shortest paths and sends updated LSPs to its neighbors.

Link State routing protocols are commonly used in large networks because they can quickly adapt to changes in the network topology. Some examples of Link State routing protocols include OSPF (Open Shortest Path First) and IS-IS (Intermediate System to Intermediate System).



### Experiment 11.2 - Flooding

Flooding is a networking technique used to disseminate information throughout a network. It involves sending packets or messages to all connected devices, regardless of whether they are the intended recipient or not. This technique is commonly used in situations where the destination of the message is unknown or when the network topology is constantly changing.

Some key points to consider when studying flooding are:
- Flooding can be an effective way to quickly disseminate information throughout a network.
- However, it can also lead to high levels of network congestion and can be resource-intensive.
- There are several variations of flooding, including selective flooding and controlled flooding, which aim to mitigate some of the drawbacks of the technique.
- Flooding is commonly used in routing protocols, such as OSPF and RIP, to quickly update routing tables and maintain network connectivity.

In summary, flooding is a powerful technique for disseminating information throughout a network, but it must be used judiciously to avoid overwhelming the network with traffic. It is important to understand the trade-offs involved when using flooding and to be aware of the various techniques available to control its impact on the network.



### Experiment 11.3 - Distance Vector

Distance vector routing is a type of routing protocol used in computer networks to determine the best path for data packets to travel from one node to another. It is based on the Bellman-Ford algorithm and is used in routing protocols such as RIP (Routing Information Protocol) and IGRP (Interior Gateway Routing Protocol).

In distance vector routing, each router maintains a routing table that contains the distance (or cost) to reach each destination network and the next hop router to reach that destination. The distance is measured in terms of a metric, such as hop count or delay.

Routers exchange their routing tables with their directly connected neighbors at regular intervals. When a router receives a routing table from a neighbor, it updates its own routing table by comparing the distances to each destination in the received table with the distances in its own table. If the received distance to a destination is shorter than the distance in its own table, the router updates its routing table with the new distance and next hop information.

Distance vector routing has some limitations, such as the count-to-infinity problem, where the convergence time can be slow in the case of a network failure. This can be mitigated by using techniques such as split horizon and poison reverse.

In summary, distance vector routing is a simple and widely used routing protocol that determines the best path for data packets based on the distance to the destination. It has some limitations, but these can be mitigated by using additional techniques.



## Experiment 12 - To learn handling and configuration of networking hardware like RJ-45 connector, CAT-6 cable, crimping tool, etc

1. **RJ-45 connector**: RJ-45 is a type of connector commonly used for Ethernet networking. It looks similar to a telephone jack, but is slightly wider. It is used to connect computers and other devices to a wired network.

2. **CAT-6 cable**: CAT-6 is a type of Ethernet cable that is used to connect devices to a network. It is capable of transmitting data at speeds of up to 10 Gbps and is backward compatible with CAT-5 and CAT-5e cables.

3. **Crimping tool**: A crimping tool is used to attach RJ-45 connectors to the ends of Ethernet cables. It is important to use the correct crimping tool for the type of connector being used, as using the wrong tool can damage the connector and affect the performance of the cable.

4. **Configuration**: To configure a network using these hardware components, the first step is to attach RJ-45 connectors to the ends of the CAT-6 cable using the crimping tool. The cable can then be connected to the devices that need to be networked. The devices will need to be configured with the appropriate network settings, such as IP addresses and subnet masks, in order to communicate with each other.

5. **Handling**: It is important to handle networking hardware carefully to avoid damaging the components. When attaching connectors to cables, make sure to use the correct crimping tool and follow the manufacturer's instructions. When connecting cables to devices, make sure to insert the connectors firmly but gently to avoid damaging the ports. Avoid bending or twisting the cables excessively, as this can affect their performance.



## Experiment 13 - Configuration of router, hub, switch etc. (using real devices or simulators)

1. **Objective:** The objective of this experiment is to learn how to configure a router, hub, switch, and other networking devices using real devices or simulators.

2. **Equipment Required:** To perform this experiment, you will need the following equipment:
    - A router
    - A hub
    - A switch
    - Ethernet cables
    - A computer with a terminal emulator or a simulator software installed

3. **Procedure:**
    1. Connect the router, hub, and switch to the computer using Ethernet cables.
    2. Open the terminal emulator or simulator software on the computer.
    3. Configure the router by entering the appropriate commands in the terminal emulator or simulator software.
    4. Repeat the above step for the hub and switch.
    5. Verify the configuration by checking the connectivity between the devices.

4. **Conclusion:** By performing this experiment, you will have learned how to configure a router, hub, switch, and other networking devices using real devices or simulators.



## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

1. **ping**: ping is a command used to test the reachability of a host on an IP network. It measures the round-trip time for messages sent from the originating host to a destination computer that are echoed back to the source.
2. **traceroute**: traceroute is a command used to diagnose the route packets take to reach a network host. It displays the path and transit times of packets across an IP network.
3. **nslookup**: nslookup is a command used to query the Domain Name System (DNS) to obtain domain name or IP address mapping or for any other specific DNS record.
4. **arp**: arp is a command used to view and manipulate the Address Resolution Protocol (ARP) cache. The ARP cache is used to store mappings between IP addresses and MAC addresses.
5. **telnet**: telnet is a command used to connect to remote computers using the Telnet protocol. It is used for remote command line login and remote command execution.
6. **ftp**: ftp is a command used to transfer files between computers on a network using the File Transfer Protocol (FTP). It can be used to upload or download files to/from a remote computer.

These commands are useful for network troubleshooting and management. They can be used to diagnose connectivity issues, view network information, and transfer files between computers. It is important to understand how to use these commands to effectively manage and troubleshoot network issues.



## Experiment 15 - Network packet analysis using tools like Wireshark, tcpdump, etc

Network packet analysis is the process of capturing, recording, and analyzing network traffic to identify performance issues, troubleshoot network problems, and detect security threats. Tools like Wireshark and tcpdump are commonly used for this purpose.

1. **Wireshark** is a free and open-source network protocol analyzer that allows users to see what's happening on their network at a microscopic level. It can capture and display packets in real-time or from a previously saved capture file. Wireshark supports a wide range of protocols and can decode and dissect many different types of packets.

2. **tcpdump** is a command-line packet analyzer that allows users to capture and display packets on a network interface. It is available on many operating systems, including Linux, macOS, and Windows. tcpdump can capture packets in real-time or save them to a file for later analysis.

Both Wireshark and tcpdump can be used to analyze network traffic and identify issues such as slow network performance, dropped packets, and security threats. They can also be used to troubleshoot network problems and verify that network protocols are working correctly.

To use these tools, a user must have a basic understanding of network protocols and how they work. It is also important to have permission to capture and analyze network traffic, as this may be restricted by network policies or local laws.



## Experiment 16 - Network simulation using tools like Cisco Packet Tracer, NetSim, OMNeT++, NS2, NS3, etc

Network simulation is the technique of modeling the behavior of a network by calculating the interaction between the different network entities using mathematical formulas. Network simulation tools are software applications that allow network administrators and researchers to study the behavior of networks under different conditions.

Some popular network simulation tools are:

1. **Cisco Packet Tracer:** A network simulation tool developed by Cisco Systems that allows users to create network topologies, configure devices, and simulate network traffic.
2. **NetSim:** A network simulation tool developed by Tetcos that supports a wide range of protocols and technologies, including routing, switching, and wireless.
3. **OMNeT++:** An open-source, modular, component-based C++ simulation library and framework primarily used for building network simulators.
4. **NS2:** An open-source, discrete-event network simulator primarily used for research and education.
5. **NS3:** An open-source, discrete-event network simulator that is a successor to NS2 and is primarily used for research and education.

These tools allow users to design and test network topologies, protocols, and configurations in a virtual environment before deploying them in a real network. This can help network administrators and researchers to identify and fix potential issues, optimize network performance, and evaluate new technologies.



## Experiment 17 - Socket programming using UDP and TCP (e.g., simple DNS, data & time client/server, echo client/server, iterative & concurrent servers)

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket (node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection. The server forms the listener socket while the client reaches out to the server.

There are two widely used socket types, stream sockets, and datagram sockets. Stream sockets use TCP (Transmission Control Protocol), which is a reliable, stream-oriented protocol, and datagram sockets use UDP (User Datagram Protocol), which is unreliable and message-oriented.

- **TCP** is a connection-oriented protocol, which means that a connection is established and maintained until the application programs at each end have finished exchanging messages. It determines how to break application data into packets that networks can deliver, sends packets to and accepts packets from the network layer, manages flow control, and handles retransmission of dropped or garbled packets as well as acknowledgment of all packets that arrive.

- **UDP** is a simpler message-based connectionless protocol. Connectionless protocols do not set up a dedicated end-to-end connection. Communication is achieved by transmitting information in one direction from source to destination without verifying the readiness or state of the receiver.

Some examples of applications that use socket programming are:

- **Simple DNS**: DNS (Domain Name System) is used to translate human-readable domain names into IP addresses. A simple DNS application can be created using socket programming to send a domain name to a DNS server and receive the corresponding IP address.

- **Data & Time Client/Server**: A data and time client/server application can be created using socket programming, where the client sends a request to the server for the current date and time, and the server responds with the requested information.

- **Echo Client/Server**: An echo client/server application can be created using socket programming, where the client sends a message to the server, and the server responds by sending the same message back to the client.

- **Iterative & Concurrent Servers**: An iterative server handles one client at a time, while a concurrent server can handle multiple clients simultaneously. Both types of servers can be created using socket programming.

In summary, socket programming is a powerful tool for creating network-based applications using TCP and UDP protocols. It allows for the creation of a wide range of applications, from simple DNS and data & time client/server applications to more complex iterative and concurrent servers.

