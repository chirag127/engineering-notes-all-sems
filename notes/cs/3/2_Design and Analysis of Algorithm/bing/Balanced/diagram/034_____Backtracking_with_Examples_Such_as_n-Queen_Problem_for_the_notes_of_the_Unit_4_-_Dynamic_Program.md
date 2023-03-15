### Backtracking with Examples Such as n-Queen Problem

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time. 
- Backtracking can be applied to problems that can be represented as a state space tree, where each node is a partial solution and the leaves are the complete solutions. 
- The basic idea of backtracking is to explore the nodes of the state space tree in a depth-first manner, and prune the branches that do not lead to a feasible solution. 
- The backtracking algorithm can be described as follows :

```
procedure backtrack(P, c) is
  if reject(P, c) then return
  if accept(P, c) then output(P, c)
  s ← first(P, c)
  while s ≠ NULL do
    backtrack(P, s)
    s ← next(P, s)
```

- Here, P is the problem instance, c is a partial candidate solution, reject(P, c) is a function that returns true if c is not a valid solution, accept(P, c) is a function that returns true if c is a complete and valid solution, output(P, c) is a function that prints or stores the solution c, first(P, c) is a function that returns the first extension of c, and next(P, c, s) is a function that returns the next extension of c after s.
- An example of a problem that can be solved by backtracking is the n-queen problem, where the goal is to place n queens on an n x n chessboard such that no two queens attack each other. 
- A possible state space tree for the n-queen problem is shown below, where each node represents a partial placement of queens on the board, and the leaves are the complete placements. The nodes marked with X are pruned by the reject function, as they violate the constraint that no two queens can be on the same row, column, or diagonal. The nodes marked with O are the valid solutions.

![n-queen state space tree](https://media.geeksforgeeks.org/wp-content/uploads/N_Queen_Problem.jpg)

- The pseudocode for the n-queen problem using backtracking is given below :

```
procedure nqueen(n) is
  create an empty array board of size n
  placeQueens(board, 0, n)

procedure placeQueens(board, row, n) is
  if row == n then
    output(board)
    return
  for col from 0 to n - 1 do
    if isSafe(board, row, col, n) then
      board[row] = col
      placeQueens(board, row + 1, n)
      board[row] = -1 // backtrack

function isSafe(board, row, col, n) is
  for i from 0 to row - 1 do
    if board[i] == col or abs(board[i] - col) == abs(i - row) then
      return false
  return true
```

- Here, board is an array that stores the column index of the queen placed in each row, row is the current row to place a queen, n is the size of the board, output(board) is a function that prints or stores the board configuration, and isSafe(board, row, col, n) is a function that checks if placing a queen at (row, col) does not conflict with the previous queens.