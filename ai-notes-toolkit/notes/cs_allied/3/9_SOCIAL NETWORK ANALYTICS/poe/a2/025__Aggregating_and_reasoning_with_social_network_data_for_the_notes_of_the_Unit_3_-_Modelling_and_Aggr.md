 Here is the formal notes in Markdown format without any feelings or friendliness:

### Aggregating and reasoning with social network data

1. Degree centrality - Counts the number of direct connections a node has to other nodes. Higher degree means the node is more central.
2. Betweenness centrality - Measures the number of shortest paths between all pairs of nodes that pass through a given node. Nodes with high betweenness centrality control the flow of information.
3. Closeness centrality - Measures the inverse of the sum of distances from a node to all other nodes. Nodes with high closeness centrality can reach other nodes more quickly.
4. Eigenvector centrality - Assigns relative scores to all nodes in the network based on the concept that connections to high-scoring nodes contribute more to the score of the node in question than equal connections to low-scoring nodes.
5. Clustering coefficient - Measures the extent to which nodes tend to cluster together in tightly knit groups. A higher clustering coefficient means more of a node's neighbors are also neighbors of each other.
6. Connected components - The largest subset of nodes in a network where there is a path between every pair of nodes. Networks can have multiple connected components if some nodes are not reachable from others.
7. Diameter - The longest shortest path between any two nodes in the network. A lower diameter means signals can spread more quickly through a network.

The nodes and connections in a social network can be analyzed using these metrics to identify influencers, bottlenecks, tightly-knit groups, and the overall efficiency of information spread. These metrics provide a macro-level understanding of network structure beyond the micro-level of individual nodes and ties. Reasoning about the implications of a network's aggregate properties allows researchers and practitioners to understand and potentially leverage social dynamics.