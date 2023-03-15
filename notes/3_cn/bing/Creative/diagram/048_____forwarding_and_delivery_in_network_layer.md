### Forwarding and Delivery in Network Layer

- The network layer supervises the handling of packets by the underlying physical networks. We call this handling as the delivery of packets to the destination .
- The delivery of a packet is called **direct** if the deliverer (host or router) and the destination are on the same network; the delivery of a packet is called **indirect** if the deliverer (host or router) and the destination are on different networks.
- The network layer also determines the route or path taken by the packets from the source to the destination. This process is called routing .
- Routing refers to the network-wide process that determines the end-to-end paths that packets take from source to destination.
- Routing involves two main activities: finding and maintaining routing information (usually in the form of routing tables) and making routing decisions for each incoming packet.
- Forwarding means placing the packet in its route to the destination and it requires a routing table .
- Forwarding refers to the router-local action of transferring packet from an input link interface to the appropriate output link interface.
- Forwarding can be done in two ways: **datagram approach** and **virtual-circuit approach** .
- In the datagram approach, each packet is treated independently, and each packet contains the full destination address. The router uses the destination address to look up the output link in the routing table .
- In the virtual-circuit approach, each packet belongs to a pre-established connection, and each packet contains a short identifier called virtual-circuit number. The router uses the virtual-circuit number to look up the output link in the forwarding table .
- Address aggregation is a technique to reduce the size of routing tables by grouping several networks into a single entry .
- Some tools or utilities that can be used to test or troubleshoot packet delivery and routing are ping, traceroute, and route .
- Ping is a tool that sends a request packet to a destination and waits for a reply packet. It measures the round-trip time and packet loss rate between the source and the destination .
- Traceroute is a tool that sends a series of request packets with increasing time-to-live (TTL) values and records the routers that send back the reply packets. It shows the route or path taken by the packets from the source to the destination .
- Route is a tool that displays or modifies the routing table of a host or a router .