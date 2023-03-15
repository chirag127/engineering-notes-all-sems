### Unitary Matrices

- A unitary matrix is a complex square matrix that satisfies the following equation:

  - U^H U = U U^H = I

  - where U^H is the conjugate transpose of U, and I is the identity matrix.

- A unitary matrix preserves the inner product of two complex vectors, that is:

  - (Ux)^H (Uy) = x^H y

  - for any complex vectors x and y.

- A unitary matrix has the following properties:

  - It is non-singular, that is, its determinant is not zero.
  - It is invertible, that is, its inverse is also a unitary matrix.
  - It is normal, that is, it commutes with its conjugate transpose.
  - It has orthonormal columns and rows, that is, the columns and rows are mutually perpendicular and have unit length.
  - It has eigenvalues of modulus one, that is, the absolute value of its eigenvalues is one.
  - It can be diagonalized by another unitary matrix, that is, there exists a unitary matrix V such that:

    - U = V D V^H

    - where D is a diagonal matrix with the eigenvalues of U on the diagonal.

- Some examples of unitary matrices are:

  - The identity matrix I.
  - The rotation matrix R(θ) = [cos(θ) -sin(θ); sin(θ) cos(θ)].
  - The Pauli matrices σ_x = [0 1; 1 0], σ_y = [0 -i; i 0], and σ_z = [1 0; 0 -1].
  - The Hadamard matrix H = 1/√2 [1 1; 1 -1].