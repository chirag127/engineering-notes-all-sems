### 7. Verification of Truth Table of Various Logic Gate

A logic gate is an electronic circuit that performs a logical operation on one or more input signals and produces a single output signal. The output signal depends on the type of logic gate and the combination of input signals. There are seven basic types of logic gates: AND, OR, NOT, NAND, NOR, XOR and XNOR. Each logic gate has a corresponding truth table that shows the output signal for every possible combination of input signals.

To verify the truth table of a logic gate, we need to use a circuit that can generate the input signals and measure the output signal. One way to do this is to use a breadboard, a battery, some switches, some LEDs and some resistors. The switches act as the input signals, the LEDs act as the output signal and the resistors limit the current flow. The logic gate can be either a discrete component or an integrated circuit.

The following steps describe how to verify the truth table of an AND gate using a breadboard:

1. Connect the positive terminal of the battery to a common power rail on the breadboard.
2. Connect the negative terminal of the battery to a common ground rail on the breadboard.
3. Connect one end of a resistor to the power rail and the other end to a row on the breadboard. This row will be the output of the AND gate.
4. Connect an LED to the same row as the resistor and the ground rail. The LED will light up when the output of the AND gate is high (1).
5. Connect the input pins of the AND gate to two different rows on the breadboard. These rows will be the inputs of the AND gate.
6. Connect two switches to the power rail and the input rows of the AND gate. The switches will act as the input signals for the AND gate. When the switch is closed, the input signal is high (1). When the switch is open, the input signal is low (0).
7. To verify the truth table of the AND gate, change the position of the switches and observe the state of the LED. The truth table of the AND gate is as follows:

| Input A | Input B | Output |
|---------|---------|--------|
| 0       | 0       | 0      |
| 0       | 1       | 0      |
| 1       | 0       | 0      |
| 1       | 1       | 1      |

The LED should only light up when both switches are closed, which corresponds to the output being high (1) when both inputs are high (1).

The same procedure can be repeated for other logic gates by changing the type of logic gate and the corresponding truth table. For example, the truth table of an OR gate is as follows:

| Input A | Input B | Output |
|---------|---------|--------|
| 0       | 0       | 0      |
| 0       | 1       | 1      |
| 1       | 0       | 1      |
| 1       | 1       | 1      |

The LED should light up when either switch is closed or both switches are closed, which corresponds to the output being high (1) when either input is high (1) or both inputs are high (1).