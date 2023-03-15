### Experiment 11.1 - Link State routing

Link State routing is a type of routing protocol used in computer networks. It is based on the concept of each router in the network maintaining a map of the entire network topology. This map is used to calculate the shortest path to each destination in the network.

The steps involved in Link State routing are as follows:

1. Each router in the network sends a "hello" message to its directly connected neighbors to discover their presence.
2. Each router then sends a Link State Packet (LSP) to all other routers in the network, containing information about its directly connected neighbors and the cost of reaching them.
3. Each router receives the LSPs from all other routers and uses this information to construct a complete map of the network topology.
4. Each router then uses a shortest path algorithm, such as Dijkstra's algorithm, to calculate the shortest path to each destination in the network.
5. The router updates its routing table with the calculated shortest paths and uses this information to forward packets to their destination.

Link State routing protocols are commonly used in large networks due to their ability to quickly adapt to changes in the network topology. Some examples of Link State routing protocols include OSPF and IS-IS.