## Implementation and verification of Encoder using logic gates for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- An encoder is a digital circuit that converts a set of binary inputs into a unique binary code.
- The binary code represents the position of the input and is used to identify the specific input that is active.
- Encoders are commonly used in digital systems to convert a parallel set of inputs into a serial code.
- An encoder can be designed with logic gates such as OR gates.
- There are different types of encoders, such as 4, 8, and 16 encoders, and the truth table of encoders depends upon a particular encoder chosen by the user.
- A simple encoder is one that assumes that only one of the inputs is high out of all the possible inputs.
- A priority encoder is one that assigns priority to the inputs and gives the output corresponding to the highest priority input.
- A 4-bit encoder is an example of a simple encoder that has four inputs and two outputs.
- The truth table of a 4-bit encoder is as follows:

| Input | Output |
|-------|--------|
| 0001  | 00     |
| 0010  | 01     |
| 0100  | 10     |
| 1000  | 11     |

- The circuit diagram of a 4-bit encoder using OR gates is as follows:

```
    A B
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |
    | |    +---+
    | +----|   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    +------+---| OR
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    +------+---| OR
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    +------+---| OR
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    +------+---| OR
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    |      |   |
    +------+---+
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           Y
```

- To implement and verify the encoder using logic gates, the following steps can be followed:

  - Connect the inputs A, B, C, and D to four switches or buttons.
  - Connect the outputs Y and Z to two LEDs or display devices.
  - Connect the OR gates as shown in the circuit diagram.
  - Apply power to the circuit and test the inputs and outputs.
  - Observe the output LEDs or display devices and compare them with the truth table.
  - Verify that the output is correct for each input combination.