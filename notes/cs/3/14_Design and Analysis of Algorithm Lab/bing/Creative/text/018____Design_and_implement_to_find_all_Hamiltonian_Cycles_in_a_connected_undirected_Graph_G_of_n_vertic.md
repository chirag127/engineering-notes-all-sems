## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

- A Hamiltonian cycle is a cycle in a graph that visits every vertex exactly once and returns to the starting vertex.
- A graph is connected if there is a path between any two vertices.
- A graph is undirected if the edges have no direction, meaning that (u, v) and (v, u) are the same edge.
- Backtracking is a general algorithmic technique that tries different solutions recursively until a desired goal is reached or no more solutions are possible.
- To find all Hamiltonian cycles in a connected undirected graph G of n vertices using backtracking, we can use the following steps:

  1. Create an array path of size n to store the vertices of the current cycle. Initialize path[0] to any vertex in G.
  2. Create a boolean matrix visited of size n x n to keep track of the edges that have been used in the current cycle. Initialize all entries to false.
  3. Define a recursive function hamCycle(G, path, pos) that takes the graph G, the path array, and the current position pos as parameters and returns true if a Hamiltonian cycle is found, and false otherwise.
  4. In the function hamCycle, if pos is equal to n, check if there is an edge from path[n-1] to path[0] in G. If yes, print the path array as a Hamiltonian cycle and return true. If no, return false.
  5. For each vertex v in G that is adjacent to path[pos-1] and not visited, do the following:
    - Mark the edge (path[pos-1], v) as visited by setting visited[path[pos-1]][v] to true.
    - Add v to the path array by setting path[pos] to v.
    - Recursively call hamCycle(G, path, pos+1) and store the result in a boolean variable res.
    - If res is true, return true.
    - Otherwise, backtrack by unmarking the edge (path[pos-1], v) as visited by setting visited[path[pos-1]][v] to false and removing v from the path array by setting path[pos] to -1.
  6. If no vertex can be added to the path array, return false.
  7. Call the function hamCycle(G, path, 1) and return its result.