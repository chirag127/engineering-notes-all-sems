# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a class of decision problems that are both in NP and NP-hard.
- NP stands for nondeterministic polynomial time, which means that there is a nondeterministic algorithm that can solve the problem in polynomial time.
- NP-hard means that any problem in NP can be reduced to the problem in polynomial time, which means that the problem is at least as hard as any problem in NP.
- NP-complete problems are the hardest problems in NP, and there is no known polynomial time algorithm to solve them, unless P = NP, which is a major open question in computer science.
- Examples of NP-complete problems are: satisfiability problem (SAT), traveling salesman problem (TSP), graph coloring problem, n-queen problem, Hamiltonian cycle problem, and sum of subsets problem.

## Approximation Algorithms

- Approximation algorithms are a way of dealing with NP-completeness for optimization problems, where the goal is to find the best solution among a set of feasible solutions.
- Approximation algorithms do not guarantee the optimal solution, but they aim to come as close as possible to the optimal solution in polynomial time.
- Approximation algorithms have a performance guarantee, which is a ratio between the value of the solution obtained by the algorithm and the value of the optimal solution.
- For example, a 2-approximation algorithm for the vertex cover problem guarantees that the size of the vertex cover found by the algorithm is at most twice the size of the optimal vertex cover.
- Examples of approximation algorithms are: greedy algorithm for the set cover problem, Christofides algorithm for the metric TSP, local search algorithm for the graph coloring problem, backtracking algorithm for the n-queen problem, and dynamic programming algorithm for the sum of subsets problem.