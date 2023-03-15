### Forwarding and Delivery in Network Layer

- The network layer supervises the handling of packets by the underlying physical networks. We define this handling as the delivery of packets to the destination.
- The delivery of a packet is called **direct** if the deliverer (host or router) and the destination are on the same network; the delivery of a packet is called **indirect** if the deliverer (host or router) and the destination are on different networks.
- The network layer also determines the route or path taken by the packets from the source to the destination. This process is called routing.
- Routing involves two basic activities: determining optimal routing paths and transporting packets through an internetwork.
- The routing process is usually performed by routers, which are network layer devices that forward packets from one network to another.
- Forwarding means placing the packet in its route to destination and it requires a routing table.
- A routing table is a data structure that stores information about the routes to various network destinations. The routing table contains a list of destination network addresses and the interface or next hop address to reach that destination.
- A router uses the destination address of a packet and the routing table to decide where to forward the packet. This is called the forwarding decision.
- Forwarding refers to the router-local action of transferring packet from an input link interface to the appropriate output link interface. Routing refers to the network-wide process that determines the end-to-end paths that packets take from source to destination.
- There are different types of routing algorithms, such as static, dynamic, distance vector, link state, hierarchical, broadcast, multicast, etc. Each algorithm has its own advantages and disadvantages in terms of complexity, scalability, robustness, optimality, etc.
- Some tools or utilities that can help in packet delivery and routing are ping, traceroute, ipconfig, netstat, etc. These tools can test the connectivity, display the route, show the configuration, and monitor the traffic of a network.

#### Mnemonics and learning tricks

- A possible mnemonic to remember the difference between forwarding and routing is: **F**orwarding is **F**ast and **F**ocused, **R**outing is **R**easoned and **R**evised.
- A possible learning trick to understand the concept of routing is to compare it with the process of finding directions on a map. The routing algorithm is like the map, the routing table is like the list of directions, and the forwarding decision is like the choice of which direction to take at each intersection.