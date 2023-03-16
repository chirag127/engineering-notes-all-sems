Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information about the network layer for the notes of the Unit 3 - IOT Data Link Layer & Network Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS.

### Network Layer

- The network layer is the third layer of the OSI model and the internet layer of the TCP/IP model.
- The network layer is responsible for addressing and routing of data packets in the internet of things (IoT) network.
- The network layer is divided into two sublayers: the routing layer and the encapsulation layer.
- The routing layer handles the transfer of packets from source to destination, using various routing protocols for low-power and lossy networks (LLNs), such as RPL, 6LoWPAN, and CoAP.
- The encapsulation layer forms the packets by adding headers and trailers to the data, using various encapsulation protocols, such as IPv4, IPv6, and UDP.
- The network layer also provides security and reliability features, such as encryption, authentication, fragmentation, and reassembly of packets.

Some of the main network layer protocols in IoT are:

- RPL: Routing Protocol for Low-Power and Lossy Networks. It is a distance-vector routing protocol that uses a directed acyclic graph (DAG) to establish routes between nodes in an LLN. It supports both IPv4 and IPv6 addressing and can operate over various link-layer technologies, such as IEEE 802.15.4, Bluetooth, and Wi-Fi.
- 6LoWPAN: IPv6 over Low-Power Wireless Personal Area Networks. It is an adaptation layer that enables the transmission of IPv6 packets over IEEE 802.15.4 networks, which have limited bandwidth, memory, and power. It compresses the IPv6 header and fragments the packets to fit the IEEE 802.15.4 frame size.
- CoAP: Constrained Application Protocol. It is an application layer protocol that provides a RESTful web service for resource-constrained devices in an LLN. It uses UDP as the transport layer protocol and supports various features, such as caching, discovery, observation, and multicast.
- IPv4: Internet Protocol version 4. It is the most widely used network layer protocol in the internet. It provides logical addressing and routing of packets across different networks. It uses 32-bit addresses and has a header size of 20 bytes.
- IPv6: Internet Protocol version 6. It is the successor of IPv4 and provides several improvements, such as larger address space, simplified header, stateless address autoconfiguration, and enhanced security. It uses 128-bit addresses and has a header size of 40 bytes.
- UDP: User Datagram Protocol. It is a connectionless and unreliable transport layer protocol that provides fast and efficient data transfer. It adds a 8-byte header to the data and does not perform any error detection, correction, or flow control. It is suitable for real-time and multimedia applications.