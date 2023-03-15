### Forwarding and Delivery in Network Layer

- The network layer supervises the handling of packets by the underlying physical networks. We call this handling as the delivery of packets to the destination.
- The delivery of a packet is called **direct** if the deliverer (host or router) and the destination are on the same network; the delivery of a packet is called **indirect** if the deliverer (host or router) and the destination are on different networks.
- The network layer also determines the route or path taken by the packets from the source to the destination. This process is called **routing**.
- Routing is a network-wide process that involves all the routers in the network. Routing algorithms are used to find the optimal paths for packet delivery.
- Forwarding is a router-local process that transfers a packet from an input link interface to the appropriate output link interface based on the routing information.
- Forwarding requires a **routing table** that maps the destination address or network to the output link interface. The routing table is updated by the routing algorithms .
- A routing table can have **static** entries that are manually configured by the network administrator, or **dynamic** entries that are automatically updated by the routing algorithms.
- A routing table can also have **default** entries that are used when no specific match is found for the destination address or network.
- A routing table can use **address aggregation** to reduce the number of entries by combining several networks into one entry. For example, if there are four networks with addresses 200.23.16.0/24, 200.23.17.0/24, 200.23.18.0/24, and 200.23.19.0/24, they can be aggregated into one entry 200.23.16.0/22.
- A router can use different methods to find the matching entry in the routing table, such as **longest prefix matching**, **next-hop matching**, or **host-specific matching**.
- Some tools or utilities that can help with packet delivery and routing are **traceroute**, **ping**, **route**, and **ipconfig** .

: Network Layer – Understanding Packet Delivery and Routing - Notesformsc
: Network Layer Delivery Forwarding and Routing - [PPT Powerpoint]
: Data Communication and Networking - Network Layer: Delivery, Forwarding, and Routing Study Notes
: Forwarding and Routing in Network Layer - Electronics Post
: Network Layer Services- Packetizing, Routing and Forwarding - GeeksforGeeks