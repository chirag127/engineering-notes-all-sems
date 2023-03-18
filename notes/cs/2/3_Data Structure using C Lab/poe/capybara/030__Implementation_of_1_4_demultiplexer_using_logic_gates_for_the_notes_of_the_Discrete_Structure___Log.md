## Implementation of 1:4 Demultiplexer Using Logic Gates

A demultiplexer, also known as a demux, is a combinational circuit that takes a single input and distributes it to multiple outputs based on the control signals. In this lab, we will be implementing a 1:4 demultiplexer using logic gates.

### Required Components

To build the 1:4 demultiplexer, you will need the following components:

- One 2-input AND gate
- Three 2-input NAND gates
- One NOT gate
- Four LEDs
- Four 220-ohm resistors
- One breadboard
- Connecting wires

### Circuit Diagram

![1:4 Demultiplexer Circuit Diagram](demux.png)

### Circuit Explanation

- The input signal is connected to the AND gate and one input of each NAND gate.
- The other input of each NAND gate is connected to the NOT gate, which inverts the input signal.
- The output of each NAND gate is connected to one LED through a 220-ohm resistor.
- The control signals are connected to the other input of the AND gate and the input of the NOT gate.

When the control signals are set to 00, the output of the AND gate is 0, and all of the NAND gates have a 1 input, which means all the output LEDs are off. When the control signals are set to 01, the output of the AND gate is 0, and the first LED is off while the other three are on. Similarly, when the control signals are set to 10, the output of the AND gate is 0, and the first two LEDs are off while the other two are on. When the control signals are set to 11, the output of the AND gate is 1, and all the output LEDs are on.

### Conclusion

In this lab, we have learned how to implement a 1:4 demultiplexer using logic gates. This circuit can be used in various applications, such as digital communication systems, data transmission, and memory circuits.