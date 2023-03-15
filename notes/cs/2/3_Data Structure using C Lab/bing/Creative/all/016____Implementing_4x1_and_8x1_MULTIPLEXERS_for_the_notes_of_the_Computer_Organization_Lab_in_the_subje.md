# Implementing 4x1 and 8x1 MULTIPLEXERS for the notes of the Computer Organization Lab in the subject of Computer Organization

- A multiplexer (MUX) is a digital device that selects one of the several input signals and forwards it to the output based on some selection logic.
- A 4x1 multiplexer has 4 data inputs, 2 selection lines and one output. A 8x1 multiplexer has 8 data inputs, 3 selection lines and one output.
- A 8x1 multiplexer can be implemented using two 4x1 multiplexers and one 2x1 multiplexer .
- The following steps describe how to implement a 8x1 multiplexer using 4x1 and 2x1 multiplexers:
  - Connect the 8 data inputs (D0 to D7) to the two 4x1 multiplexers (M0 and M1) as shown in the figure below. The data inputs D0 to D3 are connected to M0 and the data inputs D4 to D7 are connected to M1.
  - Connect the two least significant selection lines (S0 and S1) to both M0 and M1. These lines will select one of the four data inputs for each 4x1 multiplexer.
  - Connect the output of M0 and M1 to the inputs of the 2x1 multiplexer (M2). The output of M0 is connected to I0 and the output of M1 is connected to I1 of M2.
  - Connect the most significant selection line (S2) to the selection line of M2. This line will select one of the two outputs of M0 and M1 for the final output of M2.
  - The output of M2 is the output of the 8x1 multiplexer.

![8x1 multiplexer using 4x1 and 2x1 multiplexers](https://i.imgur.com/0l0y7Q2.png)

- The following table shows the truth table of the 8x1 multiplexer using 4x1 and 2x1 multiplexers:

| S2 | S1 | S0 | Output |
|----|----|----|--------|
| 0  | 0  | 0  | D0     |
| 0  | 0  | 1  | D1     |
| 0  | 1  | 0  | D2     |
| 0  | 1  | 1  | D3     |
| 1  | 0  | 0  | D4     |
| 1  | 0  | 1  | D5     |
| 1  | 1  | 0  | D6     |
| 1  | 1  | 1  | D7     |

- The following expression shows the output function of the 8x1 multiplexer using 4x1 and 2x1 multiplexers:

Output = (S2' * S1' * S0' * D0) + (S2' * S1' * S0 * D1) + (S2' * S1 * S0' * D2) + (S2' * S1 * S0 * D3) + (S2 * S1' * S0' * D4) + (S2 * S1' * S0 * D5) + (S2 * S1 * S0' * D6) + (S2 * S1 * S0 * D7)

where S2', S1' and S0' are the complements of S2, S1 and S0 respectively.