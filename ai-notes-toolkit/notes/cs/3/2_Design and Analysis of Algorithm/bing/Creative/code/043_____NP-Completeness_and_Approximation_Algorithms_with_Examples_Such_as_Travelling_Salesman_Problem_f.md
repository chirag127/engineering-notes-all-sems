Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a class of problems that are hard to solve in polynomial time, but easy to verify the correctness of a given solution in polynomial time.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time. This means that if there is a polynomial time algorithm for any NP-complete problem, then there is a polynomial time algorithm for every problem in NP.
- Some examples of NP-complete problems are: 3-SAT, Hamiltonian Cycle, Traveling Salesman Problem, Subset Sum, Vertex Cover, Clique, etc.
- To prove that a problem is NP-complete, we need to show two things:
  - The problem is in NP, i.e., there is a polynomial time verifier for it.
  - The problem is NP-hard, i.e., there is a polynomial time reduction from any other problem in NP to it.
- To show that a problem is NP-hard, we can use the technique of reduction. This means that we can transform an instance of a known NP-hard problem into an instance of the problem we want to prove NP-hard, such that the answer is preserved. For example, we can reduce 3-SAT to Clique by constructing a graph where each vertex represents a literal and each edge represents a clause, and finding a clique of size k in the graph is equivalent to finding a satisfying assignment for the 3-SAT formula.

## Approximation Algorithms

- An approximation algorithm is a way of dealing with NP-completeness for an optimization problem. This technique does not guarantee the best solution, but a solution that is close to the optimal one in polynomial time.
- The goal of an approximation algorithm is to find a solution that has a provable quality guarantee, i.e., a bound on how far the solution is from the optimal one. This is measured by the approximation ratio, which is the ratio of the cost of the solution found by the algorithm to the cost of the optimal solution.
- For example, if we have a minimization problem, and the algorithm finds a solution of cost C, and the optimal solution has cost OPT, then the approximation ratio is C/OPT. The smaller the ratio, the better the approximation. Similarly, for a maximization problem, the approximation ratio is OPT/C.
- Some examples of approximation algorithms are:
  - A 2-approximation algorithm for Vertex Cover: Find a maximal matching in the graph, and pick both endpoints of each edge in the matching as the vertex cover. This guarantees that the size of the vertex cover is at most twice the size of the optimal one.
  - A 7/8-approximation algorithm for Max 3-SAT: Assign each variable randomly with probability 1/2, and evaluate the formula. This guarantees that the expected number of satisfied clauses is at least 7/8 of the maximum possible.
  - A 2-approximation algorithm for Traveling Salesman Problem: Find a minimum spanning tree of the graph, and traverse it in a preorder fashion, skipping any visited vertices. This guarantees that the length of the tour is at most twice the length of the optimal one.
  - A (1 + 1/k)-approximation algorithm for Graph Coloring: Find a maximal independent set of vertices in the graph, and assign them the same color. Repeat this process until all vertices are colored. This guarantees that the number of colors used is at most (1 + 1/k) times the minimum number of colors needed.
  - A (1 - 1/e)-approximation algorithm for n-Queen Problem: Place a queen randomly on each row of the board, and count the number of conflicts. Repeat this process until the number of conflicts is less than n/e. This guarantees that the expected number of queens placed is at least (1 - 1/e) times the maximum number of queens that can be placed.
  - A (1/2)-approximation algorithm for Subset Sum: Sort the elements of the set in decreasing order, and add them to a subset until the sum exceeds the target value. Then, remove the last element added, and return the subset. This guarantees that the sum