### Booth's Algorithm

Booth's algorithm is a multiplication algorithm used to multiply two signed binary numbers. It was invented by Andrew Donald Booth in 1951. The algorithm is commonly used in computer hardware for multiplication.

#### Steps for Booth's algorithm

1. The two binary numbers, A and B, are written in binary format. The number of bits in A and B should be equal.

2. Extend the sign bit of A to the left by one bit. This is done to handle negative numbers.

3. Initialize the product (P) to 0.

4. Repeat the following steps until all bits in B are processed:

    a. Check the last two bits of B. If they are 01, add A to P. If they are 10, subtract A from P.

    b. Shift A and P one bit to the right.

    c. Shift B one bit to the right.

5. Ignore the last bit in P. If the sign bit of A and B are the same, the result is positive. Otherwise, it is negative.

#### Example

Let A = -5 and B = 6. The binary representation of A and B are 1011 and 0110 respectively.

1. Extend the sign bit of A to the left. The binary representation of A becomes 11011.

2. Initialize P to 0.

3. Process each bit in B:

    a. The last two bits of B are 10. Subtract A from P. P becomes 00000.

    b. Shift A and P one bit to the right. A becomes 11101 and P becomes 00000.

    c. Shift B one bit to the right. B becomes 0011.

    a. The last two bits of B are 11. Add A to P. P becomes 11011.

    b. Shift A and P one bit to the right. A becomes 11110 and P becomes 01101.

    c. Shift B one bit to the right. B becomes 0001.

4. Ignore the last bit in P, which is 1. Since the sign bits of A and B are different, the result is negative. The binary representation of -30 is 111000.

#### Advantages of Booth's algorithm

- Booth's algorithm is faster than conventional multiplication algorithm.

- It requires less hardware for implementation.

- It can handle negative numbers without using two's complement.

#### Limitations of Booth's algorithm

- Booth's algorithm can only be used for binary numbers.

- It is not efficient for small number multiplication.

- It requires extra hardware for the implementation of the algorithm.