### Experiment 11.3 - Distance vector

- A distance vector is a data structure that contains the distance and direction from a source node to a destination node in a network.
- A distance vector routing algorithm is a distributed algorithm that uses distance vectors to compute the shortest paths between nodes in a network.
- A distance vector routing algorithm works as follows:
  - Each node maintains a distance vector table that contains the distance and next hop to every other node in the network.
  - Each node periodically exchanges its distance vector table with its direct neighbors.
  - Each node updates its distance vector table based on the information received from its neighbors, using the Bellman-Ford equation: `d(x,y) = min{c(x,v) + d(v,y)}` where `d(x,y)` is the distance from node `x` to node `y`, `c(x,v)` is the cost of the link from node `x` to node `v`, and `d(v,y)` is the distance from node `v` to node `y` as reported by node `v`.
  - The algorithm converges when no node changes its distance vector table in an iteration.
- A distance vector routing algorithm has the following advantages and disadvantages:
  - Advantages:
    - It is simple and easy to implement.
    - It does not require global knowledge of the network topology.
    - It can adapt to dynamic changes in the network, such as link failures or additions.
  - Disadvantages:
    - It may take a long time to converge, especially in large networks.
    - It may suffer from the count-to-infinity problem, where a node increases its distance to a destination indefinitely due to a loop in the network.
    - It may generate a lot of traffic due to periodic updates, which may consume bandwidth and energy.