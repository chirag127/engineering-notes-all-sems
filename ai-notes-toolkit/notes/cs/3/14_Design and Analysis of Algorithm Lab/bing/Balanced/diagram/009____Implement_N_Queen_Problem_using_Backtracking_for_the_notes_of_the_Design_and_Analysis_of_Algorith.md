Hello, I am Sydney, your AI assistant. I can help you with your query.

## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- The N Queen problem is a classic example of a combinatorial optimization problem, where the goal is to place N queens on an N x N chessboard, such that no two queens can attack each other.
- A queen can attack another queen if they are on the same row, column, or diagonal.
- One way to solve this problem is to use backtracking, which is a technique of exploring all possible solutions by making a sequence of choices, and then undoing some of the choices if they lead to a dead end or a contradiction.
- The basic idea of backtracking is to use a recursive function that tries to place a queen in each column, starting from the leftmost column.
- For each column, the function checks if there is a safe row to place the queen, i.e., a row that does not conflict with any of the previously placed queens.
- If there is a safe row, the function places the queen there, and then moves on to the next column.
- If there is no safe row, the function backtracks, i.e., removes the queen from the current column, and tries a different row in the previous column.
- The function repeats this process until all the columns are filled with queens, or until it reaches the first column and finds no safe row to place the queen.
- If the function succeeds in placing all the queens, it returns true, and prints the solution. Otherwise, it returns false, and indicates that there is no solution.

- Here is a pseudocode of the backtracking algorithm for the N Queen problem:

```
// A global array to store the positions of the queens
// queen[i] = j means there is a queen at row j and column i
int queen[N]

// A function to check if a queen can be placed at row r and column c
// It returns true if there is no conflict, and false otherwise
bool isSafe(int r, int c)
  // Loop through all the columns from 0 to c-1
  for i = 0 to c-1
    // Check if there is a queen at row r or the same diagonal as (r,c)
    if queen[i] == r or abs(queen[i] - r) == abs(i - c)
      // There is a conflict, return false
      return false
  // There is no conflict, return true
  return true

// A recursive function to solve the N Queen problem
// It takes the current column c as a parameter, and returns true if a solution is found, and false otherwise
bool solveNQueen(int c)
  // Base case: if all the columns are filled, a solution is found
  if c == N
    // Print the solution
    for i = 0 to N-1
      print queen[i]
    // Return true
    return true
  // Recursive case: try to place a queen in each row of the current column
  for r = 0 to N-1
    // Check if the row is safe
    if isSafe(r, c)
      // Place the queen at row r and column c
      queen[c] = r
      // Recursively try to place the queens in the next columns
      if solveNQueen(c+1)
        // A solution is found, return true
        return true
      // No solution is found, backtrack and remove the queen from row r and column c
      queen[c] = -1
  // No solution is found for the current column, return false
  return false
```

- To start the algorithm, we call the function solveNQueen(0), which tries to place a queen in the first column.
- The time complexity of the backtracking algorithm is O(N!), where N is the size of the chessboard. This is because in the worst case, the algorithm has to try all possible permutations of the rows to place the queens.
- The space complexity of the backtracking algorithm is O(N), where N is the size of the chessboard. This is because the algorithm uses a global array of size N to store the positions of the queens, and a recursive stack of size N to store the function calls.