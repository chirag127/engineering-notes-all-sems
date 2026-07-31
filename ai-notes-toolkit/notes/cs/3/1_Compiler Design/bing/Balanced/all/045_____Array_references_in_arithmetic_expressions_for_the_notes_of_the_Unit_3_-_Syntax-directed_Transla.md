# Array references in arithmetic expressions

- An array is a data structure that stores a collection of values of the same type in a contiguous memory location.
- An array reference is an expression that denotes an element of an array, such as `A[i]` or `B[i][j]`.
- An array reference can be used as an l-value (a location that can be assigned a value) or an r-value (a value that can be used in an expression) in an arithmetic expression.
- To translate an array reference, the compiler needs to compute the address of the element in the memory, which depends on the base address of the array, the index of the element, the lower and upper bounds of the array, and the width of each element.
- For a one-dimensional array `A[low..high]`, the address of the ith element is given by:

  ```
  base + (i - low) * width
  ```

  where `base` is the base address of the array, `low` and `high` are the lower and upper bounds of the array, and `width` is the size of each element in bytes.

- For a two-dimensional array `B[low1..high1][low2..high2]`, the address of the ith row and jth column element is given by:

  ```
  base + (i - low1) * (high2 - low2 + 1) * width + (j - low2) * width
  ```

  where `base` is the base address of the array, `low1`, `high1`, `low2`, and `high2` are the lower and upper bounds of the array in each dimension, and `width` is the size of each element in bytes.

- The compiler can generate code to evaluate the address of an array reference by using arithmetic and load instructions, such as:

  ```
  // A[i] = A[i] + 1
  // Assume A[1..10] is stored at address 1000, and each element is 4 bytes
  // Assume i is stored in register R1
  R2 = 1 // load the lower bound of A
  R3 = 4 // load the width of A
  R4 = R1 - R2 // subtract the lower bound from the index
  R5 = R4 * R3 // multiply the result by the width
  R6 = 1000 // load the base address of A
  R7 = R6 + R5 // add the base address to the offset
  R8 = M[R7] // load the value of A[i] from memory
  R9 = 1 // load the constant 1
  R10 = R8 + R9 // add 1 to the value of A[i]
  M[R7] = R10 // store the result back to memory
  ```