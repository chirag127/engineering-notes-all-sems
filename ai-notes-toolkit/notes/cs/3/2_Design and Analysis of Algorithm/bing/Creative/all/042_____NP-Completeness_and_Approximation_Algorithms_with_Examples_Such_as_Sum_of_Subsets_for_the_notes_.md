# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A problem is in the class P if there is a polynomial time algorithm that can solve it, i.e., an algorithm that runs in time O(n^k) for some constant k, where n is the size of the input.
- A problem is in the class NP if there is a polynomial time algorithm that can verify a given solution, i.e., an algorithm that can check in time O(n^k) whether a given candidate answer is correct or not.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time, i.e., there is a polynomial time algorithm that can transform any instance of any NP problem into an equivalent instance of the NP-complete problem.
- NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial time algorithm that can solve them. This is the famous P vs NP problem, which is one of the most important open questions in computer science.
- Some examples of NP-complete problems are:

  - Satisfiability (SAT): Given a Boolean formula with n variables and m clauses, is there an assignment of true or false values to the variables that satisfies all the clauses?
  - Traveling Salesman Problem (TSP): Given n cities and a matrix of distances between them, is there a tour that visits each city exactly once and has a total length at most k?
  - Graph Coloring: Given a graph with n vertices and m edges, is there a way to assign k colors to the vertices such that no two adjacent vertices have the same color?
  - n-Queen Problem: Given a chessboard of size n x n, is there a way to place n queens on the board such that no two queens attack each other?
  - Hamiltonian Cycle: Given a graph with n vertices and m edges, is there a cycle that visits each vertex exactly once and returns to the starting vertex?
  - Sum of Subsets: Given a set of n positive integers and a target value k, is there a subset of the set that sums up to k?

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions, such as minimizing or maximizing some objective function.
- Approximation Algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal in polynomial time, i.e., an algorithm that runs in time O(n^k) and produces a solution that has an objective value within a factor of the optimal value.
- The factor by which the approximation algorithm deviates from the optimal value is called the approximation ratio, which is usually expressed as a function of the input size n. For example, an approximation ratio of 2 means that the algorithm produces a solution that is at most twice as bad as the optimal solution, or at least half as good as the optimal solution.
- Approximation Algorithms are useful when the optimal solution is too hard to find or too expensive to compute, and a good enough solution is acceptable for the problem at hand.
- Some examples of approximation algorithms are:

  - 2-Approximation Algorithm for Vertex Cover: A vertex cover of a graph is a subset of vertices that covers all the edges, i.e., every edge has at least one endpoint in the subset. The vertex cover problem is to find the minimum size vertex cover of a given graph. This problem is NP-complete, but there is a simple 2-approximation algorithm that works as follows:

    - Start with an empty vertex cover.
    - While there are uncovered edges, pick any such edge and add both of its endpoints to the vertex cover.
    - Return the vertex cover.

    This algorithm produces a vertex cover that is at most twice as large as the optimal vertex cover, because every edge is covered by at most two vertices, and the optimal vertex cover must cover every edge by at least one vertex.

  - 7/8-Approximation Algorithm for Max 3-SAT: A 3-SAT formula is a Boolean formula with n variables and m clauses, where each clause has exactly three literals. The max 3-SAT problem is to find the maximum number of clauses that can be satisfied by an assignment of true or false values to the variables. This problem is NP-complete, but there is a clever 7/8-approx