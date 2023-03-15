### Basic internetworking in network layer

The network layer is responsible for routing data packets from the source to the destination. It is the third layer of the OSI model and is responsible for logical addressing and routing. The following are some key points to remember about basic internetworking in the network layer:

1. The network layer uses logical addresses, such as IP addresses, to identify devices on the network. These addresses are used to route data packets to their destination.

2. Routers are the primary devices used in the network layer to route data packets between networks. They use routing tables to determine the best path for a packet to take to reach its destination.

3. The network layer is responsible for fragmentation and reassembly of data packets. If a packet is too large to be transmitted over a particular link, it is broken into smaller packets, transmitted, and then reassembled at the destination.

4. The network layer is also responsible for error handling and congestion control. If a packet is lost or corrupted during transmission, the network layer can request that it be retransmitted. It can also implement congestion control mechanisms to prevent network congestion.

5. The Internet Protocol (IP) is the most widely used protocol in the network layer. It is responsible for routing data packets across the Internet.

6. There are two versions of IP in use today: IPv4 and IPv6. IPv6 was developed to address the limitations of IPv4, including the limited address space.

7. The network layer can use both connection-oriented and connectionless services. In a connection-oriented service, a virtual circuit is established between the source and destination before data transmission begins. In a connectionless service, data packets are sent without establishing a connection first.

8. The network layer can also provide Quality of Service (QoS) guarantees, such as guaranteed bandwidth or low latency, for certain types of traffic.

A mnemonic to remember the functions of the network layer is **"RIFE"** - **R**outing, **I**nternetworking, **F**ragmentation and reassembly, and **E**rror handling and congestion control.