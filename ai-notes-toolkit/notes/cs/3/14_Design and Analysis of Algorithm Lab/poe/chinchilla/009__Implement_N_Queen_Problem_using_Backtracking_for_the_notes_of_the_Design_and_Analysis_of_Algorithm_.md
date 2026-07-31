## Implement N Queen Problem using Backtracking

The N Queen Problem is a classic problem of placing N chess queens on an N×N chessboard such that no two queens threaten each other. This means that no two queens can share the same row, column, or diagonal. In this lab, we will implement the N Queen Problem using Backtracking.

### Backtracking

Backtracking is a technique used to solve problems by attempting to build a solution incrementally, one piece at a time, while removing solutions that fail to satisfy the constraints of the problem at any point of time. Backtracking is a depth-first search (DFS) with added constraints on the search space.

### Steps to implement N Queen Problem using Backtracking

1. Create an empty chess board of size N×N.
2. Place the first queen in the first row and first column.
3. Move to the next row and check if placing a queen in any of the columns of that row violates the constraints of the problem (i.e., no two queens can share the same row, column, or diagonal).
4. If a column is found that does not violate the constraints, place a queen in that column and move to the next row.
5. If no such column is found, backtrack to the previous row and try a different column in that row.
6. Repeat steps 3 to 5 until all queens are placed on the chessboard.

### Pseudocode

The following is the pseudocode for implementing the N Queen Problem using Backtracking:

```
procedure n_queen(board, row):
   if row = N:
      return true
   for each column in row:
      if is_safe(board, row, column):
         board[row][column] = 1
         if n_queen(board, row+1) = true:
            return true
         board[row][column] = 0
   return false

function is_safe(board, row, column):
   for i = 0 to row-1:
      if board[i][column] = 1:
         return false
   for i = row-1, j = column-1; i >= 0 and j >= 0; i--, j--:
      if board[i][j] = 1:
         return false
   for i = row-1, j = column+1; i >= 0 and j < N; i--, j++:
      if board[i][j] = 1:
         return false
   return true
```

### Complexity Analysis

The time complexity of the N Queen Problem using Backtracking is O(N!), where N is the size of the chessboard. This is because the number of possible solutions to the problem is factorial in nature.

The space complexity of the algorithm is O(N^2), where N is the size of the chessboard. This is because we are using a 2D array to represent the chessboard.

### Conclusion

In this lab, we have learned how to implement the N Queen Problem using Backtracking. Backtracking is a powerful technique that can be used to solve a wide variety of problems. The N Queen Problem is just one example of a problem that can be solved using Backtracking.