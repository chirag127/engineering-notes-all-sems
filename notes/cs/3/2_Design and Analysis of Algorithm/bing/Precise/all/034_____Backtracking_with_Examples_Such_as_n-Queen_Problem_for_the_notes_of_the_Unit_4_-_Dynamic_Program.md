### Backtracking with Examples Such as n-Queen Problem

Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).

Backtracking can be used to solve problems where the solution is a sequence of choices, such as the n-Queen problem. The n-Queen problem is the problem of placing n queens on an n×n chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

The backtracking algorithm for the n-Queen problem starts by placing a queen in the first row of the chessboard. Then, it moves to the next row and tries to place a queen in a column that is not threatened by the previously placed queens. If it is not possible to place a queen in any column of the current row, the algorithm backtracks to the previous row and moves the queen to the next available column. This process is repeated until all queens are placed on the chessboard or it is determined that no solution exists.

Backtracking can be applied to other problems as well, such as graph coloring, Hamiltonian cycles, and the sum of subsets problem. In each of these problems, the solution is a sequence of choices and the backtracking algorithm incrementally builds the solution while ensuring that the constraints of the problem are satisfied.