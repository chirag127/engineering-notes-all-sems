### Forwarding and Delivery in Network Layer

- The network layer supervises the handling of packets by the underlying physical networks. We call this handling as the delivery of packets to the destination .
- The delivery of a packet is called **direct** if the deliverer (host or router) and the destination are on the same network; the delivery of a packet is called **indirect** if the deliverer (host or router) and the destination are on different networks.
- Forwarding means placing the packet in its route to the destination and it requires a routing table . A routing table is a data structure that stores the information about the best routes to reach each destination network.
- Forwarding refers to the router-local action of transferring a packet from an input link interface to the appropriate output link interface. Routing refers to the network-wide process that determines the end-to-end paths that packets take from source to destination.
- Address aggregation is a technique that reduces the size of routing tables by grouping several networks into a single entry. For example, if a router has four networks with the same prefix, it can aggregate them into one entry with a shorter prefix length.
- Some tools or utilities that can help with packet delivery and routing are :
  - **ping**: a command that sends an echo request packet to a destination and waits for an echo reply packet. It can measure the round-trip time and check the connectivity between two hosts or routers.
  - **traceroute**: a command that traces the route taken by a packet from the source to the destination. It can show the number of hops, the IP addresses of intermediate routers, and the delay of each hop.
  - **route**: a command that displays or modifies the routing table of a host or router. It can show the destination network, the gateway, the interface, and the metric for each entry.