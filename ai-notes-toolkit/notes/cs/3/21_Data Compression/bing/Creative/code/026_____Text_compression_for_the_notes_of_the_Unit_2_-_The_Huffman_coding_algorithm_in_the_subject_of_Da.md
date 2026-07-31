```
### Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters with fewer bits.
- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- The steps of the Huffman coding algorithm are  :
  - Create a leaf node for each character and add them to a priority queue based on their frequency.
  - While there is more than one node in the queue:
    - Remove the two nodes with the lowest frequency from the queue.
    - Create a new internal node with the sum of their frequencies as its frequency and the two nodes as its left and right children.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
  - Traverse the Huffman tree and assign codes to each character. The left edge is 0 and the right edge is 1.
- To compress a text file, replace each character with its corresponding code and write the output in binary format.
- To decompress a compressed file, read the file bit by bit and follow the Huffman tree from the root to the leaf. When a leaf is reached, output the character and return to the root.
- The advantages of Huffman coding are  :
  - It is optimal, meaning it generates the shortest possible codes for a given set of characters and frequencies.
  - It is lossless, meaning no information is lost during compression or decompression.
  - It is simple and efficient, meaning it can be easily implemented and executed.
- The disadvantages of Huffman coding are  :
  - It requires the knowledge of the frequencies of the characters in advance, which may not be available or accurate.
  - It requires the storage or transmission of the Huffman tree along with the compressed file, which adds some overhead.
  - It is not suitable for compressing files that have a uniform distribution of characters, as it will not reduce the size significantly.
```