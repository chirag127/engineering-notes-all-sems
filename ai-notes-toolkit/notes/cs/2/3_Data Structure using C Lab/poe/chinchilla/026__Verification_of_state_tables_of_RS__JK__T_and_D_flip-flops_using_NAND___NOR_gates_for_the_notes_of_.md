## Verification of State Tables of RS, JK, T and D Flip-Flops using NAND & NOR Gates

In this lab, we will be verifying the state tables of four different types of flip-flops (RS, JK, T, and D) using NAND and NOR gates. This is an important exercise as it will help us understand how these flip-flops work and how they can be implemented using logic gates.

### Materials Required
- Breadboard
- Power supply
- NAND gates (IC 7400)
- NOR gates (IC 7402)
- LED
- Resistors
- Wires

### Procedure
1. Connect the power supply to the breadboard.
2. Connect the IC 7400 (NAND gates) and IC 7402 (NOR gates) to the breadboard.
3. Connect the input pins of the flip-flops to switches on the breadboard.
4. Connect the output pins of the flip-flops to LEDs on the breadboard.
5. Connect the necessary resistors to the LEDs.
6. Use the state tables of RS, JK, T, and D flip-flops to determine the input combinations that correspond to each state.
7. Set the input switches to the appropriate combination for each state and observe the output on the LEDs.
8. Verify that the output matches the state table for each flip-flop.

### RS Flip-Flop
The state table for an RS flip-flop is as follows:

| S | R | Q | Q(t+1) |
|---|---|---|--------|
| 0 | 0 | Q | Q      |
| 0 | 1 | Q | 0      |
| 1 | 0 | Q | 1      |
| 1 | 1 | Q | Invalid|

To verify the state table of an RS flip-flop using NAND gates, connect the following:

- S input to one input of a NAND gate
- R input to one input of another NAND gate
- The output of the first NAND gate to one input of the second NAND gate
- The output of the second NAND gate to the Q output of the flip-flop
- Connect the inputs of the two NAND gates to the power supply through switches

To verify the state table of an RS flip-flop using NOR gates, connect the following:

- S input to one input of a NOR gate
- R input to one input of another NOR gate
- The output of the first NOR gate to one input of the second NOR gate
- The output of the second NOR gate to the Q output of the flip-flop
- Connect the inputs of the two NOR gates to the power supply through switches

### JK Flip-Flop
The state table for a JK flip-flop is as follows:

| J | K | Q | Q(t+1) |
|---|---|---|--------|
| 0 | 0 | Q | Q      |
| 0 | 1 | Q | 0      |
| 1 | 0 | Q | 1      |
| 1 | 1 | Q | ~Q     |

To verify the state table of a JK flip-flop using NAND gates, connect the following:

- J input to one input of a NAND gate with the K input connected to the other input
- Q output to one input of another NAND gate with the output of the first NAND gate connected to the other input
- The output of the second NAND gate to the Q output of the flip-flop
- Connect the inputs of the two NAND gates to the power supply through switches

To verify the state table of a JK flip-flop using NOR gates, connect the following:

- J input to one input of a NOR gate with the K input connected to the other input
- Q output to one input of another NOR gate with the output of the first NOR gate connected to the other input
- The output of the second NOR gate to the Q output of the flip-flop
- Connect the inputs of the two NOR gates to the power supply through switches

### T Flip-Flop
The state table for a T flip-flop is as follows:

| T | Q | Q(t+1) |
|---|---|--------|
| 0 | Q | Q      |
| 1 | Q | ~Q     |

To verify the state table of a T flip-flop using NAND gates, connect the following:

- T input to both inputs of a NAND gate
- Q output to one input of another NAND gate with the output of the first NAND gate connected to the other input
- The output of the second NAND gate to the Q output of the flip-flop
- Connect the inputs of the two NAND gates to the power supply through switches

To verify the state table of a T flip-flop using NOR gates, connect the following:

- T input to both inputs of a NOR gate
- Q output to one input of another NOR gate