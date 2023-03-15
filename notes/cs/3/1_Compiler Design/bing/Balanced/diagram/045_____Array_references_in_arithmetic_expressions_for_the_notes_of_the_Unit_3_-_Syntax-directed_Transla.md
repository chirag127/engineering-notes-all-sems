### Array references in arithmetic expressions

- An array reference is an expression that refers to an element of an array by specifying its index or subscript.
- An array reference has an l-value, which is the memory location of the element.
- To translate an array reference, the compiler needs to compute the offset of the element from the base address of the array, and then add it to the base address to get the l-value.
- The offset depends on the size of the array elements, the lower and upper bounds of the array, and the index expression.
- For a one-dimensional array A[low..high], the offset of A[i] is (i-low)*width, where width is the size of each element in bytes.
- For a multi-dimensional array A[low1..high1][low2..high2]...[lown..highn], the offset of A[i1][i2]...[in] is a linear combination of the index expressions and the widths of each dimension, as shown in the following formula:

![offset formula](https://www.javatpoint.com/images/array-references-in-arithmetic-expressions/offset-formula.png)

- The compiler can generate code to evaluate the offset expression and add it to the base address of the array, or it can use an intermediate representation such as a quadruple or a syntax tree to represent the array reference.