## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The N Queen Problem is to find an arrangement of N queens on a chess board of dimension N x N, such that no two queens can attack each other. A queen can attack horizontally, vertically, or diagonally.
- Backtracking is a technique to solve problems that involve searching for a feasible solution among a large number of possibilities. It works by trying a partial solution and then recursively extending it until it either reaches a complete solution or a dead end.
- The algorithm for solving the N Queen Problem using backtracking is as follows:

  1. Start in the leftmost column
  2. If all queens are placed, return true and print the solution
  3. Try all rows in the current column. Do the following for every tried row:
     - If the queen can be placed safely in this row, then mark this [row, column] as part of the solution and recursively check if placing the queen here leads to a solution.
     - If placing the queen in [row, column] leads to a solution, then return true.
     - If placing the queen does not lead to a solution, then unmark this [row, column] (backtrack) and try another row.
  4. If all rows have been tried and nothing worked, return false and backtrack to the previous column.

- The pseudocode for the algorithm is as follows:

  ```python
  # A function to check if a queen can be placed on board[row][col]
  # Note that this function is called when "col" queens are already
  # placed in columns from 0 to col -1. So we need to check only left side
  # for attacking queens
  def isSafe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
      if board[row][i] == 1:
        return false
    # Check upper diagonal on left side
    i = row
    j = col
    while i >= 0 and j >= 0:
      if board[i][j] == 1:
        return false
      i = i - 1
      j = j - 1
    # Check lower diagonal on left side
    i = row
    j = col
    while i < N and j >= 0:
      if board[i][j] == 1:
        return false
      i = i + 1
      j = j - 1
    # If none of the above cases is true, then the queen can be placed safely
    return true

  # A recursive function to solve N Queen problem
  def solveNQUtil(board, col, N):
    # Base case: If all queens are placed, then return true
    if col == N:
      return true
    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
      # Check if the queen can be placed on board[i][col]
      if isSafe(board, i, col, N):
        # Place this queen in board[i][col]
        board[i][col] = 1
        # Recur to place rest of the queens
        if solveNQUtil(board, col + 1, N):
          return true
        # If placing queen in board[i][col] doesn't lead to a solution, then
        # remove queen from board[i][col]
        board[i][col] = 0 # BACKTRACK
    # If the queen can not be placed in any row in this column col, then return false
    return false

  # A function to print the solution
  def printSolution(board, N):
    for i in range(N):
      for j in range(N):
        print(board[i][j], end = " ")
      print()

  # A function to solve the N Queen problem using backtracking
  def solveNQ(N):
    # Create a 2D array to represent the chess board
    board = [[0 for i in range(N)] for j in range(N)]
    # Call the recursive function to solve the problem
    if solveNQUtil(board, 0, N) == false:
      print("Solution does not exist")
      return false
    # Print the solution
    printSolution(board, N)
    return true
  ```

- The time complexity of the algorithm is O(N