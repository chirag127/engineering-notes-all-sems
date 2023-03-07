 Here is the content in markdown format for the topic ## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System:

# Implement N Queen Problem using Backtracking

The N Queen is a classic backtracking problem. The goal is to place N queens on an N×N chessboard such that no two queens attack each other. Two queens attack each other if they are on the same row, column, or diagonal.

## Algorithm

1.  Create a boolean array `board[N][N]` and initialize all entries to `false`.
2.  Define a recursive backtracking function `solveNQUtil()` to find a solution.
3.  In the `solveNQUtil()` function:
    -   If all queens are placed, then print the `board` and return true.
    -   Consider each row one by one and try different columns for the queen in the current row.
    	-   If it is safe to place queen in the current column, then mark this `board[row][col] = true`.
    	-   Recurse for the next row with `solveNQUtil()`.
    	-   If the queen cannot be placed in any column in the current row, then undo the changes by setting `board[row][col] = false` and return false.
4.  Call `solveNQUtil(0)` to start placing queens on the board.

```
bool solveNQUtil(int col) {
    // base case: If all queens are placed
    // then return true
    if (col >= N)
        return true;

    // Consider this queen and try placing
    // it in all rows one by one
    for (int i = 0; i < N; i++) {
        // Check if queen can be placed on
        // board[i][col]
        if (isSafe(i, col)) {
            // Place this queen in column col
            // in row i
            board[i][col] = true;

            // Make recursive call for next queen
            if (solveNQUtil(col + 1) == true)
                return true;

            // If placing queen in row i doesn't
            // lead to a solution, then remove queen
            // from board[i][col]
            board[i][col] = false;
        }
    }

    // If the queen can not be placed in any row in
    // this column col then return false
    return false;
}
```

## Analysis

- Time Complexity: Exponential `O(N!)`
- Space Complexity: `O(N)` to keep track of the board
- Advantages: Simple and efficient backtracking approach
- Applications: Scheduling, computational geometry, etc.