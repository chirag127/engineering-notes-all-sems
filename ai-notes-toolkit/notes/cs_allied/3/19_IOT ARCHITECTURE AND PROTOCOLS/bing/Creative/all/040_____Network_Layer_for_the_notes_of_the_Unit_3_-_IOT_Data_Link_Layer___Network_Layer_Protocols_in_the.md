# Network Layer

The network layer is the third layer of the OSI model and the second layer of the TCP/IP model. It is responsible for addressing and routing of data packets in a network. It also provides services such as fragmentation, error detection, congestion control, and security.

## Network Layer Protocols for IoT

The network layer protocols for IoT are designed to meet the specific requirements and challenges of IoT devices, such as low power consumption, limited bandwidth, scalability, mobility, and interoperability. Some of the common network layer protocols for IoT are:

- **IPv6**: IPv6 is the latest version of the Internet Protocol, which provides a larger address space, better security, and more efficient routing than IPv4. IPv6 is essential for IoT, as it can support the massive number of devices and sensors that need to be connected to the internet. IPv6 also enables end-to-end communication, which reduces the need for intermediate devices such as gateways and proxies.
- **6LoWPAN**: 6LoWPAN stands for IPv6 over Low-Power Wireless Personal Area Networks. It is a protocol that adapts IPv6 to the constraints of low-power and low-bandwidth wireless networks, such as ZigBee, Bluetooth Low Energy, and IEEE 802.15.4. 6LoWPAN enables IPv6 packets to be transmitted over these networks by compressing the headers, fragmenting the payloads, and using mesh routing. 6LoWPAN allows IoT devices to communicate directly with the internet, without requiring a gateway or a translation mechanism.
- **RPL**: RPL stands for Routing Protocol for Low-Power and Lossy Networks. It is a protocol that provides efficient and reliable routing for IoT networks that are characterized by high packet loss, low data rates, and dynamic topology. RPL organizes the network into a Destination-Oriented Directed Acyclic Graph (DODAG), where each node has a rank that determines its position and role in the network. RPL supports both upward and downward routing, as well as multicast and anycast communication. RPL also provides mechanisms for loop detection, loop avoidance, and loop repair.
- **CoAP**: CoAP stands for Constrained Application Protocol. It is a protocol that provides a lightweight and RESTful application layer for IoT devices. CoAP is based on the HTTP model, but uses UDP instead of TCP, and employs a binary format instead of text. CoAP supports four methods: GET, PUT, POST, and DELETE, and provides features such as caching, discovery, observation, and block-wise transfer. CoAP enables IoT devices to interact with web services and applications, as well as with each other. CoAP can also be mapped to HTTP, allowing interoperability between the two protocols.

## References

: Network Layer Protocols: IOT Part 8 - Engineers Garage
: IoT Network Layer Protocols - TechVidvan
: Architecture of Internet of Things (IoT) - GeeksforGeeks
: 6 IoT architecture layers and components explained - IoT Agenda
: Trusted Internet of Things (IoT) Device Network-Layer Onboarding and Lifecycle Management - NIST