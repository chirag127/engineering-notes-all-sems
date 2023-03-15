# Implementation of 4-bit parallel adder using 7483 IC

- A 4-bit parallel adder is a logic circuit that can perform the addition of two 4-bit binary numbers and produce a 4-bit sum and a carry output.
- A 7483 IC is a 16-pin integrated circuit that contains four interconnected full adders and a look-ahead carry circuit. It can be used to implement a 4-bit parallel adder with minimal external connections.
- The pin diagram of 7483 IC is shown below:

![Pin diagram of 7483 IC](https://eees.in/wp-content/uploads/2021/10/7483-pin-diagram.png)

- The inputs of the 7483 IC are A3, A2, A1, A0 and B3, B2, B1, B0, which represent the two 4-bit numbers to be added. The outputs are S3, S2, S1, S0, which represent the 4-bit sum, and C4, which represents the carry output.
- The 7483 IC also has a carry input C0, which can be used to cascade multiple 7483 ICs to perform addition of larger numbers. For example, to add two 8-bit numbers, two 7483 ICs can be connected as shown below:

![8-bit parallel adder using two 7483 ICs](https://eees.in/wp-content/uploads/2021/10/8-bit-adder-using-7483.png)

- The 7483 IC can also be used to perform subtraction of two 4-bit numbers by using the 2's complement method. To do this, the B inputs are complemented and the C0 input is set to 1. The S outputs will then represent the 4-bit difference and the C4 output will indicate the borrow. For example, to subtract 0101 from 1001, the inputs and outputs of the 7483 IC are as follows:

| A3 | A2 | A1 | A0 | B3 | B2 | B1 | B0 | C0 | S3 | S2 | S1 | S0 | C4 |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| 1  | 0  | 0  | 1  | 1  | 0  | 1  | 0  | 1  | 0  | 1  | 1  | 0  | 0  |

- The 4-bit parallel adder using 7483 IC can be implemented on a breadboard or a printed circuit board by connecting the inputs and outputs to the appropriate pins of the IC and providing a 5V power supply to the Vcc and GND pins. The 7483 IC belongs to the TTL family and has a typical propagation delay of 18 ns.