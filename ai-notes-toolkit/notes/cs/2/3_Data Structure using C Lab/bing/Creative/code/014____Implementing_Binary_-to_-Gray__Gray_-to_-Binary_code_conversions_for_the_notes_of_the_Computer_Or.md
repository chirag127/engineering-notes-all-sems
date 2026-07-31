# Implementing Binary-to-Gray, Gray-to-Binary code conversions

## Binary-to-Gray code conversion

- Binary code is a system of representing numbers, letters, commands, images and sounds using only two symbols, 0 and 1.
- Gray code is a binary numeral system where two successive values differ in only one bit. It is also known as the reflected binary code.
- The conversion process from binary code to gray code involves the following steps:
  - Record the most significant bit (MSB) or the leftmost bit of the given binary data as it is, to have MSB of gray equivalent.
  - Proceed towards adding the adjacent bits of the binary data starting from MSB with its adjacent bit to LSB using the XOR (^) operation. The result of each XOR operation is a bit of the gray code.
  - The formula for converting a binary bit b_i to a gray bit g_i is: g_i = b_i ^ b_(i+1), where i is the position of the bit from right to left, starting from 0.
  - The formula for converting the MSB of binary to gray is: g_(n-1) = b_(n-1), where n is the number of bits in the binary code.
- For example, to convert the binary code 1011 to gray code, we follow these steps:
  - Record the MSB of binary as it is, to have MSB of gray equivalent. So, g_3 = b_3 = 1.
  - Add the adjacent bits of the binary code starting from MSB using XOR operation. So, g_2 = b_3 ^ b_2 = 1 ^ 0 = 1, g_1 = b_2 ^ b_1 = 0 ^ 1 = 1, and g_0 = b_1 ^ b_0 = 1 ^ 1 = 0.
  - The gray code is the concatenation of the bits obtained in the previous steps. So, the gray code is 1110.
- The logical circuit which converts the binary code to equivalent gray code is known as binary to gray code converter. An n-bit gray code can be obtained by reflecting an n-bit binary code about an axis after 2^(n-1) rows and putting the MSB of 0 above the axis and the MSB of 1 below the axis.
- The following table shows the conversion of 4-bit binary codes to gray codes using the above method:

| Binary | Gray  |
| ------ | ----- |
| 0000   | 0000  |
| 0001   | 0001  |
| 0010   | 0011  |
| 0011   | 0010  |
| 0100   | 0110  |
| 0101   | 0111  |
| 0110   | 0101  |
| 0111   | 0100  |
| 1000   | 1100  |
| 1001   | 1101  |
| 1010   | 1111  |
| 1011   | 1110  |
| 1100   | 1010  |
| 1101   | 1011  |
| 1110   | 1001  |
| 1111   | 1000  |

- The following is the Verilog code for a 4-bit binary to gray code converter:

```verilog
module b2g_converter # (parameter WIDTH = 4) (
  input [WIDTH-1:0] binary,
  output [WIDTH-1:0] gray
);
  genvar i;
  generate
    for (i = 0; i < WIDTH-1; i++) begin
      assign gray[i] = binary[i] ^ binary[i+1];
    end
  endgenerate
  assign gray[WIDTH-1] = binary[WIDTH-1];
endmodule
```

## Gray-to-Binary code conversion

- Gray code is a binary numeral system where two successive values differ in only one bit. It is also known as the reflected binary code.
- Binary code is a system of representing numbers, letters, commands, images and sounds using only two symbols, 0 and 1.
- The conversion process from gray code to binary code involves the following steps:
  - Record the MSB of gray as it is, to have MSB of binary equivalent.
  - Proceed towards adding the MSB of the binary code with the next bit