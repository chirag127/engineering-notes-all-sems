## Implement N Queen Problem using Backtracking

### Introduction
The N Queen problem is a classic problem in which we have to place N queens on an N x N chessboard in such a way that no two queens can attack each other. In this lab, we will implement the solution to this problem using the Backtracking algorithm.

### Backtracking Algorithm
Backtracking is a method of solving problems by trying to build a solution incrementally, one piece at a time, and removing solutions that fail to satisfy the constraints. The basic idea is to start with an empty solution and then try to add new components one by one, checking at each step whether the new component violates the constraints. If it does, we remove it and try again with a different component.

### Steps to Implement N Queen Problem using Backtracking
1. Create an empty chessboard of size N x N.
2. Start with the first row and place a queen in each column of that row.
3. Move to the next row and try to place a queen in each column such that it does not attack any of the queens in the previous rows.
4. If a queen cannot be placed in any column of the current row, backtrack to the previous row and try a different column.
5. Repeat steps 3 and 4 until all N queens are placed on the board or until it is not possible to place any more queens without violating the constraints.

### Pseudo Code
```
function solveNQueen(N)
    chessboard = empty N x N array
    if solveNQueenUtil(chessboard, 0) == false
        print "Solution does not exist"
        return false
    printSolution(chessboard)
    return true

function solveNQueenUtil(chessboard, row)
    if row >= N
        return true
    for col in 0 to N-1
        if isSafe(chessboard, row, col) == true
            chessboard[row][col] = 1
            if solveNQueenUtil(chessboard, row + 1) == true
                return true
            chessboard[row][col] = 0
    return false

function isSafe(chessboard, row, col)
    for i in 0 to row-1
        if chessboard[i][col] == 1
            return false
    for i, j in zip(range(row, -1, -1), range(col, -1, -1))
        if chessboard[i][j] == 1
            return false
    for i, j in zip(range(row, -1, -1), range(col, N, 1))
        if chessboard[i][j] == 1
            return false
    return true
```

### Complexity Analysis
The time complexity of the backtracking algorithm for the N Queen problem is O(N!), where N is the size of the chessboard. This is because there are N choices for the first queen, N-2 choices for the second queen (since it cannot be in the same row or column as the first queen), N-4 choices for the third queen, and so on. The space complexity of the algorithm is O(N^2), which is the size of the chessboard.

### Conclusion
In this lab, we learned how to implement the N Queen problem using the Backtracking algorithm. We saw that Backtracking is a powerful method for solving problems that involve searching for solutions among a large number of possibilities. We also saw that the N Queen problem has a high time complexity, which makes it impractical for large values of N. However, for small values of N, the Backtracking algorithm provides an efficient solution to this classic problem.