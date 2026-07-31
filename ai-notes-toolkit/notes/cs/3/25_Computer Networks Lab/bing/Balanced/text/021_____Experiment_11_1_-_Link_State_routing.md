### Experiment 11.1 - Link State Routing

- Link state routing is a type of routing algorithm that uses the information about the state of each link (such as bandwidth, delay, cost, etc.) to calculate the shortest path from one node to every other node in the network .
- Link state routing is also known as Dijkstra's algorithm, which is an iterative algorithm that finds the least cost path for a given destination node after each iteration.
- Link state routing requires each node to construct a map of the network topology, in the form of a graph, by exchanging messages with all the other nodes in the network. These messages are called link state advertisements (LSAs).
- Link state routing protocols are more scalable and robust than distance-vector routing protocols, as they have a global view of the network and can detect and avoid loops and broken links .
- Examples of link state routing protocols are Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).
- The steps involved in link state routing are:
  - Each node broadcasts its LSAs to all its neighbors periodically or when there is a change in the link state.
  - Each node receives the LSAs from its neighbors and stores them in a link state database (LSDB).
  - Each node uses the LSDB to construct a graph of the network topology, where the nodes are routers and the edges are links with their costs.
  - Each node applies Dijkstra's algorithm to the graph to find the shortest path tree for itself, which contains the shortest path to every other node in the network.
  - Each node updates its routing table based on the shortest path tree, where the next hop for each destination is the first node on the shortest path.