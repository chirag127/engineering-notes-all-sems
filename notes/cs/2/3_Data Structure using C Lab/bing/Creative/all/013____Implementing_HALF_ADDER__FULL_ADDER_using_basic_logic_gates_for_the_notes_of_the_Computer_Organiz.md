# Implementing HALF ADDER, FULL ADDER using basic logic gates

- A half adder is a combinational logic circuit that performs the addition of two bits and produces a sum and a carry output.
- A full adder is a combinational logic circuit that performs the addition of three bits and produces a sum and a carry output. The third bit is the carry input from the previous stage of addition.
- A half adder can be implemented using an XOR gate and an AND gate. The XOR gate produces the sum output and the AND gate produces the carry output.
- A full adder can be implemented using two half adders and an OR gate. The first half adder takes the two input bits and produces a partial sum and a carry. The second half adder takes the partial sum and the carry input and produces the final sum and a carry. The OR gate combines the two carry outputs and produces the final carry output.
- The following diagram shows the logic circuit of a half adder:

![half adder](https://media.geeksforgeeks.org/wp-content/uploads/20191022170829/half-adder.jpg)

- The following diagram shows the logic circuit of a full adder:

![full adder](https://media.geeksforgeeks.org/wp-content/uploads/20191022170829/full-adder.jpg)

- The following table shows the truth table of a half adder:

| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

- The following table shows the truth table of a full adder:

| A | B | Carry in | Sum | Carry out |
|---|---|----------|-----|-----------|
| 0 | 0 |    0     |  0  |     0     |
| 0 | 0 |    1     |  1  |     0     |
| 0 | 1 |    0     |  1  |     0     |
| 0 | 1 |    1     |  0  |     1     |
| 1 | 0 |    0     |  1  |     0     |
| 1 | 0 |    1     |  0  |     1     |
| 1 | 1 |    0     |  0  |     1     |
| 1 | 1 |    1     |  1  |     1     |

- Half adders and full adders are the basic building blocks of arithmetic logic units that perform arithmetic operations on binary numbers.
- Half adders and full adders can be combined to form n-bit adders that can add two n-bit binary numbers. For example, a 2-bit full adder can be constructed by connecting two full adders in series as shown below:

![2-bit full adder](https://www.theengineeringprojects.com/wp-content/uploads/2021/01/2-Bit-Full-Adder-using-Logic-Gates-in-Proteus-1.png)

- The applications of half adders and full adders include digital calculators, digital signal processors, microprocessors, data encryption and decryption, error detection and correction, etc.