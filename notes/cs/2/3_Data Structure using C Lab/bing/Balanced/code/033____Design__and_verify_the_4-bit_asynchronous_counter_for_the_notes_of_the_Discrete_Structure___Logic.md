## Design, and verify the 4-bit asynchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- A 4-bit asynchronous counter is a digital circuit that can count from 0 to 15 in binary using four flip-flops.
- The flip-flops are connected in a chain, such that the output of one flip-flop drives the clock input of the next flip-flop.
- The first flip-flop is the least significant bit (LSB) and the last flip-flop is the most significant bit (MSB).
- The flip-flops are triggered by the falling edge of the clock signal, meaning that they change state when the clock signal goes from high to low.
- The counter can be designed using JK flip-flops or D flip-flops. In this note, we will use JK flip-flops.
- A JK flip-flop has two inputs, J and K, and two outputs, Q and Q'. The output Q is the state of the flip-flop, and Q' is the complement of Q.
- The truth table of a JK flip-flop is as follows:

| J | K | Q(t+1) | Description |
|---|---|--------|-------------|
| 0 | 0 | Q(t)   | No change   |
| 0 | 1 | 0      | Reset       |
| 1 | 0 | 1      | Set         |
| 1 | 1 | Q'(t)  | Toggle      |

- To design a 4-bit asynchronous counter, we need to connect four JK flip-flops in the following way:

![4-bit asynchronous counter](https://i.imgur.com/8WfzZjv.png)

- The first flip-flop, F0, is the LSB and has its J and K inputs tied to 1, meaning that it will toggle at every falling edge of the clock signal.
- The second flip-flop, F1, has its J and K inputs connected to the Q output of F0, meaning that it will toggle when F0 changes from 1 to 0, or every two clock cycles.
- The third flip-flop, F2, has its J and K inputs connected to the Q output of F1, meaning that it will toggle when F1 changes from 1 to 0, or every four clock cycles.
- The fourth flip-flop, F3, has its J and K inputs connected to the Q output of F2, meaning that it will toggle when F2 changes from 1 to 0, or every eight clock cycles.
- The outputs of the four flip-flops, Q0, Q1, Q2, and Q3, form the 4-bit binary count, with Q0 being the LSB and Q3 being the MSB.
- The counter will start from 0 (0000) and increment by 1 at every falling edge of the clock signal, until it reaches 15 (1111), and then wrap around to 0 (0000) again.
- The following table shows the state transitions of the counter:

| Clock | Q3 | Q2 | Q1 | Q0 | Count |
|-------|----|----|----|----|-------|
| ↑     | 0  | 0  | 0  | 0  | 0     |
| ↓     | 0  | 0  | 0  | 1  | 1     |
| ↑     | 0  | 0  | 0  | 1  | 1     |
| ↓     | 0  | 0  | 1  | 0  | 2     |
| ↑     | 0  | 0  | 1  | 0  | 2     |
| ↓     | 0  | 0  | 1  | 1  | 3     |
| ↑     | 0  | 0  | 1  | 1  | 3     |
| ↓     | 0  | 1  | 0  | 0  | 4     |
| ↑     | 0  | 1  | 0  | 0  | 4     |
| ↓     | 0  | 1  | 0  | 1  | 5     |
| ↑     | 0  | 1  | 0  | 1  | 5     |
| ↓     | 0  | 1  | 1  | 0  | 6     |
| ↑     | 0  |