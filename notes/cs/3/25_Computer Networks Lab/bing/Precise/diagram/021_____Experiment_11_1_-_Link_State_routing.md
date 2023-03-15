### Experiment 11.1 - Link State routing

Link State routing is a type of routing protocol used in computer networks. It is also known as shortest path first or Dijkstra's algorithm. The main features of Link State routing are:

1. Each router in the network maintains a complete map of the network topology, including the costs of each link.
2. Routers exchange information about the network topology with their neighbors using Link State packets (LSPs).
3. Each router uses the information it receives to calculate the shortest path to every other router in the network.
4. When a router detects a change in the network topology, it recalculates the shortest paths and sends updated LSPs to its neighbors.

Link State routing protocols are commonly used in large networks because they can quickly adapt to changes in the network topology. Some examples of Link State routing protocols include OSPF (Open Shortest Path First) and IS-IS (Intermediate System to Intermediate System).