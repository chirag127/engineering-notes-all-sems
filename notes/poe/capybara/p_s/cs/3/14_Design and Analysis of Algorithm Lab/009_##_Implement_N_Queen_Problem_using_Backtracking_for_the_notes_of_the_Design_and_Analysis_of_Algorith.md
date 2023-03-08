## Implement N Queen Problem using Backtracking

The N Queen Problem is a classic problem of placing N chess queens on an N x N chessboard in a way that no two queens can attack each other. The problem can be solved using the Backtracking algorithm. 

### Backtracking Algorithm

The Backtracking algorithm is a brute-force algorithm for solving problems by trying all possible solutions and backtracking when the solution does not work. It is a recursive algorithm that tries to find a solution by building it incrementally. If the algorithm finds a solution, it stops searching. If the algorithm exhausts all possible solutions, it backtracks to the previous step and tries a different path.

### Steps to Implement N Queen Problem using Backtracking

1. Define a function to place queens on the chessboard.
2. Start with the first row and place a queen in the first column.
3. Move to the second row and place a queen in the first column that does not attack the queen in the first row.
4. Repeat the previous step for all rows until all queens are placed on the board.
5. If a solution is found, return the chessboard configuration. If not, backtrack to the previous step and try a different column for the current row.
6. Repeat the previous steps until all possible solutions are found.

### Code Example

Here is an example code for implementing the N Queen Problem using Backtracking in Python:

```python
def is_safe(board, row, col, n):
    # check if the queen can be placed on the board
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queen(board, row, n):
    # base case: all queens are placed on the board
    if row >= n:
        return True
    # try to place the queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queen(board, row+1, n):
                return True
            board[row][col] = 0
    return False

n = 4
board = [[0]*n for i in range(n)]
if solve_n_queen(board, 0, n):
    print('\n'.join([' '.join([str(cell) for cell in row]) for row in board]))
else:
    print("No solution found.")
```

### Advantages

- Backtracking algorithm can solve complex problems with a large number of possible solutions.
- It guarantees to find a solution if one exists.

### Disadvantages

- The algorithm can be slow for problems with a large number of possible solutions.
- It can be difficult to implement and debug.

### Applications

- The N Queen Problem has applications in computer science, mathematics, and game theory.
- It is used in the design of chess-playing programs and in scheduling problems.

In conclusion, the N Queen Problem is a classic problem that can be solved using the Backtracking algorithm. The algorithm tries all possible solutions and backtracks when the solution does not work. The problem has applications in computer science, mathematics, and game theory. By understanding the steps to solve the problem and implementing the algorithm, we can solve complex problems with a large number of possible solutions.