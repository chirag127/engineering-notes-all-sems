 Here are the notes for ### NP-Completeness and Approximation Algorithms with Examples Such as Graph Coloring:

NP-Completeness:
- A decision problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
- NP-complete problems are the hardest problems in NP. If any NP-complete problem has a polynomial time algorithm, then every problem in NP has a polynomial time algorithm.
- Examples: Boolean Satisfiability (SAT), Travelling Salesman Problem (TSP), Hamiltonian Cycle, Graph Coloring, etc.

Graph Coloring:
- The graph coloring problem is to assign colors to vertices of a graph such that no two adjacent vertices have the same color.
- The minimum number of colors required is called chromatic number.
- It is NP-complete to decide if a graph can be colored using k colors for a fixed k.
- Approximation Algorithms:
- Greedy coloring: Assign colors one by one to uncolored vertices. Choose a color that has minimum adjacent vertices of that color. Worst case approximation ratio is ??(??D) where D is maximum degree of graph.
- Additional heuristics can give better approximations in practice.
- Lower bounds on approximation ratios of any polynomial time algorithm are NP-hard to prove.

Advantages: Approximation algorithms give feasible solutions in polynomial time with guaranteed worst-case performance.
Disadvantages: Worst-case guarantees may be weak. Obtaining tight bounds is difficult.

Applications: Frequency assignment, register allocation, timetabling, etc.

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.