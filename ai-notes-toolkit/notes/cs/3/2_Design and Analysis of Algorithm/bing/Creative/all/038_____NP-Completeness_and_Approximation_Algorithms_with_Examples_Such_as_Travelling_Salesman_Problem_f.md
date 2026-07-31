# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets

## NP-Completeness

- NP-Completeness is a concept in computational complexity theory that deals with the difficulty of solving certain problems using algorithms.
- A problem is said to be NP (nondeterministic polynomial) if it can be solved in polynomial time by a nondeterministic algorithm, which is an algorithm that can make random choices at each step.
- A problem is said to be NP-Complete if it is NP and also every other NP problem can be reduced to it in polynomial time, which means that there is a way to transform any NP problem into an instance of the NP-Complete problem such that the original problem can be solved by solving the transformed problem.
- NP-Complete problems are the hardest problems in NP, and no efficient algorithm is known to solve them in polynomial time. If any NP-Complete problem can be solved in polynomial time, then all NP problems can be solved in polynomial time, which would imply that P = NP, where P is the class of problems that can be solved in polynomial time by a deterministic algorithm. This is one of the most famous open questions in computer science.
- Some examples of NP-Complete problems are the Travelling Salesman Problem, the Graph Coloring Problem, the n-Queen Problem, the Hamiltonian Cycle Problem, and the Sum of Subsets Problem .

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-Completeness for optimization problems, which are problems that involve finding the best solution among a set of possible solutions according to some objective function.
- Approximation Algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal solution in polynomial time. Such algorithms are called approximation algorithms  .
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution. The smaller the approximation ratio, the better the algorithm.
- Some examples of approximation algorithms are the 2-approximation algorithm for the Travelling Salesman Problem, which finds a solution that is at most twice as long as the optimal solution, the greedy algorithm for the Graph Coloring Problem, which finds a solution that uses at most one more color than the optimal solution, the backtracking algorithm for the n-Queen Problem, which finds a solution that places n queens on an n x n chessboard such that no two queens attack each other, the greedy algorithm for the Hamiltonian Cycle Problem, which finds a cycle that visits every vertex of a graph exactly once, and the dynamic programming algorithm for the Sum of Subsets Problem, which finds a subset of a given set of numbers that sums up to a given target value.