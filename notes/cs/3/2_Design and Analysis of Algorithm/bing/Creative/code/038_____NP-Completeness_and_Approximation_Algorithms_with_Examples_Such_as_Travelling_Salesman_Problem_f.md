# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A problem is in the class P if there is a polynomial time algorithm that can solve it, i.e., an algorithm that runs in O(n^k) time for some constant k, where n is the size of the input.
- A problem is in the class NP if there is a polynomial time algorithm that can verify a given solution, i.e., an algorithm that can check in O(n^k) time whether a given candidate answer is correct or not.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time, i.e., there is a polynomial time transformation that can convert any instance of any NP problem to an instance of the NP-complete problem such that the answer is preserved.
- NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial time algorithm that can solve them. This is the famous P vs NP problem, which is one of the most important open questions in computer science.
- Examples of NP-complete problems are: satisfiability (SAT), traveling salesman problem (TSP), graph coloring, n-queen problem, Hamiltonian cycles, sum of subsets, etc.

## Approximation Algorithms

- Approximation algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones, such as minimizing or maximizing some objective function.
- Approximation algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal one in polynomial time, i.e., an algorithm that runs in O(n^k) time and produces a solution that has an error or ratio within some bound.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the worst-case ratio between the value of the solution produced by the algorithm and the value of the optimal solution. For example, if an algorithm produces a solution that is at most twice as bad as the optimal one, then its approximation ratio is 2.
- The goal of designing approximation algorithms is to find the best possible approximation ratio for a given problem, or to prove that no better approximation ratio is possible under some complexity assumptions.
- Examples of approximation algorithms are: 2-approximation algorithm for vertex cover, 7/8-approximation algorithm for max 3-sat, 2-approximation algorithm for TSP with triangle inequality, etc.