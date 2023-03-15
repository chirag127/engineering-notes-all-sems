# Forwarding and Delivery for the Notes of the Unit 5 - Network Layer in the Subject of Computer Networks

- The network layer is responsible for the delivery of packets from the source host to the destination host across one or more networks.
- The network layer supervises the handling of the packets by the underlying physical networks, which may have different characteristics and technologies.
- The delivery of a packet is called **direct** if the deliverer (host or router) and the destination are on the same network; the delivery of a packet is called **indirect** if the deliverer (host or router) and the destination are on different networks.
- The network layer provides two main functions: **forwarding** and **routing**.
- **Forwarding** is the process of moving a packet from an input link interface to the appropriate output link interface within a router.
- **Routing** is the process of finding the end-to-end path that packets take from the source to the destination across the network.
- Forwarding is a local action that depends on the routing table stored in the router's memory, which maps the destination address to the output interface.
- Routing is a network-wide process that involves the exchange of information among routers to update their routing tables and select the best paths.
- There are two main types of routing algorithms: **static** and **dynamic**.
- **Static routing** algorithms are fixed and do not change in response to network conditions. They are usually configured manually by the network administrator or by using a common database.
- **Dynamic routing** algorithms are adaptive and change in response to network conditions, such as congestion, link failures, or topology changes. They use routing protocols to exchange information among routers and update their routing tables periodically or on demand.
- Some examples of routing protocols are: **RIP**, **OSPF**, **BGP**, **EIGRP**, **IS-IS**, etc.
- Routing protocols can be classified into two categories: **intra-domain** and **inter-domain**.
- **Intra-domain routing** protocols are used to route packets within a single administrative domain or network, such as a campus network or an enterprise network. They are also called **interior gateway protocols (IGPs)**.
- **Inter-domain routing** protocols are used to route packets between different administrative domains or networks, such as the Internet. They are also called **exterior gateway protocols (EGPs)**.
- The most widely used inter-domain routing protocol is **Border Gateway Protocol (BGP)**, which connects autonomous systems (ASes) on the Internet and exchanges routing information among them.