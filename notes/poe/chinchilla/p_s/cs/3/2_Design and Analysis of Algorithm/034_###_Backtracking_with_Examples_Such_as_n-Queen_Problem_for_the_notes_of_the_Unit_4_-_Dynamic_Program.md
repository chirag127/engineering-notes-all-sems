### Backtracking with Examples Such as n-Queen Problem

Backtracking is a technique used in algorithmic problem-solving to find solutions by exploring all possible paths and backtracking when a solution is not found. It involves exploring all possible solutions by incrementally building a solution and then backtracking when a solution is not feasible. Backtracking is an important technique in solving optimization problems and can be applied to problems such as the n-Queen problem, Graph Coloring, and Travelling Salesman problem.

#### n-Queen Problem

The n-Queen problem is a classic example of a backtracking problem. It involves placing n queens on an n x n chessboard such that no two queens threaten each other. In other words, no two queens can be placed on the same row, column, or diagonal. 

#### Algorithm

The algorithm for solving the n-Queen problem involves the following steps:

1. Start in the leftmost column
2. If all queens are placed, return true
3. Try all rows in the current column. For each row, do the following:
   1. If the queen can be placed in this row, mark this cell and the corresponding diagonals as threatened and move to the next column.
   2. If the queen cannot be placed in this row, unmark the cell and move to the next row.
4. If all rows have been tried and nothing worked, return false to trigger backtracking.

#### Advantages and Disadvantages

- Advantages:
    - Backtracking can solve optimization problems with a large search space.
    - It is a simple and efficient algorithmic technique.
- Disadvantages:
    - Backtracking can be computationally expensive and time-consuming for large input sizes.
    - Backtracking may not always find the optimal solution.

#### Applications

Backtracking can be applied to a wide range of problems, including:
- n-Queen problem
- Graph Coloring
- Travelling Salesman problem
- Hamiltonian Cycles
- Sum of Subsets

Overall, Backtracking is a powerful technique for solving optimization problems with a large search space. It can be applied to a wide range of problems and is often used in combination with other techniques such as branch and bound. The n-Queen problem is a classic example of a backtracking problem and helps understand the concept of backtracking better.