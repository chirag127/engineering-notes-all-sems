 Here is the content in markdown format for the topic ### uniquely decodable codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression:

### Uniquely Decodable Codes

- Uniquely decodable codes are codes where each codeword is mapped to only one source symbol. This means that the decoder can always uniquely determine the original input from the codeword.
- Examples of uniquely decodable codes are:

1. Fixed-length codes: In fixed-length codes, each source symbol is mapped to a codeword of fixed length `k`. Since the codewords have fixed length, the decoder can always uniquely decode the original symbol from the codeword. For example, a ASCII code is a fixed-length uniquely decodable code.

2. Prefix codes: In prefix codes, no codeword is a prefix of another codeword. Due to this prefix property, the decoder can always uniquely decode the original symbol from the codeword. For example, Huffman codes are prefix codes and hence uniquely decodable.

3. Unary codes: In unary codes, each source symbol is mapped to a string of `k` number of 1's, where `k` is the index of the source symbol. Since each source symbol has a unique index, unary codes are uniquely decodable codes.

Advantages:

- Uniquely decodable codes ensure that the original input can always be recovered from the encoded output without any ambiguity. This is essential for lossless data compression.

Disadvantages:

- The coding efficiency of uniquely decodable codes may not be very high as the mapping from source symbols to codewords is one-to-one.

Applications:

- Uniquely decodable codes are used in lossless data compression techniques like Huffman coding, fixed-length coding, etc. where recovering the original input from the encoded output is important.