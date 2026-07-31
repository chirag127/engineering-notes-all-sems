### Backtracking with Examples Such as n-Queen Problem

Backtracking is a general algorithm for finding all (or some) solutions to a problem that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

The n-Queen problem is a classic example of a problem that can be solved using backtracking. The problem is to place n queens on an n×n chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

To solve the n-Queen problem using backtracking, we can start by placing the first queen in the first row. Then, we move to the next row and try to place the second queen in a column that is not threatened by the first queen. If we find such a column, we move to the next row and repeat the process. If we do not find such a column, we backtrack to the previous row and move the queen to a different column. We continue this process until we have placed all n queens on the board.

Here is an example of how the backtracking algorithm can be used to solve the 4-Queen problem:

1. Place the first queen in the first row, first column.
2. Move to the second row and try to place the second queen in a column that is not threatened by the first queen. The only column that is not threatened is the third column.
3. Move to the third row and try to place the third queen in a column that is not threatened by the first two queens. There is no such column, so we backtrack to the second row and move the second queen to a different column. The only other column that is not threatened is the fourth column.
4. Move to the third row and try to place the third queen in a column that is not threatened by the first two queens. The only column that is not threatened is the first column.
5. Move to the fourth row and try to place the fourth queen in a column that is not threatened by the first three queens. The only column that is not threatened is the second column.

Thus, one solution to the 4-Queen problem is to place the queens in the following positions: (1, 1), (2, 4), (3, 1), (4, 2).

Backtracking can be used to solve many other problems, such as the traveling salesman problem, graph coloring, Hamiltonian cycles, and the sum of subsets problem. In each of these problems, the backtracking algorithm incrementally builds a solution and abandons it if it is not valid. This allows the algorithm to efficiently search the solution space and find all (or some) solutions to the problem.