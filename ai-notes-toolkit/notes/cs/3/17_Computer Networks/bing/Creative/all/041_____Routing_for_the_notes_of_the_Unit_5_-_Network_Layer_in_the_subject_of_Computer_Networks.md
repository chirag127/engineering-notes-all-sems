# Routing

Routing is the process of forwarding packets from one network to another based on the destination address and the routing table. Routing takes place at the network layer (layer 3) of the OSI model . A router is a device that performs routing by examining the packet header and the forwarding table .

## Types of Routing

There are three main types of routing:

- Static routing: In static routing, the routes are manually configured by the network administrator. Static routing is simple, secure, and easy to implement, but it is not scalable, adaptive, or dynamic.
- Dynamic routing: In dynamic routing, the routes are automatically learned and updated by the routers using routing protocols. Dynamic routing is scalable, adaptive, and dynamic, but it is more complex, less secure, and requires more resources.
- Default routing: In default routing, the router forwards all packets that do not match any specific route to a default gateway. Default routing is useful for stub networks or networks with a single exit point.

## Routing Protocols

Routing protocols are the rules and algorithms that routers use to exchange routing information and maintain the routing table. Routing protocols can be classified into two categories:

- Interior Gateway Protocols (IGPs): IGPs are used to exchange routing information within an autonomous system (AS), which is a group of networks under a single administrative control. Examples of IGPs are RIP, OSPF, EIGRP, and IS-IS.
- Exterior Gateway Protocols (EGPs): EGPs are used to exchange routing information between different autonomous systems. Examples of EGPs are BGP and EGP.

## Routing Metrics

Routing metrics are the criteria that routers use to select the best route among multiple possible routes to a destination. Routing metrics can be based on various factors, such as hop count, bandwidth, delay, load, reliability, cost, etc. Different routing protocols use different routing metrics to calculate the path cost or preference.

## Routing Algorithms

Routing algorithms are the methods that routers use to determine the optimal route to a destination. Routing algorithms can be classified into two types:

- Distance-vector algorithms: Distance-vector algorithms are based on the principle of Bellman-Ford algorithm, which states that the shortest path to a destination is the sum of the shortest paths to the intermediate nodes. Distance-vector algorithms use hop count as the routing metric and exchange routing updates periodically with their neighbors. Examples of distance-vector algorithms are RIP and EIGRP.
- Link-state algorithms: Link-state algorithms are based on the principle of Dijkstra's algorithm, which states that the shortest path to a destination is the one with the minimum total cost. Link-state algorithms use various routing metrics and exchange routing updates only when there is a change in the network topology. Examples of link-state algorithms are OSPF and IS-IS.

## Routing Tables

Routing tables are the data structures that store the routing information on a router. Routing tables contain the following information:

- Destination network: The network address of the destination network or host.
- Next hop: The IP address of the next router or interface along the path to the destination network or host.
- Interface: The local interface of the router that is used to forward the packet to the next hop or destination.
- Metric: The cost or preference of the route, based on the routing metric.
- Administrative distance: The reliability or trustworthiness of the route, based on the source of the routing information.

## Routing Process

The routing process is the sequence of steps that a router follows to forward a packet to its destination. The routing process can be summarized as follows:

- The router receives a packet from a source host or another router on one of its interfaces.
- The router checks the destination IP address of the packet and compares it with the entries in its routing table.
- If the router finds a matching entry, it forwards the packet to the next hop or destination according to the routing table.
- If the router does not find a matching entry, it forwards the packet to the default gateway, if configured, or drops the packet and sends an ICMP destination unreachable message to the source host.