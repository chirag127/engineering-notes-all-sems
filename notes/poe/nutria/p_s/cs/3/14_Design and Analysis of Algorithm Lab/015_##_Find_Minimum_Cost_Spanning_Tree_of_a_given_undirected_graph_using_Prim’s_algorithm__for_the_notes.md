
## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm
Prim’s algorithm is a greedy algorithm used for finding the minimum cost spanning tree of a given undirected graph. It is used in the Design and Analysis of Algorithm Lab in the subject of Real Time System. 

The algorithm works by repeatedly adding the minimum cost edges to the spanning tree, until all the vertices of the graph are included in the tree.

The algorithm works in the following steps:
1. Select an arbitrary vertex from the graph and add it to the spanning tree.
2. Find the edge from the selected vertex to the vertex not yet included in the spanning tree, with the least cost.
3. Add this edge to the spanning tree.
4. Repeat steps 2 and 3 until all the vertices of the graph are included in the spanning tree.

The cost of the spanning tree is the sum of the costs of all the edges in the tree.

Advantages of Prim’s algorithm:
- It is simple and easy to implement.
- It finds the minimum cost spanning tree of the graph.

Disadvantages of Prim’s algorithm:
- It is not suitable for graphs with negative edge weights.
- It is not suitable for graphs with more than one connected component.

Applications of Prim’s algorithm:
- It is used in network design, such as in the design of telephone networks and computer networks.
- It is used in finding the shortest path between two vertices in a graph.
- It is used in finding the minimum cost of connecting all the cities in a country through roads.
- It is used in cluster analysis for finding the minimum cost of connecting the clusters.