

# Computer Networks

Here is an ASCII diagram of a simple computer network:

```
+------------+     +------------+
|            |     |            |
|  Computer  +-----+  Computer  |
|            |     |            |
+------+-----+     +-----+------+
       |                 |
       |                 |
       |                 |
       |                 |
+------+-----+     +-----+------+
|            |     |            |
|  Computer  +-----+  Computer  |
|            |     |            |
+------------+     +------------+
```

This diagram shows four computers connected in a network. The lines between the computers represent the connections between them, allowing them to communicate and share data with each other.




## Unit 1 - Introductory Concepts of Computer Networks and Physical Layer

Here is an ASCII diagram that illustrates the basic concepts of computer networks and the physical layer:

```
+----------------+
| Application    |
+----------------+
| Transport      |
+----------------+
| Network        |
+----------------+
| Data Link      |
+----------------+
| Physical       |
+----------------+
```

The diagram shows the five layers of the OSI model, which is a conceptual framework for understanding how data is transmitted over a network. The physical layer is the lowest layer and is responsible for transmitting raw bits over a communication channel. The data link layer is responsible for providing reliable transmission of data across the physical link. The network layer is responsible for routing data packets between devices on the network. The transport layer is responsible for providing end-to-end communication between applications. The application layer is the highest layer and is responsible for providing services to the user, such as email, file transfer, and web browsing.




### Introductory Concepts of Computer Networks

Here is an ASCII diagram that shows the basic concepts of computer networks:

```
+------------+     +------------+
|            |     |            |
|   Client   |-----|   Server   |
|            |     |            |
+------------+     +------------+
       |                 |
       |                 |
+------------+     +------------+
|            |     |            |
|   Router   |-----|   Router   |
|            |     |            |
+------------+     +------------+
       |                 |
       |                 |
+------------+     +------------+
|            |     |            |
|   Modem    |-----|   Modem    |
|            |     |            |
+------------+     +------------+
```

This diagram shows the basic components of a computer network, including clients, servers, routers, and modems. Clients and servers communicate with each other through routers, which direct data traffic between them. Modems are used to connect the network to the internet.




#### Goals and applications of networks and protocols

```
+---------------------+
|                     |
|  Networks and       |
|  Protocols          |
|                     |
+----------+----------+
           |
           |
           v
+----------+----------+
|                     |
|  Goals:             |
|  - Reliable         |
|    communication    |
|  - Efficient data   |
|    transfer         |
|  - Security         |
|                     |
+----------+----------+
           |
           |
           v
+----------+----------+
|                     |
|  Applications:      |
|  - Email            |
|  - File sharing     |
|  - Online gaming    |
|  - Video streaming  |
|  - Social media     |
|                     |
+---------------------+
```




#### Categories of networks in computer networks
There are several categories of networks in computer networks, including Local Area Networks (LANs), Wide Area Networks (WANs), Metropolitan Area Networks (MANs), and Personal Area Networks (PANs).

Here is an ASCII diagram that illustrates the different categories of networks in computer networks:

```
+----------------+
|                |
|     Internet   |
|                |
+-------+--------+
        |
        |
+-------+--------+
|                |
|       WAN      |
|                |
+-------+--------+
        |
        |
+-------+--------+
|                |
|       MAN      |
|                |
+-------+--------+
        |
        |
+-------+--------+
|                |
|       LAN      |
|                |
+-------+--------+
        |
        |
+-------+--------+
|                |
|       PAN      |
|                |
+----------------+
```

A LAN is a network that connects computers and devices in a limited geographical area, such as a home, school, or office building. A WAN is a network that covers a broad area, such as a country or the world, using leased telecommunication lines. A MAN is a network that connects LANs in a metropolitan area, such as a city or a large campus. A PAN is a network that connects devices within the range of an individual person, typically within a range of 10 meters.




#### Organization of the Internet

The Internet is a global network of interconnected computer networks. It is organized in a hierarchical structure, with the highest level being the Internet backbone, which is a network of high-speed data links that connect major computer centers around the world.

```
+----------------+
| Internet       |
| Backbone       |
+-------+--------+
        |
        |
+-------+--------+
| Internet       |
| Service        |
| Providers (ISPs)|
+-------+--------+
        |
        |
+-------+--------+
| Local Area     |
| Networks (LANs)|
+-------+--------+
        |
        |
+-------+--------+
| End Users      |
+----------------+
```

The Internet backbone is connected to Internet Service Providers (ISPs), which provide access to the Internet for individuals and organizations. ISPs are connected to Local Area Networks (LANs), which are networks of computers within a limited geographic area, such as a home, school, or office building. Finally, end users connect to the LANs to access the Internet.




#### ISP
```
+----------------+
|                |
|     ISP        |
|                |
|  +----------+  |
|  |          |  |
|  |  Router  |  |
|  |          |  |
|  +----------+  |
|                |
|  +----------+  |
|  |          |  |
|  |  Modem   |  |
|  |          |  |
|  +----------+  |
|                |
+----------------+
```



#### Network structure with reference to Computer Networks

Here is an ASCII diagram of a simple network structure with reference to computer networks:

```
+--------+       +--------+
|        |       |        |
|  Host  +-------+ Router |
|        |       |        |
+---+----+       +----+---+
    |                 |
    |                 |
+---+----+       +----+---+
|        |       |        |
|  Host  +-------+ Router |
|        |       |        |
+--------+       +--------+
```




#### Network architecture with reference to Computer Networks

Here is an ASCII diagram of a simple network architecture with reference to computer networks:

```
+------------+     +------------+
|            |     |            |
|   Router   +-----+   Switch   |
|            |     |            |
+------------+     +------------+
       |                 |
       |                 |
+------------+     +------------+
|            |     |            |
|   Host A   |     |   Host B   |
|            |     |            |
+------------+     +------------+
```

In this diagram, the router is connected to the switch, which is then connected to two hosts, Host A and Host B. The router is responsible for routing data packets between different networks, while the switch is responsible for forwarding data packets within the same network. Host A and Host B are devices that can send and receive data packets within the network.




#### Layering Principles with Reference to Network Architecture in Computer Networks

Layering is a design principle that divides a complex system into smaller, more manageable parts. Each layer provides a specific set of services to the layer above it and relies on the services provided by the layer below it. In the context of computer networks, layering is used to organize the various components and protocols that make up a network architecture.

Here is an ASCII diagram that illustrates the layering principles in a typical network architecture:

```
+----------------+
| Application    |
+----------------+
| Transport      |
+----------------+
| Network        |
+----------------+
| Data Link      |
+----------------+
| Physical       |
+----------------+
```

In this diagram, the layers are arranged from top to bottom, with the Application layer at the top and the Physical layer at the bottom. Each layer provides a specific set of services to the layer above it. For example, the Transport layer provides end-to-end communication services to the Application layer, while the Network layer provides routing and forwarding services to the Transport layer. The Data Link layer provides reliable data transfer services to the Network layer, and the Physical layer provides the means for transmitting data over a physical medium to the Data Link layer.

Each layer is responsible for a specific set of tasks, and the layers work together to provide a complete set of network services. This modular design makes it easier to develop, maintain, and update the various components of a network architecture. It also allows for the use of different technologies and protocols at different layers, providing flexibility and scalability in the design of computer networks.



#### Services in Networks Architecture in Computer Networks

In computer networks, a service is a function provided by one system or application to another, which can be accessed over a network. Services can be classified into two main categories: connection-oriented and connectionless.

1. **Connection-oriented services**: These services establish a connection between the communicating devices before any data is transmitted. The connection provides a dedicated communication path between the devices and ensures that data is delivered in the correct order. An example of a connection-oriented service is the Transmission Control Protocol (TCP).

2. **Connectionless services**: These services do not establish a dedicated connection between the communicating devices. Instead, data is transmitted as individual packets, each of which contains the destination address. The network is responsible for delivering the packets to the correct destination, but there is no guarantee that the packets will arrive in the correct order or that they will all be delivered. An example of a connectionless service is the User Datagram Protocol (UDP).

