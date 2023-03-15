# Divide and Conquer with Examples Such as Matrix Multiplication

- Divide and conquer is a technique for solving problems by breaking them into smaller and simpler subproblems, solving them recursively, and combining their solutions to obtain the solution for the original problem.
- Divide and conquer has three steps:
  - Divide: Split the problem into smaller and independent subproblems of the same type.
  - Conquer: Solve the subproblems recursively. If the subproblems are small enough, solve them directly.
  - Combine: Merge the solutions of the subproblems to obtain the solution for the original problem.
- Divide and conquer is useful for problems that have the following properties:
  - The problem can be divided into smaller subproblems of the same type.
  - The subproblems can be solved independently and recursively.
  - The solutions of the subproblems can be combined efficiently to obtain the solution for the original problem.
- Some examples of problems that can be solved by divide and conquer are sorting, matrix multiplication, convex hull, and searching.

## Matrix Multiplication

- Matrix multiplication is the operation of multiplying two matrices of compatible dimensions to obtain a third matrix.
- The standard algorithm for matrix multiplication takes O(n^3) time, where n is the number of rows and columns of the matrices.
- Divide and conquer can be used to improve the time complexity of matrix multiplication by splitting the matrices into smaller submatrices, multiplying them recursively, and adding the results to obtain the final matrix.
- One of the divide and conquer algorithms for matrix multiplication is Strassen's algorithm, which takes O(n^log7) time, where n is the number of rows and columns of the matrices.
- Strassen's algorithm works as follows:
  - Divide: Split each matrix into four submatrices of equal size by dividing the rows and columns in half.
  - Conquer: Compute seven products of submatrices recursively, using the following formulas:

    - P1 = (A11 + A22) * (B11 + B22)
    - P2 = (A21 + A22) * B11
    - P3 = A11 * (B12 - B22)
    - P4 = A22 * (B21 - B11)
    - P5 = (A11 + A12) * B22
    - P6 = (A21 - A11) * (B11 + B12)
    - P7 = (A12 - A22) * (B21 + B22)

  - Combine: Compute the four submatrices of the final matrix by adding and subtracting the products, using the following formulas:

    - C11 = P1 + P4 - P5 + P7
    - C12 = P3 + P5
    - C21 = P2 + P4
    - C22 = P1 - P2 + P3 + P6

- Strassen's algorithm reduces the number of recursive multiplications from eight to seven, which leads to a lower time complexity. However, it also increases the number of additions and subtractions, which leads to a higher space complexity and constant factor. Therefore, Strassen's algorithm is more efficient than the standard algorithm only for large matrices.