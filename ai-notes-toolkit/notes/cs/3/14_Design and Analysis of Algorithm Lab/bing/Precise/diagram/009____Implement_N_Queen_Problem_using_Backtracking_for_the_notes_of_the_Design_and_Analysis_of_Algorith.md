## Implement N Queen Problem using Backtracking

The N Queen problem is a classic problem in computer science and is often used to illustrate the concept of backtracking. The problem is to place N queens on an NxN chessboard such that no two queens attack each other. A queen can attack any piece in the same row, column, or diagonal.

Backtracking is a general algorithm for finding all (or some) solutions to a problem by incrementally building a solution and trying different possibilities. If the current solution is found to be unworkable, the algorithm backtracks to a previous state and tries a different possibility.

Here are the steps to implement the N Queen problem using backtracking:

1. Start with an empty NxN chessboard.
2. Place the first queen in the first column of the first row.
3. Move to the next column and try to place a queen in a row where it is not attacked by any other queen.
4. If a queen can be placed, move to the next column and repeat step 3.
5. If a queen cannot be placed in any row of the current column, backtrack to the previous column and move the queen to the next possible row.
6. Repeat steps 3-5 until all queens are placed or it is determined that no solution exists.
7. If all queens are placed, a solution has been found. Otherwise, no solution exists.

This algorithm can be implemented using recursion, where each recursive call represents the placement of a queen in a column. The base case is when all queens have been placed, and the recursive case is when a queen is placed in a column and the algorithm moves to the next column.

This is a brief overview of how to implement the N Queen problem using backtracking. For a more detailed explanation and example code, please refer to a textbook or online resource on the subject.