Services can also be classified based on the level of abstraction they provide. For example, some services provide a high level of abstraction, allowing applications to communicate using high-level concepts such as files and messages, while others provide a low level of abstraction, requiring applications to communicate using low-level concepts such as packets and sockets.

In a network architecture, services are typically provided by layers. Each layer provides a set of services to the layer above it, using the services of the layer below it. For example, in the Internet Protocol Suite, the Transport Layer provides services such as reliable data transmission and flow control to the Application Layer, using the services of the Internet Layer to transmit data across the network.



#### Protocols and Standards in Networks Architecture in Computer Networks

```
+---------------------+
|                     |
|  Application Layer  |
|                     |
+----------+----------+
           |
           |
+----------+----------+
|                     |
|  Transport Layer    |
|                     |
+----------+----------+
           |
           |
+----------+----------+
|                     |
|  Network Layer      |
|                     |
+----------+----------+
           |
           |
+----------+----------+
|                     |
|  Data Link Layer    |
|                     |
+----------+----------+
           |
           |
+----------+----------+
|                     |
|  Physical Layer     |
|                     |
+---------------------+
```




#### The OSI reference model in Computer Networks

The OSI (Open Systems Interconnection) reference model is a conceptual framework used to describe the functions of a networking system. It consists of seven layers, each of which performs a specific function within the network.

Here is an ASCII diagram of the OSI reference model:

```
+---------------------+
| 7. Application      |
+---------------------+
| 6. Presentation     |
+---------------------+
| 5. Session          |
+---------------------+
| 4. Transport        |
+---------------------+
| 3. Network          |
+---------------------+
| 2. Data Link        |
+---------------------+
| 1. Physical         |
+---------------------+
```

The layers, from top to bottom, are:

1. **Physical Layer:** This layer is responsible for the transmission and reception of raw data between devices. It defines the physical characteristics of the network, such as the type of cable used and the electrical signals used to transmit data.

2. **Data Link Layer:** This layer is responsible for providing a reliable link between two devices. It handles error detection and correction, as well as flow control to prevent one device from overwhelming another with data.

3. **Network Layer:** This layer is responsible for routing data between devices on different networks. It uses logical addresses, such as IP addresses, to identify devices and determine the best path for data to travel.

4. **Transport Layer:** This layer is responsible for providing end-to-end communication between devices. It handles the segmentation of data into smaller packets, as well as the reassembly of those packets at the destination.

5. **Session Layer:** This layer is responsible for managing the communication between applications on different devices. It establishes, maintains, and terminates sessions between applications.

6. **Presentation Layer:** This layer is responsible for formatting data in a way that can be understood by the application. It handles tasks such as data compression, encryption, and character encoding.

7. **Application Layer:** This layer is responsible for providing services to the user, such as email, file transfer, and web browsing. It interacts directly with the user and provides a user interface for network services.

Each layer of the OSI model provides a specific function and communicates with the layers above and below it. Data is passed down the stack from the application layer to the physical layer, where it is transmitted across the network. At the receiving end, the data is passed back up the stack to the application layer. At each layer, the data is encapsulated with additional information, such as headers and trailers, to facilitate communication between the layers.



#### TCP/IP protocol suite in Computer Networks

Here is an ASCII diagram of the TCP/IP protocol suite in Computer Networks:

```
+---------------------+
|    Application      |
+---------------------+
|    Transport        |
+---------------------+
|    Internet         |
+---------------------+
|    Network Access   |
+---------------------+
```

The TCP/IP protocol suite is divided into four layers: Application, Transport, Internet, and Network Access. Each layer has its own set of protocols and functions to perform. The Application layer is responsible for providing services to the user, such as email, file transfer, and web browsing. The Transport layer is responsible for providing end-to-end communication between devices. The Internet layer is responsible for routing data packets across the network. The Network Access layer is responsible for the physical transmission of data over the network.




#### Network devices in Computer Networks

Network devices are components used to connect computers or other electronic devices together so that they can share files or resources like printers or fax machines. Devices used to setup a Local Area Network (LAN) are the most common type of network devices used by the public. A LAN requires a hub, switch, or router to transmit data between connected devices.

Some common network devices include:

1. **Hub**: A hub is a device that connects multiple Ethernet devices together and makes them act as a single network segment. When a hub receives data from one device, it sends the data to all other connected devices.

2. **Switch**: A switch is similar to a hub, but it only sends data to the device that is intended to receive it. This reduces network traffic and improves performance.

3. **Router**: A router is a device that connects multiple networks together and routes data between them. Routers are used to connect a LAN to the Internet or to connect multiple LANs together.

4. **Modem**: A modem is a device that modulates an analog carrier signal to encode digital information and demodulates the signal to decode the transmitted information. Modems are used to connect a computer to the Internet using a telephone line or cable connection.

5. **Firewall**: A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. Firewalls are used to protect networks from unauthorized access and to prevent the spread of viruses and other malicious software.

6. **Wireless Access Point**: A wireless access point is a device that allows wireless devices to connect to a wired network. Wireless access points are used to extend the range of a wireless network or to add wireless capability to a wired network.

7. **Network Interface Card**: A network interface card (NIC) is a hardware component that connects a computer to a network. NICs are used to add networking capability to a computer or to upgrade the networking capability of an existing computer.

These are some of the common network devices used in computer networks. Each device serves a specific purpose and plays a crucial role in the overall functioning of a network.



#### Network Components in Computer Networks

Here is an ASCII diagram of the network components in computer networks:

```
+------------+       +------------+
|            |       |            |
|   Router   +-------+   Switch   |
|            |       |            |
+------+-----+       +------+-----+
       |                    |
       |                    |
+------+-----+       +------+-----+
|            |       |            |
|   Server   |       |   Client   |
|            |       |            |
+------------+       +------------+
```




### Physical Layer in Computer Networks

The Physical Layer is the first layer of the OSI model. It is responsible for the transmission and reception of raw data between a device and a physical transmission medium. Here is an ASCII diagram that represents the Physical Layer in a computer network:

```
+----------------+
|                |
|  Physical      |
|  Layer         |
|                |
|                |
|                |
|                |
|                |
|                |
|                |
|                |
|                |
|                |
|                |
|                |
|                |
+----------------+
```

The Physical Layer is responsible for the conversion of digital data into electrical, radio, or optical signals for transmission over a physical medium. It also handles the physical connection between devices, such as the type of cable or wireless technology used. The Physical Layer is responsible for the transmission rate, signal encoding, and synchronization of bits.




#### Network topology design in Computer Networks

A network topology refers to the arrangement of nodes and the connections between them in a computer network. There are several common network topologies, including star, ring, bus, mesh, and tree. Here is an ASCII diagram of these topologies:

```
Star topology:

       [H]
        |
  [H]--[S]--[H]
        |
       [H]

Ring topology:

[H]--[H]--[H]
 |         |
[H]--[H]--[H]

Bus topology:

[H]--[H]--[H]--[H]--[H]

Mesh topology:

[H]--[H]--[H]
 | \   |   /|
[H]-[H]-[H]
 | /   |   \|
[H]--[H]--[H]

Tree topology:

       [H]
        |
  [H]--[S]--[H]
        |
       [S]
      /   \
    [H]   [H]
```

In the diagrams above, [H] represents a host or node, and [S] represents a switch or hub. In a star topology, all nodes are connected to a central switch or hub. In a ring topology, nodes are connected in a closed loop. In a bus topology, all nodes are connected to a common backbone. In a mesh topology, every node is connected to every other node. In a tree topology, nodes are connected in a hierarchical structure.




#### Types of connections in Computer Networks

There are several types of connections in computer networks, including point-to-point, circuit-switched, packet-switched, and message-switched connections.

Here is an ASCII diagram illustrating these types of connections:

