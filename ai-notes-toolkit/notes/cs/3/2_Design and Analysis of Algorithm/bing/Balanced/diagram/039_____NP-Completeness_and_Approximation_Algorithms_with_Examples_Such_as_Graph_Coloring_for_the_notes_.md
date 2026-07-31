# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A problem is in the class P if there is a polynomial time algorithm that can solve it, i.e., an algorithm that runs in O(n^k) time for some constant k, where n is the size of the input.
- A problem is in the class NP if there is a polynomial time algorithm that can verify a given solution, i.e., an algorithm that can check in O(n^k) time whether a given candidate answer is correct or not.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time, i.e., there is a polynomial time algorithm that can transform any instance of any NP problem into an equivalent instance of the NP-complete problem.
- NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial time algorithm that can solve them. This is the famous P vs NP problem, which is one of the most important open questions in computer science.
- Examples of NP-complete problems are: 
  - Satisfiability (SAT): Given a boolean formula with variables and logical operators, is there an assignment of true or false values to the variables that makes the formula true?
  - Traveling Salesman Problem (TSP): Given a set of cities and distances between them, is there a tour that visits each city exactly once and has a total length less than or equal to a given limit?
  - Graph Coloring: Given a graph and a number of colors, is there a way to assign a color to each vertex such that no two adjacent vertices have the same color?
  - n-Queen Problem: Given a chessboard of size n x n, is there a way to place n queens on the board such that no two queens attack each other?
  - Hamiltonian Cycle: Given a graph, is there a cycle that visits each vertex exactly once?
  - Subset Sum: Given a set of integers and a target sum, is there a subset of the integers that adds up to the target sum?

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions, usually by minimizing or maximizing some objective function.
- Approximation Algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal in polynomial time, usually by giving a performance guarantee or an approximation ratio.
- An approximation ratio is a measure of how good the solution found by the algorithm is compared to the optimal solution. For example, if the algorithm finds a solution that is at most twice as bad as the optimal solution, then the approximation ratio is 2. The lower the approximation ratio, the better the algorithm.
- Examples of approximation algorithms are:
  - TSP: There is a 2-approximation algorithm that uses a minimum spanning tree to construct a tour that is at most twice as long as the optimal tour.
  - Graph Coloring: There is a (Δ+1)-approximation algorithm that uses a greedy strategy to color the vertices with at most Δ+1 colors, where Δ is the maximum degree of the graph.
  - n-Queen Problem: There is a (n/2)-approximation algorithm that places n/2 queens on the main diagonal and n/2 queens on the secondary diagonal, which is at most half as good as the optimal solution of n queens.
  - Hamiltonian Cycle: There is a 2-approximation algorithm that uses a minimum spanning tree to construct a cycle that is at most twice as long as the optimal cycle.
  - Subset Sum: There is a (1+ε)-approximation algorithm that uses dynamic programming to find a subset that sums up to a value that is within ε of the target sum, where ε is a small positive constant.