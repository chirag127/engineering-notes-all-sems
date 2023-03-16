### 6TiSCH

6TiSCH is a working group at the IETF, which is standardizing how to combine IEEE 802.15.4e time-slotted channel hopping (TSCH) with IPv6. The result is a solution that offers both industrial performance and seamless integration into the Internet and is therefore seen as a key technology for the Industrial Internet of Things (IIoT) .

Some of the main features and benefits of 6TiSCH are:

- It uses 128-bit IPv6 addresses, which allows for a large number of devices to be uniquely identified and connected to the Internet.
- It uses TSCH, which is a link layer protocol that allows the nodes to change their physical channel after each transmission to eliminate interference and improve reliability .
- It uses a Time Division Multiple Access (TDMA) schedule, which assigns a time slot and a channel to each node for each transmission, ensuring deterministic and bounded latency.
- It uses 6top, which is a sublayer that enables distributed and dynamic scheduling of the TSCH slots and channels, allowing the network to adapt to changing traffic patterns and network conditions.
- It uses 6LoWPAN, which is a protocol that compresses and fragments the IPv6 packets to fit the IEEE 802.15.4 frame size, reducing the overhead and increasing the efficiency.
- It uses IP-in-IP encapsulation, which is a technique that wraps an IPv6 packet inside another IPv6 packet, allowing the network to support multiple routing protocols and address spaces.
- It uses RPL, which is a routing protocol that builds a Directed Acyclic Graph (DAG) topology for the network, optimizing the path selection and the energy consumption.

6TiSCH is a promising technology for the IIoT, as it provides a low-power, high-reliability, and scalable network that can support a variety of applications and services. Some of the challenges and open issues of 6TiSCH are:

- How to design and implement efficient and secure mechanisms for network formation, join, and authentication.
- How to balance the trade-offs between centralized and distributed scheduling, and how to coordinate the 6top operations among the nodes.
- How to ensure interoperability and compatibility among different vendors and devices, and how to test and evaluate the performance and functionality of 6TiSCH networks .
- How to integrate 6TiSCH with other protocols and standards, such as CoAP, MQTT, OPC UA, and IEEE 802.1AS.