### Dynamic Programming with Examples Such as All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

Dynamic programming is a method for solving complex problems by breaking them down into smaller subproblems. It is applicable to problems that exhibit the properties of overlapping subproblems and optimal substructure. When a problem can be solved by combining optimal solutions to non-overlapping subproblems, the strategy is called "divide and conquer" instead. Dynamic programming is used when the subproblems are not independent, such as in the all pair shortest paths problem.

#### All Pair Shortest Paths

The all pair shortest paths problem is the problem of finding the shortest paths between every pair of vertices in a given edge-weighted directed graph. There are several algorithms to solve this problem, including Warshal’s and Floyd’s algorithms.

##### Warshal’s Algorithm

Warshal’s algorithm, also known as the Roy-Warshal algorithm, is an algorithm for finding the transitive closure of a directed graph. It is a dynamic programming algorithm that works by repeatedly squaring the adjacency matrix of the graph. The algorithm can be used to solve the all pair shortest paths problem for graphs with non-negative edge weights.

##### Floyd’s Algorithm

Floyd’s algorithm, also known as the Floyd-Warshall algorithm, is an algorithm for finding shortest paths in a weighted graph with positive or negative edge weights, but with no negative cycles. It is a dynamic programming algorithm that works by considering all possible paths through the graph and choosing the best one. The algorithm can be used to solve the all pair shortest paths problem for graphs with non-negative edge weights.

#### Resource Allocation Problem

The resource allocation problem is the problem of allocating resources among competing activities in the most efficient way. Dynamic programming can be used to solve this problem by breaking it down into smaller subproblems and solving them optimally.

#### Backtracking

Backtracking is a general algorithm for finding all (or some) solutions to a problem that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

#### Branch and Bound

Branch and bound is an algorithm design paradigm for discrete and combinatorial optimization problems, as well as mathematical optimization. A branch-and-bound algorithm consists of a systematic enumeration of candidate solutions by means of state space search: the set of candidate solutions is thought of as forming a rooted tree with the full set at the root. The algorithm explores branches of this tree, which represent subsets of the solution set. Before enumerating the candidate solutions of a branch, the branch is checked against upper and lower estimated bounds on the optimal solution, and is discarded if it cannot produce a better solution than the best one found so far by the algorithm.

#### Examples

Some examples of problems that can be solved using backtracking and branch and bound include the travelling salesman problem, graph coloring, n-queen problem, Hamiltonian cycles, and sum of subsets.

##### Travelling Salesman Problem

The travelling salesman problem is the problem of finding the shortest possible route that visits a given set of cities and returns to the starting city. It is an NP-hard problem in combinatorial optimization, important in operations research and theoretical computer science.

##### Graph Coloring

Graph coloring is the problem of assigning colors to the vertices of a graph in such a way that no two adjacent vertices share the same color. It is an NP-hard problem in combinatorial optimization and graph theory.

##### n-Queen Problem

The n-queen problem is the problem of placing n queens on an n×n chessboard such that no two queens threaten each other. It is an example of a constraint satisfaction problem and can be solved using backtracking.

##### Hamiltonian Cycles

A Hamiltonian cycle, also known as a Hamiltonian circuit, Hamilton cycle, or Hamilton circuit, is a cycle that visits each vertex exactly once (except for the vertex that is both the start and end, which is visited twice). Finding a Hamiltonian cycle in a given graph is an NP-hard problem.

##### Sum of Subsets

The sum of subsets problem is the problem of finding a subset of a given set of integers that adds up to a given target sum. It is an NP-hard problem and can be solved using backtracking or branch and bound.