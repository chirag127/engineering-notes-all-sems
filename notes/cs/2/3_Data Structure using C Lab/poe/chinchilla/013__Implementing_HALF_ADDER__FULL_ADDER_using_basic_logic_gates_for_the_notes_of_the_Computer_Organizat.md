## Implementing HALF ADDER, FULL ADDER using basic logic gates

In this lab, we will learn how to implement a Half Adder and a Full Adder using basic logic gates. These circuits are fundamental building blocks in digital electronics and are used extensively in computer systems.

### Half Adder

A Half Adder is a combinational logic circuit that can add two single-bit binary numbers and produce a sum bit and a carry bit as outputs. The truth table for a Half Adder is given below:

| A | B | Sum | Carry |
|---|---|-----|-------|
| 0 | 0 |  0  |   0    |
| 0 | 1 |  1  |   0    |
| 1 | 0 |  1  |   0    |
| 1 | 1 |  0  |   1    |

To implement a Half Adder, we need two basic logic gates: XOR gate and AND gate. The XOR gate produces the sum output, and the AND gate produces the carry output. The circuit diagram for a Half Adder is shown below:

![Half Adder Circuit Diagram](half_adder.png)

### Full Adder

A Full Adder is a combinational logic circuit that can add three single-bit binary numbers and produce a sum bit and a carry bit as outputs. The three inputs are two binary digits to be added and a carry input from a previous addition. The truth table for a Full Adder is given below:

| A | B | C<sub>in</sub> | Sum | C<sub>out</sub> |
|---|---|-------|-----|-------|
| 0 | 0 |   0   |  0  |   0    |
| 0 | 0 |   1   |  1  |   0    |
| 0 | 1 |   0   |  1  |   0    |
| 0 | 1 |   1   |  0  |   1    |
| 1 | 0 |   0   |  1  |   0    |
| 1 | 0 |   1   |  0  |   1    |
| 1 | 1 |   0   |  0  |   1    |
| 1 | 1 |   1   |  1  |   1    |

To implement a Full Adder, we need three basic logic gates: XOR gate, AND gate, and OR gate. The XOR gate produces the sum output, the AND gate produces a partial carry output, and the OR gate produces the final carry output. The circuit diagram for a Full Adder is shown below:

![Full Adder Circuit Diagram](full_adder.png)

### Conclusion

In this lab, we learned how to implement a Half Adder and a Full Adder using basic logic gates. These circuits are fundamental building blocks in digital electronics and are used extensively in computer systems. Understanding these circuits is essential for anyone interested in computer engineering or computer science.