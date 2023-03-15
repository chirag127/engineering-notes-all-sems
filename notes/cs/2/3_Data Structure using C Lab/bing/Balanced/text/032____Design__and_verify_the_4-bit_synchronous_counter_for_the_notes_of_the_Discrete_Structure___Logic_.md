## Design, and verify the 4-bit synchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- A 4-bit synchronous counter is a digital circuit that can count from 0 to 15 in binary using four flip-flops that are synchronized by a common clock signal.
- A synchronous counter is different from an asynchronous counter in that all the flip-flops are triggered by the same clock edge, which eliminates the propagation delay problem of the asynchronous counter .
- A 4-bit synchronous counter can be designed using different types of flip-flops, such as T, D, or J-K flip-flops. The choice of flip-flop depends on the desired counting sequence and the availability of the flip-flop inputs .
- To design a 4-bit synchronous counter using J-K flip-flops, the following steps can be followed:
  - Determine the number of states and the modulus of the counter. For a 4-bit counter, the number of states is 16 and the modulus is 16 (MOD-16).
  - Assign the output variables and the flip-flop inputs. For example, let Q3, Q2, Q1, and Q0 be the outputs of the four flip-flops, and J3, K3, J2, K2, J1, K1, J0, and K0 be the inputs of the flip-flops.
  - Construct the state table and the state diagram of the counter. The state table shows the present state, the next state, and the flip-flop inputs for each state transition. The state diagram shows the states and the transitions graphically. For example, the state table and the state diagram of a 4-bit synchronous up counter are shown below:

| Present State | Next State | Flip-flop Inputs |
|:-------------:|:----------:|:----------------:|
| Q3 Q2 Q1 Q0   | Q3 Q2 Q1 Q0 | J3 K3 J2 K2 J1 K1 J0 K0 |
| 0  0  0  0    | 0  0  0  1  | 0  X  0  X  0  X  1  X  |
| 0  0  0  1    | 0  0  1  0  | 0  X  0  X  1  X  X  1  |
| 0  0  1  0    | 0  0  1  1  | 0  X  0  X  X  1  1  X  |
| 0  0  1  1    | 0  1  0  0  | 0  X  1  X  X  1  X  1  |
| 0  1  0  0    | 0  1  0  1  | 0  X  X  1  0  X  1  X  |
| 0  1  0  1    | 0  1  1  0  | 0  X  X  1  1  X  X  1  |
| 0  1  1  0    | 0  1  1  1  | 0  X  X  1  X  1  1  X  |
| 0  1  1  1    | 1  0  0  0  | 1  X  X  1  X  1  X  1  |
| 1  0  0  0    | 1  0  0  1  | X  1  0  X  0  X  1  X  |
| 1  0  0  1    | 1  0  1  0  | X  1  0  X  1  X  X  1  |
| 1  0  1  0    | 1  0