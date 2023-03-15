## Implementing Binary-to-Gray, Gray-to-Binary code conversions for the notes of the Computer Organization Lab in the subject of Computer Organization

- Binary code is a way of representing information using only two symbols: 0 and 1.
- Gray code is a binary code where two successive values differ in only one bit. It is also known as the reflected binary code.
- Binary-to-Gray code conversion is the process of converting a binary number to its equivalent Gray code value.
- Gray-to-Binary code conversion is the process of converting a Gray code number to its equivalent binary value.
- The following are the steps and logic for both conversions:

### Binary-to-Gray code conversion
- Record the most significant bit (MSB) or the leftmost bit of the given binary number as it is, to have the MSB of the Gray code equivalent.
- Proceed towards adding the adjacent bits of the binary number starting from the MSB with its adjacent bit to the least significant bit (LSB) using the XOR (^) operation. The result of each XOR operation is a bit of the Gray code equivalent.
- For example, to convert the binary number 1011 to Gray code, we follow these steps:

| Binary | 1 | 0 | 1 | 1 |
|--------|---|---|---|---|
| Gray   | 1 | 1 | 1 | 0 |

- The MSB of the Gray code is the same as the MSB of the binary number: 1
- The second bit of the Gray code is the XOR of the first and second bits of the binary number: 1 ^ 0 = 1
- The third bit of the Gray code is the XOR of the second and third bits of the binary number: 0 ^ 1 = 1
- The LSB of the Gray code is the XOR of the third and fourth bits of the binary number: 1 ^ 1 = 0
- Therefore, the Gray code equivalent of 1011 is 1110.

### Gray-to-Binary code conversion
- Record the MSB or the leftmost bit of the given Gray code number as it is, to have the MSB of the binary equivalent.
- Proceed towards adding the MSB of the Gray code with its adjacent bit using the XOR (^) operation. The result of the XOR operation is the second bit of the binary equivalent.
- Repeat the XOR operation with the previous bit of the binary equivalent and the next bit of the Gray code until the LSB is reached. The result of each XOR operation is a bit of the binary equivalent.
- For example, to convert the Gray code number 1100 to binary, we follow these steps:

| Gray   | 1 | 1 | 0 | 0 |
|--------|---|---|---|---|
| Binary | 1 | 0 | 1 | 0 |

- The MSB of the binary number is the same as the MSB of the Gray code: 1
- The second bit of the binary number is the XOR of the MSB of the Gray code and the second bit of the Gray code: 1 ^ 1 = 0
- The third bit of the binary number is the XOR of the previous bit of the binary number and the third bit of the Gray code: 0 ^ 0 = 0
- The LSB of the binary number is the XOR of the previous bit of the binary number and the LSB of the Gray code: 0 ^ 0 = 0
- Therefore, the binary equivalent of 1100 is 1010.

- The following is the Verilog code for implementing a binary-to-Gray code converter using a parameterized module and a generate statement:

```verilog
module b2g_converter # (parameter WIDTH =4) (input [ WIDTH -1:0] binary, output [ WIDTH -1:0] gray);
  genvar i;
  generate
    for(i =0; i < WIDTH -1; i ++) begin
      assign gray [ i] = binary [ i] ^ binary [ i +1];
    end
  endgenerate
  assign gray [ WIDTH -1] = binary [ WIDTH -1];
endmodule
```

- The following is the Verilog code for implementing a Gray-to-binary code converter using a parameterized module and a generate statement:

```verilog
module g2b_converter # (parameter WIDTH =4) (input [ WIDTH -1:0] gray, output [ WIDTH -1:0] binary);
  genvar i;