### Static and Dynamic Routing for the Notes of Unit 5 - Network Layer in the Subject of Computer Networks

The network layer of the OSI model is responsible for routing data packets across different networks. In order to accomplish this, routers use routing tables to determine the most efficient path for a packet to reach its destination. There are two main types of routing: static and dynamic routing. Let's take a closer look at each of these methods.

#### Static Routing

Static routing is a method of routing that involves manually configuring a routing table on a router. The routing table contains a list of network destinations and the next hop that a packet should take to reach that destination. Static routing is typically used in small networks where the network topology is relatively simple and stable. Here are some key points to keep in mind about static routing:

- Static routing is easy to implement and typically requires minimal configuration.
- Because the routing table is manually configured, there is no need for dynamic routing protocols.
- Static routing is not very scalable and can become unmanageable in larger networks.
- If a network topology changes, the routing table will need to be manually updated.

#### Dynamic Routing

Dynamic routing is a method of routing that involves routers exchanging routing information with each other using routing protocols. The routing protocols allow routers to dynamically update their routing tables based on changes in the network topology. Here are some key points to keep in mind about dynamic routing:

- Dynamic routing is more complex than static routing and typically requires more configuration.
- Dynamic routing is highly scalable and can be used in larger and more complex networks.
- Dynamic routing protocols can adapt to changes in the network topology, so there is no need for manual updates to the routing table.
- Dynamic routing protocols can be classified as distance vector or link state protocols.

Distance vector protocols use the Bellman-Ford algorithm to calculate the shortest path to a destination network. Examples of distance vector protocols include Routing Information Protocol (RIP) and Interior Gateway Routing Protocol (IGRP).

Link state protocols use the Dijkstra algorithm to calculate the shortest path to a destination network. Examples of link state protocols include Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).

In conclusion, both static and dynamic routing have their advantages and disadvantages. Static routing is simple to implement and is best suited for small and stable networks. Dynamic routing is more complex but can adapt to changes in the network topology, making it more scalable and better suited for larger and more complex networks. Understanding these routing methods is essential for network engineers and administrators to design and maintain efficient and reliable networks.