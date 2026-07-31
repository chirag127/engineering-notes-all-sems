## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

- A Hamiltonian cycle is a cycle in a graph that visits every vertex exactly once and returns to the starting vertex.
- A graph is connected if there is a path between any two vertices.
- A graph is undirected if the edges have no direction, meaning that (u, v) and (v, u) are the same edge.
- Backtracking is a general algorithmic technique that tries different solutions recursively until a desired goal is reached or all possibilities are exhausted.
- To find all Hamiltonian cycles in a connected undirected graph G of n vertices using backtracking, we can use the following steps:

  1. Create an array path of size n to store the vertices of the current cycle. Initialize path[0] to any vertex in G.
  2. Define a function `isSafe(v, path, pos)` that returns true if vertex v can be added to path[pos] without violating the Hamiltonian cycle condition, i.e., v is adjacent to path[pos-1] and v is not already in path[0..pos-1].
  3. Define a function `hamCycleUtil(path, pos)` that recursively tries to extend the path from position pos. If pos == n, check if path[n-1] is adjacent to path[0] and print the cycle if yes. Otherwise, for each vertex v in G, if `isSafe(v, path, pos)` is true, add v to path[pos] and call `hamCycleUtil(path, pos+1)`. Backtrack by removing v from path[pos] after the recursive call returns.
  4. Call `hamCycleUtil(path, 1)` from the main function to start the backtracking process.

- Here is an example of the pseudocode for the algorithm:

```
// A function to check if v can be added to path[pos]
function isSafe(v, path, pos)
  // Check if v is adjacent to path[pos-1]
  if (G[path[pos-1]][v] == 0)
    return false
  // Check if v is already in path[0..pos-1]
  for i = 0 to pos-1
    if (path[i] == v)
      return false
  return true

// A recursive function to find all Hamiltonian cycles
function hamCycleUtil(path, pos)
  // Base case: all vertices are in the cycle
  if (pos == n)
    // Check if the last vertex is adjacent to the first vertex
    if (G[path[pos-1]][path[0]] == 1)
      // Print the cycle
      for i = 0 to n-1
        print path[i]
      print path[0]
      print "\n"
    return
  // Try different vertices as the next candidate
  for v = 0 to n-1
    // Check if v can be added to path[pos]
    if (isSafe(v, path, pos))
      // Add v to path[pos]
      path[pos] = v
      // Recur to construct the rest of the cycle
      hamCycleUtil(path, pos+1)
      // Backtrack by removing v from path[pos]
      path[pos] = -1

// A function to find all Hamiltonian cycles in G
function hamCycle(G)
  // Create an array path to store the cycle
  path = new array of size n
  // Initialize all vertices as unvisited
  for i = 0 to n-1
    path[i] = -1
  // Choose any vertex as the starting point
  path[0] = 0
  // Call the recursive function to find all cycles
  hamCycleUtil(path, 1)
```