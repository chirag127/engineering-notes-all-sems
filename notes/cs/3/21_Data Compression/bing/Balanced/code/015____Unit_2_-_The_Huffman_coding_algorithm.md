## Unit 2 - The Huffman coding algorithm

The Huffman coding algorithm is a method of data compression that assigns variable-length codes to symbols based on their frequencies of occurrence.

The main steps of the algorithm are:

- Create a frequency table that counts the number of occurrences of each symbol in the data.
- Create a priority queue of nodes, where each node represents a symbol and its frequency. The nodes with the lowest frequencies have the highest priority.
- While the queue has more than one node, do the following:
  - Dequeue the two nodes with the highest priority (lowest frequency) from the queue.
  - Create a new internal node with the sum of the frequencies of the two nodes as its frequency, and the two nodes as its left and right children.
  - Enqueue the new node to the queue.
- The remaining node in the queue is the root of the Huffman tree.
- Traverse the Huffman tree and assign codes to the symbols. The code of a symbol is the sequence of bits that corresponds to the path from the root to the leaf node of the symbol. A left branch is represented by 0 and a right branch by 1.

The Huffman coding algorithm has the following properties:

- It is a lossless compression method, meaning that no information is lost in the process of encoding and decoding.
- It is a prefix-free code, meaning that no code is a prefix of another code. This ensures that the codes can be uniquely decoded.
- It is an optimal code, meaning that it minimizes the average code length for a given set of symbols and frequencies. No other code can achieve a smaller average code length.