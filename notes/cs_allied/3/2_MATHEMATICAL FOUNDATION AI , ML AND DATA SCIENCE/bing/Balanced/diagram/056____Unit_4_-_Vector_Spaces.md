## Unit 4 - Vector Spaces

A vector space is a set of objects called vectors, which can be added together and multiplied by scalars, satisfying certain axioms.

### Definition of a vector space

A vector space V over a field F is a set of objects, called vectors, with two operations:

- Vector addition: For any two vectors u and v in V, there is a vector u + v in V.
- Scalar multiplication: For any scalar c in F and any vector v in V, there is a vector cv in V.

These operations must satisfy the following axioms:

- Commutativity: For any u, v in V, u + v = v + u.
- Associativity: For any u, v, w in V, (u + v) + w = u + (v + w).
- Identity: There is a vector 0 in V such that 0 + v = v for any v in V.
- Inverse: For any v in V, there is a vector -v in V such that v + (-v) = 0.
- Distributivity: For any c, d in F and any v in V, (c + d)v = cv + dv.
- Compatibility: For any c, d in F and any v in V, c(dv) = (cd)v.
- Scalar identity: For any v in V, 1v = v, where 1 is the multiplicative identity in F.

### Examples of vector spaces

Some common examples of vector spaces are:

- The set of all n-tuples of real numbers, denoted by R^n, with the usual operations of componentwise addition and scalar multiplication.
- The set of all n-tuples of complex numbers, denoted by C^n, with the same operations as above.
- The set of all polynomials of degree at most n with real coefficients, denoted by P_n(R), with the usual operations of polynomial addition and scalar multiplication.
- The set of all functions from a set X to a field F, denoted by F^X, with the usual operations of pointwise addition and scalar multiplication.
- The set of all matrices of size m x n with entries from a field F, denoted by M_mn(F), with the usual operations of matrix addition and scalar multiplication.

### Subspaces of a vector space

A subset W of a vector space V is called a subspace of V if W is also a vector space under the same operations as V. This means that W must satisfy the following conditions:

- W is nonempty, i.e., it contains at least one vector.
- W is closed under vector addition, i.e., for any u, v in W, u + v is also in W.
- W is closed under scalar multiplication, i.e., for any c in F and any v in W, cv is also in W.

### Examples of subspaces

Some common examples of subspaces are:

- The set of all vectors in R^n that have the form (a, 0, 0, ..., 0) for some a in R. This is a subspace of R^n, called the x-axis.
- The set of all polynomials of degree at most n with real coefficients that have a zero constant term, i.e., p(0) = 0. This is a subspace of P_n(R), called the set of zero polynomials.
- The set of all functions from a set X to a field F that are zero at a fixed point x_0 in X, i.e., f(x_0) = 0. This is a subspace of F^X, called the kernel of the evaluation map at x_0.
- The set of all matrices of size m x n with entries from a field F that have zero entries in the first row. This is a subspace of M_mn(F), called the set of row-reduced matrices.