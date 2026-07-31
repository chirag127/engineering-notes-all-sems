# Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The N Queen Problem is to find an arrangement of N queens on a chessboard of dimension N x N, such that no two queens attack each other. A queen can attack horizontally, vertically, or diagonally.
- Backtracking is a technique to solve problems that involve searching for a solution among a large number of possibilities. It involves trying a possible solution, and if it does not work, undoing it and trying another one, until a solution is found or all possibilities are exhausted.
- The algorithm for solving the N Queen Problem using backtracking is as follows:

1. Start in the leftmost column
2. If all queens are placed, return true
3. Try all rows in the current column. Do following for every tried row.
   - If the queen can be placed safely in this row, then mark this [row, column] as part of the solution and recursively check if placing queen here leads to a solution.
   - If placing the queen in [row, column] leads to a solution, then return true.
   - If placing the queen does not lead to a solution, then unmark this [row, column] (backtrack) and try another row.
4. If all rows have been tried and nothing worked, return false to trigger backtracking.

- The pseudocode for the algorithm is as follows:

```
// A utility function to check if a queen can be placed on board[row][col]
// Note that this function is called when "col" queens are already placed
// in columns from 0 to col -1. So we need to check only left side for
// attacking queens
function isSafe(board, row, col)
    // Check this row on left side
    for i = 0 to col
        if board[row][i] == 1
            return false
    // Check upper diagonal on left side
    for i = row, j = col, while i >= 0 and j >= 0
        if board[i][j] == 1
            return false
        i = i - 1
        j = j - 1
    // Check lower diagonal on left side
    for i = row, j = col, while i < N and j >= 0
        if board[i][j] == 1
            return false
        i = i + 1
        j = j - 1
    return true

// A recursive utility function to solve N Queen problem
function solveNQUtil(board, col)
    // base case: If all queens are placed then return true
    if col == N
        return true
    // Consider this column and try placing this queen in all rows one by one
    for i = 0 to N-1
        // Check if the queen can be placed on board[i][col]
        if isSafe(board, i, col)
            // Place this queen in board[i][col]
            board[i][col] = 1
            // recur to place rest of the queens
            if solveNQUtil(board, col + 1) == true
                return true
            // If placing queen in board[i][col] doesn't lead to a solution, then
            // remove queen from board[i][col]
            board[i][col] = 0 // BACKTRACK
    // If the queen can not be placed in any row in this column col, then return false
    return false

// This function solves the N Queen problem using Backtracking. It mainly uses
// solveNQUtil() to solve the problem. It returns false if queens cannot be placed,
// otherwise, return true and prints placement of queens in the form of 1s.
// Please note that there may be more than one solutions, this function prints one
// of the feasible solutions.
function solveNQ()
    board = { {0, 0, 0, 0},
              {0, 0, 0, 0},
              {0, 0, 0, 0},
              {0, 0, 0, 0} }
    if solveNQUtil(board, 0) == false
       print "Solution does not exist"
       return false
    printSolution(board)
    return true
```
- The time complexity of the algorithm is O(N!), where N is the number of queens. This is because for