```
+----------------+     +----------------+
|                |     |                |
|  Point-to-     |     |  Circuit-      |
|  Point         |     |  Switched      |
|                |     |                |
+-------+--------+     +--------+-------+
        |                       |
        |                       |
        |                       |
+-------+--------+     +--------+-------+
|                |     |                |
|  Packet-       |     |  Message-      |
|  Switched      |     |  Switched      |
|                |     |                |
+----------------+     +----------------+
```

A point-to-point connection is a direct link between two devices, while a circuit-switched connection establishes a dedicated circuit between devices. A packet-switched connection sends data in packets, while a message-switched connection sends data in messages.




Transmission media in Computer Networks refers to the physical path through which data is transmitted from one device to another. There are two types of transmission media: guided and unguided. Guided media, also known as wired or bounded transmission media, includes twisted pair cable, coaxial cable, and fiber optic cable. Unguided media, also known as wireless or unbounded transmission media, includes radio waves, microwaves, and infrared waves.

Here is an ASCII diagram that illustrates the different types of transmission media in computer networks:

```
+-----------------------+
| Transmission Media    |
|                       |
|  +-----------------+  |
|  | Guided          |  |
|  |                 |  |
|  |  +------------+ |  |
|  |  | Twisted    | |  |
|  |  | Pair Cable | |  |
|  |  +------------+ |  |
|  |                 |  |
|  |  +------------+ |  |
|  |  | Coaxial    | |  |
|  |  | Cable      | |  |
|  |  +------------+ |  |
|  |                 |  |
|  |  +------------+ |  |
|  |  | Fiber Optic| |  |
|  |  | Cable      | |  |
|  |  +------------+ |  |
|  |                 |  |
|  +-----------------+  |
|                       |
|  +-----------------+  |
|  | Unguided        |  |
|  |                 |  |
|  |  +------------+ |  |
|  |  | Radio Waves | |  |
|  |  +------------+ |  |
|  |                 |  |
|  |  +------------+ |  |
|  |  | Microwaves  | |  |
|  |  +------------+ |  |
|  |                 |  |
|  |  +------------+ |  |
|  |  | Infrared    | |  |
|  |  | Waves       | |  |
|  |  +------------+ |  |
|  |                 |  |
|  +-----------------+  |
|                       |
+-----------------------+
```



#### Signal transmission and encoding in Computer Networks

1. Signal transmission refers to the process of transmitting data from one point to another in a computer network.
2. The data is transmitted in the form of signals, which can be either analog or digital.
3. Analog signals are continuous and vary in amplitude and frequency, while digital signals are discrete and have only two states: 0 and 1.
4. Encoding is the process of converting data into a format that can be transmitted as a signal.
5. There are several encoding techniques used in computer networks, including Non-Return-to-Zero (NRZ), Manchester, and 4B/5B.
6. The choice of encoding technique depends on factors such as the transmission medium, data rate, and error detection and correction requirements.
7. The encoded signal is then transmitted over the transmission medium, which can be a wired or wireless medium.
8. The signal is received at the destination and decoded to retrieve the original data.




#### Network performance and transmission impairments in Computer Networks

Network performance refers to the level of quality of service of a telecommunications product as seen by the customer. It should not be seen merely as an attempt to get "more through" the network. Transmission impairments are factors that cause the quality of data transmission to be reduced. Impairments may be called noise or anything else that might cause an error in data transmission.

There are various kinds of transmission impairments in the network while transferring data and information through the network. The signal needs transmission media to travel from sender to receiver. The transmission media have some imperfection which causes transmission impairment. The reason behind the transmission impairment is attenuation, distortion, and noise.

The signal received may differ from the signal transmitted. The effect will degrade the signal quality for analog signals and introduce bit errors for digital signals. In a wavelength-routed optical network, a transmitted signal remains in the optical domain over the entire route (lightpath) assigned to it between its source and destination nodes. The optical signal may have to traverse a number of crossconnect switches (XCSs), fiber segments, and optical amplifiers, e.g., erbium-doped fiber amplifiers (EDFAs).

Transmission impairments can be categorized into three types: Attenuation, Distortion, and Noise. Noise can be further divided into Thermal Noise, Cross Talk, and Impulse Noise. Network performance can be measured by Bandwidth, which can be expressed in hertz or in bits per second.



#### Switching techniques and multiplexing in Computer Networks

Switching techniques and multiplexing are two important concepts in computer networks. Switching techniques refer to the methods used to connect multiple devices in a network and transfer data between them. Multiplexing, on the other hand, refers to the process of combining multiple signals into a single signal for transmission over a shared medium.

Here is an ASCII diagram that illustrates the concepts of switching techniques and multiplexing in computer networks:

```
+----------------+       +----------------+
|                |       |                |
|   Device 1     |       |   Device 2     |
|                |       |                |
+-------+--------+       +--------+-------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
+-------+--------+       +--------+-------+
|                |       |                |
|   Switch       |       |   Multiplexer  |
|                |       |                |
+-------+--------+       +--------+-------+
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
        |                         |
+-------+--------+       +--------+-------+
|                |       |                |
|   Device 3     |       |   Device 4     |
|                |       |                |
+----------------+       +----------------+
```

In the above diagram, the switch is used to connect multiple devices (Device 1 and Device 3) and transfer data between them. The multiplexer, on the other hand, combines the signals from multiple devices (Device 2 and Device 4) into a single signal for transmission over a shared medium.




## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks

Here is an ASCII diagram that represents the Link layer in Computer Networks and Medium Access Control and Local Area Networks:

```
+---------------------+
|    Application      |
+---------------------+
|    Transport        |
+---------------------+
|    Network          |
+---------------------+
|    Data Link        |
+---------------------+
|    Physical         |
+---------------------+
```

The Data Link layer is responsible for providing a reliable link between two directly connected nodes. It is divided into two sublayers: the Logical Link Control (LLC) and the Medium Access Control (MAC).

The LLC sublayer is responsible for error control, flow control, and framing. The MAC sublayer is responsible for controlling access to the shared medium, such as a LAN.

In a Local Area Network (LAN), the MAC sublayer uses protocols such as Carrier Sense Multiple Access with Collision Detection (CSMA/CD) or Carrier Sense Multiple Access with Collision Avoidance (CSMA/CA) to coordinate access to the shared medium.




#### Link layer in Computer Networks

The link layer is the lowest layer in the OSI model of computer networking. It is responsible for the transmission of data between two directly connected nodes. Here is an ASCII diagram that represents the link layer in a computer network:

```
+----------------+
| Application    |
+----------------+
| Transport      |
+----------------+
| Network        |
+----------------+
| Link           |
+----------------+
| Physical       |
+----------------+
```

The link layer is responsible for providing a reliable link between two directly connected nodes. It does this by using error detection and correction techniques to ensure that data is transmitted without errors. The link layer also provides flow control to prevent one node from overwhelming the other with data.




#### Framing in link layer in Computer Networks

Framing is the process of encapsulating data into a frame for transmission over a link layer in computer networks. The frame includes the data, as well as control information such as the source and destination addresses, error detection and correction codes, and other information necessary for the transmission and reception of the data.

Here is an ASCII diagram of a typical frame in the link layer of a computer network:

```
+-----------------+-----------------+-----------------+-----------------+
|  Preamble  |  Destination  |  Source  |  Type  |  Data  |  CRC  |
+-----------------+-----------------+-----------------+-----------------+
```

The preamble is a sequence of bits used to synchronize the receiver's clock with the sender's clock. The destination and source fields contain the addresses of the destination and source nodes, respectively. The type field indicates the type of data contained in the frame. The data field contains the actual data being transmitted. The CRC (Cyclic Redundancy Check) field contains an error-detecting code used to detect errors in the transmission of the frame.




#### Error Detection and Correction in link layer in Computer Networks

```
+---------------------+
|                     |
|    Data Link Layer  |
|                     |
+----------+----------+
           |
           |
           v
+---------------------+
|                     |
|   Error Detection   |
|                     |
+----------+----------+
           |
           |
           v
+---------------------+
|                     |
|   Error Correction  |
|                     |
+---------------------+
```

