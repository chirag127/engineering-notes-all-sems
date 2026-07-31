### Multiplication

- Multiplication is an arithmetic operation that computes the product of two numbers.
- Multiplication can be performed by repeated addition, shifting and adding, or using a multiplication algorithm.
- In binary, multiplication can be done by shifting the multiplicand left by the number of bits in the multiplier, and adding the shifted multiplicand to a partial product whenever the corresponding bit in the multiplier is 1.
- For example, to multiply 1011 (11 in decimal) by 110 (6 in decimal), the steps are:

  - Initialize the partial product to 0.
  - Shift the multiplicand left by 2 bits, since the multiplier has 2 bits. The shifted multiplicand is 101100.
  - Since the least significant bit of the multiplier is 0, do not add the shifted multiplicand to the partial product.
  - Shift the multiplier right by 1 bit, discarding the least significant bit. The multiplier is now 11.
  - Shift the multiplicand left by 1 bit. The shifted multiplicand is 1011000.
  - Since the least significant bit of the multiplier is 1, add the shifted multiplicand to the partial product. The partial product is now 1011000.
  - Shift the multiplier right by 1 bit, discarding the least significant bit. The multiplier is now 1.
  - Shift the multiplicand left by 1 bit. The shifted multiplicand is 10110000.
  - Since the least significant bit of the multiplier is 1, add the shifted multiplicand to the partial product. The partial product is now 111001000.
  - Since the multiplier is 0, the multiplication is done. The partial product is the final product, which is 111001000 (72 in decimal).

- There are other methods of binary multiplication, such as Booth's algorithm, Wallace tree, and Dadda multiplier, that can improve the speed and efficiency of the operation.