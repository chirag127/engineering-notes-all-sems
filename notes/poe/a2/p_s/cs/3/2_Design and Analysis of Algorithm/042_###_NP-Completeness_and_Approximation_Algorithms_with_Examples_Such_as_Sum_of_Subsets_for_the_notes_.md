 Here are the notes for ### NP-Completeness and Approximation Algorithms with Examples Such as Sum of Subsets:

NP-Completeness:
- A decision problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
- NP-complete problems are the hardest problems in NP. If any NP-complete problem has a polynomial time algorithm, then every problem in NP has a polynomial time algorithm.
- Examples: Boolean Satisfiability (SAT), Travelling Salesman Problem (TSP), Hamiltonian Cycle, Graph Coloring, Subset Sum, etc.

Approximation Algorithms:
- For NP-hard problems, there may not exist polynomial time exact algorithms. So we look for efficient algorithms that return solutions that are close to optimal.
- The goal is to design algorithms that have provable guarantees on the quality of the solution.
- Examples:
-- For TSP, calculate the minimum spanning tree (MST) which is a 2-approximation algorithm.
-- For Vertex Cover, take all the vertices with maximum degree (greedy approach) which is a 2-approximation algorithm.
-- For Set Cover, take the sets that cover the maximum number of uncovered elements in each iteration (greedy approach).

Sum of Subsets Problem:
- Given a set of integers, find a subset whose sum is equal to a given sum K.
- This is an NP-complete decision problem. There exists no known polynomial time exact algorithm for this problem unless P = NP.
- An approximation algorithm is to find a subset with sum closest to K. A greedy approach can be used that adds the largest element that doesn't exceed K. This is a logarithmic approximation algorithm.
- Applications: Resource allocation, database retrieval, pattern recognition, etc.