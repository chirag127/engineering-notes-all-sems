
## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm

Prim's algorithm is a greedy algorithm used to find a minimum cost spanning tree of a given undirected graph. It works by building a tree one vertex at a time, always choosing the cheapest edge that connects the current tree to a new vertex.

The algorithm starts with a single vertex, and then adds the cheapest edge connecting it to the graph. It continues to add the cheapest edge connecting the tree to a new vertex until all vertices in the graph are included in the tree.

The following steps outline the algorithm:

1. Initialize a tree with a single vertex, chosen arbitrarily from the graph.
2. Find the cheapest edge from the tree to a vertex not yet in the tree.
3. Add the cheapest edge to the tree.
4. Repeat steps 2 and 3 until all vertices are in the tree.

The resulting tree is a minimum cost spanning tree of the graph.