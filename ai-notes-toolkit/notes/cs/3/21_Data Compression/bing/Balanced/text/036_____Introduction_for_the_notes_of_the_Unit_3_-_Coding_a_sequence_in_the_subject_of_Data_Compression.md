### Introduction for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of a data set by removing redundancy or irrelevant information.
- Data compression can be lossless or lossy, depending on whether the original data can be perfectly reconstructed from the compressed data or not.
- Coding a sequence is a fundamental task in data compression, where a sequence of symbols (such as characters, bits, pixels, etc.) is represented by a shorter sequence of codes (such as binary numbers, Huffman codes, arithmetic codes, etc.).
- Coding a sequence can be done in two ways: fixed-length coding or variable-length coding.
- Fixed-length coding assigns a fixed number of bits to each symbol, regardless of its frequency or importance. For example, ASCII code uses 8 bits to represent each character.
- Variable-length coding assigns a variable number of bits to each symbol, depending on its frequency or importance. For example, Huffman code uses fewer bits to represent more frequent symbols and more bits to represent less frequent symbols.
- Variable-length coding can achieve better compression ratios than fixed-length coding, but it requires more complex algorithms and data structures to encode and decode the sequences.
- Coding a sequence can also be done in two modes: block coding or stream coding.
- Block coding divides the sequence into fixed-size blocks and encodes each block independently. For example, JPEG image compression uses block coding with 8x8 pixel blocks.
- Stream coding encodes the sequence as a continuous stream of bits, without dividing it into blocks. For example, MP3 audio compression uses stream coding with a variable bit rate.
- Stream coding can adapt to the changing characteristics of the sequence, but it requires more synchronization and error correction mechanisms to ensure reliable transmission and decoding.