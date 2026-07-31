### 7. Verification of Truth Table of Various Logic Gate

A logic gate is an electronic circuit that performs a logical operation on one or more input signals and produces a single output signal. The output signal depends on the type of logic gate and the combination of input signals. There are seven basic types of logic gates: AND, OR, NOT, NAND, NOR, XOR and XNOR.

To verify the truth table of a logic gate, we need to connect the input terminals of the gate to a switch or a voltage source, and the output terminal to a LED or a voltmeter. Then, we need to apply different combinations of input signals (0 or 1) and observe the corresponding output signal (0 or 1). The output signal should match the expected value given by the truth table of the logic gate.

For example, to verify the truth table of an AND gate, we can use the following circuit:

```
  +5V
   |
   |
   R
   |
   |
   A -----+-----+
         |     |
        SW1   SW2
         |     |
         |     |
   B ----+-----+----+
                       |
                       |
                       R
                       |
                       |
                       C
                       |
                       |
                      LED
                       |
                       |
                      GND
```

In this circuit, A and B are the input terminals of the AND gate, and C is the output terminal. SW1 and SW2 are two switches that can be turned on or off to apply 0 or 1 to the input terminals. R is a resistor that limits the current flow. LED is a light-emitting diode that glows when the output signal is 1.

The truth table of an AND gate is:

| A | B | C |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

To verify this truth table, we need to perform the following steps:

- Turn off both SW1 and SW2. This applies 0 to both A and B. The output C should be 0, and the LED should be off. This verifies the first row of the truth table.
- Turn on SW1 and turn off SW2. This applies 1 to A and 0 to B. The output C should be 0, and the LED should be off. This verifies the second row of the truth table.
- Turn off SW1 and turn on SW2. This applies 0 to A and 1 to B. The output C should be 0, and the LED should be off. This verifies the third row of the truth table.
- Turn on both SW1 and SW2. This applies 1 to both A and B. The output C should be 1, and the LED should be on. This verifies the fourth row of the truth table.

Similarly, we can verify the truth table of other logic gates by using appropriate circuits and input combinations.