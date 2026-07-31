### The LZ78 Approach

- LZ78 is a lossless data compression algorithm published by Abraham Lempel and Jacob Ziv in 1978.
- It is also known as LZ2 or dictionary-based compression.
- It compresses sequential data by building a dictionary of token sequences from the input, and then replacing the second and subsequent occurrence of the sequence in the data stream with a reference to the dictionary entry.
- The dictionary is initialized with all possible single characters as the first entries.
- The algorithm works as follows :
  - Read the next character from the input.
  - If the current token sequence followed by the character is already in the dictionary, append the character to the token sequence and repeat this step.
  - Otherwise, output a pair of the dictionary index of the current token sequence and the character, and add the new token sequence followed by the character to the dictionary with a new index.
  - Reset the token sequence to empty and go back to the first step.
- The output can be encoded using variable-length codes, such as Huffman coding, to reduce the size further.
- LZ78 is the basis for many variations and extensions, such as LZW, LZT, LZMW, and LZAP .
- LZ78 has the advantages of being simple, fast, and adaptive to different types of data.
- However, it also has some drawbacks, such as requiring a large dictionary size, producing long codes for rare sequences, and being sensitive to errors in the input or the output.