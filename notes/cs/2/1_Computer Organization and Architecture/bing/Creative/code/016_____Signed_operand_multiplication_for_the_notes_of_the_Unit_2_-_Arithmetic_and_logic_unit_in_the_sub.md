### Signed operand multiplication

- Signed operand multiplication is the process of multiplying two binary numbers that have a sign bit to indicate whether they are positive or negative.
- The sign bit is usually the most significant bit (MSB) of the number, where 0 means positive and 1 means negative.
- There are different methods to perform signed operand multiplication, such as:
  - Signed-magnitude multiplication
  - Booth's algorithm
  - Two's complement multiplication

#### Signed-magnitude multiplication

- In this method, the multiplier and the multiplicand are represented in signed-magnitude format, where the sign bit is separate from the magnitude bits.
- The sign of the product is determined by the XOR of the sign bits of the operands, and the magnitude of the product is obtained by multiplying the magnitudes of the operands using the standard binary multiplication algorithm.
- The standard binary multiplication algorithm involves shifting and adding the multiplicand based on the bits of the multiplier, starting from the least significant bit (LSB).
- For example, to multiply -5 and 3 in signed-magnitude format, we have:

```
  -5 = 1 0101
   3 = 0 0011
```

- The sign of the product is 1 XOR 0 = 1, which means negative.
- The magnitude of the product is obtained by multiplying 0101 and 0011 as follows:

```
  0101
x 0011
-----
  0101
 0000
0101
-----
 1111
```

- Therefore, the product is -15, which is 1 1111 in signed-magnitude format.

#### Booth's algorithm

- In this method, the multiplier and the multiplicand are represented in two's complement format, where the sign bit is the same as the MSB and the magnitude is obtained by complementing the bits and adding 1 if the number is negative.
- The algorithm uses a partial product register (AC), a multiplier register (QR), and an extra bit (Qn+1) to store the result of the multiplication.
- The algorithm also uses a sequence counter (SC) to keep track of the number of iterations.
- The algorithm works as follows:
  - Initialize AC and Qn+1 to 0, QR to the multiplier, and SC to the number of bits in the multiplier.
  - Repeat until SC becomes 0:
    - Check the value of Qn and Qn+1 and perform one of the following operations:
      - If QnQn+1 = 00 or 11, do nothing.
      - If QnQn+1 = 01, subtract the multiplicand from AC.
      - If QnQn+1 = 10, add the multiplicand to AC.
    - Shift right the partial product and the multiplier (including Qn+1). This is an arithmetic shift right (ashr) operation which moves AC and QR to the right and leaves the sign bit in AC unchanged.
    - Decrement SC by 1.
  - The final product is obtained by concatenating AC and QR.

- For example, to multiply -5 and 3 in two's complement format, we have:

```
  -5 = 11111011
   3 = 00000011
```

- The algorithm works as follows:

```
AC    QR    Qn+1  SC  Operation
0000  0000  0     8   Initialize
0000  0000  0     7   Shift right
0000  0000  0     6   Shift right
0000  0000  0     5   Shift right
0000  0001  0     4   Shift right
0000  0000  1     3   Shift right
1111  1011  0     2   Subtract multiplicand, shift right
1111  1101  1     1   Shift right
1111  1110  1     0   Shift right
```

- The final product is 111111101110, which is -15 in two's complement format.