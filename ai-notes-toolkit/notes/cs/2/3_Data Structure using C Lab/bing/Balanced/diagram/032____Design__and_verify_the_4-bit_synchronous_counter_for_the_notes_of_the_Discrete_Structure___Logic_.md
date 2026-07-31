## Design, and verify the 4-bit synchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

A 4-bit synchronous counter is a digital circuit that can count from 0 to 15 in binary using four flip-flops that are synchronized by a common clock signal. The output of each flip-flop represents one bit of the counter value. The design steps of a 4-bit synchronous counter using J-K flip-flops are as follows:

- Step 1: Determine the number of states and the modulus of the counter. A 4-bit counter has 16 states (from 0000 to 1111) and a modulus of 16 (MOD-16).
- Step 2: Draw the state diagram and the state table of the counter. The state diagram shows the transitions between the states and the outputs of each state. The state table lists the current state, the next state, and the outputs of each state.

![State diagram of 4-bit synchronous counter](https://physicsteacher.in/wp-content/uploads/2021/12/4-bit-synchronous-counter-state-diagram.jpg)

| Current State | Next State | Output |
|---------------|------------|--------|
| 0000          | 0001       | 0000   |
| 0001          | 0010       | 0001   |
| 0010          | 0011       | 0010   |
| 0011          | 0100       | 0011   |
| 0100          | 0101       | 0100   |
| 0101          | 0110       | 0101   |
| 0110          | 0111       | 0110   |
| 0111          | 1000       | 0111   |
| 1000          | 1001       | 1000   |
| 1001          | 1010       | 1001   |
| 1010          | 1011       | 1010   |
| 1011          | 1100       | 1011   |
| 1100          | 1101       | 1100   |
| 1101          | 1110       | 1101   |
| 1110          | 1111       | 1110   |
| 1111          | 0000       | 1111   |

- Step 3: Assign the flip-flops and the inputs to the state table. The output of each flip-flop corresponds to one bit of the state. The input of each flip-flop depends on the current state and the next state. For J-K flip-flops, the input values are as follows:

| Current State | Next State | J | K |
|---------------|------------|---|---|
| 0             | 0          | 0 | X |
| 0             | 1          | 1 | X |
| 1             | 0          | X | 1 |
| 1             | 1          | X | 0 |

- Step 4: Write the excitation equations for each flip-flop. The excitation equations are the Boolean expressions that relate the inputs of the flip-flops to the current state and the next state. For example, the excitation equation for the J input of the first flip-flop is:

J1 = Q1'Q2'Q3' + Q1'Q2Q3' + Q1Q2'Q3' + Q1Q2Q3'

- Step 5: Draw the circuit diagram of the counter. The circuit diagram shows the connections between the flip-flops, the clock signal, and the excitation equations. The output of the counter is the output of the flip-flops.

![Circuit diagram of 4-bit synchronous counter](https://physicsteacher.in/wp-content/uploads/2021/12/4-bit-synchronous-counter-circuit-diagram.jpg)

- Step 6: Verify the operation of the counter. The verification can be done by simulating the circuit using a software tool or by testing the circuit using a hardware device. The verification should check that the counter counts correctly from 0 to 15 and then resets to 0. The verification should also check that the counter is synchronized by the clock signal and that there is no delay or glitch in the output.