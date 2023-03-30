
### Experiment 11.3 - Distance Vector

1. Distance vector routing is a type of routing protocol used in computer networks. It is based on the Bellman-Ford algorithm, which calculates the shortest path between two nodes in a network.

2. Distance vector routing works by having each node in the network maintain a table of the shortest paths to all other nodes in the network. This table is referred to as the routing table.

3. Each node in the network sends its routing table to its neighbors. The neighbors then compare their routing tables with the one they received from the node. If the neighbor finds a shorter path to any node in the network, it updates its routing table accordingly.

4. The process of exchanging routing tables is known as the distance vector algorithm. It is an iterative process, meaning that the nodes keep exchanging routing tables until the tables converge to their final form.

5. The distance vector algorithm is used in a variety of different routing protocols, including RIP, IGRP, and EIGRP. It is also used in some link-state routing protocols, such as OSPF.