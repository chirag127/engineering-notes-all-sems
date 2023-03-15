## Implementation and verification of Encoder using logic gates for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- An encoder is a digital circuit that converts a set of binary inputs into a unique binary code.
- The binary code represents the position of the input and is used to identify the specific input that is active.
- Encoders are commonly used in digital systems to convert a parallel set of inputs into a serial code.
- An encoder can be represented by the general expression: E = f (D0, D1, D2, ..., D2^n-1), where E is the n-bit output code and D0 to D2^n-1 are the 2^n input lines.
- A simple encoder is a combinational logic circuit that can be used to convert 2^n lines of digital input into n bits of coded binary output.
- However, in a simple encoder, only one of the inputs is considered to be high out of all the 2^n inputs.
- If more than one input is high, the output is undefined or invalid.
- A simple encoder can be implemented using OR gates.
- For example, a 4-bit encoder can be designed as follows:

![4-bit encoder using OR gates](https://www.watelectronics.com/wp-content/uploads/2019/07/4-bit-Encoder.png)

- The truth table of the 4-bit encoder is:

| D0 | D1 | D2 | D3 | E1 | E0 |
|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 0  |
| 1  | 0  | 0  | 0  | 0  | 0  |
| 0  | 1  | 0  | 0  | 0  | 1  |
| 0  | 0  | 1  | 0  | 1  | 0  |
| 0  | 0  | 0  | 1  | 1  | 1  |
| X  | X  | X  | X  | X  | X  |

- Where X denotes an invalid or undefined output.
- To verify the encoder using logic gates, we can use a breadboard, LEDs, switches, resistors, and an OR gate IC.
- The steps are as follows:

  - Connect the power supply to the breadboard and the OR gate IC.
  - Connect the four switches to the input pins of the OR gate IC through resistors.
  - Connect the two output pins of the OR gate IC to the LEDs through resistors.
  - Turn on the power supply and test the encoder by toggling the switches and observing the LEDs.
  - Compare the output with the truth table and verify the functionality of the encoder.

- The circuit diagram of the encoder using logic gates is:

![Encoder using logic gates circuit diagram](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/Encoder-Circuit-Diagram.jpg)