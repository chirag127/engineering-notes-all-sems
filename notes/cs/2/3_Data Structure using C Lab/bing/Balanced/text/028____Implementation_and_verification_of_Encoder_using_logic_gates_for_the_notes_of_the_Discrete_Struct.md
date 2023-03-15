## Implementation and verification of Encoder using logic gates for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- An encoder is a combinational circuit that converts a binary code of n input lines into a binary code of m output lines, where m < n.
- The encoder performs the inverse function of a decoder, which converts a binary code of m input lines into a binary code of n output lines, where n > m.
- The most common types of encoders are priority encoders and binary encoders.
- A priority encoder assigns a unique binary code to the highest priority input that is active among the n inputs. The priority order is usually from the highest input to the lowest input, but it can be reversed as well.
- A binary encoder assigns a unique binary code to each of the n inputs that is active. However, a binary encoder can only work when exactly one input is active at a time. Otherwise, the output will be undefined or erroneous.
- An encoder can be implemented using logic gates such as AND, OR, and NOT gates. The number and type of gates depend on the type and size of the encoder.
- For example, a 4-to-2 priority encoder can be implemented using four 2-input AND gates, two 4-input OR gates, and four NOT gates. The circuit diagram is shown below:

![4-to-2 priority encoder](https://i.imgur.com/9Z0jXZg.png)

- The truth table for the 4-to-2 priority encoder is shown below:

| D3 | D2 | D1 | D0 | Y1 | Y0 |
|----|----|----|----|----|----|
| 0  | 0  | 0  | 0  | 0  | 0  |
| 0  | 0  | 0  | 1  | 0  | 0  |
| 0  | 0  | 1  | 0  | 0  | 1  |
| 0  | 0  | 1  | 1  | 0  | 1  |
| 0  | 1  | 0  | 0  | 1  | 0  |
| 0  | 1  | 0  | 1  | 1  | 0  |
| 0  | 1  | 1  | 0  | 1  | 0  |
| 0  | 1  | 1  | 1  | 1  | 0  |
| 1  | 0  | 0  | 0  | 1  | 1  |
| 1  | 0  | 0  | 1  | 1  | 1  |
| 1  | 0  | 1  | 0  | 1  | 1  |
| 1  | 0  | 1  | 1  | 1  | 1  |
| 1  | 1  | 0  | 0  | 1  | 1  |
| 1  | 1  | 0  | 1  | 1  | 1  |
| 1  | 1  | 1  | 0  | 1  | 1  |
| 1  | 1  | 1  | 1  | 1  | 1  |

- The verification of the encoder can be done by applying different combinations of inputs and observing the corresponding outputs. The outputs should match the expected values from the truth table.
- Alternatively, the verification can be done by using a logic simulator software that can simulate the behavior of the encoder circuit and display the outputs for different inputs.