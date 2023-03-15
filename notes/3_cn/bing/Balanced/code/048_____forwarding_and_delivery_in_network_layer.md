### Forwarding and Delivery in Network Layer

The network layer is responsible for delivering packets from the source host to the destination host across multiple networks. The network layer supervises the handling of packets by the underlying physical networks and defines the routes that packets take from source to destination. 

There are two main functions of the network layer: forwarding and routing.

- Forwarding is the process of moving a packet from an input link interface to the appropriate output link interface of a router. Forwarding is based on the destination address of the packet and the routing table of the router. The routing table contains information about the next hop for each possible destination network. Forwarding is a local action that happens at each router along the path of the packet.

- Routing is the process of determining the end-to-end paths that packets take from source to destination. Routing is based on the topology of the network and the routing algorithm used by the routers. Routing is a network-wide process that happens periodically or when there is a change in the network. Routing algorithms can be classified into static or dynamic, centralized or distributed, and link-state or distance-vector.

Here is an example of forwarding and routing in network layer:

```text
   H1 ---- R1 ---- R2 ---- R3 ---- H2
```

- H1 and H2 are the source and destination hosts, respectively.
- R1, R2, and R3 are the routers in the network.
- H1 wants to send a packet to H2.

- Routing: R1, R2, and R3 exchange routing information using a routing algorithm (e.g., RIP, OSPF, BGP) and build their routing tables. The routing tables contain the next hop for each destination network. For example, R1's routing table may look like this:

```text
   Destination Network | Next Hop
   ---------------------|---------
   H1's network         | H1
   R2's network         | R2
   R3's network         | R2
   H2's network         | R2
```

- Forwarding: H1 sends a packet to H2 with H2's address as the destination address. R1 receives the packet and looks up its routing table to find the next hop for H2's network, which is R2. R1 forwards the packet to R2. R2 receives the packet and looks up its routing table to find the next hop for H2's network, which is R3. R2 forwards the packet to R3. R3 receives the packet and looks up its routing table to find the next hop for H2's network, which is H2. R3 forwards the packet to H2. H2 receives the packet and processes it.