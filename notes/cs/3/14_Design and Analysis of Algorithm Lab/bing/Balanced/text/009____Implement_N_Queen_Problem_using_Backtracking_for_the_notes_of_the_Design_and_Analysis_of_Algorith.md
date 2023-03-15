## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The N Queen problem is a classic example of backtracking, a technique for solving problems recursively by trying to build a solution incrementally, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
- The N Queen problem is to place N queens on an N x N chessboard such that no two queens attack each other. A queen can attack another queen if they are on the same row, column, or diagonal.
- The backtracking algorithm for the N Queen problem works as follows:

  - Start from the first row and place a queen on the first column.
  - Move to the next row and try to place a queen on each column, checking if it is safe to do so. A position is safe if no other queen can attack it from the previous rows.
  - If a safe position is found, place the queen and recursively try to place the rest of the queens on the remaining rows.
  - If no safe position is found on the current row, backtrack to the previous row and move the queen to the next column. Repeat this process until all the queens are placed or all the columns are exhausted.
  - If all the queens are placed, print the solution. Otherwise, report that no solution exists.

- The pseudocode for the backtracking algorithm is given below:

  ```
  function solveNQueen(board, row, n):
    if row == n: // all queens are placed
      print board
      return true
    for col in 0 to n-1: // try each column
      if isSafe(board, row, col, n): // check if the position is safe
        board[row][col] = 1 // place the queen
        if solveNQueen(board, row+1, n): // recursively try the next row
          return true
        board[row][col] = 0 // backtrack and remove the queen
    return false // no solution on this row
  ```

- The function isSafe checks if a queen can be placed on board[row][col] by iterating over the previous rows and checking if there is a queen on the same column, the left diagonal, or the right diagonal. The pseudocode for the function is given below:

  ```
  function isSafe(board, row, col, n):
    for i in 0 to row-1: // check the same column
      if board[i][col] == 1:
        return false
    for i, j in row-1, col-1 to 0, 0: // check the left diagonal
      if board[i][j] == 1:
        return false
    for i, j in row-1, col+1 to 0, n-1: // check the right diagonal
      if board[i][j] == 1:
        return false
    return true // the position is safe
  ```

- The time complexity of the backtracking algorithm is O(N!), where N is the number of queens. This is because there are N possible choices for the first queen, N-1 for the second, N-2 for the third, and so on, resulting in N! permutations. The space complexity is O(N^2), where N is the number of queens. This is because we need to store the board of size N x N and the recursive call stack of depth N.