### Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

- Backtracking is a general algorithmic technique that involves incrementally building candidates to the solutions of a problem, and abandoning a candidate ("backtracking") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- Branch and Bound is another algorithmic technique that is used for solving optimization problems. It involves a systematic enumeration of all possible solutions by means of state space search: the set of all candidate solutions is thought of as forming a rooted tree with the full set at the root. 
- The Travelling Salesman Problem (TSP) is a classic example of a problem that can be solved using both Backtracking and Branch and Bound techniques. It is an optimization problem that involves finding the shortest possible route that visits every city exactly once and returns to the starting point.
- In Backtracking, we start with an initial solution and try to improve it by making small modifications at a time while testing the feasibility of the solution at each step. If we reach a point where the solution is no longer feasible, we backtrack to the previous step and try a different modification.
- In Branch and Bound, we create a tree of all possible solutions and iteratively eliminate branches that cannot lead to a better solution than the one found so far. 
- Other problems that can be solved using Backtracking and Branch and Bound techniques include Graph Coloring, n-Queen Problem, Hamiltonian Cycles, and Sum of Subsets.
- Graph Coloring is the problem of coloring the vertices of a graph in such a way that no two adjacent vertices share the same color. 
- The n-Queen Problem involves placing n chess queens on an n x n chessboard so that no two queens threaten each other. 
- Hamiltonian Cycles is the problem of finding a cycle that visits every vertex of a graph exactly once. 
- The Sum of Subsets problem is the problem of finding all possible subsets of a given set of numbers whose sum equals a given target value.
- When solving these problems using Backtracking and Branch and Bound techniques, it is important to keep track of the best solution found so far and to prune branches that cannot lead to a better solution.