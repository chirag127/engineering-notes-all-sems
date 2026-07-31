### Temporary Ordered Routing Algorithm (TORA)

TORA is a distributed routing protocol used in ad hoc networks. It is a reactive routing protocol that adjusts the routing tables based on the changes in network topology. 

Here are some key points about TORA:

- TORA is a hop-by-hop routing protocol, which means that each node maintains a routing table for its immediate neighbors.

- Each node in TORA maintains three types of information:

  - Height: The distance to the destination node in the network.
  
  - Set of predecessors: The set of nodes that have a lower height value than the current node.
  
  - Set of successors: The set of nodes that have a higher height value than the current node.
  
- The nodes in TORA are organized into a directed acyclic graph (DAG), with the source node at the top and the destination node at the bottom.

- When a node wants to send a packet to a destination, it first broadcasts a query packet to its neighbors asking for the height of the destination node.

- Each node that receives a query packet responds with its height and the set of its neighbors that have a lower height value.

- Based on this information, the source node can construct a route to the destination by selecting a path through the DAG that goes from nodes with a higher height value to nodes with a lower height value.

- TORA is a temporary routing algorithm because the routing tables are recomputed whenever there is a change in the network topology.

- TORA is suitable for networks with high mobility because it can quickly adapt to changes in the network topology.

- TORA is also suitable for networks with a large number of nodes because the routing tables are maintained only for the immediate neighbors, which reduces the storage and processing overhead.

In conclusion, TORA is an efficient and scalable routing protocol for ad hoc networks that can handle high mobility and a large number of nodes.