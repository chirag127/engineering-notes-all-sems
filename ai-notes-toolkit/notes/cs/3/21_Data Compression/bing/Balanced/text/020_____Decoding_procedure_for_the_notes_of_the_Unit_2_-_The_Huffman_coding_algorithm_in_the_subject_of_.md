### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies in the source data.
- To decode a Huffman-coded message, one needs to have access to the Huffman tree that was used to encode the message, or a table that maps each code to its corresponding symbol.
- The decoding procedure is as follows:
  - Start from the root of the Huffman tree and read the bits of the encoded message from left to right.
  - If the current bit is 0, move to the left child of the current node. If the current bit is 1, move to the right child of the current node.
  - If the current node is a leaf, output the symbol stored in the node and return to the root of the tree.
  - Repeat steps 2 and 3 until all the bits of the encoded message are processed.
- For example, consider the following Huffman tree and the encoded message 110010011:

![Huffman tree](https://i.imgur.com/0Z1l0fT.png)

- The decoding procedure would be:

| Bit | Current Node | Output |
| --- | ------------ | ------ |
| 1   | Root         |        |
| 1   | Right child  |        |
| 0   | Left child   | C      |
| 0   | Root         |        |
| 1   | Right child  |        |
| 0   | Left child   | C      |
| 0   | Root         |        |
| 0   | Left child   |        |
| 1   | Right child  | A      |
| 1   | Root         |        |
| 1   | Right child  |        |
| 1   | Right child  | B      |

- The decoded message is CCAAB.