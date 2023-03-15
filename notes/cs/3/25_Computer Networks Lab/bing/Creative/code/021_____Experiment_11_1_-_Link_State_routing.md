### Experiment 11.1 - Link State Routing

- Link state routing is a type of routing algorithm that uses the information about the state of each link (such as bandwidth, delay, cost, etc.) to calculate the best path from one node to every other node in the network .
- Link state routing is also known as Dijkstra's algorithm, which is an iterative algorithm that finds the shortest path from a source node to all other nodes by using a priority queue to store the nodes with the least cost.
- Link state routing is different from distance-vector routing, which is another type of routing algorithm that uses the information about the distance and direction to each destination node to update the routing tables periodically .
- Link state routing has some advantages over distance-vector routing, such as faster convergence, lower bandwidth consumption, and more accurate and reliable routing information .
- Link state routing also has some disadvantages, such as higher memory and CPU requirements, more complex configuration and management, and vulnerability to flooding attacks .
- Link state routing protocols are one of the two main classes of routing protocols used in packet switching networks for computer communications, the other being distance-vector routing protocols.
- Examples of link state routing protocols include Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS), which are widely used in the Internet and other networks.
- The basic concept of link state routing is that every node constructs a map of the connectivity to the network, in the form of a graph, showing which nodes are connected to which other nodes.
- Each node then independently calculates the next best logical path from it to every possible destination in the network, using the link state information and the Dijkstra's algorithm .
- Link state routing involves two main processes: link state advertisement and link state database .
- Link state advertisement is the process of exchanging link state information among the nodes in the network, by sending messages from node to node, until all nodes have the same information .
- Link state database is the data structure that stores the link state information of the network, which is used by the Dijkstra's algorithm to compute the shortest paths .
- Link state routing requires each node to have a unique identifier, such as an IP address, and to know the identifiers of its directly connected neighbors .
- Link state routing also requires each node to periodically send hello messages to its neighbors, to check their availability and to exchange link state information .
- Link state routing can handle changes in the network topology, such as link failures or additions, by updating the link state information and recalculating the shortest paths .
- Link state routing can also handle loops and inconsistencies in the routing information, by using sequence numbers and aging mechanisms to discard old or duplicate link state information .
- Link state routing can be implemented in different ways, depending on the network size, topology, and requirements .
- Some of the design issues and challenges of link state routing include the frequency and size of link state advertisements, the synchronization and reliability of link state information, the scalability and efficiency of link state database, and the security and robustness of link state routing protocols .