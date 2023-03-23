 Here are the notes for the given topic:

### Backtracking with Examples Such as n-Queen Problem

- Backtracking is a general algorithmic technique that considers searching through all possible candidates for the solution and abandons each partial candidate as soon as it is determined that it cannot lead to a valid full solution.
- It involves systematically building up candidates to the solutions and abandoning each partial candidate (backtrack) as soon as it is determined that it cannot lead to a valid full solution.
- The basic steps of backtracking are:
    1. Propose a partial candidate solution
    2. Check if the partial candidate solution satisfies all the constraints
    3. If satisfied, check if the partial candidate solution can lead to a complete solution
    4. If yes, explore the solution
    5. If no, backtrack - abandon the partial solution and go back to step#1 to propose another alternative

- Example: N-Queen Problem
    - The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
    - State space is the set of all distinct board configurations
    - Each queen can be placed in N squares in the first row, for each of these there are (N-1) squares in the second row and so on. Therefore, total number of possible solutions is N!.
    - However, due to constraints only some configurations are valid solutions.
    - The steps for N Queen problem using backtracking are:
        1. Place queens one by one in different columns
        2. Check if the queen can be placed safely in the selected column
        3. If yes, mark the position and proceed to place next queen
        4. If no, undo the changes and go back to step#2 to try other positions until all queens are placed safely or all positions have been tried without success

[ remaining points removed for brevity ]