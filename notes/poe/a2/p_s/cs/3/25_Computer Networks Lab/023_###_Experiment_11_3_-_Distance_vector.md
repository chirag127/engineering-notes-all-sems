 Here is the content in markdown format for the topic ### Experiment 11.3 - Distance vector:

### Experiment 11.3 - Distance vector

- Distance vector routing is a routing algorithm used for calculating routes in a computer network. It works by estimating the distance to any network node based on the number of hops required to reach that node, and then routes packets along the path with the smallest total distance.
- Each router using distance vector routing maintains a routing table that lists the "distance" to every other network node. The "distance" is a measure of the cost or metric to reach a given node, and is typically defined as the number of hops required to reach that node.
- The router periodically sends its entire routing table to each of its neighbors. A neighbor updates its own table by comparing the received distances with its own, and if one of the received distances is shorter, it updates its own table to use the shorter path. As this process happens in all routers, the routing tables eventually converge to show the shortest path between any two nodes.
- However, distance vector routing suffers from instability arising from routing loops, high convergence times, and inefficient use of bandwidth due to flooding routing updates. The stability issue can be reduced by implementing special algorithms to detect and disable bad routes, but fundamentally distance vector routing does not scale well to large networks. It has largely been replaced by link-state routing protocols that offer faster convergence and more efficient use of network resources.

- Examples of distance vector routing protocols: RIP, IGRP
- Advantages: Simple to understand and implement.
- Disadvantages: Slow convergence, count to infinity problem can lead to routing loops.
- Applications: Small to medium sized networks.

[Detailed ascii diagrams and codes can be added here to illustrate the concepts.]