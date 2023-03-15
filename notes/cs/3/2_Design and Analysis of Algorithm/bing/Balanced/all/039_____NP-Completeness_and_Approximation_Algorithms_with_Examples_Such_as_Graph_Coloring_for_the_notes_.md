# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-completeness is a concept that relates to the complexity of decision problems, which are problems that have a yes or no answer.
- A decision problem is in the class P if there is a polynomial-time algorithm that can solve it, i.e., an algorithm that runs in time O(n^k) for some constant k, where n is the size of the input.
- A decision problem is in the class NP if there is a polynomial-time algorithm that can verify a given solution, i.e., an algorithm that can check in time O(n^k) whether a given candidate answer is correct or not.
- A decision problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time, i.e., there is a polynomial-time algorithm that can transform any instance of any NP problem into an equivalent instance of the NP-complete problem.
- NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial-time algorithm that can solve them. This is the famous P vs NP problem, which is one of the most important open questions in computer science and mathematics.
- Examples of NP-complete problems are:

  - Satisfiability (SAT): Given a Boolean formula with n variables and m clauses, is there an assignment of true or false values to the variables that satisfies all the clauses?
  - Traveling Salesman Problem (TSP): Given a set of n cities and the distances between them, is there a tour that visits each city exactly once and has a total length at most k?
  - Graph Coloring: Given a graph with n vertices and m edges, and a positive integer k, is there a way to assign one of k colors to each vertex such that no two adjacent vertices have the same color?
  - n-Queen Problem: Given a positive integer n, is there a way to place n queens on an n x n chessboard such that no two queens attack each other?
  - Hamiltonian Cycle: Given a graph with n vertices and m edges, is there a cycle that visits each vertex exactly once?
  - Subset Sum: Given a set of n positive integers and a target value k, is there a subset of the integers that adds up to k?

## Approximation Algorithms

- Approximation algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones, according to some objective function.
- An approximation algorithm is a polynomial-time algorithm that produces a solution that is close to the optimal one, within some guaranteed factor or bound.
- The goal of an approximation algorithm is to come as close as possible to the optimal solution in polynomial time, without necessarily finding it.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution produced by the algorithm and the value of the optimal solution. The smaller the ratio, the better the approximation.
- For minimization problems, the approximation ratio is defined as:

  - Approximation ratio = (value of algorithm solution) / (value of optimal solution)

- For maximization problems, the approximation ratio is defined as:

  - Approximation ratio = (value of optimal solution) / (value of algorithm solution)

- An approximation algorithm is called an alpha-approximation algorithm if its approximation ratio is at most alpha for any instance of the problem, where alpha is a constant greater than or equal to one.
- Examples of approximation algorithms are:

  - Vertex Cover: A vertex cover of a graph is a subset of vertices that touches every edge, i.e., for every edge, at least one of its endpoints is in the vertex cover. The vertex cover problem is to find the minimum size vertex cover of a given graph. There is a 2-approximation algorithm for this problem, which works as follows:

    - Start with an empty vertex cover.
    - While there are edges in the graph, pick an arbitrary edge and add both of its endpoints to the vertex cover. Remove all the edges incident to these vertices from the graph.
    - Return the vertex cover.

    - This algorithm is a 2-approximation algorithm because the size of the vertex cover it produces is at most twice the size of the optimal vertex cover. To see this, note that every edge in the graph contributes at least one vertex to the optimal vertex cover, and the algorithm adds at most two vertices for each edge.

  - TSP: The traveling salesman problem is to find the minimum length tour that visits each city exactly once