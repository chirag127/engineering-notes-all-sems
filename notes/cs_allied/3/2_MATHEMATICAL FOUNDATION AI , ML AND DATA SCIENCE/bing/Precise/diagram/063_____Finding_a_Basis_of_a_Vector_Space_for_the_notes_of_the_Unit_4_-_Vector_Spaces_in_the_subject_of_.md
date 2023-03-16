### Finding a Basis of a Vector Space

A basis of a vector space is a set of vectors that is linearly independent and spans the vector space. In other words, any vector in the vector space can be written as a linear combination of the basis vectors.

Here are the steps to find a basis of a vector space:

1. Write the vectors of the vector space as rows of a matrix.
2. Use row operations to put the matrix in row echelon form.
3. The nonzero rows of the row echelon form correspond to the basis vectors of the vector space.
4. Write the basis vectors as a set.

For example, let's find a basis for the vector space spanned by the vectors (1, 2, 3), (2, 4, 6), and (3, 6, 9).

1. Write the vectors as rows of a matrix:

```
| 1 2 3 |
| 2 4 6 |
| 3 6 9 |
```

2. Use row operations to put the matrix in row echelon form:

```
| 1 2 3 |
| 0 0 0 |
| 0 0 0 |
```

3. The nonzero row corresponds to the basis vector (1, 2, 3).
4. The basis for the vector space is {(1, 2, 3)}.

Note that the basis is not unique. Any set of linearly independent vectors that spans the vector space can be a basis. For example, {(2, 4, 6)} is also a basis for the vector space in the example above. However, all bases for a given vector space have the same number of vectors, which is called the dimension of the vector space. In the example above, the dimension of the vector space is 1.