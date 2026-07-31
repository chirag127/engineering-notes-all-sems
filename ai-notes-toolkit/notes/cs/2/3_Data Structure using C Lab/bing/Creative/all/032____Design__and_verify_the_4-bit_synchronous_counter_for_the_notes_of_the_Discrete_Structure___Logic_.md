## Design and verify the 4-bit synchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

A 4-bit synchronous counter is a digital circuit that can count from 0 to 15 in binary using four flip-flops that are synchronized by a common clock signal. The design and verification steps are as follows:

- Step 1: Choose the type of flip-flop to use. For this example, we will use J-K flip-flops, which have two inputs J and K, and two outputs Q and Q'. The J-K flip-flop can toggle, set, reset, or hold its state depending on the values of J and K. The truth table of the J-K flip-flop is shown below:

| J | K | Q(t+1) | Operation |
|---|---|--------|-----------|
| 0 | 0 | Q(t)   | Hold      |
| 0 | 1 | 0      | Reset     |
| 1 | 0 | 1      | Set       |
| 1 | 1 | Q'(t)  | Toggle    |

- Step 2: Determine the state transition table of the 4-bit counter. The counter has four states, Q3 Q2 Q1 Q0, which represent the binary values from 0 to 15. The next state, Q3(t+1) Q2(t+1) Q1(t+1) Q0(t+1), is obtained by adding 1 to the current state modulo 16. The state transition table is shown below:

| Q3 | Q2 | Q1 | Q0 | Q3(t+1) | Q2(t+1) | Q1(t+1) | Q0(t+1) |
|----|----|----|----|---------|---------|---------|---------|
| 0  | 0  | 0  | 0  | 0       | 0       | 0       | 1       |
| 0  | 0  | 0  | 1  | 0       | 0       | 1       | 0       |
| 0  | 0  | 1  | 0  | 0       | 0       | 1       | 1       |
| 0  | 0  | 1  | 1  | 0       | 1       | 0       | 0       |
| 0  | 1  | 0  | 0  | 0       | 1       | 0       | 1       |
| 0  | 1  | 0  | 1  | 0       | 1       | 1       | 0       |
| 0  | 1  | 1  | 0  | 0       | 1       | 1       | 1       |
| 0  | 1  | 1  | 1  | 1       | 0       | 0       | 0       |
| 1  | 0  | 0  | 0  | 1       | 0       | 0       | 1       |
| 1  | 0  | 0  | 1  | 1       | 0       | 1       | 0       |
| 1  | 0  | 1  | 0  | 1       | 0       | 1       | 1       |
| 1  | 0  | 1  | 1  | 1       | 1       | 0       | 0       |
| 1  | 1  | 0  | 0  | 1       | 1       | 0       | 1       |
| 1  | 1  | 0  | 1  | 1       | 1       | 1       | 0       |
| 1  | 1  | 1  | 0  | 1       | 1       | 1       | 1       |
| 1  | 1  | 1  | 1  | 0       | 0       | 0       | 0       |

- Step 3: Derive the excitation equations for each flip-flop. The excitation equations are the expressions for the J and