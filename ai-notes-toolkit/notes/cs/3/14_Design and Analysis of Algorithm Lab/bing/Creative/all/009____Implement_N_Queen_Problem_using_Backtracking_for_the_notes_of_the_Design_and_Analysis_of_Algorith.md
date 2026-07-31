# Implement N Queen Problem using Backtracking

- The N Queen Problem is to find an arrangement of N queens on a chess board of dimension N x N, such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally.
- Backtracking is a technique to solve problems that involve searching for a solution among a set of possible choices. It works by trying one choice and then checking if it leads to a valid solution. If not, it backtracks and tries another choice until a solution is found or all choices are exhausted.
- The steps to implement the N Queen Problem using backtracking are:

  1. Start from the leftmost column of the board.
  2. Try placing a queen in each row of the current column, one by one.
  3. For each placement, check if it is safe, i.e., no other queen can attack it. This can be done by checking the row, column, and the two diagonals of the current position.
  4. If the placement is safe, mark it as part of the solution and recursively try placing queens in the next column.
  5. If the recursive call returns true, that means a solution is found. Return true and print the solution.
  6. If the recursive call returns false, that means the current placement does not lead to a solution. Unmark it and try the next row in the current column.
  7. If all rows in the current column are tried and none of them leads to a solution, return false and backtrack to the previous column.

- The following is a possible pseudocode for the N Queen Problem using backtracking:

  ```
  function NQueen(board, col)
    // base case: all columns are filled
    if col == N
      return true
    // try each row in the current column
    for row from 0 to N-1
      // check if the placement is safe
      if isSafe(board, row, col)
        // mark the position as part of the solution
        board[row][col] = 1
        // recursively try the next column
        if NQueen(board, col+1)
          return true
        // unmark the position if it does not lead to a solution
        board[row][col] = 0
    // return false if no solution is found in the current column
    return false
  ```

- The following is a possible diagram to illustrate the backtracking process for N = 4:

  ```
  | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |

  Try placing a queen in the first column
  | 1 | 0 | 0 | 0 |    | 0 | 1 | 0 | 0 |    | 0 | 0 | 1 | 0 |    | 0 | 0 | 0 | 1 |
  | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |    | 0 | 0 | 0 | 0 |
  | 0 | 0 | 0 | 0 |    | 0 | 0 |

```
