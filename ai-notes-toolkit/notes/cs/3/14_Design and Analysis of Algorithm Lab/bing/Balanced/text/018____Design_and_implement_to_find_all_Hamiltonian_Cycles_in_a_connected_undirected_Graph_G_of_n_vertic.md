## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

- A Hamiltonian cycle is a cycle in a graph that visits every vertex exactly once and returns to the starting vertex.
- A graph is connected if there is a path between any pair of vertices.
- A graph is undirected if the edges have no direction, meaning that (u, v) and (v, u) are the same edge.
- Backtracking is a general algorithmic technique that tries different solutions recursively until a valid solution is found or all possibilities are exhausted.
- To find all Hamiltonian cycles in a connected undirected graph G of n vertices using backtracking, we can use the following algorithm:

  - Create an array path of size n, where path[i] will store the i-th vertex in the cycle.
  - Initialize path[0] to any vertex in G, and mark it as visited.
  - Define a recursive function hamCycle(path, pos) that takes the current path and the position of the last vertex added to the path as parameters.
  - If pos == n, check if there is an edge from path[n-1] to path[0]. If yes, then we have found a Hamiltonian cycle and we can print or store the path. If no, then return false.
  - For each vertex v in G that is adjacent to path[pos-1] and not visited, do the following:
    - Mark v as visited and add it to path[pos].
    - Call hamCycle(path, pos+1) recursively. If it returns true, then return true.
    - Unmark v as visited and remove it from path[pos].
  - If no vertex can be added to the path, then return false.