### NP-Completeness and Approximation Algorithms

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A problem is in the class P if there is a polynomial time algorithm that can solve it, i.e., an algorithm that runs in time O(n^k) for some constant k, where n is the size of the input.
- A problem is in the class NP if there is a polynomial time algorithm that can verify a given solution, i.e., an algorithm that can check in time O(n^k) whether a given candidate answer is correct or not.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time, i.e., there is a polynomial time algorithm that can transform any instance of any NP problem into an equivalent instance of the NP-complete problem.
- NP-complete problems are believed to be the hardest problems in NP, and it is widely conjectured that P != NP, which means that there is no polynomial time algorithm that can solve any NP-complete problem.
- Examples of NP-complete problems are: Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles, Sum of Subsets, etc.
- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones, according to some objective function.
- Approximation Algorithms do not guarantee the best solution, but they aim to come as close as possible to the optimal solution in polynomial time, by sacrificing some accuracy for efficiency.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution produced by the algorithm and the value of the optimal solution, for any instance of the problem.
- The approximation ratio can be either a constant, a function of the input size, or a function of some parameter of the problem, depending on the problem and the algorithm.
- Examples of approximation algorithms are: 2-approximation algorithm for Vertex Cover, 7/8-approximation algorithm for Max 3-SAT, 2-approximation algorithm for Travelling Salesman Problem with triangle inequality, etc.