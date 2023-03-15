### Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- Backtracking can be applied to problems that can be formulated as a state space tree, where each node represents a partial solution and each edge represents a possible extension of the solution. The root node corresponds to the initial state and the leaf nodes correspond to the final states.  
- The backtracking algorithm traverses the state space tree in a depth-first manner, exploring one branch of the tree until it reaches a dead end or a solution, and then backtracks to the previous node and tries another branch.  
- The backtracking algorithm can be generalized by the following recursive procedure: 

```
procedure backtrack(P, c) is
  if reject(P, c) then return
  if accept(P, c) then output(P, c)
  s ← first(P, c)
  while s ≠ NULL do
    backtrack(P, s)
    s ← next(P, s)
```

- Here, P is the problem instance, c is a partial candidate, reject(P, c) is a function that returns true if c is not a valid partial solution, accept(P, c) is a function that returns true if c is a complete and valid solution, output(P, c) is a function that prints or stores the solution, first(P, c) is a function that returns the first extension of c, and next(P, c) is a function that returns the next extension of c.
- The backtracking algorithm can be customized for different problems by defining the appropriate functions and data structures for the problem domain. For example, for the n-queens problem, the partial candidates can be represented by an array of size n, where each element stores the column number of a queen placed in a row, and the functions can check the validity of the placement and generate the next possible placement. 
- One of the examples of backtracking is the Hamiltonian cycle problem, which is to find a simple cycle that visits every vertex of a graph exactly once. A possible way to solve this problem using backtracking is: 

```
procedure hamiltonian(G, v) is
  if v is the first vertex then
    mark v as visited
    add v to the cycle
  if all vertices are visited then
    if there is an edge from v to the first vertex then
      output the cycle
    else
      return
  for each neighbor u of v in G do
    if u is not visited then
      mark u as visited
      add u to the cycle
      hamiltonian(G, u)
      remove u from the cycle
      mark u as unvisited
```

- Here, G is the graph, v is the current vertex, and the cycle is a list of vertices that stores the partial candidate. The algorithm starts from an arbitrary vertex and tries to extend the cycle by visiting its neighbors recursively, until all vertices are visited or no extension is possible. If a cycle is found, it is printed or stored, and the algorithm backtracks to try another possibility.