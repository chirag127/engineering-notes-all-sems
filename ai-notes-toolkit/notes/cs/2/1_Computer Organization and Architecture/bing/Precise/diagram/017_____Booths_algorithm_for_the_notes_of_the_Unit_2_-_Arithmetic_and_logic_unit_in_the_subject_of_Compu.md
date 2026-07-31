### Booth's Algorithm

Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in two's complement notation. The algorithm was invented by Andrew Donald Booth in 1950 while doing research on crystallography at Birkbeck College in Bloomsbury, London.

Booth's algorithm is of interest in the study of computer architecture.

#### Steps for Booth's Algorithm
1. Determine the number of bits, n, in the multiplicand and multiplier.
2. Append a 0 to the right of the least significant bit of the multiplier.
3. Initialize the product register to 0.
4. Repeat the following steps n times:
    1. If the two least significant bits of the multiplier are 01, subtract the multiplicand from the product register.
    2. If the two least significant bits of the multiplier are 10, add the multiplicand to the product register.
    3. Arithmetic shift right the product register and the multiplier by one bit.
5. The product is now in the product register.

#### Example
Let's consider the multiplication of two 4-bit numbers, 3 and -4, using Booth's algorithm.

1. The multiplicand is 3, which is 0011 in binary.
2. The multiplier is -4, which is 1100 in binary.
3. We append a 0 to the right of the least significant bit of the multiplier, giving us 11000.
4. We initialize the product register to 0, giving us 0000.
5. We repeat the following steps 4 times:
    1. The two least significant bits of the multiplier are 00, so we do nothing.
    2. We arithmetic shift right the product register and the multiplier by one bit, giving us 0000 and 01100.
    3. The two least significant bits of the multiplier are 00, so we do nothing.
    4. We arithmetic shift right the product register and the multiplier by one bit, giving us 0000 and 00110.
    5. The two least significant bits of the multiplier are 10, so we add the multiplicand, 0011, to the product register, giving us 0011.
    6. We arithmetic shift right the product register and the multiplier by one bit, giving us 0001 and 00011.
    7. The two least significant bits of the multiplier are 11, so we do nothing.
    8. We arithmetic shift right the product register and the multiplier by one bit, giving us 0000 and 00001.
6. The product is now in the product register, which is 0000 in binary, or 0 in decimal.

#### Conclusion
Booth's algorithm is an efficient way to multiply two signed binary numbers. It is of interest in the study of computer architecture, particularly in the design of arithmetic and logic units. It is important to understand the steps of the algorithm and be able to apply it to example problems.