
## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm

Dijkstra's algorithm is a graph search algorithm used to find the shortest path from one node to another in a weighted graph. It is often used in routing and as a subroutine in other graph algorithms.

The algorithm works by maintaining a set of nodes for which the shortest path from the source vertex is known. At each step, the algorithm adds the node with the lowest distance to the source to the set of known nodes and updates the distance of all its neighbors.

The algorithm works by:

1. Initializing the distance of the source vertex to 0 and all other nodes to infinity.
2. Selecting the unvisited node with the smallest distance from the source.
3. Updating the distance of all the neighbors of the selected node. 
4. Repeating steps 2 and 3 until all the nodes have been visited.

The algorithm can be used to find the shortest paths from a given vertex to all other vertices in a weighted connected graph. It can also be used to find the shortest path between two given vertices.