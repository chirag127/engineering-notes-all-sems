# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A problem is in the class P if there is a polynomial time algorithm that can solve it, i.e., an algorithm that runs in time O(n^k) for some constant k, where n is the size of the input.
- A problem is in the class NP if there is a polynomial time algorithm that can verify a given solution, i.e., an algorithm that can check in time O(n^k) whether a given candidate answer is correct or not.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time, i.e., there is a polynomial time transformation that can convert any instance of any NP problem into an equivalent instance of the NP-complete problem.
- NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial time algorithm that can solve them. This is the famous P vs NP problem, which is one of the most important open questions in computer science and mathematics.
- Examples of NP-complete problems are: 
  - Travelling Salesman Problem (TSP): Given a set of cities and distances between them, find the shortest tour that visits each city exactly once and returns to the starting point.
  - Graph Coloring: Given a graph and a number k, determine whether the vertices of the graph can be assigned k different colors such that no two adjacent vertices have the same color.
  - n-Queen Problem: Given a chessboard of size n x n, place n queens on the board such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal.
  - Hamiltonian Cycle: Given a graph, determine whether there is a cycle that visits each vertex exactly once and returns to the starting point.
  - Sum of Subsets: Given a set of positive integers and a target value, determine whether there is a subset of the set that sums up to the target value.

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions, usually by minimizing or maximizing some objective function.
- Approximation Algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal solution in polynomial time, i.e., an algorithm that runs in time O(n^k) and produces a solution that has an error or a ratio within some bound compared to the optimal solution.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the worst-case ratio between the cost of the solution produced by the algorithm and the cost of the optimal solution. For minimization problems, the approximation ratio is the maximum ratio over all instances, and for maximization problems, it is the minimum ratio over all instances.
- The goal of designing approximation algorithms is to find the best possible approximation ratio for a given problem, or to prove that no polynomial time algorithm can achieve a better approximation ratio, assuming P != NP. This is called the hardness of approximation, and it is a way of quantifying how hard a problem is to approximate.
- Examples of approximation algorithms are:
  - TSP: There is a 2-approximation algorithm that uses a minimum spanning tree and a depth-first traversal to construct a tour. There is also a 1.5-approximation algorithm that uses a minimum spanning tree and a matching to construct a tour. These are the best possible approximation ratios, unless P = NP.
  - Graph Coloring: There is a simple greedy algorithm that assigns colors to vertices in an arbitrary order, and uses the smallest available color for each vertex. This algorithm has an approximation ratio of O(log n), where n is the number of vertices. There is also a more sophisticated algorithm that uses a technique called semidefinite programming and has an approximation ratio of O(sqrt(log n)). These are the best possible approximation ratios, unless P = NP.
  - n-Queen Problem: There is a simple algorithm that places queens on the main diagonal of the board, and then tries to move them to other positions that do not cause conflicts. This algorithm has an approximation ratio of n, where n is the size of the board. There is also a more sophisticated algorithm that uses a technique called local search and has an approximation ratio of O(log n). These are the best possible approximation ratios, unless P = NP.
  - Hamiltonian