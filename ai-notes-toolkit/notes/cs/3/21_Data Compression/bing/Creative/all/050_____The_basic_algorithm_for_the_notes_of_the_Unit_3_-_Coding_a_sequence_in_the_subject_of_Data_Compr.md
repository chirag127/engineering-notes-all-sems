# The basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of a data file by encoding its content in a more efficient way.
- Coding a sequence is one of the techniques used in data compression to represent a sequence of symbols (such as characters, bytes, or pixels) with a shorter code.
- There are different types of coding algorithms, such as fixed-length codes, variable-length codes, and dictionary-based codes.
- Fixed-length codes assign the same number of bits to each symbol, regardless of its frequency or importance. For example, ASCII code uses 8 bits to represent 256 symbols.
- Variable-length codes assign different numbers of bits to different symbols, depending on their frequency or importance. For example, Huffman code uses a binary tree to assign shorter codes to more frequent symbols and longer codes to less frequent symbols.
- Dictionary-based codes use a table or a dictionary to store the codes for common sequences of symbols. For example, LZW code uses codes 256 through 4095 to represent sequences of bytes that have occurred previously in the data.
- The basic algorithm for coding a sequence using a dictionary-based code is as follows:

  - Initialize the dictionary with the codes for the individual symbols (usually 0 to 255 for bytes).
  - Read the first symbol from the input and store it in a buffer.
  - While there are more symbols in the input, do the following:
    - Read the next symbol from the input and append it to the buffer.
    - If the buffer is in the dictionary, continue reading the next symbol.
    - If the buffer is not in the dictionary, do the following:
      - Output the code for the buffer without the last symbol.
      - Add the buffer with the last symbol to the dictionary with a new code.
      - Clear the buffer and store the last symbol in it.
  - Output the code for the buffer.