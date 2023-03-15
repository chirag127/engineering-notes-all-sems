# Routing

Routing is the process of forwarding packets from one network to another based on the destination address and the routing table. Routing takes place at the network layer (layer 3) of the OSI model or the internet layer of the TCP/IP model  . Routing is performed by a special device known as a router, which connects to two or more networks or subnetworks and analyses the packet header and the forwarding table to determine the best path for the packet  .

## Types of Routing

There are three main types of routing:

- Static routing: Static routing is a process in which the routes are manually added to the routing table by the network administrator. Static routing is simple, secure, and resource-efficient, but it is not scalable, adaptable, or fault-tolerant. Static routing is suitable for small and stable networks.
- Dynamic routing: Dynamic routing is a process in which the routes are automatically learned and updated by the routers using routing protocols. Dynamic routing is scalable, adaptable, and fault-tolerant, but it is complex, insecure, and resource-intensive. Dynamic routing is suitable for large and dynamic networks.
- Default routing: Default routing is a process in which a default route is configured on a router to forward all packets that do not match any specific route in the routing table. Default routing is useful for reducing the size of the routing table and providing a backup route in case of a failure.

## Routing Protocols

Routing protocols are the rules and algorithms that routers use to exchange routing information and update their routing tables. Routing protocols can be classified into two categories:

- Interior Gateway Protocols (IGPs): IGPs are the routing protocols that operate within an autonomous system (AS), which is a group of networks under the same administrative control. Examples of IGPs are RIP, OSPF, EIGRP, and IS-IS.
- Exterior Gateway Protocols (EGPs): EGPs are the routing protocols that operate between different autonomous systems. Examples of EGPs are BGP and EGP.

Routing protocols can also be classified based on the type of information they use to make routing decisions:

- Distance-vector protocols: Distance-vector protocols use the distance (or hop count) and the direction (or next hop) to the destination as the routing metrics. Distance-vector protocols are simple and easy to implement, but they are slow to converge and prone to routing loops. Examples of distance-vector protocols are RIP and EIGRP.
- Link-state protocols: Link-state protocols use the state (or cost) of each link in the network as the routing metric. Link-state protocols are fast to converge and loop-free, but they are complex and require more resources. Examples of link-state protocols are OSPF and IS-IS.
- Path-vector protocols: Path-vector protocols use the entire path to the destination as the routing metric. Path-vector protocols are scalable and flexible, but they are difficult to configure and troubleshoot. An example of a path-vector protocol is BGP.