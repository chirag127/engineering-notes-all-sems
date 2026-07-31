# Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- A prefix code is a type of code that assigns binary codewords to symbols such that no codeword is a prefix of another codeword.
- Prefix codes are also known as prefix-free codes, prefix condition codes and instantaneous codes.
- Prefix codes have the property of unique decodability, which means that any encoded message can be unambiguously decoded without any ambiguity or error.
- Prefix codes are widely used in applications that compress data, such as JPEG for images and MP3 for music.
- Prefix codes can be derived from various algorithms, such as Huffman coding, arithmetic coding, Elias coding, etc .
- Prefix codes can be represented by binary trees, where each leaf node corresponds to a symbol and its codeword, and each internal node corresponds to a common prefix of its children.
- Prefix codes can be evaluated by their average codeword length, which is the weighted sum of the lengths of all codewords, where the weights are the probabilities of the symbols.
- Prefix codes can be optimized by minimizing the average codeword length, which is equivalent to minimizing the entropy of the source.
- Prefix codes can be classified into two types: fixed-length and variable-length.
  - Fixed-length prefix codes assign codewords of the same length to all symbols, regardless of their probabilities.
  - Variable-length prefix codes assign codewords of different lengths to symbols, depending on their probabilities, such that more frequent symbols have shorter codewords and less frequent symbols have longer codewords.
  - Variable-length prefix codes are more efficient than fixed-length prefix codes in terms of compression ratio, but they require more complex encoding and decoding algorithms.
- Prefix codes can also be classified into two types: static and dynamic.
  - Static prefix codes use a fixed codebook that is known to both the encoder and the decoder, and does not change during the transmission.
  - Dynamic prefix codes use an adaptive codebook that is updated during the transmission, based on the statistics of the source.
  - Dynamic prefix codes are more adaptive than static prefix codes in terms of changing source characteristics, but they require more overhead for transmitting the codebook.