# Representation of Arrays: Row Major Order, and Column Major Order

Arrays can be stored in memory in two ways: row-major order and column-major order. These two methods determine the linear mapping of a multi-dimensional array's elements to contiguous memory locations.

## Row Major Order
In row-major order, the elements of an array are stored row by row. The first row is stored in contiguous memory locations, followed by the second row, and so on. This means that the elements in a row are stored next to each other in memory.

For example, consider a 2D array `A` with `m` rows and `n` columns. The element `A[i][j]` is located at the memory address `base_address + (i * n + j) * element_size`, where `base_address` is the memory address of the first element of the array, and `element_size` is the size of each element in the array.

## Column Major Order
In column-major order, the elements of an array are stored column by column. The first column is stored in contiguous memory locations, followed by the second column, and so on. This means that the elements in a column are stored next to each other in memory.

For example, consider a 2D array `A` with `m` rows and `n` columns. The element `A[i][j]` is located at the memory address `base_address + (j * m + i) * element_size`, where `base_address` is the memory address of the first element of the array, and `element_size` is the size of each element in the array.

Both row-major order and column-major order have their advantages and disadvantages. The choice of which method to use depends on the specific requirements of the application. For example, if the application frequently accesses the elements of a row, then row-major order may be more efficient. On the other hand, if the application frequently accesses the elements of a column, then column-major order may be more efficient.