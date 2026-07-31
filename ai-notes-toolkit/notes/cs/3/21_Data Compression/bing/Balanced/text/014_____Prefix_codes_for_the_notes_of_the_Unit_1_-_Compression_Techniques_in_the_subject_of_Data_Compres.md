### Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- A prefix code is a type of variable-length code that assigns binary codewords to symbols such that no codeword is a prefix of another codeword.
- A prefix code is also called a prefix-free code, a prefix condition code, or an instantaneous code.
- A prefix code has the property of unique decodability, which means that any encoded message can be unambiguously decoded without any ambiguity or error.
- A prefix code can be represented by a binary tree, where each leaf node corresponds to a symbol and its codeword, and each internal node corresponds to a common prefix of its children.
- A prefix code can be constructed using various algorithms, such as Huffman coding, arithmetic coding, Elias coding, etc .
- A prefix code is useful for data compression, because it can reduce the average length of the codewords by assigning shorter codewords to more frequent symbols, and longer codewords to less frequent symbols.
- A prefix code can also be used for error detection and correction, because any invalid or corrupted codeword can be detected by checking if it is a prefix of another codeword or not.