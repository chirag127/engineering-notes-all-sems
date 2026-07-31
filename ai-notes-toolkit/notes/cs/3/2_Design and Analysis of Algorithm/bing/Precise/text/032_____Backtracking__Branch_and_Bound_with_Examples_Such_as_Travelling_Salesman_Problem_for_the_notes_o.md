### Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

Backtracking and branch and bound are two optimization techniques used to solve problems in the field of computer science. Both techniques are used to find solutions to problems that can be represented as a tree of possibilities.

#### Backtracking

Backtracking is a general algorithm for finding all (or some) solutions to a problem that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Backtracking can be used to solve problems such as the n-Queens problem, where the goal is to place n queens on an n×n chessboard such that no two queens threaten each other, and the sum of subsets problem, where the goal is to find a subset of a given set of integers whose sum is equal to a given target.

#### Branch and Bound

Branch and bound is an algorithmic technique for solving optimization problems. It involves the systematic enumeration of all candidate solutions, where large subsets of fruitless candidates are discarded by using upper and lower estimated bounds of the quantity being optimized.

Branch and bound can be used to solve problems such as the travelling salesman problem, where the goal is to find the shortest possible route that visits a given set of cities and returns to the starting city, and the graph coloring problem, where the goal is to assign colors to the vertices of a graph such that no two adjacent vertices share the same color.

#### Travelling Salesman Problem

The travelling salesman problem (TSP) is an optimization problem where the goal is to find the shortest possible route that visits a given set of cities and returns to the starting city. The TSP can be solved using branch and bound by systematically enumerating all possible routes and discarding routes that are longer than the current best solution.

#### Graph Coloring

Graph coloring is the problem of assigning colors to the vertices of a graph such that no two adjacent vertices share the same color. This problem can be solved using backtracking by incrementally building a solution and backtracking when a conflict is found.

#### n-Queen Problem

The n-Queens problem is the problem of placing n queens on an n×n chessboard such that no two queens threaten each other. This problem can be solved using backtracking by incrementally building a solution and backtracking when a conflict is found.

#### Hamiltonian Cycles

A Hamiltonian cycle is a cycle in a graph that visits each vertex exactly once. The problem of finding a Hamiltonian cycle in a graph can be solved using backtracking by incrementally building a solution and backtracking when a conflict is found.

#### Sum of Subsets

The sum of subsets problem is the problem of finding a subset of a given set of integers whose sum is equal to a given target. This problem can be solved using backtracking by incrementally building a solution and backtracking when the current subset sum exceeds the target.