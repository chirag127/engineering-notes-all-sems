## Design, and verify the 4-bit asynchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

An asynchronous counter is a sequential circuit that uses a series of flip-flops to generate a binary count. The output of one flip-flop is connected to the clock input of the next flip-flop, so that each flip-flop changes state at a different time. The counter is called asynchronous because the flip-flops are not triggered by the same clock signal.

A 4-bit asynchronous counter can count from 0 to 15 in binary. It requires four flip-flops, each with a Q output and a clock input. The Q output of each flip-flop represents one bit of the counter value. The clock input of the first flip-flop is connected to an external clock source, while the clock input of the other flip-flops is connected to the Q output of the previous flip-flop.

To design a 4-bit asynchronous counter using J-K flip-flops, we need to follow these steps:

- Determine the truth table of the counter, showing the Q outputs and the J and K inputs of each flip-flop for each count value.
- Determine the excitation table of the J-K flip-flop, showing the required J and K inputs for each possible transition of the Q output.
- Compare the truth table and the excitation table, and derive the logic expressions for the J and K inputs of each flip-flop in terms of the Q outputs.
- Draw the circuit diagram of the counter, using J-K flip-flops and logic gates according to the logic expressions.

The truth table of the 4-bit asynchronous counter is shown below:

| Count | Q3 | Q2 | Q1 | Q0 | J3 | K3 | J2 | K2 | J1 | K1 | J0 | K0 |
| ----- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| 0     | 0  | 0  | 0  | 0  | 0  | X  | 0  | X  | 0  | X  | 1  | X  |
| 1     | 0  | 0  | 0  | 1  | 0  | X  | 0  | X  | 1  | X  | X  | X  |
| 2     | 0  | 0  | 1  | 0  | 0  | X  | 1  | X  | X  | X  | 1  | X  |
| 3     | 0  | 0  | 1  | 1  | 0  | X  | X  | X  | X  | X  | X  | X  |
| 4     | 0  | 1  | 0  | 0  | 1  | X  | X  | X  | 0  | X  | 1  | X  |
| 5     | 0  | 1  | 0  | 1  | X  | X  | X  | X  | 1  | X  | X  | X  |
| 6     | 0  | 1  | 1  | 0  | X  | X  | X  | X  | X  | X  | 1  | X  |
| 7     | 0  | 1  | 1  | 1  | X  | X  | X  | X  | X  | X  | X  | X  |
| 8     | 1  | 0  | 0  | 0  | X  | X  | 0  | X  | 0  | X  | 1  | X  |
| 9     | 1  | 0  | 0  | 1  | X  | X  | 0  | X  | 1  | X  | X  | X  |
| 10    | 1  | 0  | 1  | 0  | X  | X  | 1  | X  | X  | X  | 1  | X  |
| 11    | 1  | 0  | 1