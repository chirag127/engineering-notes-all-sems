### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

Arrays are an important data structure used in programming. They are used to store a collection of elements of the same data type. Arrays can be of different types, such as 1-D, 2-D, 3-D, and n-D arrays. In this section, we will discuss how to derive the index formulae for these arrays.

#### 1-D Array

A 1-D array is a collection of elements arranged in a single row. To derive the index formula for a 1-D array, we use the following formula:

```
index = base + (i * size)
```

Here, `base` is the starting address of the array, `i` is the index of the element, and `size` is the size of each element in the array.

#### 2-D Array

A 2-D array is a collection of elements arranged in a matrix format. To derive the index formula for a 2-D array, we use the following formula:

```
index = base + (i * n + j) * size
```

Here, `base` is the starting address of the array, `i` and `j` are the indices of the element, `n` is the number of columns in the array, and `size` is the size of each element in the array.

#### 3-D Array

A 3-D array is a collection of elements arranged in a cube format. To derive the index formula for a 3-D array, we use the following formula:

```
index = base + (i * n * m + j * m + k) * size
```

Here, `base` is the starting address of the array, `i`, `j`, and `k` are the indices of the element, `n` is the number of rows, `m` is the number of columns, and `size` is the size of each element in the array.

#### n-D Array

An n-D array is a collection of elements arranged in an n-dimensional space. To derive the index formula for an n-D array, we use the following formula:

```
index = base + (i1 * n1 * n2 * ... * nn + i2 * n2 * ... * nn + ... + in * 1) * size
```

Here, `base` is the starting address of the array, `i1`, `i2`, ..., `in` are the indices of the element along each dimension, `n1`, `n2`, ..., `nn` are the sizes of each dimension, and `size` is the size of each element in the array.

### Conclusion

In this section, we learned how to derive the index formulae for 1-D, 2-D, 3-D, and n-D arrays. The index formulae help us to access the elements of an array using their indices. These formulae are an important concept in the study of data structures, especially arrays.