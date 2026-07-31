# Change of Basis

- Change of basis is a technique applied to finite-dimensional vector spaces in order to rewrite vectors in terms of a different set of basis elements .
- A basis is a set of linearly independent vectors that span the vector space. Any vector in the vector space can be expressed as a unique linear combination of the basis vectors .
- The coordinates of a vector are the coefficients of the linear combination that expresses the vector in terms of the basis vectors .
- The change of basis matrix is a matrix that transforms the coordinates of a vector from one basis to another    .
- The change of basis matrix from basis B to basis C is denoted by C_B and is defined as the matrix whose columns are the coordinates of the basis vectors of B with respect to the basis C    .
- The change of basis matrix satisfies the equation C_B * [v]_B = [v]_C, where [v]_B and [v]_C are the coordinate vectors of v with respect to the bases B and C, respectively    .
- The change of basis matrix is invertible and its inverse is the change of basis matrix from C to B, i.e., C_B^-1 = B_C    .
- The change of basis matrix can also be used to rewrite a linear transformation with respect to different bases for the domain and the codomain   .
- The matrix representation of a linear transformation T: V -> W with respect to the bases B and C for V and W, respectively, is denoted by [T]_C^B and is defined as the matrix that satisfies [T(v)]_C = [T]_C^B * [v]_B for any v in V   .
- The matrix representation of a linear transformation can be changed by using the change of basis matrices for the domain and the codomain, i.e., [T]_D^A = D_C * [T]_C^B * B_A, where A and B are bases for V and C and D are bases for W   .
- The change of basis technique is useful for many types of matrix computations in linear algebra and can be viewed as a type of linear transformation   .