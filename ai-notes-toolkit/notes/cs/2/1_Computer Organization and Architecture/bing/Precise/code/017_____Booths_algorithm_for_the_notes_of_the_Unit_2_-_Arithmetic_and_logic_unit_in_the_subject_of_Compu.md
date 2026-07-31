### Booth's Algorithm

Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in two's complement notation. The algorithm was invented by Andrew Donald Booth in 1950 while doing research on crystallography at Birkbeck College in Bloomsbury, London.

Booth's algorithm is of interest in the study of computer architecture.

#### Steps for Booth's Algorithm

1. Determine the number of bits, n, needed to represent the multiplicand and multiplier.
2. Append a 0 to the right of the least significant bit of the multiplier.
3. Initialize the product register to 0.
4. Repeat the following steps n times:
    1. If the two least significant bits of the multiplier are 01, subtract the multiplicand from the product register.
    2. If the two least significant bits of the multiplier are 10, add the multiplicand to the product register.
    3. Arithmetic shift the product register and the multiplier one bit to the right.
5. The product is now in the product register.

#### Example

Let's take an example of multiplying -3 and -4 using Booth's algorithm.

1. The multiplicand is -3, which is 1101 in binary.
2. The multiplier is -4, which is 1100 in binary.
3. We append a 0 to the right of the least significant bit of the multiplier, so the multiplier is now 11000.
4. We initialize the product register to 0, so the product register is now 0000.
5. We repeat the following steps 4 times:
    1. The two least significant bits of the multiplier are 00, so we do nothing.
    2. We arithmetic shift the product register and the multiplier one bit to the right. The product register is now 0000 and the multiplier is now 01100.
    3. The two least significant bits of the multiplier are 00, so we do nothing.
    4. We arithmetic shift the product register and the multiplier one bit to the right. The product register is now 0000 and the multiplier is now 00110.
    5. The two least significant bits of the multiplier are 10, so we add the multiplicand to the product register. The product register is now 1101.
    6. We arithmetic shift the product register and the multiplier one bit to the right. The product register is now 1110 and the multiplier is now 00011.
    7. The two least significant bits of the multiplier are 11, so we do nothing.
    8. We arithmetic shift the product register and the multiplier one bit to the right. The product register is now 1111 and the multiplier is now 00001.
6. The product is now in the product register, which is 1111 in binary, or 15 in decimal.

Therefore, the product of -3 and -4 using Booth's algorithm is 15.