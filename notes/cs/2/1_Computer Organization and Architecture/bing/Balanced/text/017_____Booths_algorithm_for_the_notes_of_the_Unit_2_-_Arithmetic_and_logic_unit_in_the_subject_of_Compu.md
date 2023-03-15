### Booth's algorithm for the notes of the Unit 2 - Arithmetic and logic unit in the subject of Computer Organization and Architecture

- Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in 2's complement notation  .
- It is of interest in the study of computer architecture because it reduces the number of additions and subtractions required for the multiplication process  .
- It is based on the observation that strings of 0's in the multiplier require no addition but just shifting, and a string of 1's in the multiplier from bit weight 2^k to 2^m can be treated as 2^(m+1) - 2^k.
- The algorithm examines adjacent pairs of bits of the N-bit multiplier Y in signed 2's complement representation, including an implicit bit below the least significant bit, y-1 = 0.
- Depending on the value of the current bit and the previous bit, the algorithm performs one of the following operations on the partial product P and the multiplicand X  :
  - 00: No operation
  - 01: P = P + X
  - 10: P = P - X
  - 11: No operation
- After each operation, the partial product P is arithmetically right-shifted by one bit, so that the current bit and the previous bit of the multiplier are aligned with the least significant bit and the implicit bit of P   .
- The algorithm repeats this process N times, where N is the number of bits in the multiplier   .
- The final value of P is the product of X and Y   .
- An example of Booth's algorithm is shown below :

| Step | Operation | P | Q | A |
| --- | --- | --- | --- | --- |
| Initial values | | 0000 | 0101 | 0 |
| 1 | P = P - X | 1100 | 0101 | 0 |
| 2 | Right shift | 1110 | 0010 | 1 |
| 3 | P = P + X | 0011 | 0010 | 1 |
| 4 | Right shift | 0001 | 1001 | 0 |
| 5 | P = P - X | 0101 | 1001 | 0 |
| 6 | Right shift | 0010 | 1100 | 1 |
| 7 | P = P + X | 1011 | 1100 | 1 |
| 8 | Right shift | 1101 | 1110 | 0 |
| Final result | | 1101 | 1110 | 0 |

- The product is 11011110, which is equal to -34 in decimal. The multiplicand is 0101, which is equal to 5 in decimal. The multiplier is 1110, which is equal to -2 in decimal. Therefore, the product is correct as 5 * (-2) = -10.