The data link layer is responsible for error detection and correction in computer networks. When data is transmitted over a network, it is possible for errors to occur due to various reasons such as noise, interference, or signal attenuation. The data link layer detects these errors using techniques such as parity checking, checksum, or cyclic redundancy check (CRC). Once an error is detected, the data link layer can correct it using techniques such as retransmission, forward error correction, or error-correcting codes. This ensures that the data received at the destination is error-free and can be processed correctly.



#### Flow control in link layer in Computer Networks

Flow control in the link layer is the process of managing the rate of data transmission between two nodes to prevent a fast sender from overwhelming a slow receiver. Here is an ASCII diagram that illustrates the concept of flow control in the link layer:

```
Sender                           Receiver
+----------------+               +----------------+
|                |               |                |
|  Data to send  |               |  Receive buffer|
|                |               |                |
+-------+--------+               +-------+--------+
        |                                |
        |                                |
        |                                |
        |       +----------------+       |
        +------>|                |<------+
                |  Link layer    |
                |                |
                +----------------+
```

In this diagram, the sender has data to send to the receiver. The link layer is responsible for transmitting the data from the sender to the receiver. The receiver has a receive buffer to store the incoming data. Flow control is used to ensure that the sender does not send data at a rate faster than the receiver can handle. This is achieved by using various flow control techniques such as buffering, congestion control, and windowing.




#### Elementary Data Link Protocols in link layer in Computer Networks

The data link layer is responsible for providing reliable data transfer between two adjacent nodes in a computer network. This layer performs basic functions such as framing, error control, and flow control .

Elementary data link layer protocols are divided into three different subcategories :

1. **Unrestricted Simplex Protocol**: This protocol is used for one-way communication where the sender sends data continuously without waiting for any acknowledgment from the receiver .
2. **Simplex Stop and Wait Protocol**: This protocol is used for two-way communication where the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame .
3. **Simplex Protocol for Noisy Channels**: This protocol is used for communication over noisy channels where errors are likely to occur. It includes error detection and correction mechanisms to ensure reliable data transfer .

Some examples of data link layer protocols include Synchronous Data Link Protocol (SDLC), High-Level Data Link Protocol (HDLC), Serial Line Interface Protocol (SLIP), Point-to-Point Protocol (PPP), Link Control Protocol (LCP), Link Access Procedure (LAP), and Network Control Protocol (NCP) .



#### Sliding Window protocols in link layer in Computer Networks

- The sliding window protocol is a data link layer protocol that is useful in the sequential and reliable delivery of the data frames.
- Using the sliding window protocol, the sender can send multiple frames at a time.
- When the receiver receives the frame, it sends back an ACK (acknowledgment) to the sender.
- The sliding window protocol uses a mechanism of sequence numbers.
- The sliding window is also used in Transmission Control Protocol.
- In this protocol, multiple frames can be sent by a sender at a time before receiving an acknowledgment from the receiver.
- The sliding window (windowing) technique is used by Transmission Control Protocol (TCP) to manage the flow of packets between two computers or network hosts.
- TCP is a core component of the Internet Protocol suite and operates at the transport layer.
- It controls the data packets between the two devices where reliable and gradual delivery of data frames is needed.
- It is also used in TCP (Transmission Control Protocol).



#### Medium Access Control and Local Area Networks

Here is an ASCII diagram that illustrates the relationship between Medium Access Control (MAC) and Local Area Networks (LANs):

```
+----------------+
|                |
|     LANs       |
|                |
+-------+--------+
        |
        |
        |
+-------+--------+
|                |
|      MAC       |
|                |
+----------------+
```

In this diagram, the box labeled "LANs" represents Local Area Networks, which are computer networks that span a relatively small area, such as a single building or group of buildings. The box labeled "MAC" represents Medium Access Control, which is a sublayer of the Data Link Layer in the OSI model. The MAC sublayer is responsible for controlling how devices in a network gain access to a shared medium, such as a cable or wireless channel, in order to transmit data.

The arrow between the two boxes indicates that MAC is a component of LANs, as it is responsible for managing access to the shared medium within a LAN. In other words, MAC is a crucial part of the functioning of a LAN, as it ensures that data transmissions within the network are orderly and efficient.




#### Channel allocation in medium access control

```
+------------------------+
|                        |
|   Channel Allocation   |
|                        |
+------------------------+
           |
           |
           |
+------------------------+
|                        |
|   Medium Access        |
|   Control              |
|                        |
+------------------------+
```




#### Multiple access protocols in medium access control

```
+------------------------------------------------+
|                                                |
|  Multiple Access Protocols                     |
|                                                |
|  +----------------+  +----------------+       |
|  |                |  |                |       |
|  |  1. FDMA       |  |  4. CDMA       |       |
|  |                |  |                |       |
|  +----------------+  +----------------+       |
|                                                |
|  +----------------+  +----------------+       |
|  |                |  |                |       |
|  |  2. TDMA       |  |  5. SDMA       |       |
|  |                |  |                |       |
|  +----------------+  +----------------+       |
|                                                |
|  +----------------+  +----------------+       |
|  |                |  |                |       |
|  |  3. OFDMA      |  |  6. Others     |       |
|  |                |  |                |       |
|  +----------------+  +----------------+       |
|                                                |
+------------------------------------------------+
```




#### LAN standards in local area network
```
+----------------+----------------+----------------+
|   Standard     |  Data Rates    |  Media         |
+----------------+----------------+----------------+
|  Ethernet      |  10 Mbps       |  Coaxial cable |
|                |                |  Twisted pair  |
|                |                |  Fiber optic   |
+----------------+----------------+----------------+
|  Fast Ethernet |  100 Mbps      |  Twisted pair  |
|                |                |  Fiber optic   |
+----------------+----------------+----------------+
|  Gigabit       |  1 Gbps        |  Twisted pair  |
|  Ethernet      |                |  Fiber optic   |
+----------------+----------------+----------------+
|  10 Gigabit    |  10 Gbps       |  Twisted pair  |
|  Ethernet      |                |  Fiber optic   |
+----------------+----------------+----------------+
```



#### Link layer switches & bridges in local area network

```
+------------+       +------------+
|            |       |            |
|   Host A   |       |   Host B   |
|            |       |            |
+------------+       +------------+
      |                    |
      |                    |
+------------+       +------------+
|            |       |            |
|   Switch   |-------|   Bridge   |
|            |       |            |
+------------+       +------------+
      |                    |
      |                    |
+------------+       +------------+
|            |       |            |
|   Host C   |       |   Host D   |
|            |       |            |
+------------+       +------------+
```




#### Learning Bridge Algorithms in Local Area Network

Here is an ASCII diagram that illustrates the process of learning bridge algorithms in a local area network:

```
+------------+       +------------+
|            |       |            |
|   Host A   |       |   Host B   |
|            |       |            |
+------+-----+       +------+-----+
       |                    |
       |                    |
       |                    |
       |                    |
       |                    |
+------+-----+       +------+-----+
|            |       |            |
|   Bridge   |       |   Bridge   |
|            |       |            |
+------------+       +------------+
       |                    |
       |                    |
       |                    |
       |                    |
       |                    |
+------+-----+       +------+-----+
|            |       |            |
|   Host C   |       |   Host D   |
|            |       |            |
+------------+       +------------+
```




#### Spanning Tree Algorithms in Local Area Network

Here is an ASCII diagram that illustrates the concept of Spanning Tree Algorithms in a Local Area Network:

```
+--------+     +--------+
| Switch |-----| Switch |
+--------+     +--------+
   |   |         |   |
   |   |         |   |
+----+ +----+ +----+ +----+
| PC | | PC | | PC | | PC |
+----+ +----+ +----+ +----+
```

