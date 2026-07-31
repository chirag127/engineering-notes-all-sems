# Derivation of Index Formulae for 1-D, 2-D, 3-D and n-D Array

## 1-D Array

- A one-dimensional array is a linear collection of elements that are stored in contiguous memory locations.
- The index of the first element is usually 0 or 1, depending on the programming language or the implementation.
- To access any element of a 1-D array, we need to know its base address (the address of the first element), the size of each element (in bytes), and the index of the element.
- The formula for calculating the address of any element in a 1-D array is:

  - `LOC(A[i]) = Base_Address + W * (i - LB)`

  - Where:
    - `LOC(A[i])` is the address of the ith element of the array A
    - `Base_Address` is the address of the first element of the array A
    - `W` is the size of each element of the array A (in bytes)
    - `i` is the index of the element to be accessed
    - `LB` is the lower bound of the array A (usually 0 or 1)

  - For example, if the base address of an array A of 10 integers is 1000, the size of each integer is 4 bytes, and the lower bound of the array is 0, then the address of the 5th element of the array is:

    - `LOC(A[5]) = 1000 + 4 * (5 - 0) = 1020`

## 2-D Array

- A two-dimensional array is a collection of elements that are arranged in rows and columns, and are stored in row-major order or column-major order in memory.
- The index of the first row and the first column is usually 0 or 1, depending on the programming language or the implementation.
- To access any element of a 2-D array, we need to know its base address, the size of each element, the number of rows and columns, and the indices of the row and the column of the element.
- The formula for calculating the address of any element in a 2-D array in row-major order is:

  - `LOC(A[i][j]) = Base_Address + W * (N * (i - LB1) + (j - LB2))`

  - Where:
    - `LOC(A[i][j])` is the address of the element in the ith row and jth column of the array A
    - `Base_Address` is the address of the first element of the array A
    - `W` is the size of each element of the array A (in bytes)
    - `N` is the number of columns in the array A
    - `i` and `j` are the indices of the row and the column of the element to be accessed
    - `LB1` and `LB2` are the lower bounds of the rows and columns of the array A (usually 0 or 1)

  - For example, if the base address of an array A of 3 rows and 4 columns of integers is 2000, the size of each integer is 4 bytes, and the lower bounds of the rows and columns are 0, then the address of the element in the 2nd row and 3rd column of the array is:

    - `LOC(A[2][3]) = 2000 + 4 * (4 * (2 - 0) + (3 - 0)) = 2052`

- The formula for calculating the address of any element in a 2-D array in column-major order is:

  - `LOC(A[i][j]) = Base_Address + W * (M * (j - LB2) + (i - LB1))`

  - Where:
    - `LOC(A[i][j])` is the address of the element in the ith row and jth column of the array A
    - `Base_Address` is the address of the first element of the array A
    - `W` is the size of each element of the array A (in bytes)
    - `M` is the number of rows in the array A
    - `i` and `j` are the indices of the row and the column of the element to be accessed
    - `LB1` and `LB2` are the lower bounds of the rows and columns of the array A (usually 0 or