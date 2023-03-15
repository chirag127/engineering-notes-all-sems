### Experiment 11.1 - Link State routing

Link State routing is a type of routing protocol used in computer networks. It is based on the concept of each router in the network maintaining a map of the entire network topology. This map is used to calculate the shortest path to each destination in the network.

1. In Link State routing, each router sends information about its connected links to all other routers in the network. This information is known as a Link State Advertisement (LSA).
2. LSAs are sent periodically and whenever there is a change in the network topology.
3. Each router uses the received LSAs to construct a complete map of the network topology.
4. The map is represented as a graph, where nodes represent routers and edges represent links between routers.
5. Each router then uses a shortest path algorithm, such as Dijkstra's algorithm, to calculate the shortest path to each destination in the network.
6. The calculated shortest paths are stored in the router's routing table and used to forward packets to their destination.

Link State routing protocols are commonly used in large networks due to their ability to quickly adapt to changes in the network topology. Some examples of Link State routing protocols include Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).