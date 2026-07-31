### Booth's algorithm

Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in 2's complement notation . The algorithm was invented by Andrew Donald Booth in 1950 while doing research on crystallography at Birkbeck College in London. Booth's algorithm is of interest in the study of computer architecture, as it can reduce the number of additions and subtractions required for binary multiplication  .

The main idea of Booth's algorithm is to examine adjacent pairs of bits of the multiplier, including an implicit bit below the least significant bit, and perform different operations depending on the bit pair. The possible bit pairs are 00, 01, 10, and 11, and the corresponding operations are:

- 00: Do nothing (no addition or subtraction needed)
- 01: Add the multiplicand to the product and shift right
- 10: Subtract the multiplicand from the product and shift right
- 11: Do nothing (no addition or subtraction needed)

The algorithm can be summarized as follows  :

- Step 1: Initialize the product register to 0 and append a 0 to the right of the multiplier. The product register and the multiplier should have the same number of bits. The appended 0 is the implicit bit y<sub>-1</sub>.
- Step 2: Check the rightmost two bits of the multiplier and perform the corresponding operation. If the bit pair is 01, add the multiplicand to the product and store the result in the product register. If the bit pair is 10, subtract the multiplicand from the product and store the result in the product register. If the bit pair is 00 or 11, do nothing.
- Step 3: Arithmetic shift right the product register and the multiplier by one bit. The sign bit of the product register should be duplicated to preserve the sign of the product.
- Step 4: Repeat steps 2 and 3 until the multiplier becomes 0. The final product will be in the product register.

An example of Booth's algorithm is shown below, where the multiplicand is 3 (0011) and the multiplier is -4 (1100) in 4-bit 2's complement notation  :

| Step | Operation | Product | Multiplier | Bit pair |
|------|-----------|---------|------------|----------|
| 0    | Initial   | 0000    | 1100       | 00       |
| 1    | Nothing   | 0000    | 0110       | 10       |
| 2    | Subtract  | 1101    | 0011       | 10       |
| 3    | Subtract  | 1010    | 0001       | 11       |
| 4    | Nothing   | 1101    | 0000       | 01       |
| 5    | Add       | 0000    | 0000       | 00       |

The final product is 0000, which is -12 in 2's complement notation, and is the correct result of 3 x -4. Note that the product register has overflowed in step 5, but this does not affect the final result as the product is 8 bits long and the product register is 4 bits long.