### Verification of Truth Table of Various Logic Gate

A logic gate is a device that performs a Boolean logic operation on one or more binary inputs and then outputs a single binary output. There are different types of logic gates, such as AND, OR, NOT, NAND, NOR, and XOR, each with its own truth table that shows the output for every possible combination of inputs.

To verify the truth table of a logic gate, the following steps are required:

- Select the suitable integrated circuit (IC) that contains the logic gate to be verified. For example, IC 7408 contains four AND gates, IC 7404 contains six NOT gates, and so on.
- Connect the power supply to the IC by applying 5V to the pin 14 while the pin 7 is connected to the ground.
- Connect the logical inputs of the truth table to the input pins of the logic gate using switches or wires. For example, for a two-input AND gate, the inputs A and B can be connected to the pins 1 and 2, respectively.
- Connect the output pin of the logic gate to a LED or a voltmeter to observe the output. For example, for a two-input AND gate, the output Y can be connected to the pin 3.
- Apply the logical inputs of the truth table one by one and note the corresponding output. For example, for a two-input AND gate, the inputs can be 00, 01, 10, and 11, and the output can be 0, 0, 0, and 1, respectively.
- Compare the observed output with the expected output from the truth table and verify that they match. For example, for a two-input AND gate, the truth table is:

| A | B | Y |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

- Repeat the steps for other logic gates using the appropriate ICs and input/output pins. For example, for a two-input OR gate, the IC 7432 can be used, and the input/output pins can be 1, 2, and 3.

Some logic gates can also be verified using universal gates, such as NAND and NOR, which can implement any logic function by combining them in different ways. For example, a NOT gate can be implemented by connecting both inputs of a NAND gate together, and an AND gate can be implemented by connecting two NOT gates to the output of a NAND gate. To verify the truth table of a logic gate using universal gates, the following steps are required:

- Select the suitable IC that contains the universal gate to be used. For example, IC 7400 contains four NAND gates, and IC 7402 contains four NOR gates.
- Connect the power supply to the IC by applying 5V to the pin 14 while the pin 7 is connected to the ground.
- Connect the universal gates in the required configuration to implement the logic gate to be verified. For example, to implement a NOT gate using a NAND gate, connect both inputs of the NAND gate together and use it as the input of the NOT gate.
- Connect the logical inputs of the truth table to the input pins of the universal gate configuration using switches or wires. For example, for a NOT gate, the input A can be connected to the pins 1 and 2 of the NAND gate.
- Connect the output pin of the universal gate configuration to a LED or a voltmeter to observe the output. For example, for a NOT gate, the output Y can be connected to the pin 3 of the NAND gate.
- Apply the logical inputs of the truth table one by one and note the corresponding output. For example, for a NOT gate, the inputs can be 0 and 1, and the output can be 1 and 0, respectively.
- Compare the observed output with the expected output from the truth table and verify that they match. For example, for a NOT gate, the truth table is:

| A | Y |
|---|---|
| 0 | 1 |
| 1 | 0 |

- Repeat the steps for other logic gates using the appropriate universal gate configurations and input/output pins. For example, to implement an AND gate using NAND gates,