### The ESCAPE SYMBOL for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- The escape symbol is a special symbol that is used to indicate that a character or a sequence of characters is not in the codebook or the dictionary.
- The escape symbol is usually chosen to be a character that is unlikely to appear in the original data, such as `#`, `@`, or `^`.
- The escape symbol is followed by the raw representation of the character or the sequence of characters that is not in the codebook or the dictionary.
- The escape symbol allows the encoder and the decoder to handle new or rare symbols that are not in the codebook or the dictionary, without having to update or transmit the codebook or the dictionary.
- The escape symbol also allows the encoder and the decoder to handle variable-length codes, such as Huffman codes or Lempel-Ziv codes, without having to use end-of-block markers or padding bits.
- The escape symbol can improve the compression ratio if the frequency of new or rare symbols is low, but it can also degrade the compression ratio if the frequency of new or rare symbols is high, or if the raw representation of the symbols is longer than the codebook or the dictionary entries.