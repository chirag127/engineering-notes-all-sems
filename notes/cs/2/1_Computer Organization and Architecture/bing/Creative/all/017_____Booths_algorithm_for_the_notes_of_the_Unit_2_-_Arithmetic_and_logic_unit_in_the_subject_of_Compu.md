# Booth's Algorithm

Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in 2's complement notation. It was invented by Andrew Donald Booth in 1950 while doing research on crystallography at Birkbeck College in London.

The algorithm is based on the following observations:

- A string of 0's in the multiplier requires no addition but just shifting.
- A string of 1's in the multiplier from bit weight 2^k to 2^m can be treated as 2^(m+1) - 2^k.
- A 0-to-1 transition in the multiplier at bit weight 2^k can be treated as -2^k.

The algorithm works as follows:

- Let X and Y be the multiplicand and multiplier of N bits each, and A, S, and P be N+1 bit registers.
- Initialize A and S to 0, and P to Y appended with a 0 bit.
- Initialize S to 2's complement of X, i.e., -X.
- Repeat the following steps N times:
  - If the rightmost two bits of P are 00 or 11, do an arithmetic right shift of P by 1 bit.
  - If the rightmost two bits of P are 01, do P = P + A and then an arithmetic right shift of P by 1 bit.
  - If the rightmost two bits of P are 10, do P = P + S and then an arithmetic right shift of P by 1 bit.
- After N iterations, the product is in P.

The following example illustrates the algorithm for multiplying 3 and -4 in binary:

- X = 0011, Y = 1100
- A = 00000, S = 11101, P = 11000
- Step 1: P = 01100 (right shift)
- Step 2: P = 10001 (P + S, right shift)
- Step 3: P = 11000 (right shift)
- Step 4: P = 01100 (right shift)
- Final product: P = 01100, which is -12 in decimal.