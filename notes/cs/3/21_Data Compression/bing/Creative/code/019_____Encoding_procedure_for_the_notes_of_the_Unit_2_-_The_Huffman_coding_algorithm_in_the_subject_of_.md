### Encoding procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies . It is also known as data compression encoding. The idea is to use shorter codes for more frequent characters and longer codes for less frequent characters, so that the average code length is minimized. Huffman coding uses a specific method for choosing the representation for each symbol, resulting in a prefix code, that is, the bit string representing some particular symbol is never a prefix of the bit string representing any other symbol. Huffman coding is generally useful to compress the data in which there are frequently occurring characters.

The encoding procedure for the Huffman coding algorithm can be summarized as follows  :

- Step 1: Create a leaf node for each character and assign it a weight (frequency of appearance) of the character. Add all the nodes to a priority queue (min-heap) based on their weights.
- Step 2: Extract two nodes with the minimum weights from the priority queue. Create a new internal node with the sum of the weights of the two nodes as its weight. Make the first extracted node as its left child and the second extracted node as its right child. Add this node to the priority queue.
- Step 3: Repeat step 2 until there is only one node left in the priority queue. This node is the root of the Huffman tree.
- Step 4: Traverse the Huffman tree and assign codes to each character. Start from the root and assign 0 to the left edge and 1 to the right edge. Concatenate the edge labels along the path from the root to the leaf to get the code for each character.
- Step 5: Use the codes to encode the input data. Replace each character with its corresponding code and output the compressed data.

Here is an example of Huffman coding for the string "BCCABBDDAECCBBAEDDCC":

- Step 1: Create a leaf node for each character and assign it a weight of the character. Add all the nodes to a priority queue.

| Character | Frequency | Node |
|-----------|-----------|------|
| A         | 2         | A:2  |
| B         | 5         | B:5  |
| C         | 6         | C:6  |
| D         | 5         | D:5  |
| E         | 2         | E:2  |

- Step 2: Extract two nodes with the minimum weights from the priority queue. Create a new internal node with the sum of the weights of the two nodes as its weight. Make the first extracted node as its left child and the second extracted node as its right child. Add this node to the priority queue.

| Character | Frequency | Node |
|-----------|-----------|------|
| A         | 2         | A:2  |
| E         | 2         | E:2  |
| B         | 5         | B:5  |
| C         | 6         | C:6  |
| D         | 5         | D:5  |

Extract A:2 and E:2 and create a new node AE:4 with A:2 as the left child and E:2 as the right child. Add AE:4 to the priority queue.

| Character | Frequency | Node |
|-----------|-----------|------|
| AE        | 4         | AE:4 |
| B         | 5         | B:5  |
| C         | 6         | C:6  |
| D         | 5         | D:5  |

Extract AE:4 and B:5 and create a new node BAE:9 with AE:4 as the left child and B:5 as the right child. Add BAE:9 to the priority queue.

| Character | Frequency | Node |
|-----------|-----------|------|
| C         | 6         | C:6  |
| D         | 5         | D:5  |
| BAE       | 9         | BAE:9|

Extract C:6 and D:5 and create a new node CD:11 with C:6 as the left child and D:5 as the right child. Add CD:11 to the priority queue.

| Character | Frequency | Node |
|-----------