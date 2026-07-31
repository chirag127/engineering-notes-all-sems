## Implementation of 1:4 demultiplexer using logic gates

- A demultiplexer is a circuit that has one input and more than one output. It is used to send a signal to one of many devices based on the values of some control signals.
- A 1:4 demultiplexer has one input (D), two control signals (S1 and S0) and four outputs (Y0 to Y3). The input data goes to any one of the four outputs at a given time for a particular combination of select lines.
- The truth table of a 1:4 demultiplexer is shown below:

| S1 | S0 | Y0 | Y1 | Y2 | Y3 |
|----|----|----|----|----|----|
| 0  | 0  | D  | 0  | 0  | 0  |
| 0  | 1  | 0  | D  | 0  | 0  |
| 1  | 0  | 0  | 0  | D  | 0  |
| 1  | 1  | 0  | 0  | 0  | D  |

- The logic expressions for the outputs are:

Y0 = D.S1'.S0'

Y1 = D.S1'.S0

Y2 = D.S1.S0'

Y3 = D.S1.S0

- The circuit diagram of a 1:4 demultiplexer using logic gates is shown below:

![1:4 demultiplexer using logic gates](https://circuitverse.org/users/59463/projects/1-4-demultiplexer-using-logic-gates/image)

- The circuit can be implemented using four AND gates, two NOT gates and one OR gate.
- The demultiplexer can be used for various applications, such as data routing, memory addressing, parallel-to-serial conversion, etc.