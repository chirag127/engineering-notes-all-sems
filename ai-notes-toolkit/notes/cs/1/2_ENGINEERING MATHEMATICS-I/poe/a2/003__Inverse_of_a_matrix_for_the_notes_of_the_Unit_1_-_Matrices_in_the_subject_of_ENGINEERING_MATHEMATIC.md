 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Inverse of a matrix for the notes of the Unit 1 - Matrices in the subject of ENGINEERING MATHEMATICS-I

1. A matrix A is said to be invertible if there exists a matrix B such that AB = BA = I, where I is the identity matrix.
2. If A is invertible, then its inverse is unique.
3. For a 2x2 matrix, the inverse is:
        A = [a11, a12;
            a21, a22]

        A^-1 = [1/(a11a22 - a12a21), -(a12)/(a11a22 - a12a21);
               -(a21), (a11)/(a11a22 - a12a21)]

    * The determinant (a11a22 - a12a21) must not be 0 for A to have an inverse.
    * The inverse is obtained by taking the adjoint of A and scaling by 1/determinant.
4. For n x n matrices, Gauss-Jordan elimination can be used to calculate the inverse by performing row operations to reduce A to I. If a unique I is obtained, then A is invertible and the operations give A^-1.
5. Properties:
    * (A^-1)^-1 = A
    * (AB)^-1 = B^-1A^-1
    * I^-1 = I
    * If A is invertible, dim(A) = dim(A^-1)

The content is written in points in a formal tone without any emojis or external links as directed. Let me know if you would like me to modify or expand the content.