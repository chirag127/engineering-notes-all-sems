## Implementing 3-8 line DECODER for the notes of the Computer Organization Lab in the subject of Computer Organization

- A 3-8 line decoder is a digital circuit that converts a 3-bit binary input into an 8-bit output, where only one of the output lines is high (logic 1) and the rest are low (logic 0).
- The output line that is high corresponds to the decimal value of the input binary code. For example, if the input is 010, the output line 2 is high and the rest are low.
- A 3-8 line decoder can be implemented using logic gates, such as AND, OR and NOT gates. The truth table and the logic diagram of a 3-8 line decoder are shown below:

| Input | Output |
|:-----:|:------:|
| A B C | Y0 Y1 Y2 Y3 Y4 Y5 Y6 Y7 |
| 0 0 0 | 1  0  0  0  0  0  0  0 |
| 0 0 1 | 0  1  0  0  0  0  0  0 |
| 0 1 0 | 0  0  1  0  0  0  0  0 |
| 0 1 1 | 0  0  0  1  0  0  0  0 |
| 1 0 0 | 0  0  0  0  1  0  0  0 |
| 1 0 1 | 0  0  0  0  0  1  0  0 |
| 1 1 0 | 0  0  0  0  0  0  1  0 |
| 1 1 1 | 0  0  0  0  0  0  0  1 |

![Logic diagram of 3-8 line decoder](https://i.imgur.com/0y9W8Vj.png)

- A 3-8 line decoder can be used for various applications, such as selecting one of eight devices or memory locations, generating control signals, or implementing combinational functions.