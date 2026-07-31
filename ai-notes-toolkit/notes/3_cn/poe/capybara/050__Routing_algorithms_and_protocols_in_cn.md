### Routing algorithms and protocols in CN

Routing algorithms and protocols are an essential part of Computer Networks (CN). They help in the efficient transfer of data between hosts and networks. In this section, we will discuss the various routing algorithms and protocols used in CN.

#### Routing Algorithms

1. **Shortest Path Routing Algorithm:** This algorithm finds the shortest path between the source and destination nodes in the network. It is based on the Dijkstra algorithm and is widely used in CN.

2. **Flooding Algorithm:** In this algorithm, every node in the network forwards the incoming packet to all its neighbours, except the one from which it received the packet. This algorithm is simple but can cause network congestion.

3. **Distance Vector Routing Algorithm:** This algorithm is iterative and is based on the Bellman-Ford algorithm. Each node maintains a routing table that contains the distance to each destination node in the network.

4. **Link-State Routing Algorithm:** In this algorithm, each node in the network maintains a complete map of the network topology. The nodes use this information to calculate the shortest path to the destination node.

#### Routing Protocols

1. **Open Shortest Path First (OSPF):** OSPF is a link-state routing protocol that is widely used in large-scale networks. It uses the Dijkstra algorithm to calculate the shortest path to the destination node.

2. **Routing Information Protocol (RIP):** RIP is a distance-vector routing protocol that is widely used in small-scale networks. The RIP protocol uses hop count as the metric to calculate the shortest path to the destination node.

3. **Border Gateway Protocol (BGP):** BGP is a path-vector routing protocol that is used to connect different Autonomous Systems (AS) on the Internet. It uses the path as the metric to calculate the shortest path to the destination node.

In conclusion, routing algorithms and protocols are essential for the efficient transfer of data over a network. The choice of a routing algorithm and protocol depends on the size of the network, the traffic load, and the reliability requirements.