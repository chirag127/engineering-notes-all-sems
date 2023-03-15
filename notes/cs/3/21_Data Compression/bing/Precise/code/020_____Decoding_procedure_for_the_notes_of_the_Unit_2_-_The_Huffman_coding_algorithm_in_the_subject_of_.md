### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. The Huffman coding algorithm is a lossless data compression algorithm that assigns variable-length codes to input symbols based on their frequencies.
2. The algorithm constructs a binary tree where the leaves represent the input symbols and the path from the root to a leaf represents the code for that symbol.
3. To decode a Huffman encoded message, the decoder starts at the root of the tree and follows the path indicated by the bits in the encoded message.
4. When the decoder reaches a leaf, it outputs the symbol represented by that leaf and returns to the root of the tree to decode the next symbol.
5. This process is repeated until the entire encoded message has been decoded.
