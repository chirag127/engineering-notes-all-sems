### Introduction for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- In this unit, we will learn how to encode a sequence of symbols using different coding techniques, such as fixed-length codes, variable-length codes, prefix codes, and Huffman codes.
- A code is a mapping from a set of symbols (called the source alphabet) to a set of binary strings (called the code words).
- The goal of coding is to reduce the number of bits required to represent the sequence, while preserving the information content and allowing for efficient decoding.
- Coding can be lossless or lossy, depending on whether the original sequence can be perfectly reconstructed from the code words or not.
- Lossless coding is suitable for applications where the exact reproduction of the original sequence is essential, such as text, audio, or image compression.
- Lossy coding is acceptable for applications where some distortion or degradation of the original sequence is tolerable, such as video or speech compression.
- In this unit, we will focus on lossless coding techniques, which can be divided into two categories: entropy coding and dictionary coding.
- Entropy coding is based on the statistical properties of the source symbols, such as their frequencies or probabilities of occurrence. It assigns shorter code words to more frequent symbols and longer code words to less frequent symbols, thus minimizing the average code word length.
- Dictionary coding is based on the structural properties of the source symbols, such as their patterns or repetitions. It builds a dictionary of common phrases or substrings and assigns code words to them, thus exploiting the redundancy in the sequence.
- In the next sections, we will discuss the following topics:

  - Fixed-length codes and variable-length codes
  - Prefix codes and their properties
  - Huffman coding algorithm and its optimality
  - Extensions and variations of Huffman coding
  - Applications and examples of coding techniques