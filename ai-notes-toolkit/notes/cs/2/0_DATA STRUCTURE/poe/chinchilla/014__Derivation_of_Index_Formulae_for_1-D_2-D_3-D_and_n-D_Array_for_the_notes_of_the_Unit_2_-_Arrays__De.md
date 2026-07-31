### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

Arrays are an essential data structure used in computer science to store and access large amounts of data efficiently. Arrays can be of different dimensions, including 1-D, 2-D, 3-D, and n-D arrays. To access the elements of an array, we need to use index formulae. In this section, we will discuss the derivation of index formulae for different types of arrays.

#### 1-D Array

A 1-D array is a collection of elements that are stored in a contiguous memory location. To access the elements of a 1-D array, we need to use the following index formula:

`Address of a[i] = base_address + size_of_each_element * (i - first_index)`

Here, `a` is the name of the array, `i` is the index of the element we want to access, `first_index` is the index of the first element of the array, `size_of_each_element` is the size of each element in bytes, and `base_address` is the memory address of the first element of the array.

#### 2-D Array

A 2-D array is a collection of elements that are arranged in rows and columns. To access the elements of a 2-D array, we need to use the following index formula:

`Address of a[i][j] = base_address + size_of_each_element * [i - first_index][j - second_index]`

Here, `a` is the name of the array, `i` and `j` are the indices of the row and column of the element we want to access, `first_index` and `second_index` are the indices of the first row and first column of the array, `size_of_each_element` is the size of each element in bytes, and `base_address` is the memory address of the first element of the array.

#### 3-D Array

A 3-D array is a collection of elements that are arranged in a three-dimensional space. To access the elements of a 3-D array, we need to use the following index formula:

`Address of a[i][j][k] = base_address + size_of_each_element * [(i - first_index)*n*m + (j - second_index)*n + (k - third_index)]`

Here, `a` is the name of the array, `i`, `j`, and `k` are the indices of the three dimensions of the element we want to access, `first_index`, `second_index`, and `third_index` are the indices of the first dimension, second dimension, and third dimension of the array, respectively, `size_of_each_element` is the size of each element in bytes, `n` is the number of columns in each row, and `m` is the number of rows in each layer. `base_address` is the memory address of the first element of the array.

#### n-D Array

An n-D array is a collection of elements that are arranged in an n-dimensional space. To access the elements of an n-D array, we need to use the following index formula:

`Address of a[i1][i2]...[in] = base_address + size_of_each_element * [(i1 - first_index1)*p1*p2*...*pn-1 + (i2 - first_index2)*p2*p3*...*pn-1 + ... + (in - first_indexn-1)*pn-1 + (in - first_indexn)]`

Here, `a` is the name of the array, `i1`, `i2`, ..., `in` are the indices of the n dimensions of the element we want to access, `first_index1`, `first_index2`, ..., `first_indexn-1` are the indices of the first dimension, second dimension, ..., (n-1)th dimension of the array, respectively, `size_of_each_element` is the size of each element in bytes, `p1`, `p2`, ..., `pn-1` are the sizes of the dimensions of the array, and `base_address` is the memory address of the first element of the array.

In conclusion, the derivation of index formulae for arrays is an essential concept in data structures. The index formulae discussed in this section can be used to efficiently access the elements of different types of arrays.