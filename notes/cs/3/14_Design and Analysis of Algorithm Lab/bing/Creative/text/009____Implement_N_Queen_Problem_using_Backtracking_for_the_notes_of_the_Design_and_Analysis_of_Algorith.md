## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The N Queen Problem is to find an arrangement of N queens on a chess board of dimension N x N, such that no two queens can attack each other. A queen can attack horizontally, vertically, or diagonally.
- Backtracking is a technique to solve problems that involve searching for a solution among a large number of possibilities. It involves trying a possible solution, and if it does not work, undoing it and trying another one, until a solution is found or all possibilities are exhausted.
- The steps to implement the N Queen Problem using Backtracking are:

  1. Start from the leftmost column of the chess board.
  2. Try placing a queen in each row of the current column, and check if it is safe to do so. A queen is safe if there is no other queen in the same row, column, or diagonal.
  3. If a safe position is found, mark it as part of the solution and move to the next column. Recursively repeat steps 2 and 3 for the remaining columns.
  4. If no safe position is found in the current column, backtrack to the previous column and remove the queen from the marked position. Try placing the queen in a different row of the same column and repeat steps 2 and 3.
  5. If all columns are filled with queens, the solution is complete and can be printed or returned.
  6. If all possible positions are tried and no solution is found, the problem has no solution and can be reported.

- The following is a possible pseudocode for the N Queen Problem using Backtracking:

  ```
  function NQueen(n):
    // create an empty n x n chess board
    board = create a 2D array of size n x n and fill it with 0
    // try placing queens starting from the first column
    if NQueenHelper(board, 0, n) == false:
      // no solution exists
      print "No solution"
    else:
      // print the solution
      print board

  function NQueenHelper(board, col, n):
    // base case: all columns are filled
    if col == n:
      // solution found
      return true
    // try each row in the current column
    for row in 0 to n-1:
      // check if the queen can be placed safely
      if isSafe(board, row, col, n) == true:
        // place the queen
        board[row][col] = 1
        // try placing queens in the next column
        if NQueenHelper(board, col+1, n) == true:
          // solution found
          return true
        // if not, backtrack and remove the queen
        board[row][col] = 0
    // if no row works, no solution exists in this branch
    return false

  function isSafe(board, row, col, n):
    // check the row
    for i in 0 to col-1:
      if board[row][i] == 1:
        return false
    // check the upper left diagonal
    for i, j in row-1, col-1 to 0, 0 by -1, -1:
      if board[i][j] == 1:
        return false
    // check the lower left diagonal
    for i, j in row+1, col-1 to n-1, 0 by 1, -1:
      if board[i][j] == 1:
        return false
    // if none of the above cases are true, the position is safe
    return true
  ```