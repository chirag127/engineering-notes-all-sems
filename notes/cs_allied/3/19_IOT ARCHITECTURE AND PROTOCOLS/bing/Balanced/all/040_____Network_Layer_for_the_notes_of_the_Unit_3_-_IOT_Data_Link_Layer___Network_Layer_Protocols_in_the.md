# Network Layer

The network layer is the third layer of the OSI model and the second layer of the TCP/IP model. It is responsible for addressing and routing of data packets in a network. It also performs functions such as fragmentation, reassembly, congestion control, and error detection.

## Network Layer in IoT

In the context of IoT, the network layer is part of the infrastructure layer in the IoT reference architecture. It enables communication and connectivity between devices in the IoT system, as well as with the wider internet. The network layer in IoT is mainly divided into two parts:

- The routing layer, which sends packets from origin to destination using various routing protocols and algorithms.
- The encapsulation layer, which creates packets by adding headers and trailers to the datagrams from the transport layer. The headers contain information such as source and destination IP addresses, packet length, and checksum.

## Network Layer Protocols in IoT

There are various protocols that can be used at the network layer in IoT, depending on the requirements and constraints of the application and the network. Some of the common network layer protocols in IoT are :

- IPv4 and IPv6, which are the standard protocols for internet communication. IPv4 uses 32-bit addresses, while IPv6 uses 128-bit addresses, which allows for more scalability and security. IPv6 also supports features such as stateless address autoconfiguration, neighbor discovery, and multicast.
- 6LoWPAN, which stands for IPv6 over Low-Power Wireless Personal Area Networks. It is a protocol that adapts IPv6 to work over low-power and low-bandwidth networks, such as ZigBee, Bluetooth Low Energy, and IEEE 802.15.4. It uses header compression, fragmentation, and reassembly techniques to reduce the overhead of IPv6 packets.
- RPL, which stands for Routing Protocol for Low-Power and Lossy Networks. It is a protocol that provides efficient and reliable routing for IoT networks that have limited resources and high packet loss. It uses a Directed Acyclic Graph (DAG) structure to organize the network topology and supports multiple routing metrics and objectives.
- CoAP, which stands for Constrained Application Protocol. It is a protocol that provides a lightweight and RESTful application layer interface for IoT devices. It uses UDP as the transport protocol and supports features such as caching, discovery, observation, and multicast.