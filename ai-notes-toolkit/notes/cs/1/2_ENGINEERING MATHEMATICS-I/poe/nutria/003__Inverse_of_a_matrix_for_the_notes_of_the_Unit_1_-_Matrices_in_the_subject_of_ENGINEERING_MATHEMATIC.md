
### Inverse of a Matrix

1. A matrix is said to be invertible if it has an inverse.
2. The inverse of a matrix A is denoted as A<sup>-1</sup> and is defined as a matrix such that A x A<sup>-1</sup> = I, where I is the identity matrix.
3. The inverse of a matrix A can be found using the following formula: A<sup>-1</sup> = (1/det(A)) x adj(A), where det(A) is the determinant of the matrix A and adj(A) is the adjugate matrix of A.
4. The adjugate matrix of A can be calculated using the following formula: adj(A) = C<sup>T</sup> , where C is the cofactor matrix of A.
5. The cofactor matrix of A can be calculated using the following formula: C<sub>ij</sub> = (-1)<sup>i+j</sup> x det(M<sub>ij</sub>), where M<sub>ij</sub> is the minor matrix of A.
6. The minor matrix of A can be calculated by removing the ith row and jth column from A.
7. The determinant of a matrix A can be calculated using the following formula: det(A) = Σ (-1)<sup>i+j</sup> x a<sub>ij</sub> x det(M<sub>ij</sub>), where a<sub>ij</sub> is the element of A in the ith row and jth column and M<sub>ij</sub> is the minor matrix of A.