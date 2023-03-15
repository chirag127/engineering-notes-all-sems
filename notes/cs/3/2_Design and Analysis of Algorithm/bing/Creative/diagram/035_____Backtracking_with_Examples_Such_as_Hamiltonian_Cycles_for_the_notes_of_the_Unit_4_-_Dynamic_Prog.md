### Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- The backtracking algorithm can be described by the following recursive procedure:

```
procedure backtrack(P, c) is
  if reject(P, c) then return
  if accept(P, c) then output(P, c)
  s ← first(P, c)
  while s ≠ NULL do
    backtrack(P, s)
    s ← next(P, s)
```

- Here, P is the problem instance, c is a partial candidate, reject(P, c) is a boolean function that returns true if c cannot be extended to a valid solution, accept(P, c) is a boolean function that returns true if c is a valid solution, output(P, c) is a procedure that prints or stores the solution c, first(P, c) is a function that returns the first extension of c, and next(P, s) is a function that returns the next extension of c after s. 
- Backtracking is an important tool for solving constraint satisfaction problems, such as crosswords, verbal arithmetic, Sudoku, and many other puzzles. It is often the most convenient technique for parsing, for the knapsack problem and other combinatorial optimization problems. 
- A Hamiltonian cycle is a cycle in an undirected graph that visits each vertex exactly once and returns to the starting vertex. Finding a Hamiltonian cycle in a graph is an NP-complete problem, meaning that there is no known polynomial-time algorithm that can solve it in general. However, backtracking can be used to find all possible Hamiltonian cycles in a graph, if any exist, by exploring the state space tree of the problem. 
- The state space tree of the Hamiltonian cycle problem is a tree representing all the possible ways of choosing the next vertex to visit in the cycle, starting from an arbitrary vertex. Each node of the tree corresponds to a partial candidate, which is a sequence of vertices that forms a path in the graph. The root node is an empty sequence, and the children of a node are obtained by appending a vertex that is adjacent to the last vertex in the sequence and has not been visited before. The leaf nodes are either valid solutions (sequences that form a cycle and visit all vertices) or rejected candidates (sequences that cannot be extended to a valid solution). 
- The backtracking algorithm for finding Hamiltonian cycles can be implemented as follows:

```
procedure hamiltonian(G, v) is
  if v is the first vertex then
    add v to the path
    if path length is n then
      if v is adjacent to the first vertex then
        output the path as a solution
      return
  else
    if v is not in the path then
      add v to the path
      for each neighbor u of v do
        hamiltonian(G, u)
      remove v from the path
```

- Here, G is the graph, v is the current vertex, n is the number of vertices in the graph, and path is a global variable that stores the partial candidate. The algorithm starts from an arbitrary vertex and recursively explores the state space tree by adding a vertex to the path and calling the procedure for each of its neighbors. If the path length reaches n, the algorithm checks if the last vertex is adjacent to the first vertex, and if so, outputs the path as a solution. If the path cannot be extended to a valid solution, the algorithm backtracks by removing the last vertex from the path and trying another option.