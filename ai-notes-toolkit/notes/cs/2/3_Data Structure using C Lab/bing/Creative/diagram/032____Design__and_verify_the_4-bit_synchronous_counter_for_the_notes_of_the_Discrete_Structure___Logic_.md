## Design, and verify the 4-bit synchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

A 4-bit synchronous counter is a digital circuit that can count from 0 to 15 in binary using four flip-flops that are synchronized by a common clock signal. The flip-flops can be of any type, such as T, D, or JK, but they must have the same characteristic equation. The output of each flip-flop is connected to the input of the next one, except for the last one, which is connected to the first one. The output of the counter is the binary representation of the current state of the flip-flops.

The design steps of a 4-bit synchronous counter using JK flip-flops are as follows:

1. Draw the state diagram of the counter, showing the transitions from one state to the next. The state diagram of a 4-bit synchronous counter is shown below:

![State diagram of 4-bit synchronous counter](https://physicsteacher.in/wp-content/uploads/2021/12/4-bit-synchronous-counter-state-diagram.png)

2. Write the state table of the counter, showing the present state, the next state, and the output of each flip-flop. The state table of a 4-bit synchronous counter is shown below:

| Present State | Next State | Output |
| Q3 Q2 Q1 Q0 | Q3+ Q2+ Q1+ Q0+ | J3 K3 J2 K2 J1 K1 J0 K0 |
| 0 0 0 0 | 0 0 0 1 | 0 X 0 X 0 X 1 X |
| 0 0 0 1 | 0 0 1 0 | 0 X 0 X 1 X X 1 |
| 0 0 1 0 | 0 0 1 1 | 0 X 0 X 0 X 1 X |
| 0 0 1 1 | 0 1 0 0 | 0 X 1 X X 1 X 1 |
| 0 1 0 0 | 0 1 0 1 | 0 X 0 X 0 X 1 X |
| 0 1 0 1 | 0 1 1 0 | 0 X 0 X 1 X X 1 |
| 0 1 1 0 | 0 1 1 1 | 0 X 0 X 0 X 1 X |
| 0 1 1 1 | 1 0 0 0 | 1 X X 1 X 1 X 1 |
| 1 0 0 0 | 1 0 0 1 | 0 X 0 X 0 X 1 X |
| 1 0 0 1 | 1 0 1 0 | 0 X 0 X 1 X X 1 |
| 1 0 1 0 | 1 0 1 1 | 0 X 0 X 0 X 1 X |
| 1 0 1 1 | 1 1 0 0 | 0 X 1 X X 1 X 1 |
| 1 1 0 0 | 1 1 0 1 | 0 X 0 X 0 X 1 X |
| 1 1 0 1 | 1 1 1 0 | 0 X 0 X 1 X X 1 |
| 1 1 1 0 | 1 1 1 1 | 0 X 0 X 0 X 1 X |
| 1 1 1 1 | 0 0 0 0 | X 1 X 1 X 1 X 1 |

Note: X means don't care, i.e., the input can be either 0 or 1.

3. Simplify the output expressions for each flip-flop using Karnaugh maps or Boolean algebra. The simplified output expressions for a 4-bit synchronous counter are shown below:

| Output | Expression |
| J3 | Q2 Q1 Q0 |
| K3 | Q2 Q1 Q0 |
| J2 | Q1 Q0 |
| K2 | Q1 Q0 |
| J1 |