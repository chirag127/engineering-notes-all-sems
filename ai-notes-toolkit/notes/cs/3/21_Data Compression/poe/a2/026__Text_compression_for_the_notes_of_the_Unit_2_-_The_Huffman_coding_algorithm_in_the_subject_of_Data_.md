 Here is the formal content in Markdown format without any emojis or external links for the given topic:

### Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

1. Huffman coding is a lossless data compression algorithm. It encodes the characters in a string based on their frequency. The most frequent characters are encoded with the fewest bits.

2. The steps to create Huffman code are:

- Survey the characters and their frequencies.
- Create a leaf node for each character and make a min heap of all leaf nodes.
- Repeatedly remove the two nodes with the lowest frequency from the heap.
- Create a new internal node with these two nodes as children and assign the combined frequency of the two child nodes to the new internal node.
- Add the new internal node back to the heap.
- Repeat steps 3 and 4 until the heap contains only the root node.
- The code for each character is determined by following the path from the root to the character's leaf node.

3. The advantages of Huffman coding are:

- It produces an optimal prefix code.
- It achieves a high compression ratio.
- It is a lossless compression technique as the original data can be recovered from the compressed data.

4. The disadvantages of Huffman coding are:

- It requires two passes through the data.
- It requires significant computer resources to build the Huffman tree.
- The compression ratio depends on the skewness of the frequency distribution. If the distribution is not skewed, the compression may not be significant.