### Application of arrays

- An array is a collection of data elements of the same type, stored in contiguous memory locations and accessed by an index.
- Arrays can be used to store and manipulate various kinds of data, such as numbers, characters, strings, matrices, graphs, images, etc.
- Arrays can be classified into single and multidimensional arrays, depending on the number of dimensions or subscripts required to access an element.
- Single dimensional arrays are also called vectors or one-dimensional arrays. They have only one subscript to access an element, such as `a[i]` where `i` is the index of the element.
- Multidimensional arrays are also called matrices or n-dimensional arrays. They have more than one subscript to access an element, such as `a[i][j]` where `i` and `j` are the indices of the element in a two-dimensional array.
- The representation of arrays in memory depends on the order of storing the elements, which can be either row major order or column major order.
- Row major order is a method of storing the elements of an array in memory such that the elements of a row are stored consecutively, followed by the elements of the next row, and so on. For example, the elements of a two-dimensional array `a[3][4]` are stored in memory as `a[0][0], a[0][1], a[0][2], a[0][3], a[1][0], a[1][1], a[1][2], a[1][3], a[2][0], a[2][1], a[2][2], a[2][3]`.
- Column major order is a method of storing the elements of an array in memory such that the elements of a column are stored consecutively, followed by the elements of the next column, and so on. For example, the elements of a two-dimensional array `a[3][4]` are stored in memory as `a[0][0], a[1][0], a[2][0], a[0][1], a[1][1], a[2][1], a[0][2], a[1][2], a[2][2], a[0][3], a[1][3], a[2][3]`.
- The derivation of index formulae for 1-D, 2-D, 3-D and n-D arrays is based on the following principles:
  - The base address of the array is the starting memory location of the first element of the array, denoted by `BA`.
  - The size of each element of the array is the number of bytes required to store one element, denoted by `w`.
  - The lower bound and upper bound of each dimension of the array are the minimum and maximum values of the subscript for that dimension, denoted by `L` and `U` respectively.
  - The index of an element of the array is the relative position of the element from the base address, denoted by `I`.
  - The index formula for an array is the expression that calculates the index of an element of the array based on its subscripts and the order of storing the elements.
- The index formula for a one-dimensional array `a[n]` stored in row major order is `I = (i - L) * w` where `i` is the subscript of the element, `L` is the lower bound of the array, and `w` is the size of each element. The memory address of the element `a[i]` is `BA + I`.
- The index formula for a two-dimensional array `a[m][n]` stored in row major order is `I = ((i - L1) * n + (j - L2)) * w` where `i` and `j` are the subscripts of the element, `L1` and `L2` are the lower bounds of the first and second dimensions of the array, `n` is the number of columns of the array, and `w` is the size of each element. The memory address of the element `a[i][j]` is `BA + I`.
- The index formula for a three-dimensional array `a[l][m][n]` stored in row major order is `I = (((i - L1) * m + (j - L2)) * n + (k - L3)) * w` where `i`, `j` and `k` are the subscripts of the element, `L1`, `L2` and `L3` are the lower bounds of the first, second and third dimensions of