### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- The idea is to use shorter codes for more frequent characters and longer codes for less frequent characters, so that the average code length is minimized .
- Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code, that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol .
- The encoding procedure for the Huffman coding algorithm can be summarized as follows :
  - Create a leaf node for each character and assign it a weight (frequency of appearance) and add it to a priority queue.
  - While there is more than one node in the queue:
    - Remove the two nodes with the lowest weight from the queue.
    - Create a new internal node with these two nodes as children and with weight equal to the sum of their weights.
    - Assign a bit (0 or 1) to each edge of the tree, descending from the new node.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
  - Traverse the tree and assign codes to each character by concatenating the bits along the path from the root to the leaf node.
  - Encode each character in the input data by replacing it with its corresponding code from the tree.
  - Decode the encoded data by starting from the root of the tree and following the bits until reaching a leaf node, and then outputting the character stored in that node. Repeat until the end of the encoded data.