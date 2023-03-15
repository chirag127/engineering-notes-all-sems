## Implementing HALF ADDER, FULL ADDER using basic logic gates

- A half adder is a digital logic circuit that performs binary addition of two single-bit binary numbers.
- A full adder is a digital logic circuit that performs binary addition of three single-bit binary numbers, including a carry-in bit.
- Both half and full adders are combinational logic circuits, and they both differ from each other in the aspect of input processing.
- Any combinational circuit is devoid of memory elements- they only comprise the logic gates.

### Half Adder

- The half adder circuit has two inputs, A and B, and two outputs, SUM and CARRY.
- The SUM output is the least significant bit (LSB) of the result, while the CARRY output is the most significant bit (MSB) of the result, indicating whether there was a carry-over from the addition.
- The input variables of a half adder are called the augend and addend bits.
- The half adder circuit can be implemented using XOR gate and AND gate .
- The truth table and logic diagram of a half adder are shown below:

| A | B | SUM | CARRY |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

![Half Adder Logic Diagram](https://www.circuits-diy.com/wp-content/uploads/2020/02/Half-Adder-Circuit-Diagram.png)

### Full Adder

- The full adder circuit has three inputs, A, B and CIN, and two outputs, SUM and CARRY.
- The CIN input is the carry-in bit from the previous stage of addition, while the CARRY output is the carry-out bit to the next stage of addition.
- The full adder circuit can be implemented using two half adders and an OR gate .
- The truth table and logic diagram of a full adder are shown below:

| A | B | CIN | SUM | CARRY |
|---|---|-----|-----|-------|
| 0 | 0 |  0  |  0  |   0   |
| 0 | 0 |  1  |  1  |   0   |
| 0 | 1 |  0  |  1  |   0   |
| 0 | 1 |  1  |  0  |   1   |
| 1 | 0 |  0  |  1  |   0   |
| 1 | 0 |  1  |  0  |   1   |
| 1 | 1 |  0  |  0  |   1   |
| 1 | 1 |  1  |  1  |   1   |

![Full Adder Logic Diagram](https://www.geeksforgeeks.org/wp-content/uploads/Full-Adder.png)