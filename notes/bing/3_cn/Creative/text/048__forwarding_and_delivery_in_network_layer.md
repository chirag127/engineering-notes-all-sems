### Forwarding and Delivery in Network Layer

- The network layer is the third layer of the OSI model that is responsible for source-to-destination or host-to-host delivery of packets across multiple networks.
- The delivery of a packet is called **direct** if the deliverer (host or router) and the destination are on the same network; the delivery of a packet is called **indirect** if the deliverer (host or router) and the destination are on different networks.
- The network layer supervises the handling of the packets by the underlying physical networks. This handling is defined as the **delivery**.
- The network layer takes the data from the transport layer, adds its header, and forwards it to the data link layer.
- The network layer header contains the source and destination network addresses, which are used to route the packet through the network.
- The network layer provides two main functions: **forwarding** and **routing**.
- **Forwarding** refers to the router-local action of transferring a packet from an input link interface to the appropriate output link interface.
- **Routing** refers to the network-wide process that determines the end-to-end paths that packets take from source to destination.
- Forwarding is based on the routing table that is stored in each router. The routing table maps a destination network address to an output link interface.
- Routing is based on the routing algorithms that are used to compute the routing tables. Routing algorithms can be classified into two types: **static** and **dynamic**.
- **Static routing** algorithms use fixed routing tables that are manually configured by the network administrator. Static routing is simple and reliable, but it cannot adapt to network changes or failures.
- **Dynamic routing** algorithms use routing protocols that exchange information among routers to update their routing tables. Dynamic routing is more flexible and robust, but it requires more computation and communication overhead.
- Some examples of routing protocols are: **Distance Vector Routing**, **Link State Routing**, **Hierarchical Routing**, **Broadcast Routing**, **Multicast Routing**, and **Anycast Routing** .