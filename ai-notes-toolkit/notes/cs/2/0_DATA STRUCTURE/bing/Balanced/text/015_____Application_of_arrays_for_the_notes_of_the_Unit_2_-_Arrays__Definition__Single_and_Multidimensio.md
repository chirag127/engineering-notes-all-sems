### Application of arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by using an index.
- Arrays can be used to store and manipulate various kinds of data, such as numbers, characters, strings, matrices, graphs, images, etc.
- Arrays can be classified into single and multidimensional arrays, depending on the number of dimensions or subscripts required to access an element.
- Single dimensional arrays are also called vectors or one-dimensional arrays. They have only one subscript to access an element, such as `a[i]`, where `a` is the name of the array and `i` is the index of the element.
- Multidimensional arrays are also called matrices or n-dimensional arrays. They have more than one subscript to access an element, such as `a[i][j]`, where `a` is the name of the array and `i` and `j` are the indices of the element in the row and column respectively.
- The representation of arrays in memory depends on the order in which the elements are stored. There are two common ways of storing arrays: row major order and column major order.
- Row major order means that the elements of an array are stored row by row, starting from the first row. For example, the elements of a 3x3 matrix `a` are stored as `a[0][0], a[0][1], a[0][2], a[1][0], a[1][1], a[1][2], a[2][0], a[2][1], a[2][2]`.
- Column major order means that the elements of an array are stored column by column, starting from the first column. For example, the elements of a 3x3 matrix `a` are stored as `a[0][0], a[1][0], a[2][0], a[0][1], a[1][1], a[2][1], a[0][2], a[1][2], a[2][2]`.
- The index formulae for 1-D, 2-D, 3-D and n-D arrays are used to calculate the address of an element in memory, given the base address of the array, the size of each element, and the indices of the element.
- For a 1-D array `a` of size `n` and element size `s`, the address of `a[i]` is given by `base + i * s`, where `base` is the base address of the array and `i` is the index of the element.
- For a 2-D array `a` of size `m x n` and element size `s`, the address of `a[i][j]` is given by `base + (i * n + j) * s` in row major order and `base + (j * m + i) * s` in column major order, where `base` is the base address of the array and `i` and `j` are the indices of the element in the row and column respectively.
- For a 3-D array `a` of size `l x m x n` and element size `s`, the address of `a[i][j][k]` is given by `base + (i * m * n + j * n + k) * s` in row major order and `base + (k * l * m + j * l + i) * s` in column major order, where `base` is the base address of the array and `i`, `j` and `k` are the indices of the element in the depth, row and column respectively.
- For an n-D array `a` of size `d1 x d2 x ... x dn` and element size `s`, the address of `a[i1][i2]...[in]` is given by `base + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * s` in row major order and `base + (in * d1 * d2 * ... * dn-1 + in-1 * d1 * d2 * ... * dn-2 + ... + i1) * s` in column major order, where `base` is the base address of the array and `i1`, `i2`, ..., `in` are the indices of the element in the dimensions.

### Sparse matrices and their representations

- A sparse matrix is a matrix that has a large number of zero elements and a small number of non-zero elements