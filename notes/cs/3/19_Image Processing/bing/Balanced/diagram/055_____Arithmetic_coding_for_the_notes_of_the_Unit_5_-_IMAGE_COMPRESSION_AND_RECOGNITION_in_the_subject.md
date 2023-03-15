### Arithmetic coding for image compression

Arithmetic coding is a lossless compression technique that assigns a variable-length code to each symbol based on its probability of occurrence in the source data. Unlike Huffman coding, which assigns a fixed number of bits to each symbol, arithmetic coding can assign fractional bits to each symbol, resulting in higher compression ratios.

The basic idea of arithmetic coding is to represent the entire source data as a single fraction in the range [0, 1). This fraction is obtained by recursively dividing the range into subranges according to the probabilities of the symbols. The final code is the binary representation of the fraction.

The steps of arithmetic coding are as follows:

- Initialize the range to [0, 1).
- For each symbol in the source data, do the following:
  - Divide the range into subranges according to the probabilities of the symbols in the alphabet.
  - Select the subrange that corresponds to the current symbol and update the range to that subrange.
  - If the range becomes too small or too large, output the most significant bit of the range and shift the range to the left by one bit.
- Output the remaining bits of the range as the final code.

For example, suppose the source data is "ABAC" and the alphabet is {A, B, C} with probabilities {0.5, 0.25, 0.25}. The arithmetic coding process is shown below:

| Symbol | Range | Subranges | Output |
|--------|-------|-----------|--------|
| A      | [0, 1) | [0, 0.5), [0.5, 0.75), [0.75, 1) | None |
| B      | [0, 0.5) | [0, 0.25), [0.25, 0.375), [0.375, 0.5) | None |
| A      | [0.25, 0.375) | [0.25, 0.3125), [0.3125, 0.34375), [0.34375, 0.375) | None |
| C      | [0.34375, 0.375) | [0.34375, 0.359375), [0.359375, 0.3671875), [0.3671875, 0.375) | 0 |
| None   | [0.3671875, 0.375) | N/A | 0110 |

The final code is 00110, which is 6 in decimal. The original data is 4 symbols, each with 2 bits, so the total size is 8 bits. The compressed data is 5 bits, so the compression ratio is 8/5 = 1.6.

To decode the arithmetic code, the decoder needs to know the probabilities of the symbols and the length of the code. The decoder performs the inverse process of the encoder, as follows:

- Initialize the range to [0, 1) and the code to the binary fraction of the input bits.
- For each symbol to be decoded, do the following:
  - Divide the range into subranges according to the probabilities of the symbols in the alphabet.
  - Select the subrange that contains the code and output the corresponding symbol.
  - Update the range to that subrange.
  - If the range becomes too small or too large, shift the range to the right by one bit and read the next bit of the code.

For example, suppose the code is 00110 and the alphabet is {A, B, C} with probabilities {0.5, 0.25, 0.25}. The arithmetic decoding process is shown below:

| Code | Range | Subranges | Output |
|------|-------|-----------|--------|
| 0.0110 | [0, 1) | [0, 0.5), [0.5, 0.75), [0.75, 1) | A |
| 0.0110 | [0, 0.5) | [0, 0.25), [0.25, 0.375), [0.375, 0.5) | B |
| 0.0110 | [0.25, 0.375) | [0.25, 0.3125), [0.3125, 0.34375), [0.34375, 0.375) | A |
| 0.0110 | [0