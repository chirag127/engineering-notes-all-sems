# Implementation of 4-bit parallel adder using 7483 IC

- A 4-bit parallel adder is a logic circuit that can perform the addition of two 4-bit binary numbers and produce a 4-bit sum and a carry output.
- A 7483 IC is a 16-pin integrated circuit that contains four full adders with a look-ahead carry circuit. It can be used to implement a 4-bit parallel adder by connecting the inputs and outputs as shown below :

![7483 IC pin diagram](https://eees.in/wp-content/uploads/2021/10/7483-pin-diagram.png)

- The inputs A3, A2, A1, A0 and B3, B2, B1, B0 are the two 4-bit numbers to be added. The outputs S3, S2, S1, S0 are the 4-bit sum and Cout is the carry output. The inputs Cin and GND are connected to ground (logic 0) and the input Vcc is connected to a 5V power supply.
- The truth table for the 4-bit parallel adder using 7483 IC is given below:

![7483 IC truth table](https://eees.in/wp-content/uploads/2021/10/7483-truth-table.png)

- The logic expression for the outputs are:

S0 = A0 ⊕ B0 ⊕ Cin

S1 = A1 ⊕ B1 ⊕ C1

S2 = A2 ⊕ B2 ⊕ C2

S3 = A3 ⊕ B3 ⊕ C3

Cout = G3 + P3G2 + P3P2G1 + P3P2P1C1

where C1, C2, C3 are the internal carry outputs and G1, G2, G3 and P1, P2, P3 are the generate and propagate signals of the full adders, respectively.

- The schematic diagram for the 4-bit parallel adder using 7483 IC is shown below:

![7483 IC schematic diagram](https://i.ytimg.com/vi/RCXBG-ldt8k/maxresdefault.jpg)

- The 7483 IC can also be used to perform subtraction of two 4-bit numbers by using the 2's complement method. This can be done by connecting the inputs A3, A2, A1, A0 to the minuend, the inputs B3, B2, B1, B0 to the 2's complement of the subtrahend, and the input Cin to logic 1. The outputs S3, S2, S1, S0 will give the 2's complement of the difference and Cout will indicate the borrow output.