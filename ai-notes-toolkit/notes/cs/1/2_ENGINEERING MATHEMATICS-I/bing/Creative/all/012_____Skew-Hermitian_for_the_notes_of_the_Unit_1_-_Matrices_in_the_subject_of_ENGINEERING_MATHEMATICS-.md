Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on skew-Hermitian matrices for the notes of the Unit 1 - Matrices in the subject of ENGINEERING MATHEMATICS-I.

# Skew-Hermitian Matrices

## Definition

A square matrix A is called **skew-Hermitian** (or **antihermitian**) if it satisfies the following property:

A<sup>∗</sup> = -A

where A<sup>∗</sup> is the **conjugate transpose** of A, which means the matrix obtained by taking the complex conjugate of each element of A and then transposing the matrix.

## Properties

Some of the properties of skew-Hermitian matrices are:

- The diagonal elements of a skew-Hermitian matrix are either zeros or pure imaginary numbers (i.e., numbers of the form bi, where b is a real number and i is the imaginary unit).
- A skew-Hermitian matrix is an example of a **normal matrix**, which means that it commutes with its conjugate transpose, i.e., AA<sup>∗</sup> = A<sup>∗</sup>A.
- A skew-Hermitian matrix is **diagonalizable**, which means that it can be written as A = PDP<sup>-1</sup>, where P is a unitary matrix (i.e., P<sup>∗</sup> = P<sup>-1</sup>) and D is a diagonal matrix.
- The eigenvalues of a skew-Hermitian matrix are either purely imaginary or zeros. Furthermore, the eigenvectors of a skew-Hermitian matrix corresponding to distinct eigenvalues are orthogonal.

## Examples

Here are some examples of skew-Hermitian matrices:

- A = [0 i -i 0] is a 2 x 2 skew-Hermitian matrix, since A<sup>∗</sup> = [0 -i i 0] = -A. Its eigenvalues are ±i and its eigenvectors are [1 i] and [1 -i].
- B = [0 1 + i 2 - 3i -1 - i 0 4 + i -2 + 3i -4 - i 0] is a 3 x 3 skew-Hermitian matrix, since B<sup>∗</sup> = [0 -1 - i -2 + 3i 1 + i 0 -4 - i 2 - 3i 4 + i 0] = -B. Its eigenvalues are 0, ±2i and its eigenvectors are [1 1 1], [1 -i 1 + i] and [1 i 1 - i].