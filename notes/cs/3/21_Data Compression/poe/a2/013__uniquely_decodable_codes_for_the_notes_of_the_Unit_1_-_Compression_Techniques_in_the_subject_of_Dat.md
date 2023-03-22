 Here is the content in markdown format without any emojis or external links:

### Uniquely Decodable Codes

- A code is uniquely decodable if no two codewords have the same decoding. This is a necessary condition for a code to be useful for compression.
- For example, if the codewords 11 and 10 are used to represent the symbols A and B respectively, then the sequence 1110 can be decoded in two ways - AAB or ABA. This ambiguity makes the code unusable.
- A variable-length code can be uniquely decodable if we assign codewords in such a way that no codeword is the prefix of another codeword.
- For example, if A is coded as 0, B is coded as 10 and C is coded as 110, then this code is uniquely decodable. The codeword for each symbol is different from the beginning.
- Uniquely decodable codes are required for prefix codes which are a type of variable-length codes. Huffman coding produces prefix codes and thus produces uniquely decodable codes.
- Uniquely decodable codes are necessary to avoid ambiguity during decoding and ensure proper reconstruction of the original data from the compressed bitstream.

The content is written in points and in a formal tone without any feelings or friendliness as instructed. The emojis and external links are avoided. The content is written inside the header and in markdown format as asked. Let me know if you would like me to modify or expand the content.