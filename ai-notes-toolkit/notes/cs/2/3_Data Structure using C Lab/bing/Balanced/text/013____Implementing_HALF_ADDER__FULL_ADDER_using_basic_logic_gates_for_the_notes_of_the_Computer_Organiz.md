## Implementing HALF ADDER, FULL ADDER using basic logic gates

- A half adder is a digital logic circuit that performs binary addition of two single-bit binary numbers. It has two inputs, A and B, and two outputs, SUM and CARRY. The SUM output is the least significant bit (LSB) of the result, while the CARRY output is the most significant bit (MSB) of the result, indicating whether there was a carry-over from the addition.
- A full adder is a digital logic circuit that performs binary addition of three single-bit binary numbers: two inputs, A and B, and a carry-in, CIN. It has two outputs, SUM and CARRY. The SUM output is the LSB of the result, while the CARRY output is the MSB of the result, indicating whether there was a carry-over from the addition or from the previous stage.
- A half adder can be implemented using an XOR gate and an AND gate. The XOR gate produces the SUM output, while the AND gate produces the CARRY output. The truth table and the logic diagram of a half adder are shown below:

| A | B | SUM | CARRY |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

![Half adder logic diagram](https://www.circuits-diy.com/wp-content/uploads/2020/02/Half-Adder-Circuit-Diagram.png)

- A full adder can be implemented using two half adders and an OR gate. The first half adder adds A and B to produce a partial SUM and a partial CARRY. The second half adder adds the partial SUM and CIN to produce the final SUM and a second partial CARRY. The OR gate combines the two partial CARRYs to produce the final CARRY. The truth table and the logic diagram of a full adder are shown below:

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

![Full adder logic diagram](https://www.geeksforgeeks.org/wp-content/uploads/Full-Adder.png)

- By using half adders and full adders, larger binary numbers can be added by connecting them in a ripple-carry fashion. The CARRY output of one stage is connected to the CIN input of the next stage. The LSBs of the numbers are added by a half adder, while the rest of the bits are added by full adders. The logic diagram of a 4-bit ripple-carry adder is shown below:

![4-bit ripple-carry adder logic diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/4-bit_ripple_carry_adder.svg/1200px-4-bit_ripple_carry_adder.svg.png)