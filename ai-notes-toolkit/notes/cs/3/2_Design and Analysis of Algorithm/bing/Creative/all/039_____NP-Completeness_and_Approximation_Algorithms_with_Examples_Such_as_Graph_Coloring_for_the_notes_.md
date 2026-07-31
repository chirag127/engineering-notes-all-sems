# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a class of problems that are hard to solve in polynomial time, but easy to verify in polynomial time.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
- NP-complete problems are believed to have no efficient algorithms, unless P = NP, which is a major open question in computer science.
- Examples of NP-complete problems are: Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles, Sum of Subsets, etc.
- To show that a problem is NP-complete, one can use the following steps:
  - Show that the problem is in NP, i.e., given a solution, one can verify its correctness in polynomial time.
  - Choose a known NP-complete problem and reduce it to the given problem in polynomial time, i.e., show how to transform an instance of the known problem into an instance of the given problem such that the answer is preserved.
  - Conclude that the given problem is NP-complete by the transitivity of polynomial-time reductions.

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, where the goal is to find the best solution among a set of feasible solutions.
- Approximation Algorithms do not guarantee the optimal solution, but they aim to come as close as possible to the optimal solution in polynomial time.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution produced by the algorithm and the value of the optimal solution.
- For a minimization problem, the approximation ratio is defined as:

  - `r = max {C(A)/C(OPT), C(OPT)/C(A)}`

  - where `C(A)` is the cost of the solution produced by the algorithm, and `C(OPT)` is the cost of the optimal solution.

- For a maximization problem, the approximation ratio is defined as:

  - `r = max {C(OPT)/C(A), C(A)/C(OPT)}`

  - where `C(A)` is the value of the solution produced by the algorithm, and `C(OPT)` is the value of the optimal solution.

- An approximation algorithm is called an `r`-approximation algorithm if its approximation ratio is at most `r` for any instance of the problem.
- Examples of approximation algorithms are: 2-approximation algorithm for Vertex Cover, 7/8-approximation algorithm for Max 3-SAT, 2-approximation algorithm for Travelling Salesman Problem with triangle inequality, etc.
- To design an approximation algorithm, one can use the following techniques:
  - Greedy method: Choose the best option at each step, without looking ahead.
  - Rounding: Relax the problem to make it easier to solve, and then round the solution to make it feasible.
  - Randomization: Use random choices to explore different solutions, and then pick the best one.
  - Local search: Start with a feasible solution, and then improve it by making small changes.