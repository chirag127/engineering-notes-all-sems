 Here is the content in markdown format for the topic ### Backtracking with Examples Such as Hamiltonian Cycles for the notes of the Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets. in the subject of Design and Analysis of Algorithm:

### Backtracking
Backtracking is a general algorithmic technique that considers searching every possible combination in order to solve an optimization problem. It abandons each partial solution as soon as it determines that it cannot lead to a valid full solution.

#### Hamiltonian Cycle
A Hamiltonian cycle (or Hamiltonian circuit) is a graph cycle that visits each vertex exactly once. Determining whether such cycles exist in graphs is an NP-complete problem. Backtracking can be used to find a Hamiltonian cycle.

Algorithm:
1. Start at an arbitrary vertex v
2. If all vertices have been visited, a Hamiltonian cycle has been found. Return true
3. For each neighbour u of v:
    1. If u has not yet been visited:
        1. Mark u as visited
        2. If Backtrack(G, u) returns true, return true
4. Mark v as unvisited
5. Return false

Complexity: O(n^2*2^n)

Where n is the number of vertices in the graph. This is very inefficient for large graphs since the number of recursive calls grows exponentially.

Advantages:
- Simple to implement
- Can be applied to a wide range of problems

Disadvantages:
- May take exponential time due to recursive nature
- May explore many unnecessary paths

Applications:
- Finding solutions to combinatorial problems (Hamiltonian cycles, graph coloring, etc.)
- Games with a large search space (chess, sudoku, etc.)

#### Other Examples
- Travelling Salesman Problem: Find the shortest route visiting each city exactly once and returning to the starting city
- Graph Coloring: Assign colors to vertices such that no adjacent vertices have the same color
- N-Queens Problem: Place N queens on an N×N chessboard such that no two queens attack each other
- Sum of Subsets: Find a subset of a set of integers that has a given sum