## Implementation and verification of Decoder using logic gates for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- A decoder is a combinational circuit constructed with logic gates. It is the reverse of the encoder. A decoder circuit is used to transform a set of digital input signals into an equivalent decimal code of its output.
- A decoder takes n input lines and has 2^n output lines. These output lines can provide the minterms of input variables. Since any boolean function can be expressed as a sum of minterms, a decoder that can generate these minterms along with external OR gates that form their logical sums, can be used to form a circuit of any boolean function.
- A decoder can be implemented using AND, NOT and OR gates. The basic idea is to use one AND gate for each output line, and connect the inputs of the AND gate to the input lines or their complements according to the truth table of the decoder.
- For example, a 3-to-8 decoder has 3 input lines (X, Y, Z) and 8 output lines (D0 to D7). The truth table and the logic circuit of the decoder are shown below:

| X | Y | Z | D0 | D1 | D2 | D3 | D4 | D5 | D6 | D7 |
|---|---|---|----|----|----|----|----|----|----|----|
| 0 | 0 | 0 | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
| 0 | 0 | 1 | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
| 0 | 1 | 0 | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  |
| 0 | 1 | 1 | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  |
| 1 | 0 | 0 | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  |
| 1 | 0 | 1 | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  |
| 1 | 1 | 0 | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  |
| 1 | 1 | 1 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  |

```
D0 = X' Y' Z'
D1 = X' Y' Z
D2 = X' Y Z'
D3 = X' Y Z
D4 = X Y' Z'
D5 = X Y' Z
D6 = X Y Z'
D7 = X Y Z
```

![3-to-8 decoder logic circuit](https://programmerbay.com/wp-content/uploads/2019/03/3-to-8-decoder-logic-circuit.png)

- To verify the decoder using logic gates, we can use a logic gate calculator to input the boolean expressions of the output lines and check if they match the truth table values for different input combinations. Alternatively, we can use a breadboard and some LEDs to physically connect the logic gates and observe the output lights for different input switches.
- A decoder can be extended to have more output lines by using multiple decoders and connecting them with enable inputs. For example, a 4-to-16 decoder can be designed using two 3-to-8 decoders and one 2-to-4 decoder. The 2-to-4 decoder is used to select one of the four enable inputs of the 3-to-8 decoders, and the remaining three input lines are connected to both 3-to-8 decoders. The output lines of the 3-to-8 decoders are combined to form the 16 output lines of