## Implementation and verification of Encoder using logic gates

An encoder is a digital circuit that converts a set of binary inputs into a unique binary code. The binary code represents the position of the input and is used to identify the specific input that is active. Encoders are commonly used in digital systems to convert a parallel set of inputs into a serial code.

There are different types of encoders, such as 4, 8, and 16 encoders. The truth table of an encoder depends on the number of inputs and the encoding scheme. A simple encoder assumes that only one input is high at a time  .

For example, an 8-to-3 encoder has 8 inputs and 3 outputs. It can encode the position of the active input into a 3-bit binary code. The truth table and the circuit diagram of an 8-to-3 encoder using OR gates are shown below .

| Inputs | Outputs |
|:------:|:-------:|
| D0 D1 D2 D3 D4 D5 D6 D7 | Y0 Y1 Y2 |
| 1 0 0 0 0 0 0 0 | 0 0 0 |
| 0 1 0 0 0 0 0 0 | 0 0 1 |
| 0 0 1 0 0 0 0 0 | 0 1 0 |
| 0 0 0 1 0 0 0 0 | 0 1 1 |
| 0 0 0 0 1 0 0 0 | 1 0 0 |
| 0 0 0 0 0 1 0 0 | 1 0 1 |
| 0 0 0 0 0 0 1 0 | 1 1 0 |
| 0 0 0 0 0 0 0 1 | 1 1 1 |

![8-to-3 encoder circuit diagram](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/8-3-Encoder-Circuit-Diagram.png)

To implement and verify the encoder using logic gates, the following steps can be followed:

- Connect the inputs D0 to D7 to the switches or logic level generators.
- Connect the outputs Y0 to Y2 to the LEDs or logic probes.
- Connect the OR gates as shown in the circuit diagram.
- Apply power to the circuit and test the inputs and outputs.
- Verify that the outputs match the truth table for each input combination.
- Record the observations and results.