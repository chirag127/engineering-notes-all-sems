## Implementing 4x1 and 8x1 MULTIPLEXERS for the notes of the Computer Organization Lab in the subject of Computer Organization

- A multiplexer (MUX) is a digital device that selects one of the N inputs and directs it to the output.
- A 4x1 MUX has 4 data inputs, 2 selection lines and one output. A 8x1 MUX has 8 data inputs, 3 selection lines and one output.
- To implement a 8x1 MUX using lower order MUXes, we can use two 4x1 MUXes and one 2x1 MUX as follows :

![8x1 MUX using 4x1 and 2x1 MUXes](https://www.tutorialspoint.com/digital_circuits/images/8x1_multiplexer.jpg)

- The 8 data inputs are connected to the two 4x1 MUXes in the first stage. The two outputs of the 4x1 MUXes are connected to the 2x1 MUX in the second stage. The output of the 2x1 MUX is the final output of the 8x1 MUX.
- The selection lines S0 and S1 are common for both 4x1 MUXes. The selection line S2 is used to select the output of the 2x1 MUX.
- The truth table for the 8x1 MUX is as follows:

| S2 | S1 | S0 | Output |
|----|----|----|--------|
| 0  | 0  | 0  | I0     |
| 0  | 0  | 1  | I1     |
| 0  | 1  | 0  | I2     |
| 0  | 1  | 1  | I3     |
| 1  | 0  | 0  | I4     |
| 1  | 0  | 1  | I5     |
| 1  | 1  | 0  | I6     |
| 1  | 1  | 1  | I7     |

- The logic expression for the output of the 8x1 MUX is:

Output = (S2' S1' S0' I0) + (S2' S1' S0 I1) + (S2' S1 S0' I2) + (S2' S1 S0 I3) + (S2 S1' S0' I4) + (S2 S1' S0 I5) + (S2 S1 S0' I6) + (S2 S1 S0 I7)

- Where S2', S1' and S0' are the complements of S2, S1 and S0 respectively.
- The logic diagram for the 8x1 MUX using 4x1 and 2x1 MUXes is as follows:

![Logic diagram for 8x1 MUX using 4x1 and 2x1 MUXes](https://i.stack.imgur.com/1kZ1c.png)

- The 4x1 MUXes are labeled as M0 and M1. The 2x1 MUX is labeled as M2. The enable inputs of the 4x1 MUXes are labeled as E0 and E1. The output of M0 is labeled as O0 and the output of M1 is labeled as O1.
- The enable inputs E0 and E1 are used to avoid a short circuit condition when the outputs of the 4x1 MUXes are wired together. The logic that controls the 8x1 MUX should ensure that E0 = !E1 at all times.
- For input select = 0 - 3, it should set E0 = 1 and E1 = 0. For input select = 4 - 7, it should set E0 = 0 and E1 = 1. This way, only one of the 4x1 MUXes is enabled at a time and the output of the 2x1 MUX is selected by S2.