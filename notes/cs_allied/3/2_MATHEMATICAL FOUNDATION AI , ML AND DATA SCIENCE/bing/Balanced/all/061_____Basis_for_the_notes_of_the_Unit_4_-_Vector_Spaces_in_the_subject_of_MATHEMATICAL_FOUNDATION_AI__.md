# Basis for the notes of the Unit 4 - Vector Spaces in the subject of MATHEMATICAL FOUNDATION AI , ML AND DATA SCIENCE

- A vector space is a set of objects called vectors that can be added and multiplied by scalars (usually real or complex numbers) in a way that satisfies certain axioms.
- A vector space is also called a linear space because the operations of vector addition and scalar multiplication are linear, meaning that they satisfy the properties of distributivity, associativity, commutativity, and identity.
- A vector space can be thought of as a collection of arrows with a common origin, or as a coordinate system where each vector is represented by a list of numbers.
- The simplest example of a vector space is the Euclidean space R^n, where n is any positive integer. In this space, vectors are n-tuples of real numbers, such as (2, -3, 5) in R^3. The scalar multiplication and vector addition are defined as follows:

  - For any scalar c and vector (x_1, x_2, ..., x_n), c(x_1, x_2, ..., x_n) = (cx_1, cx_2, ..., cx_n).
  - For any vectors (x_1, x_2, ..., x_n) and (y_1, y_2, ..., y_n), (x_1, x_2, ..., x_n) + (y_1, y_2, ..., y_n) = (x_1 + y_1, x_2 + y_2, ..., x_n + y_n).

- Another example of a vector space is the set of all polynomials of degree at most n, denoted by P_n. In this space, vectors are polynomials, such as 3x^2 - 5x + 2 in P_2. The scalar multiplication and vector addition are defined as follows:

  - For any scalar c and polynomial p(x), cp(x) = c(p(x)).
  - For any polynomials p(x) and q(x), p(x) + q(x) = p(x) + q(x).

- A vector space must satisfy the following eight axioms:

  - Closure under addition: For any vectors u and v in V, u + v is also in V.
  - Closure under scalar multiplication: For any scalar c and vector v in V, cv is also in V.
  - Commutativity of addition: For any vectors u and v in V, u + v = v + u.
  - Associativity of addition: For any vectors u, v, and w in V, (u + v) + w = u + (v + w).
  - Additive identity: There exists a vector 0 in V such that for any vector v in V, v + 0 = v.
  - Additive inverse: For any vector v in V, there exists a vector -v in V such that v + (-v) = 0.
  - Distributivity of scalar multiplication over vector addition: For any scalar c and vectors u and v in V, c(u + v) = cu + cv.
  - Distributivity of vector addition over scalar multiplication: For any scalars a and b and vector v in V, (a + b)v = av + bv.

- A vector space can have different bases, which are sets of linearly independent vectors that span the whole space. For example, the standard basis of R^n is the set of n vectors e_1, e_2, ..., e_n, where e_i has 1 in the i-th position and 0 elsewhere. Any vector in R^n can be written as a linear combination of these basis vectors. For example, (2, -3, 5) = 2e_1 - 3e_2 + 5e_3.
- A vector space can also have different dimensions, which are the number of vectors in any basis of the space. For example, the dimension of R^n is n, and the dimension of P_n is n + 1. The dimension of a vector space is a measure of its size and complexity.