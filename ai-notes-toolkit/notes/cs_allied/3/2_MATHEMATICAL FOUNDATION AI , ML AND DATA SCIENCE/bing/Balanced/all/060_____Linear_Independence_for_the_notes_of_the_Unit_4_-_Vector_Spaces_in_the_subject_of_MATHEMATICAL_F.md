# Linear Independence

- Linear independence is a property of a set of vectors that means they cannot be expressed as linear combinations of each other .
- A set of vectors {v1, v2, …, vk} is linearly independent if the vector equation x1v1 + x2v2 + ⋯ + xkvk = 0 has only the trivial solution x1 = x2 = ⋯ = xk = 0. The set {v1, v2, …, vk} is linearly dependent otherwise.
- A set of vectors is linearly dependent if one of the vectors can be written as a linear combination of the others. For example, the set {(1, 1, 1), (1, -1, 2), (3, 1, 4)} is linearly dependent because (3, 1, 4) = 2(1, 1, 1) + (1, -1, 2).
- A set of vectors which is linearly independent and spans some vector space, forms a basis for that vector space. For example, the vector space of all polynomials in x over the reals has the (infinite) subset {1, x, x2, ...} as a basis.
- To check if a set of vectors is linearly independent, we can use the following methods  :
  - Write the vectors as columns of a matrix and row reduce it. If there is a pivot in every column, the vectors are linearly independent. If there is a free variable, the vectors are linearly dependent.
  - Write the vectors as rows of a matrix and find its determinant. If the determinant is nonzero, the vectors are linearly independent. If the determinant is zero, the vectors are linearly dependent.
  - Write the vector equation x1v1 + x2v2 + ⋯ + xkvk = 0 and solve for the coefficients x1, x2, ..., xk. If the only solution is x1 = x2 = ⋯ = xk = 0, the vectors are linearly independent. If there is a nontrivial solution, the vectors are linearly dependent.