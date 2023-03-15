### Backtracking with Examples Such as n-Queen Problem

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- The backtracking algorithm can be described by the following recursive procedure: 

```
procedure backtrack (P, c) is
  if reject (P, c) then return
  if accept (P, c) then output (P, c)
  s ← first (P, c)
  while s ≠ NULL do
    backtrack (P, s)
    s ← next (P, s)
```

- Here, P is the problem instance, c is a partial candidate, reject (P, c) is a function that returns true if c cannot be extended to a valid solution, accept (P, c) is a function that returns true if c is a valid solution, output (P, c) is a function that prints or stores the solution c, first (P, c) is a function that returns the first extension of c, and next (P, s) is a function that returns the next extension of c after s.
- Backtracking can be applied to a variety of problems, such as crosswords, verbal arithmetic, Sudoku, and many other puzzles. It is often the most convenient technique for parsing, for the knapsack problem and other combinatorial optimization problems. 
- One example of a problem that can be solved by backtracking is the n-queen problem, which asks for all the possible ways of placing n queens on an n×n chessboard, such that no two queens attack each other. 
- The n-queen problem can be solved by the following backtracking algorithm: 

```
procedure nqueen (n, row, board) is
  if row > n then output (board)
  for col from 1 to n do
    if safe (row, col, board) then
      place (row, col, board)
      nqueen (n, row + 1, board)
      remove (row, col, board)
```

- Here, n is the size of the chessboard, row is the current row to place a queen, board is a two-dimensional array that represents the chessboard, safe (row, col, board) is a function that returns true if placing a queen at (row, col) does not conflict with any other queen on the board, place (row, col, board) is a function that places a queen at (row, col) on the board, remove (row, col, board) is a function that removes the queen from (row, col) on the board, and output (board) is a function that prints or stores the board configuration.
- The algorithm starts with an empty board and tries to place a queen in each column of the first row. If the placement is safe, it recursively tries to place a queen in the next row. If the placement is not safe, it backtracks and tries a different column. The algorithm terminates when all the rows are filled or when there is no more column to try.