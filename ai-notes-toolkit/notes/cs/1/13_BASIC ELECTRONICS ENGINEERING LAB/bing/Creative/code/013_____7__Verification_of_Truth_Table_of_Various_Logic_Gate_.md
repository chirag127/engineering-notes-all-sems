### 7. Verification of Truth Table of Various Logic Gate

- A logic gate is an electronic circuit that performs a logical operation on one or more input signals and produces a single output signal.
- The input and output signals can have only two values: 0 (low) or 1 (high), which represent the binary digits or bits.
- The most common logic gates are AND, OR, NOT, NAND, NOR, XOR and XNOR gates.
- Each logic gate has a corresponding truth table that shows the output value for every possible combination of input values.
- To verify the truth table of a logic gate, we need to connect the input terminals of the gate to a switch or a voltage source, and the output terminal to a LED or a voltmeter.
- Then, we need to vary the input values and observe the output value, and compare it with the expected value from the truth table.
- For example, to verify the truth table of an AND gate, we can use the following circuit:

![AND gate circuit](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/AND_from_NAND.svg/1200px-AND_from_NAND.svg.png)

- The truth table of an AND gate is:

| A | B | Output |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 0      |
| 1 | 0 | 0      |
| 1 | 1 | 1      |

- To verify this, we can set the input values as follows:

| A | B | Output | LED |
|---|---|--------|-----|
| 0 | 0 | 0      | Off |
| 0 | 1 | 0      | Off |
| 1 | 0 | 0      | Off |
| 1 | 1 | 1      | On  |

- We can see that the output value matches the truth table value for each input combination, and the LED is on only when both inputs are 1, which verifies the AND gate operation.