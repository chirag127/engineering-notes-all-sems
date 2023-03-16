### Inner Product Spaces

- An inner product space is a vector space V over a field F (usually R or C) with an operation called an inner product, which is a function that assigns a scalar to every pair of vectors in V.
- The inner product of two vectors u and v in V is denoted by <u,v> or (u,v) and must satisfy the following properties for all u, v, w in V and all c in F :
  - Conjugate symmetry: <u,v> = <v,u>*
  - Linearity in the first argument: <cu + w, v> = c<u,v> + <w,v>
  - Positive-definiteness: <u,u> ≥ 0 and <u,u> = 0 if and only if u = 0
  - Here, <v,u>* denotes the complex conjugate of <v,u>, which is equal to <v,u> if F is R and is obtained by changing the sign of the imaginary part of <v,u> if F is C.
- An inner product space is also a normed linear space, which means that we can define a norm (or a length) of a vector u in V by ||u|| = √<u,u> and use it to measure the distance between two vectors by d(u,v) = ||u - v||.
- Some examples of inner product spaces are:
  - R^n with the standard dot product: <u,v> = u1v1 + u2v2 + ... + unvn
  - C^n with the Hermitian dot product: <u,v> = u1v1* + u2v2* + ... + unvn*
  - The space of continuous functions on a closed interval [a,b] with the inner product: <f,g> = ∫ab f(x)g(x) dx
  - The space of square-integrable functions on a domain D with the inner product: <f,g> = ∫D f(x)g(x)* dx
- An inner product space allows us to generalize the concepts of angle, orthogonality, projection, and ortho-normal basis to any vector space with an inner product.
  - The angle θ between two nonzero vectors u and v in V is defined by cos θ = <u,v> / (||u|| ||v||)
  - Two vectors u and v in V are orthogonal if <u,v> = 0
  - The projection of a vector u onto a nonzero vector v in V is given by projv u = (<u,v> / <v,v>) v
  - An ortho-normal basis of V is a basis {v1, v2, ..., vn} such that <vi, vj> = 0 if i ≠ j and <vi, vi> = 1 for all i and j
- An inner product space is a special case of a more general concept called a Hilbert space, which is an inner product space that is also complete, meaning that every Cauchy sequence in the space converges to a limit in the space.