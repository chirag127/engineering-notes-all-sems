### Finding a Basis of a Vector Space

A basis of a vector space is a set of vectors that is linearly independent and spans the vector space. In other words, any vector in the vector space can be written as a linear combination of the basis vectors.

Here are the steps to find a basis of a vector space:

1. Write the vectors in the vector space as columns of a matrix.
2. Row reduce the matrix to its row echelon form.
3. The pivot columns of the row echelon form correspond to the basis vectors of the vector space.
4. The basis vectors can be obtained by taking the corresponding columns from the original matrix.

For example, consider the vector space spanned by the vectors [1, 2, 3] and [4, 5, 6]. We can write these vectors as columns of a matrix:

```
[ 1 4 ]
[ 2 5 ]
[ 3 6 ]
```

Row reducing this matrix, we get:

```
[ 1 0 ]
[ 0 1 ]
[ 0 0 ]
```

The pivot columns are the first and second columns, so the basis vectors are [1, 2, 3] and [4, 5, 6].

It is important to note that a basis is not unique. There can be multiple bases for a given vector space. However, the number of basis vectors, or the dimension of the vector space, is always the same. In the above example, the dimension of the vector space is 2.