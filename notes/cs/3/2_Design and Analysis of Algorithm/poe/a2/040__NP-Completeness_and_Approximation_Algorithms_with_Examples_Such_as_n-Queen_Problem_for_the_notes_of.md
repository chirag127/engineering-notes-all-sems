 Here are the notes on NP-Completeness and Approximation Algorithms with Examples Such as n-Queen Problem:

### NP-Completeness

- A decision problem is NP-complete if it is in NP and every NP problem can be reduced to it in polynomial time.
- NP-complete problems are the hardest problems in NP. If any NP-complete problem has a polynomial time algorithm, then all problems in NP can be solved in polynomial time.
- Examples of NP-complete problems: Boolean Satisfiability (SAT), Travelling Salesman Problem (TSP), Hamilton Path, Vertex Cover, Clique, etc.

### Approximation Algorithms

- Since NP-complete problems cannot be solved in polynomial time, we look for efficient algorithms that produce approximate solutions.
- An Approximation algorithm is a polynomial time algorithm that finds an approximate solution with a guaranteed worst-case performance ratio (approximation ratio).
- Examples:
-- For TSP, construct a minimum spanning tree (approx ratio = 2)
-- For Vertex Cover, select all vertices (approx ratio = 2)
-- For Set Cover, select sets greedily (approx ratio = log(n))

### n-Queen Problem

- The n-Queen problem is to place n queens on an n??n chessboard such that no two queens attack each other.
- The n-Queen problem is NP-hard. So, there is no known polynomial time optimal algorithm to solve it.
- An approximate algorithm places queens one by one in the first n rows such that the current queen does not attack the previously placed queens. The approximation ratio is n.
- The n-Queen problem is used to demonstrate backtracking algorithms and generate permutations and combinations.

Does this help? Let me know if you would like me to modify or expand the notes.