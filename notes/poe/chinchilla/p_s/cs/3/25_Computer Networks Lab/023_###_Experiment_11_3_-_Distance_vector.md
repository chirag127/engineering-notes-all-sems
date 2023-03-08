### Experiment 11.3 - Distance Vector

In computer networking, a Distance Vector algorithm is used to calculate the best path for data packets to travel from one network node to another. The algorithm is commonly used in routing protocols for IP networks.

#### How Distance Vector Works

Distance Vector algorithms work by having each network node send information about the path it has chosen to its neighboring nodes. Each node then uses this information to update its routing table with the best path to the destination node. This process is repeated until all nodes have updated their routing tables and the best path is determined.

#### Advantages of Distance Vector

- Simple and easy to implement
- Can handle small to medium-sized networks efficiently
- Can adapt to changes in the network topology quickly

#### Disadvantages of Distance Vector

- Slow convergence time in larger networks
- Prone to routing loops and count to infinity problems
- Not suitable for larger networks with complex topologies

#### Example of Distance Vector

Consider a network with four nodes, A, B, C, and D, where A is the source node and D is the destination node. Each node has a routing table that stores the best path to reach the destination node.

Initially, node A sends its routing table to its neighbors, which are nodes B and C. Nodes B and C update their routing tables with the information received from node A and send their updated routing tables to their neighbors. This process continues until all nodes have updated their routing tables with the best path to reach the destination node.

#### Applications of Distance Vector

Distance Vector algorithms are used in routing protocols such as Routing Information Protocol (RIP) and Interior Gateway Routing Protocol (IGRP). These protocols are used in IP networks to determine the best path for data packets to travel from one network node to another.

#### Conclusion

Distance Vector is a simple and efficient algorithm for routing data packets in small to medium-sized networks. It has its advantages and disadvantages and is best suited for networks with simple topologies. It is commonly used in routing protocols for IP networks and plays a crucial role in the functioning of the internet.