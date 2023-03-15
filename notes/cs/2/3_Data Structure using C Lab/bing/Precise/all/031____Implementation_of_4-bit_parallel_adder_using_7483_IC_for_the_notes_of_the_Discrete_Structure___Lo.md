## Implementation of 4-bit parallel adder using 7483 IC for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

1. A 4-bit parallel adder is a digital circuit that can add two 4-bit binary numbers and produce a 5-bit sum.
2. The 7483 IC is a 4-bit binary full adder that can be used to implement a 4-bit parallel adder.
3. The 7483 IC has 16 pins, including 4 pins for each of the two 4-bit inputs (A and B), 4 pins for the 4-bit sum output (S), 1 pin for the carry-in input (C0), 1 pin for the carry-out output (C4), and 2 pins for power supply (Vcc and GND).
4. To implement a 4-bit parallel adder using a 7483 IC, the two 4-bit inputs (A and B) are connected to the corresponding input pins of the IC, the carry-in input (C0) is connected to either ground or a logic high voltage depending on whether there is a carry-in or not, and the 4-bit sum output (S) and the carry-out output (C4) are taken from the corresponding output pins of the IC.
5. The 7483 IC performs the addition operation by adding the two 4-bit inputs (A and B) and the carry-in (C0) bit-by-bit, starting from the least significant bit, and producing a 4-bit sum (S) and a carry-out (C4) bit.
6. The truth table for the 4-bit parallel adder using a 7483 IC is as follows:

| A3 | A2 | A1 | A0 | B3 | B2 | B1 | B0 | C0 | S3 | S2 | S1 | S0 | C4 |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 1  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 1  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 0  | 0  | 0  | 0  | 1  |
| ...| ...| ...| ...| ...| ...| ...| ...| ...| ...| ...| ...| ...| ...|
| 1  | 1  | 1  | 1  | 1  | 1  | 1  | 1  | 1  | 1  | 1  | 1  | 1  | 1  |

7. The 7483 IC can also be cascaded to implement an n-bit parallel adder, where n is a multiple of 4, by connecting the carry-out output (C4) of one IC to the carry-in input (C0) of the next IC.