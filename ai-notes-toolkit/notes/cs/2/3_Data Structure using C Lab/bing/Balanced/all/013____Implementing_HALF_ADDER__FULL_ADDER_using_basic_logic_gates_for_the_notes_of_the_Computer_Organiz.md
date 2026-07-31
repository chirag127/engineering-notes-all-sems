## Implementing HALF ADDER, FULL ADDER using basic logic gates

- A half adder is a digital logic circuit that performs binary addition of two single-bit binary numbers.
- A full adder is a digital logic circuit that performs binary addition of three single-bit binary numbers, two operands and a carry-in.
- Both half and full adders are combinational logic circuits, and they both differ from each other in the aspect of input processing.
- Any combinational circuit is devoid of memory elements- they only comprise the logic gates.

### Half Adder

- The half adder circuit has two inputs: A and B, which add two input digits and generates a carry and a sum.
- The output obtained from the EX-OR gate is the sum of the two numbers while that obtained by AND gate is the carry.
- The half adder circuit can be implemented using basic logic gates such as XOR and AND.
- The truth table and the logic diagram of a half adder are shown below:

| A | B | SUM | CARRY |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

![Half Adder Logic Diagram](https://www.circuits-diy.com/wp-content/uploads/2020/02/Half-Adder-Circuit-Diagram.png)

### Full Adder

- The full adder circuit has three inputs: A, B and C<sub>in</sub>, which add three input digits and generates a carry and a sum.
- The output obtained from the EX-OR gate is the sum of the three numbers while that obtained by OR gate is the carry.
- The full adder circuit can be implemented using two half adders and an OR gate.
- The truth table and the logic diagram of a full adder are shown below:

| A | B | C<sub>in</sub> | SUM | C<sub>out</sub> |
|---|---|----------------|-----|-----------------|
| 0 | 0 |      0         |  0  |       0         |
| 0 | 0 |      1         |  1  |       0         |
| 0 | 1 |      0         |  1  |       0         |
| 0 | 1 |      1         |  0  |       1         |
| 1 | 0 |      0         |  1  |       0         |
| 1 | 0 |      1         |  0  |       1         |
| 1 | 1 |      0         |  0  |       1         |
| 1 | 1 |      1         |  1  |       1         |

![Full Adder Logic Diagram](https://www.geeksforgeeks.org/wp-content/uploads/Full-Adder-1.png)