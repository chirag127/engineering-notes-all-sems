### Booth's algorithm

Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in 2's complement notation. It was invented by Andrew Donald Booth in 1950 while doing research on crystallography at Birkbeck College in London.

The main features of Booth's algorithm are:

- It examines adjacent pairs of bits of the multiplier and performs different operations based on the bit pair.
- It reduces the number of partial products by half, compared to the conventional method of shifting and adding for each bit of the multiplier.
- It handles both positive and negative numbers using 2's complement representation.
- It can be implemented using a simple circuit consisting of an adder, a shifter and a control unit.

The steps of Booth's algorithm are:

1. Let the multiplicand be M and the multiplier be Q. Both are n-bit signed numbers in 2's complement notation. Initialize an n-bit accumulator A to 0 and an extra bit Q-1 to 0.
2. For i from 0 to n-1, do the following:
   - If the bit pair Q[i]Q-1 is 01, then add M to A and store the result in A.
   - If the bit pair Q[i]Q-1 is 10, then subtract M from A and store the result in A.
   - If the bit pair Q[i]Q-1 is 00 or 11, then do nothing.
   - Right shift the combined value of AQ by one bit, filling the most significant bit of A with its previous value. This is an arithmetic shift.
   - Set Q-1 to the least significant bit of Q.
3. The final product is obtained by concatenating A and Q.

The following diagram illustrates the Booth's algorithm for an example of multiplying 3 and -4 in binary.

![Booth's algorithm example](https://i.imgur.com/6Qw1Q8L.png)

The algorithm starts with A = 0000, Q = 1100 and Q-1 = 0. The bit pair Q[0]Q-1 is 00, so no operation is performed and AQ is right shifted. The bit pair Q[1]Q-1 is 10, so M is subtracted from A and AQ is right shifted. The bit pair Q[2]Q-1 is 11, so no operation is performed and AQ is right shifted. The bit pair Q[3]Q-1 is 01, so M is added to A and AQ is right shifted. The final product is -12 in binary, which is 11110100.

Booth's algorithm is of interest in the study of computer architecture, as it can improve the speed and efficiency of binary multiplication. It can also be extended to handle larger operands and different number representations.