### Forwarding and Delivery

Forwarding and delivery are two important concepts in the network layer of the OSI model in computer networks.

1. **Forwarding** refers to the process of moving a packet from an incoming link to an outgoing link within a router. This is done by looking up the destination address of the packet in the forwarding table of the router and determining the appropriate outgoing link.

2. **Delivery** refers to the process of delivering a packet from the source host to the destination host. This involves forwarding the packet through multiple routers along the path from the source to the destination.

3. The forwarding process is performed by routers, while the delivery process is performed by both routers and end hosts.

4. The forwarding table is a data structure that is used by routers to determine the appropriate outgoing link for a packet. It contains a list of destination addresses and the corresponding outgoing links.

5. The forwarding table is typically populated using routing protocols, which are used by routers to exchange information about the network topology and to determine the best path for packets.

6. The delivery process involves several steps, including error checking, fragmentation and reassembly, and congestion control.

7. Error checking is used to detect and correct errors that may have occurred during transmission. Fragmentation and reassembly are used to divide large packets into smaller packets for transmission and to reassemble them at the destination.

8. Congestion control is used to prevent network congestion by regulating the flow of packets into the network.

In summary, forwarding and delivery are two important processes in the network layer that are used to move packets from the source to the destination in a computer network. These processes involve the use of forwarding tables, routing protocols, error checking, fragmentation and reassembly, and congestion control.