In this diagram, there are two switches connected to each other, and each switch is connected to two PCs. The Spanning Tree Algorithm is used to prevent loops in the network by disabling redundant links. In this case, one of the links between the two switches would be disabled to prevent a loop.




## Unit 3 - Network Layer in Computer Networks

Here is an ASCII diagram of the Network Layer in Computer Networks:

```
+----------------+
| Application    |
+----------------+
| Transport      |
+----------------+
| Network        |
+----------------+
| Data Link      |
+----------------+
| Physical       |
+----------------+
```

The Network Layer is responsible for routing data packets from the source to the destination. It is the third layer in the OSI model and is responsible for logical addressing, routing, and forwarding of data packets. The Network Layer uses protocols such as IP (Internet Protocol) to perform its functions.




### Point-to-point networks in network layer

A point-to-point network is a type of network topology in which each pair of nodes is connected by a dedicated communication link. In the network layer, this type of network can be used to establish a direct connection between two devices, allowing them to communicate with each other without the need for intermediate devices.

Here is an ASCII diagram that illustrates a point-to-point network in the network layer:

```
+--------+             +--------+
|        |             |        |
| Device |-------------| Device |
|   A    |             |   B    |
|        |             |        |
+--------+             +--------+
```

In this diagram, Device A and Device B are connected by a dedicated communication link, allowing them to communicate directly with each other. This type of network is commonly used in situations where a direct connection between two devices is necessary, such as in a long-distance telephone call or a remote access connection.




### Logical addressing in network layer

Logical addressing is used to provide a universal addressing scheme for identifying hosts on a network. The network layer uses logical addresses to identify the source and destination hosts in a packet. These addresses are used by routers to forward packets to their destination.

Here is an ASCII diagram that illustrates the concept of logical addressing in the network layer:

```
+------------+       +------------+
|            |       |            |
|   Host A   |       |   Host B   |
|            |       |            |
+-----+------+       +------+-----+
      |                     |
      |                     |
+-----+------+       +------+-----+
|            |       |            |
|   Router   |       |   Router   |
|            |       |            |
+------------+       +------------+
```

In this diagram, Host A and Host B are two devices on a network. Each host has a unique logical address assigned to it. When Host A wants to send a packet to Host B, it includes the logical address of Host B in the packet. The packet is then sent to the nearest router, which uses the logical address to determine the next hop for the packet. The packet is forwarded from router to router until it reaches the router connected to Host B. The router then delivers the packet to Host B using its logical address.




### Basic internetworking in network layer

Here is an ASCII diagram that illustrates basic internetworking in the network layer:

```
+--------+       +--------+
|        |       |        |
| Host A +-------+ Router +-------+ Host B |
|        |       |        |       |        |
+--------+       +--------+       +--------+
```

In this diagram, Host A and Host B are connected to a router. The router is responsible for forwarding packets between the two hosts. The network layer is responsible for providing logical addressing and routing services to enable internetworking.




#### IP

IP stands for Internet Protocol. It is a set of rules that govern how data is transmitted over the internet. The IP protocol is responsible for routing data packets from the source to the destination, based on the IP addresses of the devices involved.

Some key points to remember about IP are:

- IP is a connectionless protocol, meaning that it does not establish a dedicated end-to-end connection before transmitting data.
- IP is responsible for routing data packets across the internet, based on the destination IP address.
- IP addresses are unique numerical identifiers assigned to devices connected to the internet.
- The current version of IP is IPv4, but a newer version, IPv6, is being gradually adopted to address the shortage of available IPv4 addresses.
- IP is the primary protocol in the internet layer of the internet protocol suite, which also includes other protocols such as ICMP and IGMP.




#### CIDR
Classless Inter-Domain Routing (CIDR) is a method for allocating IP addresses and routing Internet Protocol packets. Here is an ASCII diagram that illustrates the concept of CIDR notation:

```
  192.168.100.14/24
  |__________| |__|
       |        |
       |        |
 IP Address   Prefix Length
```

In this example, the IP address is `192.168.100.14` and the prefix length is `24`. The prefix length specifies how many of the leftmost contiguous bits of the address comprise the network portion of the address. In this case, the first 24 bits of the IP address are the network portion, and the remaining 8 bits are the host portion. This means that all IP addresses in the range `192.168.100.0` to `192.168.100.255` are in the same network.




#### ARP
Here is an ASCII diagram of the Address Resolution Protocol (ARP):

```
Sender                        Network                      Receiver
+------+                      +------+                      +------+
|      |  ARP Request         |      |                      |      |
|      |--------------------->|      |                      |      |
|      |                      |      |                      |      |
+------+                      +------+                      +------+
                               |      |
                               |      |
                               |      |
                               |      |
                               v      v
+------+                      +------+                      +------+
|      |                      |      |                      |      |
|      |                      |      |  ARP Reply           |      |
|      |                      |      |<---------------------|      |
+------+                      +------+                      +------+
```

In this diagram, the sender sends an ARP request to the network, asking for the MAC address of the receiver. The network then forwards the request to the receiver. The receiver then sends an ARP reply back to the network, which forwards it to the sender. The sender can then use the MAC address of the receiver to send data directly to it.




#### RARP
- RARP stands for Reverse Address Resolution Protocol.
- It is a protocol based on computer networking.
- It is employed by a client computer to request its IP address from a gateway server’s Address Resolution Protocol table or cache .
- The network administrator creates a table in gateway-router, which is used to map the MAC address to its corresponding IP address .
- RARP is a protocol a physical machine in a local area network (LAN) can use to request its IP address .
- It does this by sending the device's physical address to a specialized RARP server that is on the same LAN and is actively listening for RARP requests .
- The RARP is a protocol which was published in 1984 and was included in the TCP/IP protocol stack .
- The RARP is on the Network Access Layer (i.e. the lowest layer of the TCP/IP protocol stack) and is thus a protocol used to send data between two points in a network .



#### DHCP
```
DHCP (Dynamic Host Configuration Protocol) is a protocol used to automatically assign IP addresses to devices on a network.

Here is an ASCII diagram of the DHCP process:

Client                            DHCP Server
   |                                   |
   |-------DHCPDISCOVER-------------->|
   |                                   |
   |<------DHCPOFFER------------------|
   |                                   |
   |-------DHCPREQUEST--------------->|
   |                                   |
   |<------DHCPACK--------------------|
   |                                   |
   |-------DHCPINFORM---------------->|
   |                                   |
   |<------DHCPACK--------------------|
   |                                   |
```
The DHCP process involves the following steps:
1. The client sends a broadcast message (DHCPDISCOVER) to discover available DHCP servers.
2. The DHCP server responds with a message (DHCPOFFER) containing an IP address offer.
3. The client sends a message (DHCPREQUEST) to request the offered IP address.
4. The DHCP server sends a message (DHCPACK) to acknowledge the request and assign the IP address to the client.
5. The client sends a message (DHCPINFORM) to request additional configuration information.
6. The DHCP server sends a message (DHCPACK) to acknowledge the request and provide the requested information.




#### ICMP
- ICMP stands for Internet Control Message Protocol.
- It is a network layer protocol used by network devices to send error messages and operational information.
- ICMP is mainly used to report error conditions and diagnose network issues.
- ICMP messages are typically generated by network devices, such as routers, to indicate errors or provide other information about the network.
- ICMP messages are encapsulated within IP datagrams and are therefore transmitted using the IP protocol.
- Some common ICMP message types include:
  - Destination Unreachable: sent by a router to indicate that a destination host or network is unreachable.
  - Echo Request and Echo Reply (Ping): used to test the reachability of a host on an IP network.
  - Time Exceeded: sent by a router to indicate that a datagram has been discarded because its time to live (TTL) value has reached zero.
  - Redirect: sent by a router to inform a host to send its traffic through a different router to reach a specific destination.



### Routing in network layer

