### Experiment 11.3 - Distance vector

- A distance vector is a data structure that contains the distance and direction from a source node to a destination node in a network.
- A distance vector routing protocol is a type of routing protocol that uses distance vectors to exchange routing information between neighboring nodes.
- The goal of a distance vector routing protocol is to find the shortest path from each node to every other node in the network, based on the distance and direction information in the distance vectors.
- A distance vector routing protocol works as follows:
  - Each node maintains a distance vector table that contains an entry for every other node in the network, with the distance and direction to reach that node.
  - Each node periodically broadcasts its distance vector table to its neighbors, or sends it only when there is a change in the network topology.
  - Each node receives the distance vector tables from its neighbors and updates its own table based on the Bellman-Ford algorithm, which calculates the minimum distance and direction to each destination node.
  - The process repeats until all nodes have consistent and accurate distance vector tables, or until a steady state is reached.
- An example of a distance vector routing protocol is the Routing Information Protocol (RIP), which uses hop count as the distance metric and sends updates every 30 seconds.