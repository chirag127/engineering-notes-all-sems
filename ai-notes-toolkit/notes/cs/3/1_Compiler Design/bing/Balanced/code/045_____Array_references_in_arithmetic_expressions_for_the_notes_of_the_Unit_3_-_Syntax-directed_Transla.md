### Array references in arithmetic expressions

- An array reference is an expression that refers to an element of an array by specifying its index or subscript.
- An array reference has an l-value, which is the memory location of the element.
- To translate an array reference, the compiler needs to compute the offset of the element from the base address of the array, and then add it to the base address to get the l-value.
- The offset depends on the size of the array elements, the lower and upper bounds of the array, and the index expression.
- For a one-dimensional array A[low..high], the offset of A[i] is (i-low)*width, where width is the size of each element in bytes.
- For a multi-dimensional array A[low1..high1][low2..high2]...[lown..highn], the offset of A[i1][i2]...[in] is a linear combination of the index expressions and the widths of each dimension, which can be computed using the formula:

  offset = width * (i1-low1) * (high2-low2+1) * ... * (highn-lown+1) + width * (i2-low2) * (high3-low3+1) * ... * (highn-lown+1) + ... + width * (in-lown)

- The base address of the array can be a constant, a variable, or a register, depending on how the array is declared and allocated.
- The compiler can generate code to evaluate the offset and the base address, and then add them to get the l-value of the array reference.
- The code can be optimized by using constant folding, strength reduction, and loop invariant code motion techniques to reduce the number of arithmetic operations and memory accesses.