 Here are the notes for the topic ### Backtracking with Examples Such as Sum of Subsets for the Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets. in the subject of Design and Analysis of Algorithm:

## Backtracking
Backtracking is a general algorithmic technique that considers searching every possible combination in order to solve an optimization problem. It abandons each partial solution as soon as it determines that it cannot lead to a valid full solution.

### Steps involved in Backtracking:
1. Start with the first choice.
2. Check if the choice leads to a solution.
3. If yes, then print the solution.
4. If not, then undo the choice and go to the next choice.
5. Repeat steps#2 to #4 until all choices are exhausted.

### Advantages:
- Simple and easy to implement.
- Can lead to optimal solutions.
- Useful for combinatorial problems like finding subsets, permutations, etc.

### Disadvantages:
- Not efficient for larger problems as it examines a large number of unnecessary paths.
- Lot of wasted computations in abandoning partial solutions.

### Examples:
- Sum of subsets problem: Find a subset of a given set whose sum is equal to a given sum.
- Hamiltonian cycle: Find if a Hamiltonian cycle exists in a given graph.
- N-Queen problem: Place N queens on an N*N chessboard such that no two queens attack each other.
- Graph coloring: Color a given graph using minimum colors such that no two adjacent vertices have the same color.

### Applications:
- Used to solve various puzzles and games involving sequence generation or constrained search spaces.
- Used in AI for decision making under constraints.
- Used for scheduling and optimization problems to find best solutions.