 Here is the content in markdown format for the given topic:

### Experiment 11.1 - Link State routing

Link state routing is an advanced routing algorithm used in networks. It has the following key points:

1. Each router maintains a map of the network topology. This map is constructed by each router broadcasting information about its directly connected links to all the other routers in the network. Each router then uses this information to construct a map of the network.
2. Based on the network map, each router calculates the shortest path to every other router in the network using a shortest path algorithm like Dijkstra's algorithm. The routing table is then updated with the shortest path to each destination router.
3. Whenever there is a change in the network topology, the router detecting the change broadcasts the information to all other routers. Each router then updates its network map and recomputes the shortest paths using the updated map. The routing tables are then updated with the new shortest paths.
4. Since each router has a view of the complete network topology and takes part in determining the shortest paths, link state routing provides very fast convergence when the network topology changes. However, it requires greater processing power and memory to calculate the shortest paths. It also generates more traffic as link state information has to be broadcast to all routers whenever there is a change.

Some key advantages of link state routing are fast convergence, support for variable length subnet masks (VLSM), and support for discontiguous networks. The key disadvantages are the high resource usage and additional network traffic generated.

Link state routing is commonly used in large networks by routing protocols such as Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.