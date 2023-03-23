 Here are the notes for the topic -

Backtracking, Branch and Bound with Examples Such as Graph Coloring

### Backtracking
- Backtracking is a general algorithmic technique that considers all possible candidates for a solution and abandons each partial candidate c ("backtracks") as soon as it is clear that it cannot lead to a valid solution.
- It is often used for finding all (or some) solutions to some computational problems, particularly in constraint satisfaction problems.
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem.
- The partial candidates are represented by the values assigned to some variables of the problem.

### Branch and Bound
- Branch and bound is a general algorithmic method for discrete and combinatorial optimization.
- It consists of a systematic enumeration of candidate solutions by means of state space search: the set of candidate solutions is thought of as forming a rooted tree with the full set at the root.
- The algorithm iteratively partitions the search space into subsets(branches) by making choices, then prunes (bounds) some of those subsets, narrowing down the search.
- The pruning is done by usingupper and lower bounds on the optimal solution; the subsets for which a provable lower bound exceeds a known upper bound cannot contain the optimal solution, so they can be cut (pruned) from the search.

### Examples
- Graph Coloring - Assigning colors to vertices of a graph such that no two adjacent vertices have the same color. Backtracking can be used to find a valid coloring.
- Travelling Salesman Problem - Finding the shortest tour that visits each city exactly once. Branch and bound can be used where lower bounds are calculated using nearest neighbor heuristics.
- n-Queen Problem - Placing n queens on an n×n chessboard such that no two queens attack each other. Backtracking can be used by trying different rows for each queen.
- Hamiltonian Cycles - Finding a cycle that visits each vertex exactly once. Backtracking can be used by trying to extend a partial cycle.
- Sum of Subsets - Finding a subset of numbers that adds up to a given sum. Backtracking can be used by trying different numbers to add to the subset.