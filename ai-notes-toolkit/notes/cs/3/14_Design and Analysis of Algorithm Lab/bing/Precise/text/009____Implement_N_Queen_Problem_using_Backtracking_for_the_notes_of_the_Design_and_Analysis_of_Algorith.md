## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

The N Queen problem is a classic problem in computer science, where the goal is to place N queens on an NxN chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal.

One way to solve the N Queen problem is by using backtracking. Backtracking is a general algorithm for finding all (or some) solutions to a problem by incrementally building a solution and trying different possibilities. If a partial solution is found to be invalid, the algorithm backtracks to a previous state and tries a different possibility.

Here are the steps to implement the N Queen problem using backtracking:

1. Start with an empty NxN chessboard.
2. Place the first queen in the first column of the first row.
3. Move to the next column and try to place a queen in a row where it is not threatened by any previously placed queen.
4. If a valid position is found, place the queen and move to the next column.
5. If no valid position is found, backtrack to the previous column and move the queen to a different row.
6. Repeat steps 3-5 until all queens are placed or it is determined that no solution exists.

This algorithm can be implemented using recursion, where each recursive call represents the placement of a queen in a column. The base case is when all queens have been placed, and the recursive case is when a queen is placed in a column and the algorithm moves to the next column.

The time complexity of this algorithm is O(N!), where N is the number of queens. This is because, in the worst case, the algorithm must try all possible permutations of queen placements. However, in practice, the algorithm is much faster due to the pruning of invalid solutions.

In conclusion, the N Queen problem can be solved using backtracking, where the algorithm incrementally builds a solution and backtracks when an invalid partial solution is found. This algorithm can be implemented using recursion and has a time complexity of O(N!).