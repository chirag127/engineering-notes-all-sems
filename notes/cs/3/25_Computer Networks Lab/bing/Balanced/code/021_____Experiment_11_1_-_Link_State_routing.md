Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content in markdown format on the topic of Experiment 11.1 - Link State routing. Here is the content:

### Experiment 11.1 - Link State routing

- Link state routing is a dynamic routing protocol that uses the concept of link state advertisements (LSAs) to exchange information about the network topology and the cost of reaching different destinations.
- LSAs are broadcasted periodically by each router to all its neighbors, and then flooded throughout the network. Each router maintains a link state database (LSDB) that contains all the LSAs it has received.
- Based on the LSDB, each router computes the shortest path to every other router in the network using an algorithm such as Dijkstra's algorithm. This results in a routing table that maps each destination to the next hop router along the shortest path.
- Link state routing has some advantages over distance vector routing, such as faster convergence, loop-free routing, and support for hierarchical routing. However, it also has some disadvantages, such as higher memory and bandwidth requirements, and vulnerability to misconfigured or malicious routers.