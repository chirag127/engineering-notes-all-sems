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

- The logic diagram of a 1:4 demultiplexer using logic gates is shown below :

![1:4 demultiplexer using logic gates](https://circuitverse.org/users/121884/projects/1-4-demultiplexer-using-logic-gates-c228d6b5-1d9b-4a5b-aa57-405a57474f41/master/image.png)

- The circuit consists of four AND gates, two NOT gates and one OR gate. The input D is connected to all the AND gates. The control signals S1 and S0 are used to select the output by enabling or disabling the AND gates. The OR gate is used to combine the outputs of the AND gates and produce the final output Y.
- The working of the circuit can be explained as follows:

  - When S1 = 0 and S0 = 0, the output of the first NOT gate is 1 and the output of the second NOT gate is 1. This enables the first AND gate and disables the other three AND gates. The input D is passed to the output Y0 and the other outputs are 0.
  - When S1 = 0 and S0 = 1, the output of the first NOT gate is 1 and the output of the second NOT gate is 0. This enables the second AND gate and disables the other three AND gates. The input D is passed to the output Y1 and the other outputs are 0.
  - When S1 = 1 and S0 = 0, the output of the first NOT gate is 0 and the output of the second NOT gate is 1. This enables the third AND gate and disables the other three AND gates. The input D is passed to the output Y2 and the other outputs are 0.
  - When S1 = 1 and S0 = 1, the output of the first NOT gate is 0 and the output of the second NOT gate is 0. This enables the fourth AND gate and disables the other three AND gates. The input D is passed to the output Y3 and the other outputs are 0.

- The 1:4 demultiplexer can be used for various applications, such as data distribution, memory addressing, data routing, etc. . It can also be used to implement a decoder by connecting the input D to a constant value, such as 1.