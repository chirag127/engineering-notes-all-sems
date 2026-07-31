### Generating a binary code for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Data compression is the process of reducing the size of data by encoding it using fewer bits.
- Binary code is a way of representing data using only two symbols: 0 and 1.
- A fixed-length binary code assigns the same number of bits to each symbol, regardless of its frequency.
- A variable-length binary code assigns different numbers of bits to different symbols, depending on their frequency.
- A prefix code is a variable-length binary code that has the property that no code is a prefix of any other code. This makes it easier to decode the message without ambiguity.
- Huffman coding is a technique for generating a prefix code that minimizes the total number of bits required to encode a message.
- The steps of Huffman coding are :
  - Create a frequency table that counts the occurrence of each symbol in the message.
  - Create a binary tree that has a node for each symbol and its frequency. The root node has the total frequency of all symbols.
  - Sort the nodes in ascending order of frequency and merge the two nodes with the lowest frequency into a new node. The new node has the sum of the frequencies of the two nodes as its frequency. Repeat this step until there is only one node left, which is the root of the tree.
  - Assign a bit (0 or 1) to each edge of the tree. The code for each symbol is the sequence of bits along the path from the root to the leaf node corresponding to that symbol.
  - Encode the message by replacing each symbol with its code.
  - Decode the message by following the path from the root to the leaf node indicated by the bits in the encoded message.