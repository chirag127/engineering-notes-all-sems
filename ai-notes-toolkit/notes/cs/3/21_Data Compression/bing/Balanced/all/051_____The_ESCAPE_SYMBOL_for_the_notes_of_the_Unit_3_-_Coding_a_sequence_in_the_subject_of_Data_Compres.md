# The ESCAPE SYMBOL for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The ESCAPE SYMBOL is a special symbol that is used to indicate that a character in a sequence is not in the codebook.
- The ESCAPE SYMBOL is usually chosen to be a character that is unlikely to appear in the sequence, such as `#` or `*`.
- The ESCAPE SYMBOL is followed by the binary representation of the character that is not in the codebook, using a fixed number of bits.
- The ESCAPE SYMBOL allows the encoder to handle any character that is not in the codebook, without having to update the codebook or send it to the decoder.
- The ESCAPE SYMBOL also allows the encoder to adapt to changes in the source distribution, by adding new characters to the codebook as they appear in the sequence.
- The ESCAPE SYMBOL has a trade-off between the size of the codebook and the length of the encoded sequence. A smaller codebook requires fewer bits to represent each character, but also increases the probability of using the ESCAPE SYMBOL. A larger codebook reduces the use of the ESCAPE SYMBOL, but also increases the number of bits needed for each character.
- The ESCAPE SYMBOL can be combined with other coding techniques, such as Huffman coding or arithmetic coding, to improve the compression ratio.