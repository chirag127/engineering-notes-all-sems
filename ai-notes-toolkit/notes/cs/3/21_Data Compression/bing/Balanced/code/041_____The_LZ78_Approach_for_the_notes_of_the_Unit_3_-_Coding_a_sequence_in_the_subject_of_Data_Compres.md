# The LZ78 Approach

- LZ78 is a lossless data compression algorithm published by Abraham Lempel and Jacob Ziv in 1978.
- It is also known as LZ2 or dictionary-based compression .
- It compresses sequential data by building a dictionary of token sequences from the input, and then replacing the second and subsequent occurrence of the sequence in the data stream with a reference to the dictionary entry .
- The dictionary is initialized with all possible single characters as the first entries.
- The algorithm works as follows:
  - Read the next character from the input.
  - If the current token (the longest sequence of characters that has been seen so far) followed by the next character is already in the dictionary, append the next character to the current token and go back to step 1.
  - Otherwise, output a pair of the dictionary index of the current token and the next character, and add the current token followed by the next character to the dictionary as a new entry.
  - Reset the current token to the next character and go back to step 1.
  - Repeat until the end of the input is reached.
- The output can be encoded using variable-length codes, such as Huffman coding, to reduce the size further.
- LZ78 has the advantage of not requiring a sliding window, which reduces the memory usage and allows random access to the compressed data.
- However, it also has some drawbacks, such as the possibility of the dictionary becoming too large, the inefficiency of encoding single characters, and the lack of adaptation to the changing statistics of the input .
- LZ78 is the basis for many variations and improvements, such as LZW, LZSS, LZMA, and others .