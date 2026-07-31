### Inner Product Spaces

- An inner product space is a vector space V over a field F (usually R or C) with an operation called an inner product, which is a function that assigns a scalar to each pair of vectors in V.
- The inner product of two vectors u and v in V is denoted by <u,v> and must satisfy the following properties for all u, v, w in V and all c in F :
  - Conjugate symmetry: <u,v> = <v,u>*
  - Linearity in the first argument: <cu + w, v> = c<u,v> + <w,v>
  - Positive-definiteness: <u,u> ≥ 0 and <u,u> = 0 if and only if u = 0
- The inner product can be used to define a norm on V, which is a function that measures the length or magnitude of a vector. The norm of a vector u in V is denoted by ||u|| and is given by ||u|| = √<u,u>.
- The norm satisfies the following properties for all u, v in V and all c in F:
  - Non-negativity: ||u|| ≥ 0 and ||u|| = 0 if and only if u = 0
  - Absolute homogeneity: ||cu|| = |c| ||u||
  - Triangle inequality: ||u + v|| ≤ ||u|| + ||v||
- The inner product can also be used to define an angle between two vectors in V, which is a measure of how close they are to being orthogonal or perpendicular. Two vectors u and v in V are orthogonal if <u,v> = 0. The angle θ between u and v is given by cos θ = <u,v> / (||u|| ||v||).
- Some examples of inner product spaces are:
  - R^n with the standard dot product: <u,v> = u1v1 + u2v2 + ... + unvn
  - C^n with the Hermitian dot product: <u,v> = u1v1* + u2v2* + ... + unvn*
  - The space of continuous functions on a closed interval [a,b] with the integral inner product: <f,g> = ∫ab f(x)g(x) dx
  - The space of square-integrable functions on a domain D with the L2 inner product: <f,g> = ∫D f(x)g(x)* dx