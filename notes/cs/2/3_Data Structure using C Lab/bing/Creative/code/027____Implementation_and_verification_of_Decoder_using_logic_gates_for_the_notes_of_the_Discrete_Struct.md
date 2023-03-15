## Implementation and verification of Decoder using logic gates for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

- A decoder is a combinational circuit constructed with logic gates. It is the reverse of the encoder. A decoder circuit is used to transform a set of digital input signals into an equivalent decimal code of its output.
- A decoder takes n input lines and has 2^n output lines. These output lines can provide the minterms of input variables. Since any boolean function can be expressed as a sum of minterms, a decoder that can generate these minterms along with external OR gates that form their logical sums, can be used to form a circuit of any boolean function.
- A decoder can be designed using AND, NOT and OR gates. The basic idea is to use one AND gate for each output line, and connect the inputs of the AND gate to the input lines or their complements according to the truth table of the decoder.
- For example, a 3-to-8 decoder can be implemented as follows:

![3-to-8 decoder](https://programmerbay.com/wp-content/uploads/2019/10/3-to-8-decoder.png)

- The truth table of the 3-to-8 decoder is:

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

- The logic expressions for each output line are:

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

- To verify the decoder, we can use a logic gate calculator to input the logic expressions and the input values, and check if the output values match the truth table. For example, if we input X = 0, Y = 1, Z = 0, we should get D0 = 0, D1 = 0, D2 = 1, D3 = 0, D4 = 0, D5 = 0, D6 = 0, D7 = 0.
- A 4-to-16 decoder can be designed using two 3-to-8 decoders and one 2-to-4 decoder. The idea is to use the 2-to-4 decoder to select one of the four 3-to-8 decoders, and then use the remaining three input lines to decode the output of the selected 3-to-8 decoder.
- The implementation of the 4-to-16 decoder is as follows[^