
## Implement N Queen Problem using Backtracking 

1. N Queen Problem is an example of a combinatorial optimization problem. It involves placing N number of queens on an NxN chessboard in such a way that no two queens can attack each other.
2. The problem can be solved using a technique known as backtracking. Backtracking is a general algorithmic technique that considers searching every possible combination in order to solve a problem.
3. In the case of the N Queen Problem, the algorithm starts by placing a queen in the first row and then moves on to the next row. In each row, the algorithm places a queen in each column and then checks if the current configuration is valid.
4. If the current configuration is valid, the algorithm moves on to the next row and repeats the process. If the current configuration is not valid, the algorithm backtracks to the previous row and tries a different configuration.
5. This process is repeated until a valid solution is found or all configurations have been checked. The time complexity of the backtracking algorithm is O(N!).
6. The Design and Analysis of Algorithm Lab in the subject of Real Time System focuses on the implementation of the backtracking algorithm to solve the N Queen Problem. The lab also covers topics such as time complexity analysis, memory management, and optimization techniques.