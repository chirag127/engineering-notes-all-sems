# Backtracking with Examples Such as n-Queen Problem

- Backtracking is a technique to solve problems that involve finding all possible solutions or configurations that satisfy some constraints or criteria.
- Backtracking works by exploring the solution space incrementally, making a partial choice at each step, and then checking if the choice is feasible or not.
- If the choice is feasible, then the algorithm continues to make further choices until a complete solution is found or no more choices are available.
- If the choice is not feasible, then the algorithm backtracks, i.e., it undoes the last choice and tries a different alternative.
- Backtracking is often implemented using recursion, where each recursive call represents a choice and the base case represents a solution or a dead end.
- Backtracking can be applied to many problems, such as puzzles, games, combinatorial optimization, constraint satisfaction, etc.

## n-Queen Problem

- n-Queen problem is one of the most common examples of backtracking.
- n-Queen problem is defined as, “given n x n chess board, arrange n queens in such a way that no two queens attack each other by being in same row, column or diagonal”.
- For n = 1, this is a trivial case. For n = 2 or n = 3, there is no solution. For n >= 4, there are one or more solutions.
- One way to solve the n-Queen problem using backtracking is as follows:

  - Start from the first row of the board and place a queen in the first column.
  - Move to the next row and try to place a queen in each column, checking if it is safe or not. A queen is safe if it does not share the same row, column or diagonal with any other queen on the board.
  - If a safe column is found, place the queen and recurse for the next row. If no safe column is found, backtrack to the previous row and move the queen to the next safe column.
  - Repeat this process until all the rows are filled with queens or no more safe columns are left.

- The pseudocode for the algorithm is given below:

```
# n is the size of the board
# board is a 2D array of size n x n, initialized with 0
# row is the current row to place a queen

def solve_n_queen(n, board, row):
  # base case: all rows are filled with queens
  if row == n:
    return True
  
  # try each column in the current row
  for col in range(n):
    # check if the queen can be placed safely
    if is_safe(board, row, col):
      # place the queen
      board[row][col] = 1
      # recurse for the next row
      if solve_n_queen(n, board, row + 1):
        return True
      # backtrack if the next row cannot be solved
      board[row][col] = 0
  
  # no solution for the current row
  return False

def is_safe(board, row, col):
  # check the same column
  for i in range(row):
    if board[i][col] == 1:
      return False
  
  # check the upper left diagonal
  i = row - 1
  j = col - 1
  while i >= 0 and j >= 0:
    if board[i][j] == 1:
      return False
    i -= 1
    j -= 1
  
  # check the upper right diagonal
  i = row - 1
  j = col + 1
  while i >= 0 and j < len(board):
    if board[i][j] == 1:
      return False
    i -= 1
    j += 1
  
  # the queen is safe
  return True
```

- The time complexity of the algorithm is O(n^n), where n is the size of the board. This is because there are n possible choices for each row, and there are n rows to fill.
- The space complexity of the algorithm is O(n^2), where n is the size of the board. This is because the board is a 2D array of size n x n, and the recursive call stack can go up to n levels deep.