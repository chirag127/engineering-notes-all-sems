## 26. WAP to add and multiply two matrices of order nxn.

A matrix is a two-dimensional array of numbers. The order of a matrix is the number of rows and columns it has. For example, a matrix of order 3x3 has 3 rows and 3 columns.

To add two matrices of the same order, we simply add the corresponding elements of the two matrices. For example, if A and B are two matrices of order 3x3, then the sum of the two matrices, C, is given by:

C[i][j] = A[i][j] + B[i][j]

where i and j are the row and column indices, respectively.

To multiply two matrices, the number of columns of the first matrix must be equal to the number of rows of the second matrix. The product of two matrices, A and B, of orders nxm and mxp, respectively, is a matrix C of order nxp, where:

C[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j] + ... + A[i][m-1] * B[m-1][j]

Here is an example of a program in C that adds and multiplies two matrices of order nxn:

```c
#include <stdio.h>

int main() {
    int n, i, j;
    printf("Enter the order of the matrices: ");
    scanf("%d", &n);
    int A[n][n], B[n][n], C[n][n], D[n][n];
    printf("Enter the elements of the first matrix: ");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &A[i][j]);
    printf("Enter the elements of the second matrix: ");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &B[i][j]);
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            C[i][j] = A[i][j] + B[i][j];
    printf("The sum of the two matrices is:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++)
            printf("%d ", C[i][j]);
        printf("\n");
    }
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++) {
            D[i][j] = 0;
            for (int k = 0; k < n; k++)
                D[i][j] += A[i][k] * B[k][j];
        }
    printf("The product of the two matrices is:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++)
            printf("%d ", D[i][j]);
        printf("\n");
    }
    return 0;
}
```

This program first asks the user to enter the order of the matrices, then the elements of the two matrices. It then calculates the sum and product of the two matrices and prints the results.