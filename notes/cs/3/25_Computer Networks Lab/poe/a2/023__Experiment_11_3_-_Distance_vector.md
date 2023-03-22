 Here is the content in Markdown format without any emojis or external links, written in a formal tone with points:

### Experiment 11.3 - Distance vector

1. Distance vector routing is a routing technique in which each router maintains a vector (table) of minimum distances to every network.
2. The vector is updated periodically using a routing update algorithm. Each router sends its distance vector to neighboring routers.
3. When a router receives an update from a neighbor, it checks if the reported distances are shorter. If so, it updates its distance vector and propagates the update to its neighbors.
4. This process continues iteratively until all routers have the shortest path distances to all networks.
5. The main drawbacks are:
- Slow convergence when the network topology changes.
- The routing loop problem (counting to infinity).
- Wastage of bandwidth due to periodic route updates.

Does this match your requirements? Let me know if you would like me to modify or add anything.