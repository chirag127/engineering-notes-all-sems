### Single and Multidimensional Arrays

- An array is a data structure that stores a collection of elements of the same type in a contiguous block of memory.
- Each element in an array can be accessed by its index, which is a non-negative integer that represents its position in the array.
- The index of the first element in an array is usually 0, and the index of the last element is the length of the array minus 1.
- Arrays can have one or more dimensions, depending on how many indices are needed to specify an element.
- A one-dimensional array (or 1D array) is an array that has only one index. It can be visualized as a row of elements, such as `[1, 2, 3, 4, 5]`.
- A two-dimensional array (or 2D array) is an array that has two indices. It can be visualized as a matrix or table of elements, such as `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`.
- A three-dimensional array (or 3D array) is an array that has three indices. It can be visualized as a cube or stack of matrices of elements, such as `[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]`.
- A n-dimensional array (or nD array) is an array that has n indices, where n is any positive integer. It can be visualized as a nested structure of arrays of arrays of ... of elements, such as `[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]` for a 4D array.
- The number of dimensions of an array is also called its rank or order.
- The size of an array is the total number of elements it can hold. It is equal to the product of the lengths of each dimension. For example, a 2D array with 3 rows and 4 columns has a size of 3 x 4 = 12.
- The shape of an array is the tuple of the lengths of each dimension. For example, a 2D array with 3 rows and 4 columns has a shape of (3, 4).
- Arrays can be used to implement other data structures, such as stacks, queues, heaps, graphs, etc.
- Arrays can also be used to store and manipulate data, such as matrices, vectors, images, etc.
- Arrays can be represented in different ways in memory, depending on how the elements are ordered and stored. Two common ways are row-major order and column-major order.
- In row-major order, the elements of an array are stored row by row, such that the elements of the first row are stored first, followed by the elements of the second row, and so on. For example, the 2D array `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` is stored in row-major order as `[1, 2, 3, 4, 5, 6, 7, 8, 9]`.
- In column-major order, the elements of an array are stored column by column, such that the elements of the first column are stored first, followed by the elements of the second column, and so on. For example, the 2D array `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]` is stored in column-major order as `[1, 4, 7, 2, 5, 8, 3, 6, 9]`.
- The choice of row-major or column-major order affects how the indices of an element are mapped to its memory location. A formula can be derived to calculate the memory address of an element given its indices and the shape of the array.
- For a 1D array of size n, the