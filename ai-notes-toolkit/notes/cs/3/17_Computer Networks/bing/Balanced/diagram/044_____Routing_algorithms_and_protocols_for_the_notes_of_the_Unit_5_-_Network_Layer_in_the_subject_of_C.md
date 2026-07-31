### Routing algorithms and protocols for the notes of the Unit 5 - Network Layer in the subject of Computer Networks

- Routing is the process of finding and selecting the best path for data transmission from source to destination in a computer network.
- Routing algorithms are the software programs that implement the logic of routing, i.e., deciding the optimal path for each packet.
- Routing protocols are the set of rules and messages that routers use to communicate with each other and exchange routing information.
- Routing algorithms and protocols can be classified into two main categories: static and dynamic.
  - Static routing algorithms and protocols are fixed and do not change according to the network conditions. They are manually configured by the network administrator and are suitable for small and stable networks. An example of a static routing protocol is RIP (Routing Information Protocol).
  - Dynamic routing algorithms and protocols are adaptive and change according to the network conditions. They are automatically updated by the routers and are suitable for large and complex networks. An example of a dynamic routing protocol is OSPF (Open Shortest Path First).
- Routing algorithms and protocols can also be classified based on the scope of their operation: intra-domain and inter-domain.
  - Intra-domain routing algorithms and protocols are used within a single autonomous system (AS), which is a group of routers under the same administrative control. They are also called interior gateway protocols (IGPs). An example of an intra-domain routing protocol is OSPF.
  - Inter-domain routing algorithms and protocols are used between different autonomous systems. They are also called exterior gateway protocols (EGPs). An example of an inter-domain routing protocol is BGP (Border Gateway Protocol).
- Routing algorithms and protocols can also be classified based on the type of information they use to make routing decisions: distance vector and link state.
  - Distance vector routing algorithms and protocols use the distance (or hop count) and the direction (or next hop) to each destination as the routing metric. They exchange routing information with their immediate neighbors only. They are simple and easy to implement, but they may suffer from slow convergence and routing loops. An example of a distance vector routing protocol is RIP.
  - Link state routing algorithms and protocols use the state (or cost) of each link in the network as the routing metric. They exchange routing information with all the routers in the network. They are complex and resource-intensive, but they offer faster convergence and loop-free routing. An example of a link state routing protocol is OSPF.
- Routing algorithms and protocols perform three basic functions: discovery, route management, and path determination.
  - Discovery is the process of identifying other routers on the network and establishing connections with them.
  - Route management is the process of keeping track of the possible destinations and the pathways to reach them.
  - Path determination is the process of making dynamic decisions for where to send each packet based on the routing metric and the network conditions.