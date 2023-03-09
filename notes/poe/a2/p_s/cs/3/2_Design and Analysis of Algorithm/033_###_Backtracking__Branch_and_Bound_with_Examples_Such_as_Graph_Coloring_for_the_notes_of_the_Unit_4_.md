 Here is the content in markdown format for the topic ### Backtracking, Branch and Bound with Examples Such as Graph Coloring for the notes of the Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets. in the subject of Design and Analysis of Algorithm:

### Backtracking
- Backtracking is a general algorithmic technique that considers searching through all possible combinations systematically and abandons each partial solution as soon as it determines that it cannot lead to a valid full solution.
- It is useful to solve problems that exhibit the properties of exhaustive search and pruning (like the brute-force approach).
- The basic steps in backtracking are:
1. considering a partial candidate solution
2. extending the partial candidate solution to a full valid solution if possible
3. otherwise backtracking by undoing the recent changes to the partial candidate solution
- Examples: Graph coloring, Hamiltonian cycle, N-Queens problem, Subset sum problem, etc.

Advantages:
- Guaranteed to find a solution if one exists
- Simple to implement

Disadvantages:
- Wasteful as it explores many fruitless paths
- May take exponential time in the worst case

### Branch and Bound
- Branch and bound is a metaheuristic for combinatorial optimization problems.
- It consists of an enumeration-like technique that explores a tree-structured search space in a depth-first manner.
- The key idea is to use upper and lower bounds on the optimal solution value to prune subtrees that cannot contain an optimal solution.
- Examples: Travelling salesman problem, Knapsack problem, Graph coloring, etc.

Advantages:
- May find the optimal solution
- May explore fewer nodes than naive enumeration

Disadvantages:
- May still explore an exponential number of nodes in the worst case
- Finding good bounds can be difficult

[Detailed explanations, diagrams and examples can be added here if required.]