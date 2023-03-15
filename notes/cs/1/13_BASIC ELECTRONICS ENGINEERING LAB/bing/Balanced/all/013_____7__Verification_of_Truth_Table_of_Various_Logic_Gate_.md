# 7. Verification of Truth Table of Various Logic Gate

A logic gate is an electronic circuit that performs a logical operation on one or more input signals and produces a single output signal. The output signal depends on the type of logic gate and the combination of input signals.

There are seven basic logic gates: AND, OR, NOT, NAND, NOR, XOR and XNOR. Each logic gate has a corresponding truth table that shows the output signal for every possible combination of input signals.

To verify the truth table of a logic gate, we need to perform the following steps:

- Connect the logic gate to a power supply and a voltmeter or an LED indicator.
- Connect the input terminals of the logic gate to switches that can be turned on or off to represent the binary values 1 and 0.
- For each row of the truth table, set the input switches to the corresponding values and observe the output voltage or the LED status.
- Record the output signal for each input combination and compare it with the expected value from the truth table.
- If the output signal matches the truth table for all input combinations, the logic gate is verified.

For example, to verify the truth table of an AND gate, we can use the following circuit:

![AND gate circuit](https://i.imgur.com/8w7Zw0R.png)

The truth table of an AND gate is:

| A | B | Output |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 0      |
| 1 | 0 | 0      |
| 1 | 1 | 1      |

To verify the truth table, we can perform the following steps:

- Set both switches A and B to 0 (off) and observe the output voltage or the LED status. It should be 0 (off) as well, matching the first row of the truth table.
- Set switch A to 0 (off) and switch B to 1 (on) and observe the output. It should be 0 (off) as well, matching the second row of the truth table.
- Set switch A to 1 (on) and switch B to 0 (off) and observe the output. It should be 0 (off) as well, matching the third row of the truth table.
- Set both switches A and B to 1 (on) and observe the output. It should be 1 (on) as well, matching the fourth row of the truth table.

Since the output signal matches the truth table for all input combinations, the AND gate is verified. We can repeat the same process for other logic gates using different circuits and truth tables.