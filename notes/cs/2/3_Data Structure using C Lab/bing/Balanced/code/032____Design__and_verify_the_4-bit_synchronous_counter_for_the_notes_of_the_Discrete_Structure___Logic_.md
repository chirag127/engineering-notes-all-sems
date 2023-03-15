## Design, and verify the 4-bit synchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

A 4-bit synchronous counter is a digital circuit that can count from 0 to 15 in binary using four flip-flops that are synchronized by a common clock signal. The flip-flops can be of any type, such as J-K, D, or T, but they must have the same characteristic equation and propagation delay. The output of each flip-flop is connected to the input of the next one in a chain, and the input of the first flip-flop is controlled by a logic circuit that determines the counting sequence. The logic circuit can be designed using a state diagram, a state table, or a Karnaugh map.

The following steps can be followed to design and verify a 4-bit synchronous counter using J-K flip-flops:

1. Draw the state diagram of the counter, showing the transitions from one state to another for each clock pulse. For example, a 4-bit synchronous up counter that counts from 0 to 15 and then resets to 0 would have the following state diagram:

![State diagram of 4-bit synchronous up counter](https://i.imgur.com/9zgZ7a0.png)

2. Draw the state table of the counter, showing the present state, the next state, and the inputs of each flip-flop for each state transition. For example, the state table of the 4-bit synchronous up counter would be:

| Present State | Next State | J0 | K0 | J1 | K1 | J2 | K2 | J3 | K3 |
|---------------|------------|----|----|----|----|----|----|----|----|
| 0000          | 0001       | 1  | X  | 0  | X  | 0  | X  | 0  | X  |
| 0001          | 0010       | 0  | X  | 1  | X  | 0  | X  | 0  | X  |
| 0010          | 0011       | 1  | X  | 0  | X  | 0  | X  | 0  | X  |
| 0011          | 0100       | 0  | X  | 0  | X  | 1  | X  | 0  | X  |
| 0100          | 0101       | 1  | X  | 0  | X  | 0  | X  | 0  | X  |
| 0101          | 0110       | 0  | X  | 1  | X  | 0  | X  | 0  | X  |
| 0110          | 0111       | 1  | X  | 0  | X  | 0  | X  | 0  | X  |
| 0111          | 1000       | 0  | X  | 0  | X  | 0  | X  | 1  | X  |
| 1000          | 1001       | 1  | X  | 0  | X  | 0  | X  | 0  | X  |
| 1001          | 1010       | 0  | X  | 1  | X  | 0  | X  | 0  | X  |
| 1010          | 1011       | 1  | X  | 0  | X  | 0  | X  | 0  | X  |
| 1011          | 1100       | 0  | X  | 0  | X  | 1  | X  | 0  | X  |
| 1100          | 1101       | 1  | X  | 0  | X  | 0  | X  | 0  | X  |
| 1101          | 1110       | 0  | X  | 1  | X  | 0  | X  | 0  | X  |
| 1110          | 1111       | 1  | X  | 0  | X  | 0  | X  | 0