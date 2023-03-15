# Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
- Backtracking can be viewed as a way of traversing a state space tree, which is a tree representing all the possible states (solution or nonsolution) of the problem.
- The backtracking algorithm reduces the problem to the call `backtrack(root(P))`, where `backtrack` is the following recursive procedure:

```
procedure backtrack(P, c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        backtrack(P, s)
        s ← next(P, s)
```

- The procedure `backtrack` takes two arguments: a problem instance `P` and a candidate `c`. The procedure `reject` tests whether the candidate is worth completing, and returns true if it is not. The procedure `accept` tests whether the candidate is a solution, and returns true if it is. The procedure `output` processes the solution in some way. The procedure `first` generates the first extension of the candidate, and `next` generates the next alternative extension after a given one. If there are no more extensions, `next` returns NULL.
- A common example of a problem that can be solved by backtracking is the Hamiltonian cycle problem, which is to find a cycle in a graph that visits every vertex exactly once. A possible backtracking algorithm for this problem is as follows:

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
    for each neighbor u of v do
        if u is not visited then
            mark u as visited
            add u to the cycle
            hamiltonian(G, u)
            remove u from the cycle
            mark u as unvisited
```

- The procedure `hamiltonian` takes two arguments: a graph `G` and a vertex `v`. The procedure marks `v` as visited and adds it to the cycle. If all vertices are visited, it checks if there is an edge from `v` to the first vertex, and outputs the cycle if there is. Otherwise, it returns. Then, it loops through all the neighbors of `v`, and recursively calls `hamiltonian` on each unvisited neighbor, after marking it as visited and adding it to the cycle. After the recursive call, it removes the neighbor from the cycle and marks it as unvisited, and continues with the next neighbor.