### Static and Dynamic Routing for the Notes of Unit 5 - Network Layer in the Subject of Computer Networks

In computer networks, routing refers to the process of selecting the path that network packets take between devices on a network. The network layer is responsible for routing packets across multiple networks. The two types of routing are static and dynamic routing.

#### Static Routing

Static routing is a simple and straightforward routing approach. In static routing, the network administrator manually configures the routing table of each device in the network. The routing table contains information about the network topology, such as the IP addresses of the other devices in the network and the routes to reach them.

Advantages of Static Routing:
- Simple to configure and maintain.
- Efficient in small networks with few changes in the network topology.
- No overhead of computing routes dynamically.

Disadvantages of Static Routing:
- Inflexible in large networks with frequent changes in network topology.
- Prone to errors, especially in complex networks.
- Not suitable for networks with multiple paths to the same destination.

#### Dynamic Routing

Dynamic routing is an automated approach to routing that uses routing protocols to calculate the best path for packets to take through a network. Dynamic routing protocols exchange information about the network topology with other routers, and use this information to calculate the best path for packets to take.

Types of Dynamic Routing Protocols:
1. Distance Vector Routing Protocol - In this protocol, each router maintains a vector of distances to all the other routers in the network. The router exchanges its vector with its neighboring routers, and each router updates its vector based on the information received.
2. Link State Routing Protocol - In this protocol, each router maintains a database of all the links in the network. The router uses this database to calculate the shortest path to every other router in the network.

Advantages of Dynamic Routing:
- Adaptable to changes in network topology.
- Suitable for large networks with multiple paths to the same destination.
- Less prone to errors than static routing.

Disadvantages of Dynamic Routing:
- More complex to configure and maintain than static routing.
- Can generate network traffic due to frequent updates.
- May lead to suboptimal routing decisions in some cases.

#### Examples of Routing Protocols

1. Routing Information Protocol (RIP) - A distance vector routing protocol that uses the hop count as the metric for determining the best path. RIP is suitable for small networks.
2. Open Shortest Path First (OSPF) - A link state routing protocol that uses the shortest path first algorithm to determine the best path. OSPF is suitable for large networks.
3. Border Gateway Protocol (BGP) - A path vector routing protocol used in the Internet to exchange routing information between different autonomous systems.

In conclusion, both static and dynamic routing have their advantages and disadvantages. Static routing is simple and efficient in small networks with few changes in the network topology, while dynamic routing is adaptable to changes in network topology and suitable for large networks with multiple paths to the same destination. The choice of routing approach depends on the size and complexity of the network, as well as the network's performance and reliability requirements.