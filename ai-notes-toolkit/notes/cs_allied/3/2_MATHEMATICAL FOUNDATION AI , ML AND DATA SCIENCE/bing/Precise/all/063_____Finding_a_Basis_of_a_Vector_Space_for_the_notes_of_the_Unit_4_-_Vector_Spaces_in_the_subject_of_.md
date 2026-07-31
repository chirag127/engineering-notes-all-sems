### Finding a Basis of a Vector Space

A basis of a vector space is a set of vectors that is linearly independent and spans the vector space. This means that any vector in the vector space can be written as a linear combination of the basis vectors.

Here are the steps to find a basis of a vector space:

1. Write the vectors in the vector space as columns of a matrix.
2. Row reduce the matrix to its row echelon form.
3. The pivot columns of the row echelon form correspond to the basis vectors of the vector space.
4. The basis vectors can be obtained by taking the corresponding columns from the original matrix.

Example: Consider the vector space spanned by the vectors (1, 2, 3), (2, 4, 6), and (3, 6, 9). To find a basis for this vector space, we can write these vectors as columns of a matrix:

```
| 1 2 3 |
| 2 4 6 |
| 3 6 9 |
```

Row reducing this matrix, we obtain:

```
| 1 2 3 |
| 0 0 0 |
| 0 0 0 |
```

The pivot column is the first column, so the basis vector is (1, 2, 3). Thus, the basis for the vector space spanned by the vectors (1, 2, 3), (2, 4, 6), and (3, 6, 9) is {(1, 2, 3)}.