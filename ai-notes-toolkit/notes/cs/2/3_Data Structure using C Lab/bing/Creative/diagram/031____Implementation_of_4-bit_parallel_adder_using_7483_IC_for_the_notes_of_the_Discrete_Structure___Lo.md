## Implementation of 4-bit parallel adder using 7483 IC

- A 4-bit parallel adder is a logic circuit that can perform the addition of two 4-bit binary numbers and produce a 4-bit sum and a carry output.
- A 7483 IC is a 16-pin integrated circuit that contains four full adders with a look-ahead carry circuit. It can be used to implement a 4-bit parallel adder by connecting the inputs and outputs as shown in the diagram below.

![Diagram of 4-bit parallel adder using 7483 IC](https://eees.in/wp-content/uploads/2021/10/4-bit-adder-using-7483.png)

- The inputs A3, A2, A1, A0 and B3, B2, B1, B0 are the two 4-bit numbers to be added. The outputs S3, S2, S1, S0 are the 4-bit sum and Cout is the carry output. The input Cin is the carry input, which can be used to cascade multiple 7483 ICs for larger bit addition.
- The truth table for the 4-bit parallel adder using 7483 IC is given below.

| A3 | A2 | A1 | A0 | B3 | B2 | B1 | B0 | Cin | Cout | S3 | S2 | S1 | S0 |
|----|----|----|----|----|----|----|----|-----|------|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0   | 0    | 0  | 0  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1   | 0    | 0  | 0  | 0  | 1  |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0   | 0    | 0  | 0  | 0  | 1  |
| 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1   | 0    | 0  | 0  | 1  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0   | 0    | 0  | 0  | 1  | 0  |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 1   | 0    | 0  | 0  | 1  | 1  |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 0   | 0    | 0  | 0  | 1  | 1  |
| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 1  | 1   | 0    | 0  | 1  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0   | 0    | 0  | 1  | 0  | 0  |
| 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 1   | 0    | 0  | 1  | 0  | 1  |
| 0  | 0  | 0  | 0  | 0  | 1  | 0  | 1  | 0   | 0    | 0  | 1  |