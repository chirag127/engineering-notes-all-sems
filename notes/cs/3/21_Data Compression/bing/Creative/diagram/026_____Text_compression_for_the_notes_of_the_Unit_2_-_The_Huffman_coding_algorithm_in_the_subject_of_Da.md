### Text compression for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Text compression is the process of reducing the size of a text file by encoding its characters with fewer bits.
- Huffman coding is a lossless data compression algorithm that assigns variable-length codes to input characters based on their frequencies .
- The most frequent character gets the smallest code and the least frequent character gets the largest code.
- Huffman coding works by creating a binary tree that represents the codes of each character .
- The root of the tree has no code, and each child node inherits the code of its parent with an additional bit (0 for left child, 1 for right child).
- The leaf nodes of the tree are the characters and their codes are the paths from the root to the leaf.
- To construct the Huffman tree, the algorithm follows these steps  :
  - Create a node for each character and its frequency and add them to a priority queue (min-heap).
  - While the queue has more than one node, do the following:
    - Remove the two nodes with the lowest frequency from the queue.
    - Create a new internal node with the sum of the frequencies of the two nodes as its frequency.
    - Make the two nodes the left and right children of the new node.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the Huffman tree.
- To encode a text file, the algorithm traverses the Huffman tree and generates the codes for each character .
- To decode a compressed file, the algorithm starts from the root of the Huffman tree and follows the bits of the file until it reaches a leaf node, which is the decoded character.
- Huffman coding is a greedy algorithm that guarantees an optimal compression ratio for a given text file .
- Huffman coding is widely used in various applications such as computer networks, fax machines, modems, and HDTV.