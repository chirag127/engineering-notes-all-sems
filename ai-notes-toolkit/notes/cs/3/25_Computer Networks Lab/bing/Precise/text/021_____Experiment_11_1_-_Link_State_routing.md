### Experiment 11.1 - Link State routing

Link State routing is a type of routing protocol used in computer networks. It is based on the concept of each router in the network maintaining a map of the entire network topology. This map is used to calculate the shortest path to a destination and to update the routing table.

1. Link State routing protocols use a complex algorithm to calculate the shortest path to a destination. This algorithm is known as the Dijkstra's algorithm.
2. Each router in the network maintains a Link State Database (LSDB) which contains information about the network topology.
3. The LSDB is updated by exchanging Link State Advertisements (LSAs) between routers.
4. LSAs contain information about the state of the links between routers, including the cost of the link and the identity of the neighboring routers.
5. When a router receives an LSA, it updates its LSDB and recalculates the shortest path to all destinations.
6. Link State routing protocols are more scalable than distance vector routing protocols because they do not suffer from the "count to infinity" problem.
7. Examples of Link State routing protocols include Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).
