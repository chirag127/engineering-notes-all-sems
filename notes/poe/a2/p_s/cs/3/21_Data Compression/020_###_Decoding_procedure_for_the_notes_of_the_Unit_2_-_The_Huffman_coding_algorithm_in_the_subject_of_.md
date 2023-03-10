 Here is the content in markdown format for the topic -

### Decoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. Receive the Huffman encoded bitstream and extract the bits one by one.
2. Start from the root node of the Huffman tree.
3. For each extracted bit:

- If it is 0, move to the left child node.
- If it is 1, move to the right child node.

4. When a leaf node is reached, the corresponding character is the decoded character. Output the character.
5. Go back to the root node and repeat steps 3 and 4 till all bits are decoded.

The decoding procedure is simple as it just traverses the already constructed Huffman tree. The traversal is guided by the encoded bits. When a leaf node is reached, the corresponding character is decoded. This is repeated till the whole bitstream is decoded.

**Advantages:**

- Decoding is simple and fast.
- The Huffman tree ensures that the decoded characters are decoded in the correct order.

**Disadvantages:**

- The encoder and decoder must both have the same Huffman tree for proper decoding. So, the Huffman tree must be transmitted along with the encoded bitstream. This adds overhead.
- Dynamic Huffman coding where the tree is built on the fly based on changing frequencies cannot be decoded properly without transmitting the changing trees. This affects compression ratio.

**Applications:**

- Data compression in files, images, videos, etc.
- Lossless data compression algorithms.

[ Ascii diagrams and examples can be added here for better understanding. ]

Hope this helps! Let me know if you would like me to elaborate on any part of the answer.