# Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

Backtracking and branch and bound are two techniques for solving optimization and decision problems that involve searching a finite set of possible solutions. They both use a state-space tree to represent the partial and complete solutions, and they both use a bounding function to prune the tree and eliminate unpromising candidates. However, they differ in the way they traverse the tree and the type of bounding function they use.

## Backtracking

Backtracking is an algorithm for finding all solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions. It works by exploring the state-space tree in a depth-first manner, and backtracks whenever the current partial solution violates some constraints or cannot be extended to a complete solution. Backtracking can be seen as a generalization of recursion, where instead of making a single recursive call, we make multiple recursive calls for each possible choice.

The main steps of a backtracking algorithm are:

- Choose a variable to assign a value from a finite domain.
- Check if the current assignment is consistent with the constraints. If not, backtrack and try another value.
- If the current assignment is consistent, check if it is a complete solution. If yes, report the solution and backtrack to find more solutions. If no, choose another variable and repeat the process.

The main advantages of backtracking are:

- It can find all possible solutions to a problem, or report that none exists.
- It can be easily implemented using recursion and a stack data structure.
- It can be applied to a wide range of problems, such as sudoku, n-queens, graph coloring, etc.

The main disadvantages of backtracking are:

- It can be very inefficient, as it may explore a large number of irrelevant or redundant branches in the tree.
- It can be very sensitive to the order of variables and values, as some choices may lead to early pruning or late pruning of the tree.
- It can be very difficult to design a good bounding function that can effectively prune the tree and reduce the search space.

## Branch and Bound

Branch and bound is an algorithm for discrete and combinatorial optimization problems and mathematical optimization. It works by exploring the state-space tree in a best-first manner, and bounds the optimal value of the objective function using a lower bound (for minimization problems) or an upper bound (for maximization problems). It prunes the tree by discarding the branches that cannot contain the optimal solution, based on the comparison of the bounds.

The main steps of a branch and bound algorithm are:

- Choose a node to expand from the tree, based on some selection rule (such as least cost, most promising, etc.).
- Check if the node is a leaf node, i.e., a complete solution. If yes, update the best solution and the bound, and backtrack to the parent node.
- If the node is not a leaf node, generate its children nodes by branching on a variable or a constraint, and compute the bound for each child node.
- Prune the child nodes that have a worse bound than the current best solution, and add the remaining child nodes to the tree.
- Repeat the process until the tree is empty or the bound is tight enough.

The main advantages of branch and bound are:

- It can find the optimal solution to a problem, or report that none exists.
- It can be more efficient than backtracking, as it can prune more branches in the tree using the bound information.
- It can be applied to a wide range of problems, such as 0/1 knapsack, travelling salesman, resource allocation, etc.

The main disadvantages of branch and bound are:

- It can still be very expensive, as it may explore a large number of nodes in the tree, especially if the bound is loose or the problem is hard.
- It can be very sensitive to the choice of the selection rule, the branching rule, and the bounding function, as they may affect the quality and the speed of the algorithm.
- It can be very difficult to design a good bounding function that can accurately estimate the optimal value of the objective function.

## Examples

### Travelling Salesman Problem

The travelling salesman problem (TSP) is a classic optimization problem, where given a set of n cities and the distances between them, the goal is to find the shortest tour that visits each city exactly once and returns to the starting city. The TSP is a NP-hard problem, meaning that there is no known polynomial-time algorithm that can solve it optimally.

One way to solve the TSP using backtracking is to use a permutation-based approach,