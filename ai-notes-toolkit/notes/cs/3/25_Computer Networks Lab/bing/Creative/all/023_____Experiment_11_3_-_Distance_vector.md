# Experiment 11.3 - Distance vector routing algorithm

- Distance vector routing is a dynamic routing protocol that uses the Bellman-Ford algorithm or the shortest path algorithm to find the best routes between nodes in a network .
- Distance vector routing algorithm works by exchanging information about the distances and directions to the destination nodes with the neighboring nodes that have a direct link .
- Each node maintains a distance vector table that contains the distance and the next hop for each possible destination in the network .
- The distance vector table is updated periodically by sending and receiving the distance vectors from the neighboring nodes .
- The distance vector routing algorithm can handle changes in the network topology by propagating the updates to all the nodes in the network .
- The distance vector routing algorithm has some advantages and disadvantages, such as:
  - Advantages:
    - It is simple and easy to implement .
    - It does not require much computational power or memory .
    - It can adapt to different network sizes and topologies .
  - Disadvantages:
    - It can cause routing loops and count-to-infinity problems .
    - It can have slow convergence and high bandwidth consumption .
    - It can be vulnerable to malicious attacks and false information .