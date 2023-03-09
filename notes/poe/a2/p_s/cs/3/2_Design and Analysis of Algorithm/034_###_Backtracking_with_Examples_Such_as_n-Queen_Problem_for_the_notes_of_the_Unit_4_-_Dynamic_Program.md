 Here are the notes for the topic ### Backtracking with Examples Such as n-Queen Problem for the unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets. in the subject of Design and Analysis of Algorithm:

### Backtracking
Backtracking is a general algorithmic technique that considers searching through all possible candidates for a solution and abandons each partial candidate ("backtracks") as soon as it is clear that it cannot lead to a valid solution.

- It is a trial-and-error mechanism
- It is a systematic enumeration of candidate solutions
- It is a depth-first search

**Steps involved in backtracking algorithm:**
1. Initialize the solution vector.
2. If the current vector satisfies the objective/complete solution, return the solution.
3. For each possible choice at the current stage, recursively construct the solutions by assuming the choice as part of the solution.
4. Backtrack (remove the choice) if the choice does not lead to a valid solution.

**Applications of Backtracking:**
- Finding all (or some) solutions to some computational problems, such as constraint satisfaction and optimization problems.
- Combinatorial problems such as:
    - Permutations
    - Subsets
    - Graph coloring
    - Hamiltonian cycles
- Games with large search spaces, such as chess and Go.

**Pros of Backtracking:**
- Guaranteed to find a solution if one exists
- Simple to implement

**Cons of Backtracking:**
- May take exponential time due to enumerating all candidates
- May encounter repeated work if the same partial candidates are explored more than once

**Example: N-Queen Problem**
The N queen problem is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
The constraints are:
- Each queen can move any number of squares in any horizontal, vertical, or diagonal direction.
- No two queens can be in the same row, column, or diagonal.

We can solve this using backtracking as follows:
1. Place the first queen in the first column
2. For each row in the first column, recursively place the remaining queens
3. If it is not possible to place all queens, backtrack and try other positions for the first queen
4. Repeat step#2 until all queens are placed or backtracking is required

This will print all distinct solutions to the N queen problem.

The time complexity of this algorithm is O(N!).

Does this help? Let me know if you would like me to elaborate on any part of the notes.