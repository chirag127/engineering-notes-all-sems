### Adaptive Huffman coding

Adaptive Huffman coding is a technique for compressing data without prior knowledge of the source distribution. It is based on Huffman coding, which assigns variable-length codes to symbols based on their frequencies. However, unlike Huffman coding, which requires two passes over the data (one to build the code and one to encode the data), adaptive Huffman coding builds the code dynamically as the symbols are being transmitted, and adapts to changing conditions in the data. 

The main idea of adaptive Huffman coding is to maintain a binary tree that represents the code for each symbol, and update the tree whenever a new symbol is encountered or an existing symbol is repeated. The tree is initialized with a single node, called the NYT (Not Yet Transmitted) node, which represents all the symbols that have not been seen so far. The tree is updated according to the following rules:

- When a new symbol is encountered, it is assigned a code consisting of the current code for the NYT node followed by a fixed-length code for the symbol (usually the binary representation of its ASCII value). The NYT node is then split into two nodes: a new NYT node and a leaf node for the new symbol, both with a weight of 1. The new symbol node is placed as the right child of the old NYT node, and the new NYT node is placed as the left child. The old NYT node becomes an internal node with a weight of 2 (the sum of its children's weights).
- When an existing symbol is encountered, it is encoded using its current code in the tree. The weight of its node is incremented by 1, and the tree is restructured to preserve the Huffman property: the nodes are ordered by increasing weight, and nodes with equal weight are ordered by increasing order of appearance. To restructure the tree, the following steps are performed:
  - Find the highest numbered (rightmost) node in the same block (set of nodes with the same weight) as the symbol node. If the symbol node is not the highest numbered node in its block, swap it with the highest numbered node. This ensures that the symbol node moves up in the tree as its frequency increases.
  - Increment the weight of the symbol node and its ancestors by 1.
  - Repeat the above steps until the root of the tree is reached.

The following diagram shows an example of adaptive Huffman coding for the string "ABRACADABRA". The numbers in the nodes indicate the weights, and the letters in the nodes indicate the symbols. The codes for each symbol are shown below the tree.

![Adaptive Huffman coding example](https://i.imgur.com/9Zl7lZf.png)

The codes for each symbol are:

- A: 0
- B: 100
- R: 101
- C: 1100
- D: 1101

The encoded string is:

0 100 101 0 1100 0 1101 0 100 101 0

The encoded string has 23 bits, while the original string has 88 bits (assuming 8 bits per character), so the compression ratio is 23/88 = 0.26.