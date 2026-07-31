# Booth's Algorithm

Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in two's complement notation. It was invented by Andrew Donald Booth in 1950 while doing research on crystallography at Birkbeck College in London.

The main features of Booth's algorithm are:

- It examines adjacent pairs of bits of the multiplier and performs different operations based on the bit pair.
- It reduces the number of additions and subtractions required for multiplication, compared to the conventional method of shifting and adding.
- It can handle both positive and negative operands, as well as overflow and underflow conditions.

The steps of Booth's algorithm are:

1. Initialize the accumulator (A) and the quotient (Q) registers to zero. The A register has the same number of bits as the multiplicand (M), and the Q register has the same number of bits as the multiplier (Y). Also, initialize a single-bit register (Q-1) to zero. This register holds the previous bit of the multiplier.
2. Perform a right arithmetic shift on the combined register AQ and Q-1. This means that the sign bit of A is copied to the leftmost bit of Q, and the rightmost bit of Q is copied to Q-1. The rightmost bit of A is discarded.
3. Examine the two rightmost bits of AQ and Q-1. Depending on the bit pair, perform one of the following operations:
    - If the bit pair is 00 or 11, do nothing.
    - If the bit pair is 01, add the multiplicand M to the accumulator A and store the result in A.
    - If the bit pair is 10, subtract the multiplicand M from the accumulator A and store the result in A.
4. Repeat steps 2 and 3 for n times, where n is the number of bits in the multiplier Y.
5. The final product is obtained by concatenating the accumulator A and the quotient Q. If the product is negative, it is in two's complement form.

The following example illustrates the Booth's algorithm for multiplying 3 and -4 in binary:

| Step | A  | Q  | Q-1 | Operation |
| ---- | -- | -- | --- | --------- |
| 0    | 0  | 0011 | 0   | Initial values |
| 1    | 0  | 0001 | 1   | Right shift |
| 2    | 1100 | 0001 | 1   | A = A - M |
| 3    | 1110 | 0000 | 1   | Right shift |
| 4    | 1110 | 0000 | 1   | Do nothing |
| 5    | 1111 | 0000 | 0   | Right shift |
| 6    | 0011 | 1000 | 0   | A = A + M |
| 7    | 0001 | 1100 | 0   | Right shift |
| 8    | 0001 | 1100 | 0   | Do nothing |
| 9    | 0000 | 1110 | 0   | Right shift |
| 10   | 0000 | 1110 | 0   | Do nothing |
| 11   | 0000 | 0111 | 0   | Right shift |
| 12   | 0000 | 0111 | 0   | Do nothing |

The final product is 000001110000, which is -12 in decimal. This is the correct answer, since 3 x -4 = -12.