# Booth's algorithm

Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in 2's complement notation. It was invented by Andrew Donald Booth in 1950 while doing research on crystallography at Birkbeck College in London.

## Steps of Booth's algorithm

1. Let X and Y be the multiplicand and multiplier of N bits each, and A, S and P be registers of size 2N+1 bits each. Initialize A and S to 0 and P to Y with an extra 0 bit at the right end.
2. For each bit position from right to left in P, examine the rightmost two bits of P. If they are 00 or 11, do nothing. If they are 01, add A to P and store the result in P. If they are 10, add S to P and store the result in P.
3. After each addition or no-operation, arithmetically right shift P by one bit, discarding the rightmost bit and duplicating the sign bit.
4. Repeat steps 2 and 3 for N times. The final value of P is the product of X and Y.

## Example of Booth's algorithm

Let X = 3 and Y = -4, which are 011 and 100 in 2's complement notation respectively. We want to compute X*Y using Booth's algorithm.

1. Initialize A, S and P as follows:

| A | S | P |
|---|---|---|
| 0000 | 1110 | 1000 |

2. Examine the rightmost two bits of P, which are 00. Do nothing and right shift P by one bit.

| A | S | P |
|---|---|---|
| 0000 | 1110 | 0100 |

3. Examine the rightmost two bits of P, which are 00. Do nothing and right shift P by one bit.

| A | S | P |
|---|---|---|
| 0000 | 1110 | 0010 |

4. Examine the rightmost two bits of P, which are 10. Add S to P and store the result in P. Right shift P by one bit.

| A | S | P |
|---|---|---|
| 0000 | 1110 | 0001 |

5. Examine the rightmost two bits of P, which are 01. Add A to P and store the result in P. Right shift P by one bit.

| A | S | P |
|---|---|---|
| 0000 | 1110 | 1000 |

6. Examine the rightmost two bits of P, which are 00. Do nothing and right shift P by one bit.

| A | S | P |
|---|---|---|
| 0000 | 1110 | 1100 |

7. Examine the rightmost two bits of P, which are 00. Do nothing and right shift P by one bit.

| A | S | P |
|---|---|---|
| 0000 | 1110 | 1110 |

8. Examine the rightmost two bits of P, which are 10. Add S to P and store the result in P. Right shift P by one bit.

| A | S | P |
|---|---|---|
| 0000 | 1110 | 0111 |

9. The final value of P is 0111, which is -12 in 2's complement notation. This is the correct product of 3 and -4.

## Advantages and disadvantages of Booth's algorithm

- Booth's algorithm reduces the number of additions and subtractions required for multiplying two signed binary numbers, especially when there are long strings of 0s or 1s in the multiplier.
- Booth's algorithm also simplifies the hardware design of the multiplier circuit, as it only requires one adder-subtractor unit and one right shifter unit.
- However, Booth's algorithm has some drawbacks, such as the need for extra sign extension bits and the possibility of overflow or underflow during the additions or subtractions.