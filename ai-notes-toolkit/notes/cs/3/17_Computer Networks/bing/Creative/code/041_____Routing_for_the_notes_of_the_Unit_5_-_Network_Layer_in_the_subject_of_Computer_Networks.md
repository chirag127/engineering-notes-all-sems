# Routing

Routing is the process of forwarding packets from one network to another based on the destination address and the routing table. Routing takes place at the network layer (layer 3) of the OSI model . A router is a device that performs routing by examining the packet header and the forwarding table .

## Types of Routing

There are three main types of routing:

- Static routing: In static routing, the routes are manually configured by the network administrator. Static routing is simple, secure, and easy to implement, but it is not scalable, adaptive, or dynamic.
- Dynamic routing: In dynamic routing, the routes are automatically learned and updated by the routers using routing protocols. Dynamic routing is scalable, adaptive, and dynamic, but it is more complex, less secure, and requires more resources.
- Default routing: In default routing, a default route is used to forward packets to a single gateway when no specific route is available. Default routing is useful for stub networks or networks with a single exit point.

## Routing Protocols

Routing protocols are algorithms that enable routers to exchange routing information and maintain routing tables. Routing protocols can be classified into two categories:

- Interior Gateway Protocols (IGPs): IGPs are used to exchange routing information within an autonomous system (AS), which is a group of networks under a single administrative control. Examples of IGPs are RIP, OSPF, EIGRP, and IS-IS.
- Exterior Gateway Protocols (EGPs): EGPs are used to exchange routing information between different autonomous systems. Examples of EGPs are BGP and EGP.

## Routing Metrics

Routing metrics are values that are used to measure the suitability of a route. Routing metrics can be based on various factors, such as hop count, bandwidth, delay, load, reliability, cost, etc. Different routing protocols use different metrics to select the best route. For example, RIP uses hop count, OSPF uses cost, and EIGRP uses a composite metric based on bandwidth, delay, load, and reliability.