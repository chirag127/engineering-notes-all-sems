## Implementation of 1:4 demultiplexer using logic gates

A demultiplexer is a digital circuit that takes one input signal and distributes it to one of several output signals according to a set of selection signals. A 1:4 demultiplexer has one input (D), two selection signals (S1 and S0) and four outputs (Y0 to Y3). The input signal is directed to one of the four outputs based on the binary value of the selection signals. The truth table and the block diagram of a 1:4 demultiplexer are shown below.

| S1 | S0 | Y0 | Y1 | Y2 | Y3 |
|----|----|----|----|----|----|
| 0  | 0  | D  | 0  | 0  | 0  |
| 0  | 1  | 0  | D  | 0  | 0  |
| 1  | 0  | 0  | 0  | D  | 0  |
| 1  | 1  | 0  | 0  | 0  | D  |

![Block diagram of 1:4 demultiplexer](https://www.tutorialspoint.com/digital_circuits/images/demultiplexer_1x4.jpg)

A 1:4 demultiplexer can be implemented using logic gates as follows:

- The input signal D is connected to the inputs of four AND gates.
- The selection signals S1 and S0 are used to control the enabling of the AND gates using NOT and OR gates.
- The output of each AND gate is connected to one of the outputs Y0 to Y3.

The logic diagram of a 1:4 demultiplexer using logic gates is shown below.

![Logic diagram of 1:4 demultiplexer using logic gates](https://circuitverse.org/simulator/embed/1-4-demultiplexer-using-logic-gates-c228d6b5-1d9b-4a5b-aa57-405a57474f41)

The working of the circuit can be verified by observing the output signals for different combinations of the input and selection signals. For example, when D = 1, S1 = 0 and S0 = 1, the output Y1 will be 1 and the rest of the outputs will be 0. This corresponds to the second row of the truth table.

A 1:4 demultiplexer can be used for various applications, such as:

- Routing a single data signal to one of several devices
- Converting a serial data signal to a parallel data signal
- Expanding the output capability of a decoder
- Implementing a state machine with multiple outputs