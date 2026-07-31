### Array references in arithmetic expressions

- An array reference is an expression that refers to an element of an array by specifying its index or subscript.
- An array reference has an l-value, which is the address of the element in memory.
- To compute the l-value of an array reference, the compiler needs to know the base address of the array, the lower and upper bounds of the index, the width of each element, and the order of storage (row-major or column-major).
- The general formula for computing the l-value of an array reference A[i] is:

  - `base + (i - low) * width`
  - where `base` is the base address of the array, `low` is the lower bound of the index, and `width` is the width of each element.

- For multidimensional arrays, the formula is extended by multiplying the index of each dimension by the product of the widths of the lower dimensions, and adding them together. For example, for a two-dimensional array A[i][j], the formula is:

  - `base + (i - low1) * width1 * (high2 - low2 + 1) + (j - low2) * width2`
  - where `low1` and `high1` are the lower and upper bounds of the first dimension, `low2` and `high2` are the lower and upper bounds of the second dimension, `width1` is the width of each row, and `width2` is the width of each element.

- The compiler can generate code to evaluate the l-value of an array reference by using arithmetic instructions and memory operations. For example, for the array reference A[i][j], the compiler can generate the following code:

  - `t1 = i - low1`
  - `t2 = t1 * width1 * (high2 - low2 + 1)`
  - `t3 = j - low2`
  - `t4 = t3 * width2`
  - `t5 = t2 + t4`
  - `t6 = base + t5`
  - `t6` is the l-value of A[i][j]

- The compiler can also optimize the code by using constants and loop-invariant expressions. For example, if `low1`, `low2`, `width1`, `width2`, and `base` are constants, and `i` is loop-invariant, the compiler can generate the following code:

  - `t1 = i - low1`
  - `t2 = t1 * width1 * (high2 - low2 + 1)`
  - `t3 = base - low2 * width2 + t2`
  - `t4 = j - low2`
  - `t5 = t4 * width2`
  - `t6 = t3 + t5`
  - `t6` is the l-value of A[i][j]

- Array references in arithmetic expressions can be used as operands or as targets of assignments. For example, the statement `A[i][j] = B[i] + C[j]` can be translated as:

  - `t1 = i - low1`
  - `t2 = t1 * width1 * (high2 - low2 + 1)`
  - `t3 = base - low2 * width2 + t2`
  - `t4 = j - low2`
  - `t5 = t4 * width2`
  - `t6 = t3 + t5`
  - `t7 = i - lowB`
  - `t8 = t7 * widthB`
  - `t9 = baseB + t8`
  - `t10 = j - lowC`
  - `t11 = t10 * widthC`
  - `t12 = baseC + t11`
  - `t13 = M[t9]`
  - `t14 = M[t12]`
  - `t15 = t13 + t14`
  - `M[t6] = t15`
  - where `M` is the memory array, and `baseB`, `lowB`, and `widthB` are the base address, lower bound, and width of array B, and `baseC`, `lowC`, and `widthC` are the base address, lower bound, and width of array C.