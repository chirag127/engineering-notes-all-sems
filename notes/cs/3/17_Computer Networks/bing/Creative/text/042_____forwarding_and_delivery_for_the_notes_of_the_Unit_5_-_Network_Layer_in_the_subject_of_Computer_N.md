### Forwarding and Delivery in Network Layer

- The network layer supervises the handling of packets by the underlying physical networks. We call this handling as the delivery of packets to the destination .
- The delivery of a packet is called **direct** if the deliverer (host or router) and the destination are on the same network; the delivery of a packet is called **indirect** if the deliverer (host or router) and the destination are on different networks.
- The network layer also determines the route or path taken by the packets from the source to the destination. This process is called routing .
- Routing involves two basic activities: determining optimal routing paths and transporting packets through an internetwork.
- The former is handled by routing algorithms, the latter by switching or forwarding.
- Forwarding means placing the packet in its route to the destination and it requires a routing table .
- A routing table is a data structure that stores information about the routes to various network destinations.
- The routing table is updated periodically using routing protocols or algorithms.
- Forwarding refers to the router-local action of transferring a packet from an input link interface to the appropriate output link interface .
- Forwarding can be done in different ways, such as datagram approach, virtual-circuit approach, or source routing.
- Address aggregation is a technique to reduce the size of routing tables by grouping several networks into a single entry .
- Address aggregation can be done at different levels, such as classful, classless, or hierarchical .
- Some tools or utilities that can help in packet delivery and routing are ping, traceroute, ipconfig, and netstat .
- Ping is a utility that tests the reachability of a host by sending an echo request and waiting for an echo reply .
- Traceroute is a utility that traces the route of a packet from the source to the destination, showing the intermediate routers and the round-trip time for each hop .
- Ipconfig is a utility that displays the IP address, subnet mask, default gateway, and other network configuration parameters of a host .
- Netstat is a utility that displays the status of active connections, routing tables, network interfaces, and network protocols of a host .