```
+--------+       +--------+       +--------+
|        |       |        |       |        |
| Router |-------| Router |-------| Router |
|   A    |       |   B    |       |   C    |
|        |       |        |       |        |
+--------+       +--------+       +--------+
   |  |             |  |             |  |
   |  |             |  |             |  |
+----+----+     +----+----+     +----+----+
|         |     |         |     |         |
| Network |     | Network |     | Network |
|    1    |     |    2    |     |    3    |
|         |     |         |     |         |
+---------+     +---------+     +---------+
```

In the network layer, routers are responsible for routing packets from one network to another. In the diagram above, there are three routers, A, B, and C, connected to each other. Each router is also connected to a network, 1, 2, and 3 respectively. When a packet is sent from a device in network 1 to a device in network 3, the packet will first be sent to router A. Router A will then forward the packet to router B, which will then forward the packet to router C. Finally, router C will forward the packet to the destination device in network 3. This process is known as routing.



### Forwarding and Delivery in Network Layer

```
+----------------+      +----------------+
|                |      |                |
|   Router 1     |      |   Router 2     |
|                |      |                |
+-------+--------+      +--------+-------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
+-------+--------+      +--------+-------+
|                |      |                |
|   Router 3     |      |   Router 4     |
|                |      |                |
+----------------+      +----------------+
```

In the network layer, forwarding and delivery refer to the process of moving data packets from one network node to another. In the diagram above, the data packets would be forwarded from Router 1 to Router 3 or Router 4, depending on the destination address of the packet. The same process would occur between Router 2 and Router 3 or Router 4. This process is repeated until the data packet reaches its final destination.




### Static and dynamic routing in cn

Static routing is a type of routing that is manually configured by a network administrator. In static routing, the administrator manually enters the routes and their corresponding network addresses into the routing table. This type of routing is best suited for small networks where the network administrator has a good understanding of the network topology and the traffic patterns.

Dynamic routing, on the other hand, is a type of routing that is automatically configured by routing protocols. In dynamic routing, the routing protocols automatically discover the network topology and the best routes to reach a destination. This type of routing is best suited for large networks where the network topology and the traffic patterns are constantly changing.

Here is an ASCII diagram that illustrates the difference between static and dynamic routing:

```
+------------+                       +------------+
|            |                       |            |
|  Router A  |                       |  Router B  |
|            |                       |            |
+------+-----+                       +------+-----+
       |                                    |
       |                                    |
       |                                    |
       |                                    |
       |                                    |
       |                                    |
+------+-----+                       +------+-----+
|            |                       |            |
|  Router C  |                       |  Router D  |
|            |                       |            |
+------------+                       +------------+

Static Routing:
- Router A has a manually configured route to reach Router D via Router C
- Router B has a manually configured route to reach Router C via Router D

Dynamic Routing:
- Router A and Router B automatically discover the best route to reach each other via Router C or Router D
```



### Routing algorithms and protocols in cn

Here is an ASCII diagram that illustrates the concept of routing algorithms and protocols in computer networks:

```
+------------+       +------------+
|            |       |            |
|   Router   |-------|   Router   |
|            |       |            |
+------------+       +------------+
       |                   |
       |                   |
+------------+       +------------+
|            |       |            |
|   Router   |-------|   Router   |
|            |       |            |
+------------+       +------------+
```




### Congestion Control Algorithms in Computer Networks

Congestion control is a mechanism that controls the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse. Congestive-Avoidance Algorithms (CAA) are implemented at the TCP layer as the mechanism to avoid congestive collapse in a network.

There are two congestion control algorithms which are as follows:

1. **Leaky Bucket Algorithm**: The leaky bucket algorithm discovers its use in the context of network traffic shaping or rate-limiting. A leaky bucket execution and a token bucket execution are predominantly used for traffic shaping algorithms. This algorithm is used to control the rate at which data packets are sent into the network.

2. **Open Loop Congestion Control**: Open loop congestion control policies are applied to prevent congestion before it happens.

Congestion control algorithms use packet losses and delays as signals to infer congestion and decide how fast to send data. But the internet is complicated, and packets can be delayed and lost for reasons unrelated to network congestion.



Here is a detailed ASCII diagram for IPv6 in computer networks:

### IPv6 in CN
```
  +----------------+
  |  Version (4)   |
  +----------------+
  | Traffic Class  |
  |     (8)        |
  +----------------+
  |  Flow Label    |
  |     (20)       |
  +----------------+
  |  Payload       |
  |  Length (16)   |
  +----------------+
  |  Next Header   |
  |     (8)        |
  +----------------+
  |  Hop Limit     |
  |     (8)        |
  +----------------+
  |  Source        |
  |  Address (128) |
  +----------------+
  |  Destination   |
  |  Address (128) |
  +----------------+
```

This diagram shows the structure of an IPv6 packet header. The numbers in parentheses indicate the number of bits used for each field. The Version field is 4 bits long and indicates the version of the Internet Protocol being used. The Traffic Class field is 8 bits long and is used to differentiate between different classes of traffic. The Flow Label field is 20 bits long and is used to identify a specific flow of data. The Payload Length field is 16 bits long and indicates the length of the payload in octets. The Next Header field is 8 bits long and indicates the type of header that follows the IPv6 header. The Hop Limit field is 8 bits long and is used to limit the number of hops a packet can make before being discarded. The Source Address and Destination Address fields are each 128 bits long and contain the IPv6 addresses of the source and destination of the packet, respectively.




## Unit 4 - Transport Layer in Computer Networks

Here is an ASCII diagram of the Transport Layer in Computer Networks:

```
+---------------------+
|    Application      |
+---------------------+
|    Transport        |
+---------------------+
|    Network          |
+---------------------+
|    Data Link        |
+---------------------+
|    Physical         |
+---------------------+
```

The Transport Layer is responsible for providing end-to-end communication services for applications. It provides logical communication between application processes running on different hosts. Some of the key functions of the Transport Layer include:

- Connection-oriented communication
- Reliable data transfer
- Flow control
- Congestion control
- Multiplexing




### Process-to-process delivery in transport layer

```
+---------------------+
| Application Layer   |
+---------------------+
          |
          |
          V
+---------------------+
| Transport Layer     |
+---------------------+
|                     |
|  +---------------+  |
|  |    Process    |  |
|  |   Multiplexing|  |
|  +---------------+  |
|                     |
|  +---------------+  |
|  |   Flow and    |  |
|  | Congestion    |  |
|  |   Control     |  |
|  +---------------+  |
|                     |
|  +---------------+  |
|  |   Error       |  |
|  |   Control     |  |
|  +---------------+  |
|                     |
+---------------------+
          |
          |
          V
+---------------------+
| Network Layer       |
+---------------------+
```

The transport layer is responsible for process-to-process delivery of the entire message. It provides services such as connection-oriented data transfer, reliability, flow control, and multiplexing. The transport layer ensures that the whole message arrives intact and in order, overseeing both error control and flow control at the source-to-destination level. It also provides the acknowledgment of the successful data transmission and sends the next data if no errors occurred. The transport layer creates segments out of the message received from the application layer. Segmentation is the process of dividing a long message into smaller messages. These smaller messages are easier to transmit and manage. The transport layer header is then added to each segment, and the resulting segment is passed to the network layer. The transport layer header contains the source and destination port numbers, which are used for multiplexing and demultiplexing data from multiple applications. The transport layer is also responsible for flow control and congestion control. Flow control is the process of adjusting the rate of data transmission between two nodes based on the network's capacity. Congestion control is the process of preventing network congestion by reducing the rate of data transmission when the network is congested. The transport layer can use various mechanisms to control the flow of data and prevent congestion, such as sliding window protocols and congestion avoidance algorithms. The transport layer also provides error control by detecting and correcting errors that may occur during transmission. Error control mechanisms include checksums, acknowledgments, and retransmissions. If an error is detected, the transport layer can request that the data be retransmitted. The transport layer is responsible for ensuring that the data is delivered correctly and in the correct order. It provides a reliable, process-to-process communication service between applications running on different hosts. The transport layer is a crucial component of the OSI model, providing the necessary services for end-to-end communication between applications.



