### Inner Product Spaces

- An inner product space is a vector space V over a field F (usually R or C) with an operation called an inner product, which is a function that assigns a scalar to every pair of vectors in V.
- The inner product of two vectors u and v in V is denoted by <u,v> and satisfies the following properties for all u, v, w in V and all c in F :
  - Linearity: <cu + v, w> = c<u, w> + <v, w>
  - Symmetry: <u, v> = <v, u>
  - Positive-definiteness: <u, u> >= 0 and <u, u> = 0 if and only if u = 0
- An inner product induces a norm on V, which is a function that measures the length or magnitude of a vector. The norm of a vector u in V is denoted by ||u|| and defined by ||u|| = sqrt(<u, u>).
- The norm satisfies the following properties for all u, v in V and all c in F:
  - Non-negativity: ||u|| >= 0 and ||u|| = 0 if and only if u = 0
  - Homogeneity: ||cu|| = |c| ||u||
  - Triangle inequality: ||u + v|| <= ||u|| + ||v||
- An inner product also defines a notion of angle and orthogonality in V. Two vectors u and v in V are orthogonal if <u, v> = 0. The angle between two non-zero vectors u and v in V is given by cos(theta) = <u, v> / (||u|| ||v||).
- Some examples of inner product spaces are:
  - R^n with the standard dot product: <u, v> = u1v1 + u2v2 + ... + unvn
  - C^n with the complex dot product: <u, v> = u1v1 + u2v2 + ... + unvn, where v is the complex conjugate of v
  - The space of continuous functions on a closed interval [a, b] with the inner product: <f, g> = integral from a to b of f(x)g(x) dx
  - The space of square-integrable functions on a domain D with the inner product: <f, g> = integral over D of f(x)g(x) dx, where f and g are complex-valued functions and g is the complex conjugate of g