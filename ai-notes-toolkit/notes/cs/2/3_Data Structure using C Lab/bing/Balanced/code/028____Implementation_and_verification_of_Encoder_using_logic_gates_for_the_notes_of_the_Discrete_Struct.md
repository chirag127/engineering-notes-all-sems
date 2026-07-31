# Implementation and verification of Encoder using logic gates

An encoder is a digital circuit that converts a set of binary inputs into a unique binary code. The binary code represents the position of the input and is used to identify the specific input that is active. Encoders are commonly used in digital systems to convert a parallel set of inputs into a serial code.

A simple encoder has 2^n inputs and n outputs, where only one of the inputs is considered to be high at a time. For example, a 4-bit encoder has 4 inputs and 2 outputs, as shown below:

![4-bit encoder](https://technobyte.org/wp-content/uploads/2019/07/4-bit-encoder.png)

The truth table of a 4-bit encoder is:

| Inputs | Outputs |
|--------|---------|
| D0 | 00 |
| D1 | 01 |
| D2 | 10 |
| D3 | 11 |

The logic expression for the outputs can be obtained by using OR gates as follows:

Y0 = D1 + D3

Y1 = D2 + D3

The circuit diagram of a 4-bit encoder using OR gates is:

![4-bit encoder circuit](https://technobyte.org/wp-content/uploads/2019/07/4-bit-encoder-circuit.png)

To implement and verify the encoder using logic gates, we need the following components:

- A 4-input OR gate IC (such as 74LS32)
- A breadboard
- A power supply
- Four push buttons
- Two LEDs
- Resistors
- Connecting wires

The steps to implement and verify the encoder are:

- Connect the power supply to the breadboard and the Vcc and GND pins of the IC.
- Connect the four push buttons to the inputs of the IC and the two LEDs to the outputs of the IC, as shown in the circuit diagram.
- Connect resistors between the push buttons and the GND, and between the LEDs and the Vcc, to limit the current flow.
- Turn on the power supply and test the encoder by pressing the push buttons one at a time and observing the LEDs.
- Verify that the LEDs display the correct binary code for each input, as per the truth table.