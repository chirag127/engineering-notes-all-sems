 Here is the content in markdown format without any emojis or external links and in formal tone:

## Implement N Queen Problem using Backtracking for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System.

1. Problem Statement: Place N queens on an N×N chessboard such that no two queens attack each other.
2. Algorithm:
- Define a function placeQueens(n, row, col):
- If row = n, print the solution.
- Else:
- Try placing queen in all rows one by one.
- For each row 'i', check if queen can be placed safely in that row. If yes, mark that position (row[i] = 1) and recur for next row (i.e. placeQueens(n, i+1, 0)).
- If placing in row i is not safe, then unmark that position (row[i] = 0) and go to next row (i+1) to check.
3. Backtracking: If no safe position can be found to place queen in the current row, then go back and undo the changes by unmarking the positions of previously placed queens and try other positions in previous rows.
4. Time Complexity: O(N!), but it gets pruned by backtracking. So, actual complexity is O(N × 2^N).
5. Dry Run and Examples:
- N = 4
- Place queen in first row: row[0] = 1
- Try second row. Since it is safe, place queen: row[1] = 1
- Try third row. Since it is safe, place queen: row[3] = 1
- Try fourth row. Since it is safe, place queen: row[3] = 1
- Print the solution.