## Implementing HALF ADDER, FULL ADDER using basic logic gates

- A half adder is a digital logic circuit that performs binary addition of two single-bit binary numbers.
- A full adder is a digital logic circuit that performs binary addition of three single-bit binary numbers, including a carry-in bit.
- Both half and full adders are combinational logic circuits, and they both differ from each other in the aspect of input processing.
- Any combinational circuit is devoid of memory elements- they only comprise the logic gates.

### Half Adder

- The half adder circuit has two inputs, A and B, and two outputs, SUM and CARRY.
- The SUM output is the least significant bit (LSB) of the result, while the CARRY output is the most significant bit (MSB) of the result, indicating whether there was a carry-over from the addition.
- The input variables of a half adder are called the augend and addend bits.
- The half adder circuit can be built using XOR gate and AND gate.
- The output obtained from the XOR gate is the sum of the two numbers while that obtained by AND gate is the carry.
- The truth table and the logic diagram of a half adder are shown below:

| A | B | SUM | CARRY |
|---|---|-----|-------|
| 0 | 0 |  0  |   0   |
| 0 | 1 |  1  |   0   |
| 1 | 0 |  1  |   0   |
| 1 | 1 |  0  |   1   |

```
    A ---|>o---|       |--- SUM
         |  XOR  |---o-|
    B ---|>o---|       |
                 |  AND  |--- CARRY
    A ---|>o---|       |
         |      |---o-|
    B ---|>o---|
```

### Full Adder

- The full adder circuit has three inputs, A, B and CIN, and two outputs, SUM and COUT.
- The SUM output is the LSB of the result, while the COUT output is the MSB of the result, indicating whether there was a carry-over from the addition.
- The input variables of a full adder are called the augend, addend and carry-in bits.
- The full adder circuit can be built using two half adders and an OR gate.
- The output obtained from the first half adder is the partial sum of A and B, while the output obtained from the second half adder is the final sum of A, B and CIN.
- The output obtained from the OR gate is the final carry of the addition.
- The truth table and the logic diagram of a full adder are shown below:

| A | B | CIN | SUM | COUT |
|---|---|-----|-----|------|
| 0 | 0 |  0  |  0  |   0  |
| 0 | 0 |  1  |  1  |   0  |
| 0 | 1 |  0  |  1  |   0  |
| 0 | 1 |  1  |  0  |   1  |
| 1 | 0 |  0  |  1  |   0  |
| 1 | 0 |  1  |  0  |   1  |
| 1 | 1 |  0  |  0  |   1  |
| 1 | 1 |  1  |  1  |   1  |

```
    A ---|>o---|       |---o-|       |--- SUM
         |  XOR  |---o-|  XOR  |---o-|
    B ---|>o---|       |       |     |
                 |  AND  |---o-|  OR  |--- COUT
    A ---|>o---|       |       |     |
         |      |---o-|       |---o-|
    B ---