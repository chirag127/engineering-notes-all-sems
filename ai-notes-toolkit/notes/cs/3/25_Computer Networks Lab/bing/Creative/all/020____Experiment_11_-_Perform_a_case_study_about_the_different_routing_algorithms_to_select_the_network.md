# Experiment 11 - Perform a case study about the different routing algorithms to select the network path with its optimum and economical during data transfer

## Objective
The objective of this experiment is to understand the concept and working of different routing algorithms and to compare their performance in terms of network efficiency and cost.

## Introduction
Routing is the process of finding the best path for sending data packets from a source node to a destination node in a network. Routing algorithms are the rules or methods that routers use to determine the optimal path for each packet. Routing algorithms can be classified into two main categories: adaptive and non-adaptive.

- Adaptive algorithms are the algorithms that change their routing decisions whenever network topology or traffic load changes. The changes in routing decisions are reflected in the topology as well as the traffic of the network. Adaptive algorithms can be further divided into centralized, distributed, and isolated algorithms.

- Non-adaptive algorithms are the algorithms that do not change their routing decisions once the network is established. They are also called static algorithms. Non-adaptive algorithms are simpler and faster than adaptive algorithms, but they may not be able to cope with dynamic network conditions.

## Case Study
In this case study, we will compare four different routing algorithms: shortest path, flooding, distance vector, and link state. We will use a hypothetical network topology as shown in the figure below. The numbers on the links represent the cost or distance of each link. The cost can be measured in terms of hop count, delay, bandwidth, or any other metric.

![Network Topology](https://i.imgur.com/9Q9Xx8Z.png)

We will assume that each node in the network is a router that can run any of the four routing algorithms. We will also assume that each router has a routing table that stores the best path and cost to reach every other node in the network. The routing table is updated periodically or whenever there is a change in the network.

We will analyze the performance of each routing algorithm in terms of the following criteria:

- Completeness: The ability of the algorithm to find a path to every destination in the network.
- Correctness: The ability of the algorithm to find the optimal path to every destination in the network.
- Robustness: The ability of the algorithm to adapt to changes in the network topology or traffic load.
- Efficiency: The amount of resources (such as bandwidth, memory, or processing power) consumed by the algorithm.
- Scalability: The ability of the algorithm to handle large and complex networks.

## Shortest Path Algorithm
The shortest path algorithm is a non-adaptive algorithm that finds the path with the minimum cost to every destination in the network. The algorithm uses a global view of the network, which means that every router knows the cost of every link in the network. The algorithm can be implemented using Dijkstra's algorithm or Bellman-Ford algorithm.

The shortest path algorithm is complete and correct, as it always finds the optimal path to every destination in the network. However, the algorithm is not robust, as it does not react to changes in the network topology or traffic load. The algorithm is also not efficient, as it requires a lot of communication and computation to maintain a global view of the network. The algorithm is not scalable, as it becomes impractical for large and complex networks.

## Flooding Algorithm
The flooding algorithm is a non-adaptive algorithm that sends every packet to every link in the network. The algorithm does not use any routing table or cost information. The algorithm relies on the destination node to recognize and accept the packet, and on the source node to stop sending the packet after a certain number of hops or a certain time.

The flooding algorithm is complete, as it guarantees that every packet will reach the destination node. However, the algorithm is not correct, as it does not find the optimal path to the destination node. The algorithm is robust, as it can cope with any changes in the network topology or traffic load. However, the algorithm is very inefficient, as it consumes a lot of bandwidth and creates a lot of redundancy and congestion in the network. The algorithm is not scalable, as it becomes unmanageable for large and complex networks.

## Distance Vector Algorithm
The distance vector algorithm is an adaptive algorithm that finds the best path to every destination in the network based on the distance or cost information from the neighboring routers. The algorithm uses a distributed view of the network, which means that every router only knows the cost of the links to its neighbors. The algorithm can be implemented using the Bellman-Ford algorithm or the RIP protocol.

The distance vector algorithm is complete and correct, as it eventually converges to the optimal path to every destination in