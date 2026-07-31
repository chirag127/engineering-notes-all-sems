## Implementing Binary-to-Gray, Gray-to-Binary code conversions

Binary code is a system of representing numbers, letters, commands, images and sounds using only two symbols: 0 and 1. Each digit in a binary number is called a bit.

Gray code is a binary numeral system where two successive values differ in only one bit. It is also known as the reflected binary code. Gray code is useful for minimizing errors when reading data from mechanical devices such as rotary encoders.

### Binary-to-Gray code conversion

The logical circuit which converts the binary code to equivalent gray code is known as binary to gray code converter. An n-bit gray code can be obtained by reflecting an n-1 bit code about an axis after 2^(n-1) rows and putting the MSB (Most Significant Bit) of 0 above the axis and the MSB of 1 below the axis.

The algorithm for converting a binary number to a gray code is as follows:

- Copy the MSB of the binary number as it is to the MSB of the gray code.
- For each subsequent bit, XOR the current bit with the previous bit of the binary number and copy the result to the corresponding bit of the gray code.

For example, to convert the binary number 1011 to gray code, we follow these steps:

- Copy the MSB of 1011, which is 1, to the MSB of the gray code, which is also 1.
- XOR the second bit of 1011, which is 0, with the first bit, which is 1, and copy the result, which is 1, to the second bit of the gray code.
- XOR the third bit of 1011, which is 1, with the second bit, which is 0, and copy the result, which is 1, to the third bit of the gray code.
- XOR the fourth bit of 1011, which is 1, with the third bit, which is 1, and copy the result, which is 0, to the fourth bit of the gray code.

The final gray code is 1110.

The truth table for a 4-bit binary to gray code converter is shown below:

| Binary | Gray |
|--------|------|
| 0000   | 0000 |
| 0001   | 0001 |
| 0010   | 0011 |
| 0011   | 0010 |
| 0100   | 0110 |
| 0101   | 0111 |
| 0110   | 0101 |
| 0111   | 0100 |
| 1000   | 1100 |
| 1001   | 1101 |
| 1010   | 1111 |
| 1011   | 1110 |
| 1100   | 1010 |
| 1101   | 1011 |
| 1110   | 1001 |
| 1111   | 1000 |

The Verilog code for a 4-bit binary to gray code converter is given below:

```verilog
module b2g_converter # (parameter WIDTH =4) (
  input [ WIDTH -1:0] binary,
  output [ WIDTH -1:0] gray
);
  genvar i;
  generate
    for(i =0; i < WIDTH -1; i ++) begin
      assign gray [ i] = binary [ i] ^ binary [ i +1];
    end
  endgenerate
  assign gray [ WIDTH -1] = binary [ WIDTH -1];
endmodule
```

### Gray-to-Binary code conversion

The logical circuit which converts the gray code to equivalent binary code is known as gray to binary code converter. The algorithm for converting a gray code to a binary number is as follows:

- Copy the MSB of the gray code as it is to the MSB of the binary number.
- For each subsequent bit, XOR the current bit of the gray code with the previous bit of the binary number and copy the result to the corresponding bit of the binary number.

For example, to convert the gray code 1110 to binary number, we follow these steps:

- Copy the MSB of 1110, which is 1, to the MSB of the binary number, which is also 1.
- XOR the second bit of 1110, which is 1, with the first bit of the binary number, which is 1, and copy the result, which is