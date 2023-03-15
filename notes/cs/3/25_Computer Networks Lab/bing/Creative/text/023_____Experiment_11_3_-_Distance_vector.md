### Experiment 11.3 - Distance vector routing algorithm

- Distance vector routing is a dynamic routing protocol that uses the Bellman-Ford algorithm to find the shortest paths between nodes in a network  .
- Distance vector routing works by having each router maintain a routing table that contains the distance and direction (or vector) to each destination in the network .
- Each router periodically exchanges its routing table with its directly connected neighbors, and updates its own table based on the information received  .
- Distance vector routing is simple, easy to implement, and scalable for large networks . However, it also has some drawbacks, such as slow convergence, counting to infinity problem, and routing loops  .
- To improve the performance and reliability of distance vector routing, some enhancements have been proposed, such as split horizon, poison reverse, triggered updates, and hold-down timers  .
- Some examples of distance vector routing protocols are Routing Information Protocol (RIP), Interior Gateway Routing Protocol (IGRP), and Enhanced Interior Gateway Routing Protocol (EIGRP) .