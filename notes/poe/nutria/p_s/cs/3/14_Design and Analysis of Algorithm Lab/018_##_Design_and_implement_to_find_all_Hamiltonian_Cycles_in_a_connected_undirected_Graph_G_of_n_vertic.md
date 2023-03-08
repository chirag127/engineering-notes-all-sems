
## Design and Implement to Find All Hamiltonian Cycles in a Connected Undirected Graph G of n Vertices Using Backtracking Principle

Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time. In the context of Hamiltonian cycles, backtracking can be used to find all possible Hamiltonian cycles in a connected undirected graph G of n vertices.

### Algorithm

1. Start with a vertex v of the graph G.
2. Mark v as visited and store it in the current path.
3. Check if there is an edge from the current vertex v to any other unvisited vertex w.
   - If there is no such edge, then backtrack to the previous vertex in the path.
   - If there is an edge from v to w, mark w as visited and store it in the current path.
4. If all the vertices in the current path are visited, then a Hamiltonian cycle is found.
5. If all the vertices in the current path are not visited, then repeat steps 2-4 for the current vertex w.

### Advantages

- The backtracking approach to finding Hamiltonian cycles is relatively simple and easy to understand.
- It is a general approach that can be used to find all possible Hamiltonian cycles in a graph.

### Disadvantages

- The backtracking approach can be time-consuming, as it requires checking all possible paths in the graph.
- It is not the most efficient approach to finding Hamiltonian cycles, as it may lead to unnecessary computations.

### Examples

Consider the following graph G with 8 vertices:

![Graph G](https://i.imgur.com/K5U6VjK.png)

Using the backtracking approach, the following Hamiltonian cycles can be found in the graph G:

- (A, B, C, D, E, F, G, H, A)
- (A, B, E, F, G, H, A, C, D)
- (A, B, E, F, G, C, D, H, A)
- (A, B, E, D, C, F, G, H, A)

### Applications

- The backtracking approach can be used to solve the travelling salesman problem, which is a problem of finding the shortest possible route that visits each city exactly once.
- It can also be used to solve other optimization problems, such as the knapsack problem.