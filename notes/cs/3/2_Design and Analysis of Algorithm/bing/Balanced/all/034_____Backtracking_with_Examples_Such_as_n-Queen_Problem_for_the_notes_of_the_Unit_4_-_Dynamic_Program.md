# Backtracking with Examples Such as n-Queen Problem

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- The backtracking algorithm reduces the problem to the call `backtrack(root(P))`, where `backtrack` is the following recursive procedure: 

```
procedure backtrack(P, c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        backtrack(P, s)
        s ← next(P, s)
```

- The procedure `backtrack` takes two arguments: a problem `P` and a candidate `c`. The problem `P` defines the constraints and the goal of the problem, and the candidate `c` is a partial solution that may or may not satisfy the constraints or the goal. 
- The procedure `reject` tests whether the candidate `c` violates any of the constraints of `P`. If it does, the procedure returns `true` and the candidate is discarded. Otherwise, it returns `false` and the candidate is further explored. 
- The procedure `accept` tests whether the candidate `c` satisfies the goal of `P`. If it does, the procedure returns `true` and the candidate is output as a solution. Otherwise, it returns `false` and the candidate is extended. 
- The procedure `first` returns the first extension of the candidate `c` that is consistent with the constraints of `P`. If there is no such extension, it returns `NULL`. 
- The procedure `next` returns the next extension of the candidate `c` that is consistent with the constraints of `P`, after the previous extension `s`. If there is no such extension, it returns `NULL`. 
- The backtracking algorithm can be applied to a variety of problems, such as crosswords, verbal arithmetic, Sudoku, and many other puzzles. 
- One example of a problem that can be solved by backtracking is the n-queen problem, which is to place n queens on an n×n chessboard such that no two queens attack each other. 
- The n-queen problem can be formulated as follows: 
  - The problem `P` is to place n queens on an n×n chessboard.
  - A candidate `c` is an array of size n, where `c[i]` represents the column of the queen in the i-th row. The array is initialized with all zeros, meaning no queens are placed yet.
  - The procedure `reject` returns `true` if any of the following conditions are true: 
    - `c[i]` is zero, meaning the i-th row is empty.
    - `c[i]` is equal to `c[j]` for some `j < i`, meaning two queens are in the same column.
    - `|c[i] - c[j]|` is equal to `|i - j|` for some `j < i`, meaning two queens are in the same diagonal.
  - The procedure `accept` returns `true` if `i` is equal to `n`, meaning all rows are filled with queens. 
  - The procedure `first` returns `1` if `c[i]` is zero, meaning the i-th row is empty. Otherwise, it returns `NULL`. 
  - The procedure `next` returns `c[i] + 1` if `c[i] < n`, meaning the i-th row can be extended to the next column. Otherwise, it returns `NULL`. 
- The following is an example of a solution to the 4-queen problem, where `c = [2, 4, 1, 3]`: 

```
. Q . .
. . . Q