### Transport layer protocols

The transport layer is responsible for providing end-to-end communication services for applications. It provides services such as connection-oriented data stream support, reliability, flow control, and multiplexing. The two most common transport layer protocols are the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP).

Here is an ASCII diagram that illustrates the relationship between the transport layer and other layers in the OSI model:

```
+---------------------+
|    Application      |
+---------------------+
|    Presentation     |
+---------------------+
|       Session       |
+---------------------+
|      Transport      |
+---------------------+
|       Network       |
+---------------------+
|       Data Link     |
+---------------------+
|       Physical      |
+---------------------+
```

In this diagram, the transport layer is shown as the fourth layer from the top, sitting between the session layer and the network layer. The transport layer is responsible for taking data from the session layer, segmenting it into smaller units, and passing it down to the network layer for transmission across the network. At the receiving end, the transport layer reassembles the data and passes it up to the session layer.




#### UDP Transport layer protocol

Here is an ASCII diagram of the UDP Transport layer protocol:

```
+---------------------+
|      IP Header      |
+---------------------+
|     UDP Header      |
+---------------------+
|                     |
|     Data Payload    |
|                     |
+---------------------+
```

The UDP Header consists of four fields: Source Port, Destination Port, Length, and Checksum. Each field is 16 bits in size.

```
+----------------+----------------+
|  Source Port   | Destination Port|
+----------------+----------------+
|     Length     |    Checksum     |
+----------------+----------------+
```




#### TCP Transport layer protocol

```
  +---------------------+
  |  Application Layer  |
  +---------------------+
           |
           |
           V
  +---------------------+
  |    Transport Layer  |
  +---------------------+
  |                     |
  |    +----------+     |
  |    |   TCP    |     |
  |    +----------+     |
  |                     |
  +---------------------+
           |
           |
           V
  +---------------------+
  |   Network Layer     |
  +---------------------+
           |
           |
           V
  +---------------------+
  |   Data Link Layer   |
  +---------------------+
           |
           |
           V
  +---------------------+
  |   Physical Layer    |
  +---------------------+
```

TCP (Transmission Control Protocol) is one of the main protocols in the Transport Layer of the OSI model. It provides reliable, ordered, and error-checked delivery of a stream of octets (bytes) between applications running on hosts communicating via an IP network. Major internet applications such as the World Wide Web, email, remote administration, and file transfer rely on TCP.



### Multiplexing in transport layer
```
+---------------------+
|   Application       |
+---------------------+
|   Transport         |
+---------------------+
|   Network           |
+---------------------+
|   Data Link         |
+---------------------+
|   Physical          |
+---------------------+

```
In the transport layer, multiplexing is the process of combining multiple application-layer data streams into a single transport-layer data stream. This is done by assigning each application-layer data stream a unique identifier, called a port number. The transport layer then uses these port numbers to direct incoming data to the correct application.

Here is an example of how multiplexing works in the transport layer:

```
+---------------------+
|   Application       |
+----------+----------+
|   HTTP   |   FTP    |
+----------+----------+
|   Port 80|   Port 21|
+----------+----------+
|   Transport         |
+---------------------+
|   Network           |
+---------------------+
|   Data Link         |
+---------------------+
|   Physical          |
+---------------------+

```
In this example, the HTTP application is assigned port 80 and the FTP application is assigned port 21. When data is sent from the HTTP application, it is sent to the transport layer with the port number 80. The transport layer then uses this port number to direct the data to the correct application when it is received on the other end. Similarly, data sent from the FTP application is sent with the port number 21 and is directed to the correct application when it is received.




### Connection management in transport layer

Connection management in the transport layer involves establishing, maintaining, and terminating a connection between two endpoints. Here is an ASCII diagram that illustrates the process of connection management in the transport layer using the example of the TCP protocol:

```
    Endpoint A                                      Endpoint B
    (Client)                                        (Server)

    CLOSED                                          LISTEN

    SYN_SENT  ------ SYN ------->                   SYN_RCVD

    ESTABLISHED  <---- SYN/ACK ----                 ESTABLISHED

    ESTABLISHED  ------ ACK ------->                ESTABLISHED

    (Data transfer)

    FIN_WAIT_1  ------ FIN ------->                 CLOSE_WAIT

    FIN_WAIT_2  <---- ACK --------                  LAST_ACK

    TIME_WAIT   <---- FIN --------                  CLOSED

    CLOSED      ------ ACK ------->
```

In this diagram, Endpoint A (the client) initiates a connection to Endpoint B (the server) by sending a SYN (synchronize) packet. Endpoint B responds with a SYN/ACK (synchronize/acknowledge) packet, and Endpoint A sends an ACK (acknowledge) packet to confirm the establishment of the connection. Data transfer can then take place between the two endpoints. When the data transfer is complete, Endpoint A initiates the termination of the connection by sending a FIN (finish) packet. Endpoint B responds with an ACK packet and sends its own FIN packet. Endpoint A sends a final ACK packet to confirm the termination of the connection, and both endpoints return to the CLOSED state.




### Flow control in transport layer

Flow control is a mechanism used in the transport layer of the TCP/IP model to manage the rate of data transmission between two nodes. It is necessary to prevent a fast sender from transmitting more data than can be supported by the receiving data buffer, causing a buffer overrun. This can also be used to improve efficiency by reducing buffer underrun.

The transport layer provides a flow control mechanism between the adjacent layers of the TCP/IP model. TCP also prevents data loss due to a fast sender and slow receiver by imposing some flow control techniques .

Flow control in the transport layer ensures the delivery of the message globally, as the two points of connection over this protocol are logically connected. Whereas in the data-link layer, the concern is to deliver the message locally, as the two points of connection over this protocol are physically connected.



### etransmission in transport layer

```
+---------------------+
|                     |
|    Application      |
|                     |
+---------------------+
          |
          |
          V
+---------------------+
|                     |
|     Transport       |
|                     |
+---------------------+
          |
          |
          V
+---------------------+
|                     |
|    etransmission    |
|                     |
+---------------------+
          |
          |
          V
+---------------------+
|                     |
|      Network        |
|                     |
+---------------------+
          |
          |
          V
+---------------------+
|                     |
|      Data Link      |
|                     |
+---------------------+
          |
          |
          V
+---------------------+
|                     |
|      Physical       |
|                     |
+---------------------+
```




### Window management in transport layer

- The sliding window technique is used by Transmission Control Protocol (TCP) to manage the flow of packets between two computers or network hosts .
- TCP is a core component of the Internet Protocol suite and operates at the transport layer .
- The transport layer is at the lowest level of the channel stack .
- The main transports used in Windows Communication Foundation (WCF) are HTTP, HTTPS, TCP, and named pipes .
- Flow control is performed end to end rather than across a single link .
- Transport layer flow control uses a sliding window protocol .
- The window at the transport layer can vary in size to accommodate buffer occupancy .




### TCP Congestion control in transport layer

Here is an ASCII diagram that illustrates the TCP Congestion control in the transport layer:

```
          +------------+
          | Application|
          +------+-----+
                 |
          +------+-----+
          |   Transport|
          |  +-------+ |
          |  |  TCP  | |
          |  +---+---+ |
          |      |     |
          |Congestion  |
          | Control    |
          +------+-----+
                 |
          +------+-----+
          |   Network  |
          +------+-----+
                 |
          +------+-----+
          | Data Link  |
          +------+-----+
                 |
          +------+-----+
          |  Physical  |
          +------------+
```

TCP congestion control is a mechanism used by the transport layer to control the flow of data in a network. It aims to prevent network congestion by regulating the amount of data that can be sent at any given time. This is achieved by adjusting the size of the congestion window, which determines the maximum amount of data that can be sent before receiving an acknowledgment from the receiver. The size of the congestion window is adjusted based on network conditions, such as packet loss or delay, to ensure that the network is not overwhelmed with traffic.




