# Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies  .
- Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code, that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol.
- Huffman coding is generally useful to compress the data in which there are frequently occurring characters.
- Huffman coding is an efficient method of compressing data without losing information.

The encoding procedure for the Huffman coding algorithm consists of the following steps:

1. Create a leaf node for each character and add it to the priority queue.
2. While there is more than one node in the queue:
    - Remove the two nodes of the highest priority (the lowest frequency) from the queue.
    - Create a new internal node with these two nodes as children and with a frequency equal to the sum of the two nodes' frequencies.
    - Add the new node to the queue.
3. The remaining node is the root node and the tree is complete.
4. Traverse the tree from the root to the leaves and assign a bit (0 or 1) to each edge, such that no two edges along any path have the same bit.
5. For each character, concatenate the bits along the path from the root to the leaf node, forming the code for that character.

Here is an example of Huffman coding for the string "BCCABBDDAECCBBAEDDCC":

![Huffman coding example](https://www.geeksforgeeks.org/wp-content/uploads/generating-huffman-1.png)

The codes for each character are:

- A: 000
- B: 001
- C: 01
- D: 10
- E: 110

The encoded string is:

- 00101100100100101000011001100100100011010100101101

The encoded string has 38 bits, while the original string has 80 bits, resulting in a compression ratio of 47.5%.