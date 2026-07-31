## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

- A Hamiltonian cycle is a cycle in an undirected graph that visits each vertex exactly once and returns to the starting vertex.
- Finding a Hamiltonian cycle in a graph is an NP-complete problem, meaning that there is no known efficient algorithm to solve it in polynomial time.
- However, using backtracking, we can explore the possible paths in the graph and prune the search space when we encounter a dead end or a repeated vertex.
- The backtracking algorithm can be summarized as follows:

  - Start from any vertex and mark it as visited.
  - For each adjacent vertex that is not visited, add it to the current path and recursively check if this path can be extended to a Hamiltonian cycle.
  - If the path can be extended, return true and print the path.
  - If the path cannot be extended, remove the last vertex from the path and mark it as unvisited, then backtrack to the previous vertex and try another adjacent vertex.
  - If all adjacent vertices have been tried and none of them can extend the path, return false and indicate that there is no Hamiltonian cycle.

- The pseudocode for the backtracking algorithm is given below:

  ```
  // Input: a graph G of n vertices
  // Output: true if there is a Hamiltonian cycle, false otherwise
  function hamiltonianCycle(G):
    // create an array to store the path
    path = []
    // create a boolean array to mark the visited vertices
    visited = [false] * n
    // choose any vertex as the starting point
    start = 0
    // add the start vertex to the path and mark it as visited
    path.append(start)
    visited[start] = true
    // call the recursive helper function to find the cycle
    return hamiltonianCycleHelper(G, path, visited, start)

  // Input: a graph G, a path array, a visited array, and the current vertex
  // Output: true if the path can be extended to a Hamiltonian cycle, false otherwise
  function hamiltonianCycleHelper(G, path, visited, curr):
    // base case: if the path length is equal to the number of vertices
    if len(path) == n:
      // check if there is an edge from the last vertex to the start vertex
      if G[curr][start] == 1:
        // print the path as a cycle
        print(path + [start])
        // return true to indicate that a cycle is found
        return true
      else:
        // return false to indicate that the path cannot be extended
        return false
    // recursive case: for each adjacent vertex of the current vertex
    for i in range(n):
      // if the vertex is not visited and there is an edge from the current vertex to it
      if visited[i] == false and G[curr][i] == 1:
        // add the vertex to the path and mark it as visited
        path.append(i)
        visited[i] = true
        // recursively check if the path can be extended
        if hamiltonianCycleHelper(G, path, visited, i):
          // return true if a cycle is found
          return true
        // if the path cannot be extended, remove the vertex from the path and mark it as unvisited
        path.pop()
        visited[i] = false
    // if all adjacent vertices have been tried and none of them can extend the path, return false
    return false
  ```
- The time complexity of the backtracking algorithm is O(n!), since there are n! possible permutations of the vertices, and each permutation is checked for validity in O(n) time.
- The space complexity of the backtracking algorithm is O(n), since the path and visited arrays use O(n) space, and the recursive stack also uses O(n) space in the worst case.