### Quality of service in transport layer

```
+---------------------+
|   Application       |
+---------------------+
|   Transport         |
+---------------------+
|   Network           |
+---------------------+
|   Data Link         |
+---------------------+
|   Physical          |
+---------------------+

```

Quality of service (QoS) in the transport layer refers to the ability of the transport layer to provide different levels of service to different applications or data flows. This is achieved through mechanisms such as traffic classification, traffic shaping, and traffic policing. These mechanisms allow the transport layer to prioritize certain types of traffic over others, ensuring that high-priority traffic receives the necessary bandwidth and low latency, while lower-priority traffic may be subject to delays or dropped packets.



## Unit 5 - Application Layer in Computer Networks

The Application Layer is the topmost layer in the OSI model of computer networks. It provides services to the user, such as email, file transfer, and web browsing. Here is an ASCII diagram that illustrates the Application Layer in relation to the other layers in the OSI model:

```
+----------------+
| Application    |
+----------------+
| Presentation   |
+----------------+
| Session        |
+----------------+
| Transport      |
+----------------+
| Network        |
+----------------+
| Data Link      |
+----------------+
| Physical       |
+----------------+
```

The Application Layer interacts with the Presentation Layer, which is responsible for data representation and encryption. The Session Layer manages the communication session between two devices. The Transport Layer provides end-to-end communication and error control. The Network Layer is responsible for routing data packets. The Data Link Layer provides error-free transmission of data frames. The Physical Layer is responsible for transmitting bits over a physical medium.




Here is an ASCII diagram for the World Wide Web:

### World Wide Web
```
+----------------+
|                |
|    Browser     |
|                |
+-------+--------+
        |
        |
        v
+-------+--------+
|                |
|     Server     |
|                |
+-------+--------+
        |
        |
        v
+-------+--------+
|                |
|      HTML      |
|                |
+-------+--------+
        |
        |
        v
+-------+--------+
|                |
|      CSS       |
|                |
+-------+--------+
        |
        |
        v
+-------+--------+
|                |
|     JavaScript |
|                |
+----------------+
```



### Hyper Text Transfer Protocol

Hyper Text Transfer Protocol (HTTP) is an application layer protocol used for transmitting data over the internet. It is a request-response protocol between a client and a server. Here is an ASCII diagram that illustrates the basic flow of HTTP:

```
    +--------+                                   +--------+
    |        |                                   |        |
    | Client |                                   | Server |
    |        |                                   |        |
    +----+---+                                   +---+----+
         |                                           |
         | 1. Request (GET /index.html HTTP/1.1)     |
         |------------------------------------------>|
         |                                           |
         | 2. Response (HTTP/1.1 200 OK)             |
         |<------------------------------------------|
         |                                           |
         | 3. Response body (HTML, CSS, JS, etc.)    |
         |<------------------------------------------|
         |                                           |
    +----+---+                                   +---+----+
    |        |                                   |        |
    | Client |                                   | Server |
    |        |                                   |        |
    +--------+                                   +--------+
```

In this diagram, the client sends an HTTP request to the server, asking for the `index.html` page. The server responds with an HTTP response, indicating that the request was successful (`200 OK`). The server then sends the response body, which contains the requested data (in this case, the HTML, CSS, and JS files for the `index.html` page). The client receives the response and can then render the page for the user to view.




### Electronic mail in application layer

Electronic mail (email) is a method of exchanging messages between people using electronic devices. Email operates across computer networks, primarily the Internet. In the application layer of the OSI model, email is one of the protocols used for communication.

Here is an ASCII diagram that illustrates the process of sending an email from the sender to the recipient through the application layer:

```
Sender's device                      Email server                      Recipient's device
+----------------+                   +------------+                   +-----------------+
|                |   SMTP request    |            |   SMTP delivery   |                 |
|  Email client  |------------------>|            |------------------>|   Email client  |
|                |                   |            |                   |                 |
+----------------+                   +------------+                   +-----------------+
```

In this diagram, the sender composes an email using an email client on their device. The email client sends the email to the email server using the Simple Mail Transfer Protocol (SMTP). The email server then delivers the email to the recipient's email client, also using SMTP.




### File Transfer Protocol in application layer

```
+---------------------+
|  Application Layer  |
+---------------------+
|                     |
|  +---------------+  |
|  |      FTP      |  |
|  +---------------+  |
|                     |
+---------------------+
|  Transport Layer    |
+---------------------+
|  Internet Layer     |
+---------------------+
|  Link Layer         |
+---------------------+
```

File Transfer Protocol (FTP) is an application layer protocol used for transferring files between network hosts. FTP uses a client-server architecture, where the client initiates a connection to the server to request a file transfer. FTP uses the Transmission Control Protocol (TCP) in the transport layer to establish a reliable connection between the client and server and to transfer data.




### Remote Login in Application Layer

Remote login is a process that allows a user to log into a computer or network from a remote location. This is typically done using a protocol such as Telnet or Secure Shell (SSH) that operates at the application layer of the OSI model.

Some key points to consider when discussing remote login in the application layer are:

1. Remote login protocols, such as Telnet and SSH, operate at the application layer of the OSI model.
2. These protocols allow a user to access a computer or network from a remote location.
3. Telnet is an older protocol that is considered less secure than SSH.
4. SSH provides encrypted communication between the client and server, making it a more secure option for remote login.
5. Remote login can be used for a variety of purposes, including system administration, file transfer, and remote command execution.



### Network management in application layer

```
+---------------------+
|                     |
|   Application       |
|   Layer             |
|                     |
+----------+----------+
           |
           |
+----------+----------+
|                     |
|   Network           |
|   Management        |
|                     |
+---------------------+
```




### Data compression in application layer

Data compression in the application layer is the process of encoding information using fewer bits than the original representation. This can be achieved through various algorithms and techniques that reduce the size of the data without losing its meaning. Here is an ASCII diagram that illustrates the process of data compression in the application layer:

```
+---------------------+
|   Application Data  |
+---------------------+
           |
           |
           v
+---------------------+
| Compression Algorithm|
+---------------------+
           |
           |
           v
+---------------------+
| Compressed Data     |
+---------------------+
```

In this diagram, the application data is passed through a compression algorithm, which reduces its size and produces compressed data. This compressed data can then be transmitted or stored more efficiently than the original data. There are many different compression algorithms that can be used, depending on the type of data and the desired level of compression. Some common algorithms include Huffman coding, Lempel-Ziv-Welch (LZW), and Deflate.



### Cryptography in application layer

Cryptography is associated with the process of converting plain text into cipher text, which is unintelligible and vice-versa. It provides secure communication in the presence of adversaries. Encryption is the process of transforming plain text data into encrypted text using an algorithm and a key.

Application layer encryption is a data-security solution that encrypts nearly any type of data passing through an application. When encryption occurs at this level, data is encrypted across multiple (including disk, file, and database) layers . This application layer encryption approach increases security by reducing the number of potential attack vectors.

Application-layer encryption, or shift-left cryptography, is part of this trend. It means giving developers more control over what gets encrypted and who gets the keys for decryption. In some cases, the users themselves may be the only parties with the keys. Application-layer cryptography is part of a trend to move more infrastructure and IT accountabilities into developer or DevOps roles. End-to-end encryption is an increasingly popular type of application-layer cryptography. This type of encryption lets organizations enforce access control using key management as well as policy.

Like in that use case, application layer encryption improves privacy. In some cases, it improves privacy substantially. It's actually significantly harder for developers than just implementing something like HTTPS.



### Basic Concepts of Cryptography in Application Layer

```
+----------------+     +----------------+
|                |     |                |
|   Application  |     |   Application  |
|                |     |                |
+-------+--------+     +--------+-------+
        |                       |
        |                       |
        |                       |
        |                       |
+-------+--------+     +--------+-------+
|                |     |                |
|   Cryptography |     |   Cryptography |
|                |     |                |
+----------------+     +----------------+
```


