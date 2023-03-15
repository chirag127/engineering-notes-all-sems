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

- The circuit uses four AND gates, two NOT gates and one OR gate. The input D is connected to all the AND gates. The control signals S1 and S0 are inverted by the NOT gates and then fed to the AND gates. The output of each AND gate is connected to one of the outputs Y0 to Y3. The OR gate is used to indicate if any output is active or not.
- The 1:4 demultiplexer can be used to implement a 4-bit decoder by connecting the input D to logic 1. It can also be used to distribute a single data line to multiple devices, such as memory chips or LEDs .