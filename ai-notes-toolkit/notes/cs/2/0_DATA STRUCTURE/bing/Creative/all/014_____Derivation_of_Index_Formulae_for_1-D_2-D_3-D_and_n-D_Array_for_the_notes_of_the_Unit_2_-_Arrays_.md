# Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

## 1-D Array

A one-dimensional array is a linear collection of elements that are stored in contiguous memory locations. The elements of a one-dimensional array can be accessed by using an index that specifies the position of the element in the array. The index usually starts from zero or one, depending on the programming language or the convention used.

The index formula for a one-dimensional array is a function that calculates the memory address of any element in the array, given the base address of the array, the size of each element, and the index of the element. The index formula for a one-dimensional array can be derived as follows:

- Let A be the name of the array, B be the base address of the array, W be the size of each element in bytes, and i be the index of the element to be accessed.
- The address of the first element of the array, A[0] or A[1], is equal to the base address of the array, B.
- The address of the second element of the array, A[1] or A[2], is equal to the base address of the array plus the size of one element, B + W.
- The address of the third element of the array, A[2] or A[3], is equal to the base address of the array plus the size of two elements, B + 2W.
- In general, the address of the ith element of the array, A[i] or A[i+1], is equal to the base address of the array plus the size of i elements, B + iW.

Therefore, the index formula for a one-dimensional array is:

LOC(A[i]) = B + iW

where LOC(A[i]) is the address of the ith element of the array .

## 2-D Array

A two-dimensional array is a collection of elements that are arranged in rows and columns, forming a matrix or a table. The elements of a two-dimensional array can be accessed by using two indices that specify the row and the column of the element in the array. The indices usually start from zero or one, depending on the programming language or the convention used.

The index formula for a two-dimensional array is a function that calculates the memory address of any element in the array, given the base address of the array, the size of each element, the number of columns in the array, and the row and column indices of the element. The index formula for a two-dimensional array can be derived as follows:

- Let A be the name of the array, B be the base address of the array, W be the size of each element in bytes, C be the number of columns in the array, and i and j be the row and column indices of the element to be accessed, respectively.
- The address of the first element of the first row of the array, A[0][0] or A[1][1], is equal to the base address of the array, B.
- The address of the second element of the first row of the array, A[0][1] or A[1][2], is equal to the base address of the array plus the size of one element, B + W.
- The address of the first element of the second row of the array, A[1][0] or A[2][1], is equal to the base address of the array plus the size of one row, B + WC.
- The address of the second element of the second row of the array, A[1][1] or A[2][2], is equal to the base address of the array plus the size of one row and one element, B + WC + W.
- In general, the address of the element in the ith row and jth column of the array, A[i][j] or A[i+1][j+1], is equal to the base address of the array plus the size of i rows and j elements, B + iWC + jW.

Therefore, the index formula for a two-dimensional array is:

LOC(A[i][j]) = B + iWC + jW

where LOC(A[i][j]) is the address of the element in the ith row and jth column of the array .

## 3-D Array

A three-dimensional array is a collection of elements that are arranged in layers, rows, and columns, forming a cube or a box. The elements of a three