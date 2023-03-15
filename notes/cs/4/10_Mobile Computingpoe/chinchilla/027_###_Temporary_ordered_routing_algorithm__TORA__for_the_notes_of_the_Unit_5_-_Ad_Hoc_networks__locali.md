### Temporary Ordered Routing Algorithm (TORA)

Temporary Ordered Routing Algorithm (TORA) is a distributed routing protocol designed for mobile ad hoc networks (MANETs). It is a reactive routing protocol, which means that it only establishes routes as needed, rather than maintaining a full network topology at all times.

#### Working of TORA

The TORA algorithm works by maintaining a directed acyclic graph (DAG) of the network topology. Each node in the network maintains a set of links to its neighbors, and uses these links to construct a directed graph of the network. The TORA algorithm operates in three phases:

1. Route Creation: When a node needs to send a packet to a destination node, it first creates a set of routes to the destination. These routes are created by flooding the network with query packets, which are broadcast to all neighbors.

2. Route Maintenance: Once a set of routes has been created, the TORA algorithm maintains the routes by periodically updating them. Each node in the network maintains a set of metrics for each route, such as the distance to the destination node. If a link fails, the affected nodes update their metrics and broadcast the changes to their neighbors.

3. Route Deletion: If a node no longer needs a particular route, it can delete the route by broadcasting a delete packet to its neighbors. The delete packet propagates through the network, causing nodes to remove the route from their routing tables.

#### Advantages of TORA

1. TORA is a highly adaptable routing protocol that can handle a wide range of network topologies and conditions.

2. TORA is a reactive protocol, which means that it only establishes routes when they are needed. This reduces overhead and improves network efficiency.

3. TORA is a distributed protocol, which means that there is no single point of failure. This improves network resilience and makes it easier to scale the network.

#### Disadvantages of TORA

1. TORA requires a significant amount of processing power and memory to maintain the directed acyclic graph (DAG) of the network topology. This can be a problem in large networks or networks with limited resources.

2. TORA can be slow to establish routes in networks with high mobility, as the network topology changes frequently.

#### Mnemonics and Learning Tricks

Unfortunately, there are no easy mnemonics or learning tricks for TORA, as the algorithm is relatively complex and requires a good understanding of graph theory and distributed systems. However, students can improve their understanding of TORA by studying the key concepts and working through examples and practice problems.