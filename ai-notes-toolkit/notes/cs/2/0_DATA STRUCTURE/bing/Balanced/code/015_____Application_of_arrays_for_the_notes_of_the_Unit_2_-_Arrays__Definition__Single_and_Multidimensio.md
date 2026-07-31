### Application of arrays

- Arrays are the simplest data structures that store items of the same data type in a contiguous and adjacent memory location .
- Arrays have a fixed size that cannot be changed once declared .
- Arrays can be used to store data in tabular format, such as contacts on a mobile device, matrix storage and binary tree elements  .
- Arrays can also be used for sorting and searching algorithms, such as binary search, merge sort, quick sort, etc.
- Arrays can be classified into single and multidimensional arrays, depending on the number of dimensions or subscripts used to access the elements.
- Single dimensional arrays have only one subscript, such as `a[0]`, `a[1]`, ..., `a[n-1]`, where `n` is the size of the array.
- Multidimensional arrays have more than one subscript, such as `a[0][0]`, `a[0][1]`, ..., `a[m-1][n-1]`, where `m` and `n` are the dimensions of the array.
- The representation of arrays can be done in two ways: row major order and column major order.
- Row major order stores the elements of an array row by row, such that the first element of the first row is stored first, followed by the second element of the first row, and so on.
- Column major order stores the elements of an array column by column, such that the first element of the first column is stored first, followed by the second element of the first column, and so on.
- The derivation of index formulae for 1-D, 2-D, 3-D and n-D arrays can be done using the base address, the size of each element, and the subscripts of the array.
- For a 1-D array `a[n]`, the index formula is `LOC(a[i]) = BA + i * size`, where `LOC(a[i])` is the location of the `i`th element, `BA` is the base address, and `size` is the size of each element.
- For a 2-D array `a[m][n]`, the index formula for row major order is `LOC(a[i][j]) = BA + (i * n + j) * size`, where `i` and `j` are the row and column subscripts, respectively.
- For a 2-D array `a[m][n]`, the index formula for column major order is `LOC(a[i][j]) = BA + (j * m + i) * size`, where `i` and `j` are the row and column subscripts, respectively.
- For a 3-D array `a[l][m][n]`, the index formula for row major order is `LOC(a[i][j][k]) = BA + (i * m * n + j * n + k) * size`, where `i`, `j`, and `k` are the subscripts for the three dimensions.
- For a 3-D array `a[l][m][n]`, the index formula for column major order is `LOC(a[i][j][k]) = BA + (k * l * m + j * l + i) * size`, where `i`, `j`, and `k` are the subscripts for the three dimensions.
- For an n-D array `a[d1][d2]...[dn]`, the index formula for row major order is `LOC(a[i1][i2]...[in]) = BA + (i1 * d2 * d3 * ... * dn + i2 * d3 * d4 * ... * dn + ... + in) * size`, where `i1`, `i2`, ..., `in` are the subscripts for the n dimensions.
- For an n-D array `a[d1][d2]...[dn]`, the index formula for column major order is `LOC(a[i1][i2]...[in]) = BA + (in * d1 * d2 * ... * d(n-1) + in-1 * d1 * d2 * ... * d(n-2) + ... + i1