### Backtracking with Examples Such as Hamiltonian Cycles

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- Backtracking can be viewed as a depth-first search of a state space tree, where each node represents a partial solution, and the branches are the possible extensions of the partial solution. 
- Backtracking can be applied to problems that involve making a sequence of decisions, such as finding a path in a maze, placing queens on a chessboard, or coloring a graph. 
- A general backtracking algorithm can be described as follows: 

```
procedure backtrack(P, c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        backtrack(P, s)
        s ← next(P, s)
```

- Here, P is the problem instance, c is a candidate solution, reject is a function that checks if c is invalid, accept is a function that checks if c is a complete solution, output is a function that prints or stores the solution, first is a function that returns the first extension of c, and next is a function that returns the next extension of c.
- An example of a problem that can be solved by backtracking is the Hamiltonian cycle problem, which asks whether there is a cycle in a given graph that visits every vertex exactly once. 
- A possible backtracking algorithm for this problem is: 

```
procedure hamiltonian(G, v) is
    if v is the first vertex then
        mark v as visited
        add v to the cycle
    if all vertices are visited then
        if there is an edge from v to the first vertex then
            output the cycle
            return true
        else
            return false
    for each neighbor u of v do
        if u is not visited then
            mark u as visited
            add u to the cycle
            if hamiltonian(G, u) then
                return true
            else
                unmark u as visited
                remove u from the cycle
    return false
```

- Here, G is the graph, v is the current vertex, and the cycle is a list of vertices that forms the potential solution. The algorithm starts from an arbitrary vertex, and recursively explores all possible extensions of the cycle, backtracking when a dead end is reached. The algorithm outputs the cycle if it finds one, or returns false otherwise.