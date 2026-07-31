# Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters with fewer bits.
- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- The idea is to use shorter codes for more frequent characters and longer codes for less frequent characters, so that the average code length is minimized  .
- Huffman coding consists of two steps: building a Huffman tree and generating codes for each character .
- To build a Huffman tree, we need to follow these steps  :
  - Create a leaf node for each character and add it to a priority queue based on its frequency.
  - While there is more than one node in the queue:
    - Remove the two nodes with the lowest frequency from the queue.
    - Create a new internal node with these two nodes as children and the sum of their frequencies as the frequency.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
- To generate codes for each character, we need to traverse the Huffman tree and assign 0 or 1 to each edge  .
  - The code for a character is the concatenation of the edge labels along the path from the root to the leaf node representing that character.
  - The codes are prefix-free, meaning that no code is a prefix of another code .
- To compress a text file, we need to replace each character with its corresponding code and store the Huffman tree along with the encoded data  .
- To decompress a text file, we need to use the Huffman tree to decode the encoded data by following the edge labels from the root to the leaf nodes  .