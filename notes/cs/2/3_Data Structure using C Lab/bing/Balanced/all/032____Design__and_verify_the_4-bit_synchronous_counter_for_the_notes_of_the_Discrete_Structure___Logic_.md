## Design and verify the 4-bit synchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- A 4-bit synchronous counter is a digital circuit that can count from 0 to 15 in binary using four flip-flops that are synchronized by a common clock signal.
- A synchronous counter is different from an asynchronous counter in that all the flip-flops are triggered by the same clock edge, which eliminates the propagation delay problem and increases the operating speed.
- A 4-bit synchronous counter can be designed using different types of flip-flops, such as T, D, or J-K flip-flops. In this note, we will use J-K flip-flops as an example.
- The design steps of a 4-bit synchronous counter using J-K flip-flops are as follows:

  - Step 1: Draw the state diagram of the counter, which shows the sequence of states and the transitions between them. For a 4-bit counter, there are 16 states, from 0000 to 1111. The state diagram is shown below:

  ![State diagram of 4-bit synchronous counter](https://i.imgur.com/1Z0w7fL.png)

  - Step 2: Derive the state table of the counter, which shows the current state, the next state, and the outputs of the flip-flops for each state. The state table is shown below:

  | Current State | Next State | Q3 | Q2 | Q1 | Q0 |
  |---------------|------------|----|----|----|----|
  | 0000          | 0001       | 0  | 0  | 0  | 1  |
  | 0001          | 0010       | 0  | 0  | 1  | 0  |
  | 0010          | 0011       | 0  | 0  | 1  | 1  |
  | 0011          | 0100       | 0  | 1  | 0  | 0  |
  | 0100          | 0101       | 0  | 1  | 0  | 1  |
  | 0101          | 0110       | 0  | 1  | 1  | 0  |
  | 0110          | 0111       | 0  | 1  | 1  | 1  |
  | 0111          | 1000       | 1  | 0  | 0  | 0  |
  | 1000          | 1001       | 1  | 0  | 0  | 1  |
  | 1001          | 1010       | 1  | 0  | 1  | 0  |
  | 1010          | 1011       | 1  | 0  | 1  | 1  |
  | 1011          | 1100       | 1  | 1  | 0  | 0  |
  | 1100          | 1101       | 1  | 1  | 0  | 1  |
  | 1101          | 1110       | 1  | 1  | 1  | 0  |
  | 1110          | 1111       | 1  | 1  | 1  | 1  |
  | 1111          | 0000       | 0  | 0  | 0  | 0  |

  - Step 3: Find the excitation table of the J-K flip-flop, which shows the inputs of the flip-flop for each possible transition of the output. The excitation table is shown below:

  | Q(t) | Q(t+1) | J | K |
  |------|--------|---|---|
  | 0    | 0      | 0 | X |
  | 0    | 1      | 1 | X |
  | 1    | 0      | X | 1 |
  | 1    | 1      | X | 0 |

  - Step 4: Combine the state table and the excitation table to obtain the input table of the counter, which shows the inputs of the flip-flops for each state. The