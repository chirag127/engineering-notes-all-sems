### Routing in network layer

Routing is the process of selecting a path across one or more networks for data packets to travel from their source to their destination. Routing is performed by a special device known as a router, which works at the network layer in the OSI model and internet layer in TCP/IP model. A router is a networking device that forwards the packet based on the information available in the packet header and forwarding table. The routing algorithms are used for routing the packets.

The network layer is responsible for routing packets from the source host to the destination host. The routes can be based on static tables that are rarely changed, or they can be automatically updated depending on network conditions. Many networks are partitioned into sub-networks or subnets.

The network layer must determine the route or path taken by packets as they flow from a sender to a receiver. The algorithms that calculate these paths are referred to as routing algorithms. Routing algorithms can be classified into two types: static routing and dynamic routing.

- Static routing: In static routing, the routes are fixed and do not change unless the network administrator manually updates them. Static routing is simple and secure, but it is not scalable or adaptable to network changes. Static routing is suitable for small networks that have a stable topology and low traffic.
- Dynamic routing: In dynamic routing, the routes are updated automatically based on network conditions, such as traffic load, link failures, or topology changes. Dynamic routing is more complex and less secure, but it is more scalable and adaptable to network changes. Dynamic routing is suitable for large networks that have a dynamic topology and high traffic.

Dynamic routing uses various routing protocols to exchange routing information between routers. Routing protocols can be classified into two types: distance vector routing and link state routing.

- Distance vector routing: In distance vector routing, each router maintains a routing table that contains the distance (or cost) and the next hop to reach each destination. The routers periodically exchange their routing tables with their neighbors and update their own tables based on the information received. Distance vector routing is simple and easy to implement, but it is slow to converge and prone to routing loops. An example of distance vector routing is the Routing Information Protocol (RIP).
- Link state routing: In link state routing, each router maintains a link state database that contains the state (or status) of each link in the network. The routers periodically broadcast their link state information to all other routers in the network and update their own databases based on the information received. Link state routing is more complex and difficult to implement, but it is fast to converge and avoids routing loops. An example of link state routing is the Open Shortest Path First (OSPF) protocol.

Routing and forwarding are two other services offered by the network layer. Routing is the process of finding the best path for a packet, while forwarding is the process of moving the packet from one router to the next along the path.

- Forwarding: Forwarding is the process of moving a packet from an input port to an output port of a router based on the packet's destination address and the router's forwarding table. The forwarding table is a data structure that maps destination addresses to output ports. The forwarding table can be static or dynamic, depending on the routing algorithm used. Forwarding can be done in two ways: datagram forwarding and virtual circuit forwarding.
  - Datagram forwarding: In datagram forwarding, each packet is treated independently and forwarded based on its destination address. Datagram forwarding does not require any connection setup or state information at the routers. Datagram forwarding is simple and flexible, but it may cause packet reordering or duplication. Datagram forwarding is used in the Internet Protocol (IP).
  - Virtual circuit forwarding: In virtual circuit forwarding, a connection is established between the source and the destination before any packets are sent. Each packet is assigned a virtual circuit identifier (VCI) that is used to forward the packet along the connection. Virtual circuit forwarding requires connection setup and state information at the routers. Virtual circuit forwarding is more reliable and efficient, but it is less flexible and scalable. Virtual circuit forwarding is used in the Asynchronous Transfer Mode (ATM) protocol.

Here is an example of a network with four routers and six links. The network layer services of routing and forwarding are illustrated in this example.

![network diagram](https://i.imgur.com/4j0Z9gW.png)

- Routing: Suppose router A wants to send a packet to router D. Router A can use either static routing or dynamic routing to find the best path to router D. For example, if router A uses static routing, it may