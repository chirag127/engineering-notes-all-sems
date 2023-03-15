# Implementing Binary-to-Gray, Gray-to-Binary code conversions

## Binary-to-Gray code conversion

- Binary code is a system of representing numbers, letters, commands, images and sounds using only two symbols: 0 and 1.
- Gray code is a binary numeral system where two successive values differ in only one bit. It is also known as the reflected binary code.
- The conversion from binary code to gray code can be done by using the following steps :
  - Record the most significant bit (MSB) or the leftmost bit of the given binary data as it is, to have MSB of gray equivalent.
  - Proceed towards adding the adjacent bits of the binary data starting from MSB with its adjacent bit to LSB using the XOR (^) operation. The result of each XOR operation is a bit of the gray code.
  - The LSB of the gray code is the same as the LSB of the binary code.
- The logical circuit that performs the binary-to-gray code conversion is known as a binary-to-gray code converter. It consists of XOR gates that take the binary bits as inputs and produce the gray bits as outputs.
- The following is an example of a 4-bit binary-to-gray code converter:

![Binary-to-Gray code converter](https://vlsiverify.com/wp-content/uploads/2019/08/binary-to-gray-code-converter.png)

- The following is the truth table for the 4-bit binary-to-gray code converter:

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

## Gray-to-Binary code conversion

- The conversion from gray code to binary code can be done by using the following steps :
  - Record the MSB or the leftmost bit of the given gray code as it is, to have MSB of binary equivalent.
  - Proceed towards adding the MSB of the binary code with the next bit of the given gray code using the XOR (^) operation. The result of the XOR operation is the next bit of the binary code.
  - Repeat the previous step until all the bits of the gray code are processed.
  - The LSB of the binary code is the same as the LSB of the gray code.
- The logical circuit that performs the gray-to-binary code conversion is known as a gray-to-binary code converter. It consists of XOR gates that take the gray bits as inputs and produce the binary bits as outputs.
- The following is an example of a 4-bit gray-to-binary code converter:

![Gray-to-Binary code converter](https://media.geeksforgeeks.org/wp-content/uploads/20190806164850/gray-to-binary-code-converter.png)

- The following is the truth table for the 4-bit gray-to-binary code converter:

| Gray  | Binary |
|-------|--------|
| 0000  | 0000   |
| 0001  | 0001   |
| 0011  | 0010   |
| 0010  | 0011   |
| 0110  | 0100   |
| 0111  | 0101   |
| 0101  | 0110   |
| 0100  | 0111   |
| 1100  | 1000   |
| 1101  | 1001   |
| 1111  | 1010   |
| 1110  | 1011   |
| 1010  | 1100   |
| 1011  | 1101   |
| 1001  | 1110   |
| 1000  | 1111   |

## References

: https://www.electrical4u.com/binary-to-gray-code-converter