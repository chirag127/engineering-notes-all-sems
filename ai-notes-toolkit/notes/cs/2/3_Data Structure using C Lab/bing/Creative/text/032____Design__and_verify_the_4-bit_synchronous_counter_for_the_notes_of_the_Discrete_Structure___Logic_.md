## Design and verify the 4-bit synchronous counter for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- A synchronous counter is a type of counter that uses a common clock signal to trigger all the flip-flops simultaneously.
- A 4-bit synchronous counter can count from 0 to 15 in binary, or from 0 to 9 in decimal if it is a decade counter.
- A 4-bit synchronous counter can be designed using J-K flip-flops, which toggle their output when both J and K inputs are high.
- The design steps of a 4-bit synchronous counter using J-K flip-flops are as follows:

  - Draw the state diagram of the counter, showing the transitions from one state to the next for each clock pulse.
  - Write the state table of the counter, showing the present state, the next state, and the outputs of each flip-flop.
  - Find the excitation table of the J-K flip-flop, showing the required inputs for each possible transition of the output.
  - Use the state table and the excitation table to find the expressions for the J and K inputs of each flip-flop in terms of the present state outputs.
  - Draw the circuit diagram of the counter, using J-K flip-flops and logic gates to implement the expressions for the inputs.
  - Verify the operation of the counter by simulating it or testing it on a breadboard.

- An example of a 4-bit synchronous counter using J-K flip-flops is shown below:

  - State diagram:

  ![State diagram of 4-bit synchronous counter](https://physicsteacher.in/wp-content/uploads/2021/12/4-bit-synchronous-counter-state-diagram.jpg)

  - State table:

  | Present state | Next state | Q3 Q2 Q1 Q0 | J3 K3 | J2 K2 | J1 K1 | J0 K0 |
  |---------------|------------|-------------|-------|-------|-------|-------|
  | 0000          | 0001       | 0 0 0 0     | 0 0   | 0 0   | 0 0   | 1 1   |
  | 0001          | 0010       | 0 0 0 1     | 0 0   | 0 0   | 1 1   | 0 0   |
  | 0010          | 0011       | 0 0 1 0     | 0 0   | 0 0   | 0 0   | 1 1   |
  | 0011          | 0100       | 0 0 1 1     | 0 0   | 1 1   | 0 0   | 0 0   |
  | 0100          | 0101       | 0 1 0 0     | 0 0   | 0 0   | 0 0   | 1 1   |
  | 0101          | 0110       | 0 1 0 1     | 0 0   | 0 0   | 1 1   | 0 0   |
  | 0110          | 0111       | 0 1 1 0     | 0 0   | 0 0   | 0 0   | 1 1   |
  | 0111          | 1000       | 0 1 1 1     | 1 1   | 0 0   | 0 0   | 0 0   |
  | 1000          | 1001       | 1 0 0 0     | 0 0   | 0 0   | 0 0   | 1 1   |
  | 1001          | 1010       | 1 0 0 1     | 0 0   | 0 0   | 1 1   | 0 0   |
  | 1010          | 1011       | 1 0 1 0     | 0 0   | 0 0   | 0 0   | 1 1   |
  | 1011          | 1100       | 1 0 1