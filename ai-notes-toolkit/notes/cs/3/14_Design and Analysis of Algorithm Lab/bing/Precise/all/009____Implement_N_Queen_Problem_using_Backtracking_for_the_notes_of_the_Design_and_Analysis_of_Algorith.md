## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

The N Queen problem is a classic problem in computer science. The goal is to place N queens on an NxN chessboard such that no two queens threaten each other. This means that no two queens can be in the same row, column, or diagonal.

Backtracking is a general algorithm for finding all (or some) solutions to a problem that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Here are the steps to implement the N Queen problem using backtracking:

1. Start in the leftmost column.
2. If all queens are placed, return true.
3. Try all rows in the current column. For each row, do the following:
    a. If the queen can be placed safely in this row, mark this [row, column] as part of the solution and recursively check if placing the queen here leads to a solution.
    b. If placing the queen in [row, column] leads to a solution, return true.
    c. If placing the queen doesn't lead to a solution, unmark this [row, column] (backtrack) and go to step 3 to try other rows.
4. If all rows have been tried and nothing worked, return false to trigger backtracking.

This algorithm can be implemented using recursion and backtracking. The time complexity of this algorithm is O(N!) as there are N! permutations of the N queens on the NxN chessboard. However, the backtracking helps to prune the search space and reduce the time complexity.
