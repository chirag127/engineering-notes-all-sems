### The basic algorithm for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Data compression can be either lossless or lossy. Lossless compression preserves the exact information of the original data, while lossy compression discards some information to achieve higher compression ratios.
- Coding a sequence is a technique of lossless compression that assigns codes to sequences of symbols or bytes in the data. The codes are usually shorter than the original sequences, resulting in compression .
- One example of coding a sequence is the Lempel–Ziv–Welch (LZW) algorithm, which works as follows :
  - Initialize a code table with 256 entries, corresponding to the 256 possible byte values.
  - Read the first byte of the data and store it as the current sequence.
  - Repeat until the end of the data:
    - Read the next byte and append it to the current sequence.
    - If the current sequence is in the code table, continue reading the next byte.
    - If the current sequence is not in the code table, output the code for the previous sequence (without the last byte), add the current sequence to the code table with a new code, and reset the current sequence to the last byte.
  - Output the code for the final sequence.
- Another example of coding a sequence is the Huffman coding algorithm, which works as follows:
  - Count the frequencies of each symbol or byte in the data and create a leaf node for each symbol with its frequency as the weight.
  - Repeat until there is only one node left:
    - Find the two nodes with the lowest weights and merge them into a new node with the sum of their weights as the new weight.
    - Assign the new node as the parent of the two nodes and label the edges with 0 and 1.
  - The final node is the root of a binary tree that represents the code table. The code for each symbol is the sequence of 0s and 1s along the path from the root to the leaf node.
  - Traverse the data and output the code for each symbol according to the code table.