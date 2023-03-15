### Verification of Truth Table of Various Logic Gate

A logic gate is a device that performs a Boolean logic operation on one or more binary inputs and then outputs a single binary output. There are different types of logic gates, such as AND, OR, NOT, NAND, NOR, and XOR, each with its own truth table that shows the output for every possible combination of inputs.

To verify the truth table of a logic gate, the following steps are required:

- Select the suitable integrated circuit (IC) that contains the logic gate to be verified. For example, IC 7408 contains four AND gates, IC 7404 contains six NOT gates, and so on.
- Connect the IC to a power supply of 5V, with pin 14 as the positive terminal and pin 7 as the ground terminal.
- Connect the input pins of the logic gate to switches or logic level generators that can provide either 0V (logic 0) or 5V (logic 1) as inputs.
- Connect the output pin of the logic gate to a LED or a logic probe that can indicate either 0V (logic 0) or 5V (logic 1) as output.
- Apply the logical inputs of the truth table to the input pins and observe the corresponding output on the LED or the logic probe.
- Compare the observed output with the expected output from the truth table and verify if they match.

The following table shows the IC numbers, pin numbers, and truth tables of some common logic gates:

| Logic gate | IC number | Input pins | Output pin | Truth table |
|------------|-----------|------------|------------|-------------|
| AND        | 7408      | 1, 2       | 3          | A | B | Y |
|            |           |            |            | 0 | 0 | 0 |
|            |           |            |            | 0 | 1 | 0 |
|            |           |            |            | 1 | 0 | 0 |
|            |           |            |            | 1 | 1 | 1 |
| OR         | 7432      | 1, 2       | 3          | A | B | Y |
|            |           |            |            | 0 | 0 | 0 |
|            |           |            |            | 0 | 1 | 1 |
|            |           |            |            | 1 | 0 | 1 |
|            |           |            |            | 1 | 1 | 1 |
| NOT        | 7404      | 1          | 2          | A | Y |
|            |           |            |            | 0 | 1 |
|            |           |            |            | 1 | 0 |
| NAND       | 7400      | 1, 2       | 3          | A | B | Y |
|            |           |            |            | 0 | 0 | 1 |
|            |           |            |            | 0 | 1 | 1 |
|            |           |            |            | 1 | 0 | 1 |
|            |           |            |            | 1 | 1 | 0 |
| NOR        | 7402      | 1, 2       | 3          | A | B | Y |
|            |           |            |            | 0 | 0 | 1 |
|            |           |            |            | 0 | 1 | 0 |
|            |           |            |            | 1 | 0 | 0 |
|            |           |            |            | 1 | 1 | 0 |
| XOR        | 7486      | 1, 2       | 3          | A | B | Y |
|            |           |            |            | 0 | 0 | 0 |
|            |           |            |            | 0 | 1 | 1 |
|            |           |            |            | 1 | 0 | 1 |
|            |           |            |            | 1 | 1 | 0 |