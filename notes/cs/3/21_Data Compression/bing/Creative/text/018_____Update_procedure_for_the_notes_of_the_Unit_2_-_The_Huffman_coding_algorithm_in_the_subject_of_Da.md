### Update procedure for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- The Huffman coding algorithm is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies of occurrence in the data.
- The algorithm works by building a binary tree of nodes, where each node represents a symbol or a group of symbols. The root node represents the entire data, and the leaf nodes represent the individual symbols. The frequency of each node is the sum of the frequencies of its children.
- The algorithm starts with a list of nodes, each containing a symbol and its frequency. The list is sorted in ascending order of frequency. Then, the algorithm repeatedly performs the following steps until there is only one node left in the list:
  - Select the two nodes with the lowest frequency and create a new node with the sum of their frequencies as its frequency. The two nodes become the left and right children of the new node.
  - Remove the two nodes from the list and insert the new node in the sorted order.
- The final node is the root of the Huffman tree. The code for each symbol is obtained by traversing the tree from the root to the leaf, appending a 0 for each left branch and a 1 for each right branch.
- The Huffman coding algorithm is optimal, meaning that it produces the shortest possible code for any given data. However, the optimality depends on the accuracy of the frequency estimates and the assumption that the symbols are independent and identically distributed.
- The Huffman coding algorithm can be extended to handle more than two symbols per node, such as ternary Huffman coding, or to handle unequal costs for different symbols, such as arithmetic coding.