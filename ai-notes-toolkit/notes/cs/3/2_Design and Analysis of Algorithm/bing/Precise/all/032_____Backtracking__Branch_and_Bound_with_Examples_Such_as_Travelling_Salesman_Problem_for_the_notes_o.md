# Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

Backtracking and branch and bound are two optimization techniques used to solve problems in the field of computer science. Both techniques are used to find solutions to problems that can be represented as a tree of possibilities.

## Backtracking

Backtracking is a general algorithm for finding all (or some) solutions to a problem that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Backtracking can be used to solve problems such as the n-Queens problem, where the goal is to place n queens on an n×n chessboard such that no two queens threaten each other, and the sum of subsets problem, where the goal is to find a subset of a given set of integers that adds up to a given target number.

## Branch and Bound

Branch and bound is an algorithm design paradigm for discrete and combinatorial optimization problems, as well as mathematical optimization. A branch-and-bound algorithm consists of a systematic enumeration of candidate solutions by means of state space search: the set of candidate solutions is thought of as forming a rooted tree with the full set at the root.

Branch and bound can be used to solve problems such as the travelling salesman problem, where the goal is to find the shortest possible route that visits a given set of cities and returns to the starting city, and the graph coloring problem, where the goal is to assign colors to the vertices of a graph in such a way that no two adjacent vertices share the same color.

## Travelling Salesman Problem

The travelling salesman problem (TSP) is an NP-hard problem in combinatorial optimization, important in operations research and theoretical computer science. Given a list of cities and the distances between each pair of cities, the task is to find the shortest possible route that visits each city exactly once and returns to the origin city.

One approach to solving the TSP using branch and bound is to represent the problem as a tree of possibilities, where each node represents a partial solution to the problem. The algorithm then explores the tree, using a bounding function to determine which nodes to explore and which to prune. The bounding function calculates a lower bound on the cost of any solution that can be obtained by extending the current partial solution. If the lower bound is greater than the cost of the best solution found so far, the node can be pruned.

## Conclusion

Backtracking and branch and bound are powerful optimization techniques that can be used to solve a wide range of problems. These techniques can be applied to problems such as the travelling salesman problem, graph coloring, n-Queen problem, Hamiltonian cycles, and sum of subsets, among others. By using these techniques, it is possible to find solutions to problems that would otherwise be intractable.