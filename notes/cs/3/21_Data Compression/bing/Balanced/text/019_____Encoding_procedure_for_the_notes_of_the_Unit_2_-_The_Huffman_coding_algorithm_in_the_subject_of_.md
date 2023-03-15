### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code, that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol.
- Huffman coding is generally useful to compress the data in which there are frequently occurring characters.
- The encoding procedure for the Huffman coding algorithm can be summarized as follows  :

  - Create a leaf node for each character and add them to a priority queue based on their frequency.
  - While there is more than one node in the queue:
    - Remove the two nodes with the lowest frequency from the queue.
    - Create a new internal node with these two nodes as children and with frequency equal to the sum of their frequencies.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
  - Traverse the Huffman tree and assign codes to each character. The left child gets a 0 bit and the right child gets a 1 bit.
  - Store the codes in a map or a table for easy lookup.
  - To encode a given message, replace each character with its corresponding code from the map or the table.
  - To decode a given encoded message, start from the root of the Huffman tree and follow the bits until reaching a leaf node, then output the character and restart from the root.