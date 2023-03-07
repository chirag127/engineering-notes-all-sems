## Implement N Queen Problem using Backtracking

The N Queen problem is a classic problem in computer science that involves placing N chess queens on an N x N chessboard so that no two queens can threaten each other. The problem is to find all possible solutions to this problem. Backtracking is an algorithmic technique that can be used to solve this problem.

### Backtracking Algorithm

The backtracking algorithm works by exploring all possible solutions to a problem, one at a time. At each step, the algorithm makes a choice and explores that choice until it either finds a solution or determines that the choice cannot lead to a solution. If the choice does not lead to a solution, the algorithm "backtracks" and tries another choice.

### Implementing N Queen Problem using Backtracking

To implement the N Queen problem using backtracking, we follow these steps:

1. Start with an empty chessboard of size N x N.
2. Place the first queen in the first row of the chessboard.
3. For each column in the first row, check if the queen can be placed in that column without being threatened by any other queens.
4. If a safe column is found, place the queen in that column and move to the next row.
5. Repeat steps 3 and 4 for each row until all N queens have been placed on the board.
6. If a solution is found, print the placement of the queens on the board. If not, backtrack to the previous row and try another column.

### Advantages of Backtracking Algorithm

1. Backtracking is a general algorithmic technique that can be used to solve a wide variety of problems.
2. It is an efficient way to explore all possible solutions to a problem.
3. Backtracking can be used to find one solution or all possible solutions to a problem.

### Disadvantages of Backtracking Algorithm

1. Backtracking can be very slow for problems with a large search space.
2. It may not be possible to find a solution using backtracking if the problem is too complex or the search space is too large.

### Example

Suppose we want to place 4 queens on a 4 x 4 chessboard. Here is one possible solution using backtracking:

```
| Q |   |   |   |
|   |   | Q |   |
|   |   |   | Q |
|   | Q |   |   |
```

### Applications

The N Queen problem has applications in many areas, such as:

1. Scheduling problems
2. Data mining
3. Artificial intelligence
4. Computer vision
5. Robotics

In conclusion, implementing the N Queen problem using backtracking is a useful technique to explore all possible solutions to the problem. However, it may not be the most efficient algorithm for large search spaces.