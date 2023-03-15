### Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- The backtracking algorithm reduces the problem to the call `backtrack(root(P))`, where `backtrack` is the following recursive procedure: 

```python
procedure backtrack(P, c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        backtrack(P, s)
        s ← next(P, s)
```

- The procedure `backtrack` takes two arguments: a problem instance `P` and a partial candidate `c`. The procedure `reject` tests whether the partial candidate is worth completing, and returns `true` if it is not. The procedure `accept` tests whether the partial candidate is a solution, and returns `true` if it is. The procedure `output` prints or stores the solution. The procedure `first` generates the first extension of the partial candidate, and `next` generates the next extension after a given one. If there are no more extensions, `next` returns `NULL`.
- Backtracking is an important tool for solving constraint satisfaction problems, such as crosswords, verbal arithmetic, Sudoku, and many other puzzles. It is often the most convenient technique for parsing, for the knapsack problem and other combinatorial optimization problems. 
- A Hamiltonian cycle (or Hamiltonian circuit) is a cycle in an undirected graph that visits each vertex exactly once and also returns to the starting vertex. Finding a Hamiltonian cycle in a given graph is an NP-complete problem. 
- One way to find a Hamiltonian cycle in a graph is to use backtracking. The idea is to start from any vertex and keep adding adjacent vertices to the current path until either all vertices are visited or there is no more adjacent vertex to extend the path. If all vertices are visited, then check if there is an edge from the last vertex to the first vertex to complete the cycle. If there is no such edge, then backtrack and remove the last vertex from the path and try another adjacent vertex. If there is no more adjacent vertex to extend the path, then backtrack and remove the last vertex from the path and try another adjacent vertex. Repeat this process until either a Hamiltonian cycle is found or all possible paths are exhausted. 
- The following is a pseudocode for finding a Hamiltonian cycle using backtracking: 

```python
# Assume that the graph is represented by an adjacency matrix adj
# Assume that n is the number of vertices in the graph
# Assume that path is an array of size n to store the current path
# Assume that pos is the current position in the path array
# Assume that v is the current vertex to be added to the path

procedure hamiltonian(v, pos) is
    # Base case: all vertices are visited
    if pos == n then
        # Check if there is an edge from the last vertex to the first vertex
        if adj[v][path[0]] == 1 then
            # A Hamiltonian cycle is found
            output(path)
            return true
        else
            # No Hamiltonian cycle is possible
            return false
    # Recursive case: try all possible extensions of the current path
    for u in range(n) do
        # Check if u is adjacent to v and not already in the path
        if adj[v][u] == 1 and u not in path[0..pos-1] then
            # Add u to the path
            path[pos] = u
            # Recursively extend the path from u
            if hamiltonian(u, pos+1) then
                return true
            # Backtrack and remove u from the path
            path[pos] = -1
    # No extension is possible
    return false

# Start from any vertex as the first vertex in the path