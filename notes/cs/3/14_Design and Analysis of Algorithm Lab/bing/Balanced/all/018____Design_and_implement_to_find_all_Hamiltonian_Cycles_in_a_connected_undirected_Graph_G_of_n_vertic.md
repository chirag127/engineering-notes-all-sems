## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

- A Hamiltonian cycle is a cycle in a graph that visits every vertex exactly once and returns to the starting vertex.
- A graph is connected if there is a path between any two vertices.
- A graph is undirected if the edges have no direction, meaning that (u, v) and (v, u) are the same edge.
- Backtracking is a general algorithmic technique that tries different solutions recursively until a desired goal is reached or all possibilities are exhausted.
- To find all Hamiltonian cycles in a connected undirected graph G of n vertices using backtracking, we can use the following steps:

  - Start from any vertex v and mark it as visited.
  - Add v to the current path and check if the path is a Hamiltonian cycle. If yes, print or store the path and backtrack to the previous vertex.
  - For each neighbor u of v that is not visited, recursively explore the graph from u, marking u as visited and adding it to the path.
  - After exploring all neighbors of v, unmark v as visited and remove it from the path.
  - Repeat the above steps for all vertices as the starting point.

- The pseudocode for the algorithm is given below:

  ```
  // G is the adjacency matrix of the graph
  // n is the number of vertices
  // path is an array to store the current path
  // pos is the current position in the path
  // visited is a boolean array to mark the visited vertices

  // A function to check if the vertex v can be added to the path
  function isSafe(v, G, path, pos)
    // Check if v is adjacent to the last vertex in the path
    if G[path[pos - 1]][v] == 0
      return false
    // Check if v is already in the path
    for i = 0 to pos - 1
      if path[i] == v
        return false
    return true

  // A recursive function to find all Hamiltonian cycles
  function findHamiltonianCycles(G, path, pos, visited)
    // Base case: the path is a Hamiltonian cycle
    if pos == n
      // Check if the last vertex is adjacent to the first vertex
      if G[path[pos - 1]][path[0]] == 1
        // Print or store the path
        print path
      return
    // Try different vertices as the next candidate
    for v = 0 to n - 1
      // Check if v can be added to the path
      if isSafe(v, G, path, pos)
        // Mark v as visited and add it to the path
        visited[v] = true
        path[pos] = v
        // Recursively explore the graph from v
        findHamiltonianCycles(G, path, pos + 1, visited)
        // Backtrack to the previous vertex
        visited[v] = false
        path[pos] = -1

  // A function to initialize the algorithm
  function findAllHamiltonianCycles(G)
    // Initialize the path, visited and position arrays
    path = new int[n]
    visited = new boolean[n]
    pos = 0
    // Fill the path and visited arrays with -1 and false respectively
    for i = 0 to n - 1
      path[i] = -1
      visited[i] = false
    // Call the recursive function for each vertex as the starting point
    for v = 0 to n - 1
      // Mark v as visited and add it to the path
      visited[v] = true
      path[pos] = v
      // Recursively explore the graph from v
      findHamiltonianCycles(G, path, pos + 1, visited)
      // Backtrack to the previous vertex
      visited[v] = false
      path[pos] = -1
  ```