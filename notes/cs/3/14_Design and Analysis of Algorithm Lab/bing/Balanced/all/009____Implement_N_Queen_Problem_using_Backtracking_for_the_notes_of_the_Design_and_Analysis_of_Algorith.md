## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The N Queen problem is a classic example of backtracking, a technique for solving problems recursively by trying to build a solution incrementally, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
- The N Queen problem is to place N queens on an N x N chessboard such that no two queens attack each other. A queen can move horizontally, vertically, or diagonally on the board.
- The backtracking algorithm for the N Queen problem works as follows:

  - Start from the leftmost column of the board.
  - For each row in the current column, do the following:
    - Check if placing a queen in this row is safe, i.e., it does not conflict with any of the previously placed queens.
    - If it is safe, mark this row and column as part of the solution and recursively try to place the rest of the queens in the next columns.
    - If placing a queen in this row leads to a solution, return true.
    - If placing a queen in this row does not lead to a solution, unmark this row and column as part of the solution and backtrack to the previous column.
  - If all the rows in the current column have been tried and none of them leads to a solution, return false.

- The pseudocode for the backtracking algorithm is given below:

  ```
  function solveNQueen(board, col)
    // base case: all queens are placed
    if col == N
      return true
    // consider each row in the current column
    for row from 0 to N-1
      // check if placing a queen in this row is safe
      if isSafe(board, row, col)
        // mark this row and column as part of the solution
        board[row][col] = 1
        // recursively try to place the rest of the queens
        if solveNQueen(board, col + 1)
          return true
        // if placing a queen in this row does not lead to a solution, backtrack
        board[row][col] = 0
    // if no row in the current column leads to a solution, return false
    return false
  ```

- The function isSafe(board, row, col) checks if placing a queen in the given row and column is safe, i.e., it does not conflict with any of the previously placed queens. It can be implemented as follows:

  ```
  function isSafe(board, row, col)
    // check the left side of the current row
    for i from 0 to col-1
      if board[row][i] == 1
        return false
    // check the upper left diagonal
    for i, j from row-1, col-1 to 0, 0
      if board[i][j] == 1
        return false
    // check the lower left diagonal
    for i, j from row+1, col-1 to N-1, 0
      if board[i][j] == 1
        return false
    // if none of the above cases is true, return true
    return true
  ```

- The time complexity of the backtracking algorithm is O(N!), where N is the number of queens. This is because there are N possible choices for the first queen, N-1 for the second queen, and so on, until 1 for the last queen. The space complexity is O(N^2), where N is the number of queens. This is because we need to store the board of size N x N and the recursive call stack of depth N.