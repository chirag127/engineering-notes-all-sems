Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Compression. Here is the introduction for the notes of the Unit 3 - Coding a sequence.

### Introduction

- In this unit, we will learn how to encode a sequence of symbols using different coding techniques, such as fixed-length codes, variable-length codes, prefix codes, and Huffman codes.
- A code is a mapping from a set of symbols (called the source alphabet) to a set of binary strings (called the codewords).
- The goal of coding is to compress the data by reducing the number of bits required to represent the symbols, while preserving the information content and allowing for efficient decoding.
- A code is said to be optimal if it minimizes the average codeword length, which is the expected number of bits per symbol.
- A code is said to be uniquely decodable if there is a unique way to recover the original sequence of symbols from the encoded sequence of bits.
- A code is said to be prefix-free or instantaneous if no codeword is a prefix of another codeword. This property ensures that the code is uniquely decodable and allows for simple decoding without knowing the length of each codeword.
- A Huffman code is a prefix-free code that is optimal for a given source alphabet and a given probability distribution of the symbols. It is constructed by using a binary tree that assigns shorter codewords to more frequent symbols and longer codewords to less frequent symbols.