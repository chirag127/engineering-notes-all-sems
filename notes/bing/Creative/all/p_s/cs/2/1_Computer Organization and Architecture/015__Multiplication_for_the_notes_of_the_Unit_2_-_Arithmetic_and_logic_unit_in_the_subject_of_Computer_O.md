### Multiplication

Multiplication is an arithmetic operation that computes the product of two binary numbers. It is frequently required in computer applications, such as graphics, cryptography, and signal processing. There are different algorithms for performing multiplication, depending on the representation and size of the operands.

Some of the common multiplication algorithms are:

- **Shift-and-add algorithm**: This is the simplest and most intuitive method of multiplying two binary numbers. It is based on the idea of multiplying by powers of two, which can be done by shifting the multiplicand left and adding it to a partial product. The algorithm consists of the following steps:

  - Initialize the partial product to zero.
  - For each bit of the multiplier, starting from the least significant bit:
    - If the bit is 1, add the multiplicand to the partial product.
    - Shift the partial product and the multiplicand left by one bit.
  - The final partial product is the result of the multiplication.

  For example, to multiply 1101 (13) by 1010 (10), we can use the shift-and-add algorithm as follows:

  ```
  Partial product   Multiplier   Multiplicand
  0000              1010         1101
  1101              1010         1101
  11010             101          11010
  11010             101          11010
  110100            10           110100
  110100            10           110100
  1101000           1            1101000
  10011101          0            11010000
  10011101          0            11010000
  ```

  The result is 10011101 (157), which is the correct product of 13 and 10.

  The shift-and-add algorithm has some advantages and disadvantages:

  - Advantages:
    - It is simple and easy to implement in hardware or software.
    - It works for any representation of the operands, such as unsigned, signed-magnitude, or two's complement.
    - It can be extended to handle fractional or floating-point numbers by adjusting the position of the decimal point.
  - Disadvantages:
    - It is slow, as it requires n iterations for n-bit operands, where each iteration involves a shift and an add operation.
    - It can overflow if the result is larger than the word size of the computer.

- **Booth's algorithm**: This is a multiplication algorithm that multiplies two signed binary numbers in two's complement notation. It was invented by Andrew Donald Booth in 1950 while doing research on crystallography at Birkbeck College in Bloomsbury, London. Booth's algorithm is of interest in the study of computer architecture.

  Booth's algorithm is based on the observation that a string of consecutive 1s in the multiplier can be treated as a single unit, and that a string of 0s can be skipped. The algorithm uses a special encoding of the multiplier, called the Booth's code, which is obtained by adding a 0 to the right of the multiplier and then taking the difference of each pair of adjacent bits. For example, the Booth's code of 1010 is 0110, and the Booth's code of 1101 is 1001.

  The algorithm consists of the following steps:

  - Initialize the partial product to zero and extend it by one bit to the left.
  - Encode the multiplier using the Booth's code and extend it by one bit to the right.
  - For each bit of the Booth's code, starting from the rightmost bit:
    - If the bit pair is 01, subtract the multiplicand from the partial product.
    - If the bit pair is 10, add the multiplicand to the partial product.
    - If the bit pair is 00 or 11, do nothing.
    - Shift the partial product and the Booth's code right by one bit, with sign extension.
  - The final partial product, without the extra bit, is the result of the multiplication.

  For example, to multiply 1101 (-3) by 1010 (-6), we can use the Booth's algorithm as follows:

  ```
  Partial product   Booth's code   Multiplicand
  00000             10010          1101
  00000             1001           1101
  01101             100            11010
  00110             10             110100
  11111             1

Some possible mnemonics and learning tricks for the topic are:

- To remember the steps of the shift-and-add algorithm, you can use the acronym SASHA: Shift, Add, Shift, Add, ...
- To remember the steps of the Booth's algorithm, you can use the acronym BASS: Booth's code, Add, Subtract, Shift.
- To remember the Booth's code of a binary number, you can use the following rules:
  - If the number ends with 0, add 0 to the right and take the difference of each pair of adjacent bits.
  - If the number ends with 1, add 1 to the right and take the complement of the difference of each pair of adjacent bits.
  - For example, the Booth's code of 1010 is 0110, and the Booth's code of 1101 is 1001.