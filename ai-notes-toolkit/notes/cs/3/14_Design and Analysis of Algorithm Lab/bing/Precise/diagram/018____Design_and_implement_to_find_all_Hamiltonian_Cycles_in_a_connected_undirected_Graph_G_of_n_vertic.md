## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle

A Hamiltonian cycle is a cycle in an undirected graph that visits each vertex exactly once and returns to the starting vertex. The problem of finding all Hamiltonian cycles in a graph is a well-known NP-complete problem.

One approach to finding all Hamiltonian cycles in a graph is to use the backtracking principle. This involves recursively exploring all possible paths in the graph, while keeping track of the vertices visited so far. If a path visits all vertices exactly once and returns to the starting vertex, it is a Hamiltonian cycle.

The algorithm can be implemented as follows:

1. Start with an empty path and a boolean array to keep track of visited vertices.
2. Add the starting vertex to the path and mark it as visited.
3. For each unvisited neighbor of the current vertex, add it to the path and mark it as visited. Recursively call the function with the new path and visited array.
4. If the path contains all vertices and the last vertex is a neighbor of the starting vertex, the path is a Hamiltonian cycle. Add it to the list of Hamiltonian cycles.
5. Backtrack by removing the current vertex from the path and marking it as unvisited.

This algorithm will find all Hamiltonian cycles in a connected undirected graph using the backtracking principle. It has an exponential time complexity, as it explores all possible paths in the graph. However, it can be an effective approach for small graphs or graphs with certain properties that make it easier to find Hamiltonian cycles.