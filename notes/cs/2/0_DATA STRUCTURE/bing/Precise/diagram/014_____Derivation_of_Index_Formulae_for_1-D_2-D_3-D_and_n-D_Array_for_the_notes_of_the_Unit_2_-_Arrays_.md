### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

The index formulae for arrays are used to calculate the memory address of an element in an array. The formulae vary depending on the dimension of the array and the order in which the elements are stored.

#### 1-D Array

For a 1-D array, the memory address of an element at index `i` can be calculated using the formula:

`Address = Base_address + (i * size_of_element)`

where `Base_address` is the memory address of the first element of the array and `size_of_element` is the size of each element in the array.

#### 2-D Array

For a 2-D array, the memory address of an element at row `i` and column `j` can be calculated using the formula:

`Address = Base_address + ((i * number_of_columns + j) * size_of_element)`

if the array is stored in row-major order, or

`Address = Base_address + ((j * number_of_rows + i) * size_of_element)`

if the array is stored in column-major order.

#### 3-D Array

For a 3-D array, the memory address of an element at position `(i, j, k)` can be calculated using the formula:

`Address = Base_address + (((i * number_of_rows + j) * number_of_columns + k) * size_of_element)`

if the array is stored in row-major order, or

`Address = Base_address + (((k * number_of_columns + j) * number_of_rows + i) * size_of_element)`

if the array is stored in column-major order.

#### n-D Array

For an n-D array, the memory address of an element at position `(i1, i2, ..., in)` can be calculated using the formula:

`Address = Base_address + (((...((i1 * size2 + i2) * size3 + i3) * ... + in-1) * sizen + in) * size_of_element)`

if the array is stored in row-major order, or

`Address = Base_address + (((...((in * sizen-1 + in-1) * sizen-2 + in-2) * ... + i2) * size1 + i1) * size_of_element)`

if the array is stored in column-major order.

where `size1, size2, ..., sizen` are the sizes of each dimension of the array.

These formulae can be used to calculate the memory address of any element in an array, regardless of its dimension or the order in which the elements are stored. They are an important tool for efficiently accessing and manipulating data in arrays.