# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A problem is in the class P if there is a polynomial time algorithm that can solve it, i.e., an algorithm that runs in O(n^k) time for some constant k, where n is the size of the input.
- A problem is in the class NP if there is a polynomial time algorithm that can verify a given solution, i.e., an algorithm that can check in O(n^k) time whether a given candidate answer is correct or not.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time, i.e., there is a polynomial time algorithm that can transform any instance of any NP problem into an equivalent instance of the NP-complete problem.
- NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial time algorithm that can solve them. This is the famous P vs NP problem, which is one of the most important open questions in computer science and mathematics.
- Examples of NP-complete problems are: 
  - Satisfiability (SAT): Given a boolean formula with variables and logical operators, is there an assignment of true or false values to the variables that makes the formula true?
  - Traveling Salesman Problem (TSP): Given a set of cities and distances between them, is there a tour that visits each city exactly once and has a total length less than or equal to a given limit?
  - Graph Coloring: Given a graph and a number of colors, is there a way to assign a color to each vertex such that no two adjacent vertices have the same color?
  - n-Queen Problem: Given a chessboard of size n x n, is there a way to place n queens on the board such that no two queens attack each other?
  - Hamiltonian Cycle: Given a graph, is there a cycle that visits each vertex exactly once?
  - Subset Sum: Given a set of integers and a target sum, is there a subset of the integers that adds up to the target sum?

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible ones, according to some objective function.
- An approximation algorithm does not guarantee the optimal solution, but rather a solution that is close to the optimal one, within some factor or bound.
- The goal of an approximation algorithm is to come as close as possible to the optimal solution in polynomial time, i.e., an algorithm that runs in O(n^k) time for some constant k, where n is the size of the input.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution. The smaller the ratio, the better the approximation.
- For minimization problems, the approximation ratio is defined as:

  - Approximation Ratio = (Value of Algorithm Solution) / (Value of Optimal Solution)

- For maximization problems, the approximation ratio is defined as:

  - Approximation Ratio = (Value of Optimal Solution) / (Value of Algorithm Solution)

- Examples of approximation algorithms are:
  - TSP: A 2-approximation algorithm is to find a minimum spanning tree of the graph, and then visit the cities in the order of a preorder traversal of the tree. This algorithm guarantees that the tour length is at most twice the optimal length .
  - Graph Coloring: A simple approximation algorithm is to assign colors to the vertices in any order, and use a new color whenever a vertex has a neighbor with the same color. This algorithm guarantees that the number of colors used is at most the maximum degree of the graph plus one.
  - n-Queen Problem: A heuristic approximation algorithm is to place the queens one by one, starting from the first row, and choose the column that has the least number of conflicts with the previous queens. This algorithm does not guarantee a solution, but it works well in practice for large n.
  - Hamiltonian Cycle: A 2-approximation algorithm is to find a minimum spanning tree of the graph, and then visit the vertices in the order of a preorder traversal of the tree, skipping any repeated vertices. This algorithm guarantees that the cycle length is at most twice the optimal length[^5