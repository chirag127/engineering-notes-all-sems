## Design and Implement to Find All Hamiltonian Cycles in a Connected Undirected Graph G of n Vertices Using Backtracking Principle

Hamiltonian cycle is a cycle in an undirected graph G that passes through each vertex exactly once. Finding all Hamiltonian cycles in a connected undirected graph is an important problem in graph theory. In this lab, we will learn how to design and implement an algorithm to find all Hamiltonian cycles in a connected undirected graph G of n vertices using the backtracking principle.

### Algorithm Design

The algorithm to find all Hamiltonian cycles in a connected undirected graph G of n vertices using backtracking principle can be designed using the following steps:

1. Initialize an empty list to store all Hamiltonian cycles.
2. Choose a vertex v from the graph G.
3. Add v to the current path and mark it as visited.
4. If the current path contains all n vertices, add it to the list of Hamiltonian cycles and return.
5. Otherwise, for each unvisited neighbor u of v, add u to the current path and mark it as visited.
6. Recursively call the algorithm on the updated path and unmark u.
7. If no Hamiltonian cycle is found, remove v from the current path and mark it as unvisited.

### Algorithm Analysis

The time complexity of the algorithm to find all Hamiltonian cycles in a connected undirected graph G of n vertices using backtracking principle is O(n!) as there can be n! possible permutations of vertices in a Hamiltonian cycle. However, the actual time complexity may vary depending on the structure of the graph and the chosen vertex.

### Advantages and Disadvantages

Advantages:
- The algorithm can find all Hamiltonian cycles in a connected undirected graph of n vertices.
- The algorithm can be implemented using simple data structures like lists and arrays.

Disadvantages:
- The time complexity of the algorithm is O(n!), which can be impractical for large values of n.
- The algorithm may not terminate if the graph does not contain a Hamiltonian cycle.

### Example

Let's consider the following graph with 4 vertices:

```
   1
 / | \
2--3--4
```

The algorithm to find all Hamiltonian cycles in this graph using backtracking principle can be executed as follows:

1. Choose vertex 1 as the starting vertex.
2. Add vertex 1 to the current path and mark it as visited.
3. Choose vertex 2 as the next vertex and add it to the current path. Mark vertex 2 as visited.
4. Choose vertex 3 as the next vertex and add it to the current path. Mark vertex 3 as visited.
5. Choose vertex 4 as the next vertex and add it to the current path. Mark vertex 4 as visited.
6. The current path contains all vertices, so add it to the list of Hamiltonian cycles.
7. Remove vertex 4 from the current path and mark it as unvisited.
8. Choose vertex 3 as the next vertex and add it to the current path. Mark vertex 3 as visited.
9. Choose vertex 4 as the next vertex and add it to the current path. Mark vertex 4 as visited.
10. The current path contains all vertices, so add it to the list of Hamiltonian cycles.
11. Remove vertex 4 from the current path and mark it as unvisited.
12. Remove vertex 3 from the current path and mark it as unvisited.
13. Choose vertex 4 as the next vertex and add it to the current path. Mark vertex 4 as visited.
14. The current path does not contain all vertices, so backtrack.
15. Remove vertex 4 from the current path and mark it as unvisited.
16. Remove vertex 2 from the current path and mark it as unvisited.
17. Choose vertex 3 as the next vertex and add it to the current path. Mark vertex 3 as visited.
18. Choose vertex 4 as the next vertex and add it to the current path. Mark vertex 4 as visited.
19. The current path contains all vertices, so add it to the list of Hamiltonian cycles.
20. Remove vertex 4 from the current path and mark it as unvisited.
21. Remove vertex 3 from the current path and mark it as unvisited.
22. Remove vertex 1 from the current path and mark it as unvisited.
23. Choose vertex 2 as the next vertex and repeat the algorithm.

The list of Hamiltonian cycles for the given graph is {(1, 2, 3, 4), (1, 4, 3, 2), (2, 3, 4, 1), (4, 3, 2, 1)}.

### Applications

The algorithm to find all Hamiltonian cycles in a connected undirected graph G of n vertices using backtracking principle has applications in various fields such as:
- Network routing
- Chemical graph theory