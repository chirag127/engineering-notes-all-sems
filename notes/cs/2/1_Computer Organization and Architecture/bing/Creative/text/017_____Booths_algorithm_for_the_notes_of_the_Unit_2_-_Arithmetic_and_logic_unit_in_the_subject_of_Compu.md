### Booth's algorithm

Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in two's complement notation. The algorithm was invented by Andrew Donald Booth in 1950 while doing research on crystallography at Birkbeck College in Bloomsbury, London.

The main idea of Booth's algorithm is to reduce the number of additions and subtractions required by examining the bits of the multiplier and performing different operations based on the bit patterns. The algorithm can be summarized as follows:

- Let X and Y be the multiplicand and the multiplier, respectively, of N bits each.
- Let A be an accumulator of 2N bits, initially zero.
- Let Q be a register of N+1 bits, initially holding the value of Y with an extra 0 bit at the rightmost position. This extra bit is called the Q-1 bit.
- Let count be a register of log2(N+1) bits, initially holding the value of N+1.
- Repeat the following steps until count becomes zero:
  - If the rightmost two bits of Q are 01, then add X to A and ignore the overflow.
  - If the rightmost two bits of Q are 10, then subtract X from A and ignore the overflow.
  - If the rightmost two bits of Q are 00 or 11, then do nothing.
  - Arithmetic right shift the combined value of A and Q by one bit, filling the leftmost bit of A with the previous sign bit of A, and filling the Q-1 bit with the previous rightmost bit of Q.
  - Decrement count by one.
- The final product is obtained by discarding the Q-1 bit and taking the remaining 2N bits of A and Q.

The following example illustrates the algorithm for multiplying 3 and -4 in binary:

- X = 0011, Y = 1100, A = 00000000, Q = 11000, count = 5
- Step 1: Q = 10, subtract X from A, A = 11111101, right shift A and Q, A = 11111111, Q = 11100, count = 4
- Step 2: Q = 00, do nothing, right shift A and Q, A = 11111111, Q = 11110, count = 3
- Step 3: Q = 10, subtract X from A, A = 11111100, right shift A and Q, A = 11111111, Q = 01111, count = 2
- Step 4: Q = 11, do nothing, right shift A and Q, A = 11111111, Q = 10111, count = 1
- Step 5: Q = 11, do nothing, right shift A and Q, A = 11111111, Q = 11011, count = 0
- The final product is A Q = 1111111111011, which is -12 in decimal.

Booth's algorithm is of interest in the study of computer architecture, as it can improve the performance of multiplication operations in hardware. However, it has some drawbacks, such as requiring extra hardware for shifting and adding/subtracting, and being sensitive to the distribution of 0s and 1s in the multiplier. There are also some variations and extensions of Booth's algorithm, such as Booth's recoding, modified Booth's algorithm, and radix-4 Booth's algorithm, that aim to overcome some of these limitations.