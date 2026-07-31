### Experiment 11.3 - Distance vector

- A distance vector is a data structure that contains the distance and direction from a source node to a destination node in a network.
- A distance vector routing protocol is a type of routing protocol that uses distance vectors to exchange routing information between neighboring nodes.
- The main advantage of distance vector routing is its simplicity and low overhead. The main disadvantage is its slow convergence and susceptibility to routing loops.
- An example of a distance vector routing protocol is the Routing Information Protocol (RIP), which uses hop count as the distance metric and sends updates every 30 seconds.
- The algorithm for distance vector routing is as follows:

  - Each node maintains a distance vector table that contains the distance and next hop to every other node in the network.
  - Each node periodically broadcasts its distance vector table to its neighbors.
  - Upon receiving a distance vector table from a neighbor, a node updates its own table by applying the Bellman-Ford equation: 
    - For each destination d, if the distance to d through the neighbor n is smaller than the current distance to d, then update the distance to d as the sum of the distance to n and the distance from n to d, and update the next hop to d as n.
  - The algorithm terminates when there are no more updates to any distance vector table.