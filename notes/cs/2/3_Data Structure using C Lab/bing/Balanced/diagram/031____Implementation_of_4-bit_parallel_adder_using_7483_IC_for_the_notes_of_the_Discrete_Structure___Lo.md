## Implementation of 4-bit parallel adder using 7483 IC

- A 4-bit parallel adder is a logic circuit that can perform the addition of two 4-bit binary numbers and produce a 4-bit sum and a carry output.
- A 7483 IC is a 16-pin integrated circuit that contains four interconnected full adders and a look-ahead carry circuit. It can be used to implement a 4-bit parallel adder with minimal external connections.
- The pin diagram of 7483 IC is shown below:

![7483 IC pin diagram](https://eees.in/wp-content/uploads/2021/10/7483-pin-diagram.png)

- The inputs of the 7483 IC are A3, A2, A1, A0 and B3, B2, B1, B0, which represent the two 4-bit numbers to be added. The inputs also include a carry-in (Cn) pin, which can be used to cascade multiple 7483 ICs for larger numbers.
- The outputs of the 7483 IC are S3, S2, S1, S0 and Cn+4, which represent the 4-bit sum and the carry-out of the addition. The outputs also include a mode control (M) pin, which can be used to select between binary and BCD addition modes.
- The truth table of the 7483 IC is shown below:

| A3 | A2 | A1 | A0 | B3 | B2 | B1 | B0 | Cn | M | S3 | S2 | S1 | S0 | Cn+4 |
|----|----|----|----|----|----|----|----|----|---|----|----|----|----|------|
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0 | 0  | 0  | 0  | 0  | 0    |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1 | 0  | 0  | 0  | 0  | 0    |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0 | 0  | 0  | 0  | 1  | 0    |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1 | 0  | 0  | 0  | 1  | 0    |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0 | 0  | 0  | 0  | 1  | 0    |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 1 | 0  | 0  | 0  | 1  | 0    |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 0 | 0  | 0  | 1  | 0  | 0    |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1 | 0  | 0  | 1  | 0  | 0    |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0 | 0  | 0  | 1  | 0  | 0    |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0