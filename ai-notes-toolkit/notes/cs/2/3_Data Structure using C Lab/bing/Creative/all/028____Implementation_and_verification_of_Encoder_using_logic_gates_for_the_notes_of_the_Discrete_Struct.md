# Implementation and verification of Encoder using logic gates for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- An encoder is a digital circuit that converts a set of binary inputs into a unique binary code.
- The binary code represents the position of the input and is used to identify the specific input that is active.
- Encoders are commonly used in digital systems to convert a parallel set of inputs into a serial code.
- There are different types of encoders, such as 4, 8, and 16 encoders, and the truth table of encoders depends upon a particular encoder chosen by the user.
- A simple encoder is a combinational logic circuit that can be used to convert 2^n lines of digital input into n bits of coded binary output.
- However, in a simple encoder, only one of the inputs is considered to be high out of all the 2^n inputs.
- A simple encoder can be implemented using OR gates.
- For example, a 4-bit encoder can be designed as follows:

![4-bit encoder using OR gates](https://circuitdigest.com/sites/default/files/circuitdiagram_mic/4-bit-Encoder-Circuit-Diagram.png)

- The truth table of the 4-bit encoder is:

| Input | Output |
|:-----:|:------:|
| D0    | 00     |
| D1    | 01     |
| D2    | 10     |
| D3    | 11     |

- The Boolean expressions for the output bits are:

Y0 = D1 + D3

Y1 = D2 + D3

- To verify the encoder using logic gates, we can use a breadboard, LEDs, switches, and OR gate ICs.
- The steps are:

  - Connect the power supply to the breadboard and the OR gate ICs.
  - Connect the switches to the inputs of the OR gate ICs and the LEDs to the outputs of the OR gate ICs.
  - Connect the inputs and outputs of the OR gate ICs according to the circuit diagram.
  - Turn on the power supply and test the encoder by changing the switch positions and observing the LED states.
  - Compare the LED states with the truth table and verify that the encoder works correctly.