### Array references in arithmetic expressions

- An array reference is an expression that denotes the location of an element of an array in memory.
- An array reference has an l-value, which is the address of the element, and an r-value, which is the value stored at that address.
- To translate an array reference in a source program, we need to compute the l-value of the expression that specifies the array element.
- Computing the l-value involves finding the offset of the referred element from the base address of the array, and then adding it to the base address.
- The offset depends on the dimensions, bounds, and element size of the array, as well as the index expressions used to access the element.
- For a one-dimensional array A[low..high], the l-value of A[i] is given by:

  - base + (i - low) * width
  - where base is the base address of A, low and high are the lower and upper bounds of A, width is the size of each element of A, and i is the index expression.

- For a multi-dimensional array A[low1..high1][low2..high2]...[lown..highn], the l-value of A[i1][i2]...[in] is given by:

  - base + (i1 - low1) * width1 + (i2 - low2) * width2 + ... + (in - lown) * widthn
  - where base is the base address of A, lowj and highj are the lower and upper bounds of the jth dimension of A, widthj is the size of each element of the jth dimension of A, and ij is the index expression for the jth dimension.

- To generate code for an array reference, we can use a temporary variable to store the l-value, and then use an indirect load or store instruction to access the element.
- For example, the code for A[i] = B[j] + C[k] can be:

  - t1 = i - lowA
  - t2 = t1 * widthA
  - t3 = baseA + t2
  - t4 = j - lowB
  - t5 = t4 * widthB
  - t6 = baseB + t5
  - t7 = *t6
  - t8 = k - lowC
  - t9 = t8 * widthC
  - t10 = baseC + t9
  - t11 = *t10
  - t12 = t7 + t11
  - *t3 = t12

- Alternatively, we can use an address mode that allows adding an offset to a base register, and then use a direct load or store instruction to access the element.
- For example, the code for A[i] = B[j] + C[k] can be:

  - t1 = i - lowA
  - t2 = j - lowB
  - t3 = k - lowC
  - t4 = * (baseB + t2 * widthB)
  - t5 = * (baseC + t3 * widthC)
  - t6 = t4 + t5
  - * (baseA + t1 * widthA) = t6

- The choice of code generation strategy depends on the target architecture and the optimization level of the compiler.