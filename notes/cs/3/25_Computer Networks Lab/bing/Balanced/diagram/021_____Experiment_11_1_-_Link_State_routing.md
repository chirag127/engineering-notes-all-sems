### Experiment 11.1 - Link State Routing

- Link state routing is a type of routing algorithm that uses the information about the state of each link (such as bandwidth, delay, cost, etc.) to calculate the best path from one node to every other node in the network.
- Link state routing is also known as Dijkstra's algorithm, which is an iterative algorithm that finds the shortest path from a source node to all other nodes by using a priority queue to store the nodes with the least cost paths.
- Link state routing requires each node to construct a map of the network topology, which is a graph that shows the nodes and the links between them. Each node exchanges messages with its neighbors to learn the state of each link, and then broadcasts this information to all other nodes in the network.
- Link state routing has some advantages over distance-vector routing, such as faster convergence, less routing loops, and more accurate routing information. However, link state routing also has some disadvantages, such as higher memory and CPU usage, more bandwidth consumption, and more complexity.
- Link state routing protocols are widely used in packet switching networks for computer communications, such as the Internet. Some examples of link state routing protocols are Open Shortest Path First (OSPF) and Intermediate System to Intermediate System (IS-IS).
- Link state routing protocols have some common features, such as:
  - Hello protocol: A mechanism to establish and maintain neighbor relationships between nodes.
  - Link state advertisement (LSA): A message that contains the information about the state of a link or a group of links.
  - Link state database (LSDB): A data structure that stores the LSAs received from all other nodes in the network.
  - Link state request (LSR): A message that requests a specific LSA from another node.
  - Link state update (LSU): A message that contains one or more LSAs to be sent to another node.
  - Link state acknowledgment (LSAck): A message that confirms the receipt of an LSU from another node.
  - Shortest path first (SPF) algorithm: A procedure that calculates the best path from a node to all other nodes in the network by using the LSDB as the input.