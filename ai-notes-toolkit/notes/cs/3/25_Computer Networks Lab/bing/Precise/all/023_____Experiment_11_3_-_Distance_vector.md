### Experiment 11.3 - Distance Vector

Distance vector routing is a type of routing protocol used in computer networks. It is based on the Bellman-Ford algorithm and is used to calculate the shortest path between two nodes in a network.

1. In distance vector routing, each router maintains a routing table that contains the distance (or cost) to reach each destination in the network.
2. The distance is measured in terms of hops, where a hop is the number of routers that a packet must pass through to reach its destination.
3. Each router periodically sends its routing table to its neighboring routers. The neighboring routers then update their own routing tables based on the information received.
4. If a router receives a routing table from a neighbor that contains a shorter path to a destination, it updates its own routing table with the new information.
5. This process continues until all routers have the same information and the routing tables converge.
6. Distance vector routing is simple to implement and works well in small networks. However, it has some limitations, such as the count-to-infinity problem, which can cause routing loops and slow convergence in larger networks.
