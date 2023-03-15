### Booth's algorithm

Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in two's complement notation. The algorithm was invented by Andrew Donald Booth in 1950 while doing research on crystallography at Birkbeck College in Bloomsbury, London.

The main idea of Booth's algorithm is to reduce the number of additions and subtractions required by examining the bits of the multiplier and performing different operations based on the bit patterns. The algorithm can be summarized as follows:

- Let X and Y be the multiplicand and the multiplier, respectively, of N bits each.
- Let A be an accumulator of 2N bits, initially set to 0.
- Let Q be a register of N+1 bits, initially set to Y with an extra 0 bit at the rightmost position. This extra bit is called Q-1 and it is used to keep track of the previous bit of the multiplier.
- Let count be a register of log2(N+1) bits, initially set to N+1.
- Repeat the following steps until count becomes 0:
  - If Q-1 is 0 and the rightmost bit of Q is 1, then subtract X from A and shift AQ right by 1 bit. This is called a negative operation.
  - If Q-1 is 1 and the rightmost bit of Q is 0, then add X to A and shift AQ right by 1 bit. This is called a positive operation.
  - If Q-1 and the rightmost bit of Q are both 0 or both 1, then do not change A and shift AQ right by 1 bit. This is called a skip operation.
  - Decrement count by 1.
- The final product is stored in AQ.

The algorithm works by exploiting the fact that a string of 0s in the multiplier does not require any addition, but only shifting, and a string of 1s in the multiplier from bit weight 2^k to 2^m can be treated as 2^(m+1) - 2^k. For example, if the multiplier has a bit pattern of 0111, then it can be replaced by 1000 - 0001, which means adding the multiplicand shifted left by 3 bits and subtracting the multiplicand shifted left by 0 bits.

The following example illustrates the algorithm for multiplying 3 (0011) and -4 (1100) using 4 bits:

| Step | A    | Q    | Q-1 | Operation |
| ---- | ---- | ---- | --- | --------- |
| 0    | 0000 | 1100 | 0   | Initial   |
| 1    | 0000 | 0110 | 0   | Skip      |
| 2    | 0000 | 0011 | 0   | Skip      |
| 3    | 1101 | 0001 | 1   | Negative  |
| 4    | 1110 | 1000 | 1   | Skip      |
| 5    | 1111 | 0100 | 0   | Positive  |

The final product is -12 (11110100), which is correct.

: Booth's multiplication algorithm - Wikipedia