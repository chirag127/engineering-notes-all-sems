### Orthonormal (Orthogonal) Basis

- An orthonormal basis for a vector space V with an inner product is a set of vectors that are linearly independent, have unit length, and are orthogonal to each other .
- That is, if B = {v_1, ..., v_n} is an orthonormal basis for V, then for any i and j, we have:

  - <v_i, v_j> = 0 if i ≠ j (orthogonality)
  - <v_i, v_i> = 1 for all i (normality)
  - span(B) = V (basis)

- An orthonormal basis has the advantage of simplifying many computations involving inner products, norms, angles, and projections.
- For example, if B is an orthonormal basis for V, then the norm of any vector v in V can be easily found by:

  - ||v||^2 = <v, v> = <∑a_i v_i, ∑a_j v_j> = ∑a_i a_j <v_i, v_j> = ∑a_i^2

- Similarly, the angle between two vectors u and v in V can be calculated by:

  - cos(θ) = <u, v> / (||u|| ||v||) = <∑b_i v_i, ∑c_j v_j> / (√∑b_i^2 √∑c_j^2) = ∑b_i c_i

- Moreover, the projection of a vector v onto a vector u in V can be obtained by:

  - proj_u(v) = (<v, u> / ||u||^2) u = (<∑a_i v_i, u> / 1) u = a_i u

- Every finite-dimensional inner product space has an orthonormal basis, which may be obtained from an arbitrary basis using the Gram–Schmidt process.
- In functional analysis, the concept of an orthonormal basis can be generalized to arbitrary (infinite-dimensional) inner product spaces.