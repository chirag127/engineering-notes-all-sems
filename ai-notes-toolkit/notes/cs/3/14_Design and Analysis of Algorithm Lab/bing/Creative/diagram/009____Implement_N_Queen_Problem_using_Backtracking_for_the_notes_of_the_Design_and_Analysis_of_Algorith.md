## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The N Queen Problem is to find an arrangement of N queens on a chess board of dimension N x N, such that no two queens can attack each other   .
- A queen can attack horizontally, vertically, or diagonally  .
- Backtracking is a technique to solve problems that involve searching for a feasible solution among a large number of possibilities .
- Backtracking works by systematically trying all possible assignments of values to the variables in a problem, to find the feasible solutions.
- If a partial solution is found to be invalid, the algorithm backtracks to the previous step and tries a different value  .
- The algorithm stops when all possible solutions are explored or a valid solution is found  .

### Algorithm

- The algorithm for solving the N Queen Problem using backtracking is as follows  :

1. Start in the leftmost column
2. If all queens are placed, return true
3. Try all rows in the current column. Do the following for every tried row:
   - If the queen can be placed safely in this row, then mark this [row, column] as part of the solution and recursively check if placing the queen here leads to a solution
   - If placing the queen in [row, column] leads to a solution, then return true
   - If placing the queen does not lead to a solution, then unmark this [row, column] (backtrack) and try another row
4. If all rows have been tried and nothing worked, return false to trigger backtracking

### Implementation

- The implementation of the algorithm in C++ is as follows  :

```cpp
#include <iostream>
using namespace std;

// N is the size of the chessboard
#define N 4

// A utility function to print the solution matrix
void printSolution(int board[N][N]) {
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++)
      cout << board[i][j] << " ";
    cout << endl;
  }
}

// A utility function to check if a queen can be placed on board[row][col]
// Note that this function is called when "col" queens are already placed
// in columns from 0 to col - 1. So we need to check only left side for
// attacking queens
bool isSafe(int board[N][N], int row, int col) {
  // Check this row on left side
  for (int i = 0; i < col; i++)
    if (board[row][i])
      return false;

  // Check upper diagonal on left side
  for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
    if (board[i][j])
      return false;

  // Check lower diagonal on left side
  for (int i = row, j = col; j >= 0 && i < N; i++, j--)
    if (board[i][j])
      return false;

  return true;
}

// A recursive utility function to solve N Queen problem
bool solveNQUtil(int board[N][N], int col) {
  // Base case: If all queens are placed, then return true
  if (col >= N)
    return true;

  // Consider this column and try placing this queen in all rows one by one
  for (int i = 0; i < N; i++) {
    // Check if the queen can be placed on board[i][col]
    if (isSafe(board, i, col)) {
      // Place this queen in board[i][col]
      board[i][col] = 1;

      // Recur to place rest of the queens
      if (solveNQUtil(board, col + 1))
        return true;

      // If placing queen in board[i][col] doesn't lead to a solution, then
      // remove queen from board[i][col]
      board[i][col] = 0

```
