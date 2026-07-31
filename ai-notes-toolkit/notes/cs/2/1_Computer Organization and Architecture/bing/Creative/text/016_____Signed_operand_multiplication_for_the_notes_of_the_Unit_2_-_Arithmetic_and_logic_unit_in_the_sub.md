### Signed operand multiplication

- Signed operand multiplication is the process of multiplying two binary numbers that have a sign bit, usually in 2's complement representation.
- The sign bit is the most significant bit of the number, and it indicates whether the number is positive (0) or negative (1).
- The sign of the product is determined by the exclusive OR of the sign bits of the operands, i.e., the product is negative if and only if the operands have opposite signs.
- The magnitude of the product is obtained by multiplying the magnitudes of the operands, i.e., the bits other than the sign bit, using the shift-and-add algorithm or other methods.
- The shift-and-add algorithm involves shifting the multiplicand left by one bit position for each bit of the multiplier, starting from the least significant bit, and adding the shifted multiplicand to a partial product if the corresponding multiplier bit is 1.
- The partial product is initially zero, and it has one more bit than the operands to accommodate the possible overflow.
- The final product has twice as many bits as the operands, and it may need to be sign-extended or truncated to fit the desired size.
- An example of signed operand multiplication using 4-bit numbers is shown below:

```
  0011 (-5 in 2's complement)
x 1101 (3 in 2's complement)
------
  0011 (shifted multiplicand, multiplier bit is 1)
+ 0000 (partial product)
------
  0011 (new partial product)
 0110 (shifted multiplicand, multiplier bit is 0)
+ 0011 (partial product)
------
  0011 (new partial product)
 1100 (shifted multiplicand, multiplier bit is 1)
+ 0011 (partial product)
------
  1111 (new partial product)
 1000 (shifted multiplicand, multiplier bit is 1)
+ 1111 (partial product)
------
1 0111 (final product, -15 in 2's complement)
```

- Some variations of signed operand multiplication are:

  - Signed-magnitude multiplication: The operands are in signed-magnitude representation, where the sign bit is separate from the magnitude, and the magnitude is in binary. The sign of the product is computed by the exclusive OR of the sign bits, and the magnitude of the product is computed by the shift-and-add algorithm as usual.
  - Booth's algorithm: The operands are in 2's complement representation, but the algorithm reduces the number of additions and subtractions by encoding the multiplier into groups of 0's and 1's, and using a single adder-subtractor unit to perform the partial product updates.
  - IMUL instruction: The IMUL instruction is an assembly language instruction that performs signed integer multiplication on 8-, 16-, or 32-bit operands, using either AL, AX, or EAX as the implicit multiplicand. The instruction preserves the sign of the product by sign-extending it into the upper half of the destination register, and sets the overflow flag if the product cannot fit in the lower half of the destination register.