## Design and implement to find all Hamiltonian Cycles in a connected undirected Graph G of n vertices using backtracking principle.

A Hamiltonian cycle is a cycle in a graph that visits every vertex exactly once and returns to the starting vertex. Finding all Hamiltonian cycles in a graph is an NP-hard problem, meaning that there is no known efficient algorithm to solve it in polynomial time. However, using the backtracking principle, we can design and implement a recursive algorithm that explores all possible paths in the graph and checks if they form a Hamiltonian cycle.

The backtracking principle is a general technique for solving combinatorial problems, where we incrementally build a solution and discard partial solutions that do not lead to a complete solution. The idea is to use a depth-first search (DFS) to traverse the graph, and maintain a boolean array `visited` to keep track of the vertices that have been visited so far. We also maintain a list `path` to store the current path of vertices.

The algorithm works as follows:

- Start from any vertex `v` and mark it as visited. Add `v` to the path.
- For each neighbor `u` of `v` that is not visited, recursively call the algorithm with `u` as the current vertex.
- If the path contains `n` vertices and the last vertex is adjacent to the first vertex, then we have found a Hamiltonian cycle. Print or store the path as a solution.
- Backtrack by removing `v` from the path and marking it as unvisited. Return to the previous vertex.

The pseudocode of the algorithm is given below:

```
# Input: a graph G of n vertices, a starting vertex v, a visited array, and a path list
# Output: print or store all Hamiltonian cycles in G

def findHamiltonianCycles(G, v, visited, path):
  # Mark the current vertex as visited and add it to the path
  visited[v] = true
  path.append(v)

  # If the path contains n vertices and the last vertex is adjacent to the first vertex
  if len(path) == n and G[v][path[0]] == 1:
    # Print or store the path as a solution
    print(path)

  # For each neighbor u of v that is not visited
  for u in range(n):
    if G[v][u] == 1 and visited[u] == false:
      # Recursively call the algorithm with u as the current vertex
      findHamiltonianCycles(G, u, visited, path)

  # Backtrack by removing v from the path and marking it as unvisited
  visited[v] = false
  path.pop()
```

The time complexity of the algorithm is O(n!), since there are at most n! permutations of the vertices to check. The space complexity is O(n), since we need to store the visited array and the path list.