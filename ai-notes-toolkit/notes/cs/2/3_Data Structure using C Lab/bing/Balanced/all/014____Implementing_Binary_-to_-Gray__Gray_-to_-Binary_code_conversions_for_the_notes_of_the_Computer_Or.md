# Implementing Binary-to-Gray, Gray-to-Binary code conversions

## Binary-to-Gray code conversion

- Binary code is a system of representing numbers, letters, commands, images and sounds using two symbols, usually 0 and 1.
- Gray code is a binary code system where two successive values differ in only one bit. It is also known as the reflected binary code.
- The conversion from binary code to gray code can be done by using the following logic  :

  - The most significant bit (MSB) or the leftmost bit of the binary code is copied as it is to the MSB of the gray code.
  - The remaining bits of the gray code are obtained by performing the exclusive-OR (XOR) operation between the corresponding and adjacent bits of the binary code, starting from the MSB and moving towards the least significant bit (LSB).

- For example, to convert the binary code 1011 to gray code, we follow these steps:

  - The MSB of the binary code is 1, so we copy it to the MSB of the gray code: 1___
  - The next bit of the binary code is 0, so we XOR it with the previous bit 1: 1 XOR 0 = 1. We append this result to the gray code: 11__
  - The next bit of the binary code is 1, so we XOR it with the previous bit 0: 0 XOR 1 = 1. We append this result to the gray code: 111_
  - The LSB of the binary code is 1, so we XOR it with the previous bit 1: 1 XOR 1 = 0. We append this result to the gray code: 1110

- Therefore, the gray code equivalent of 1011 is 1110.

- The binary-to-gray code conversion can be implemented using a combinational circuit with XOR gates. The following is a Verilog code for a 4-bit binary-to-gray code converter:

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

## Gray-to-Binary code conversion

- The conversion from gray code to binary code can be done by using the following logic :

  - The MSB of the gray code is copied as it is to the MSB of the binary code.
  - The remaining bits of the binary code are obtained by performing the XOR operation between the corresponding bit of the gray code and the previous bit of the binary code, starting from the MSB and moving towards the LSB.

- For example, to convert the gray code 1100 to binary code, we follow these steps:

  - The MSB of the gray code is 1, so we copy it to the MSB of the binary code: 1___
  - The next bit of the gray code is 1, so we XOR it with the previous bit of the binary code 1: 1 XOR 1 = 0. We append this result to the binary code: 10__
  - The next bit of the gray code is 0, so we XOR it with the previous bit of the binary code 0: 0 XOR 0 = 0. We append this result to the binary code: 100_
  - The LSB of the gray code is 0, so we XOR it with the previous bit of the binary code 0: 0 XOR 0 = 0. We append this result to the binary code: 1000

- Therefore, the binary code equivalent of 1100 is 1000.

- The gray-to-binary code conversion can be implemented using a combinational circuit with XOR gates. The following is a Verilog code for a 4-bit gray-to-binary code converter:

```verilog
module g2b_converter # (parameter WIDTH =4) (
  input [ WIDTH -1:0] gray,
  output [ WIDTH -1:0] binary
);
  genvar i;
  generate

```
