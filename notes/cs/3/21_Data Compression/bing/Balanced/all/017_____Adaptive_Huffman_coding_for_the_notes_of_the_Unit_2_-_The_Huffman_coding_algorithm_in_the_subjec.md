# Adaptive Huffman coding

Adaptive Huffman coding is a technique for compressing data without prior knowledge of the source distribution. It is based on Huffman coding, which assigns variable-length codes to symbols based on their frequencies. However, unlike Huffman coding, adaptive Huffman coding does not require a separate step to construct the code tree. Instead, it builds and updates the code tree dynamically as the symbols are being transmitted, adapting to the changing conditions in the data.

The main advantages of adaptive Huffman coding are:

- It allows one-pass encoding and decoding, without the need to store or transmit the code tree separately.
- It can handle non-stationary sources, where the symbol frequencies may vary over time.
- It can achieve optimal compression for any source, as long as the encoder and decoder use the same algorithm.

The main challenges of adaptive Huffman coding are:

- It requires more complex algorithms and data structures to maintain and update the code tree efficiently.
- It may incur some overhead in the beginning of the transmission, when the code tree is not well adapted to the source.

There are different algorithms for implementing adaptive Huffman coding, such as Vitter's algorithm, which uses a special data structure called a splay tree to update the code tree. The basic steps of adaptive Huffman coding are:

- Initialize the code tree with a single node, called the NYT (Not Yet Transmitted) node, which represents all the symbols that have not been encountered yet. Assign a weight of zero to this node.
- For each symbol to be encoded or decoded, do the following:
  - If the symbol has not been encountered before, output the code for the NYT node, followed by the fixed-length code for the symbol (usually the ASCII code). Then, add a new node for the symbol as a child of the NYT node, and assign a weight of one to it. Also, create a new NYT node as the other child of the old NYT node, and assign a weight of zero to it.
  - If the symbol has been encountered before, output the code for the node corresponding to the symbol. Then, increment the weight of the node by one.
  - After encoding or decoding a symbol, update the code tree to maintain the following properties:
    - The nodes are ordered by increasing weight, from left to right and from bottom to top. This means that the nodes with the same weight are ordered by the order of their appearance in the data.
    - The sibling property: the nodes with the same parent have different codes, and the left child has a code of 0 and the right child has a code of 1.
    - The weight-balanced property: for any node in the tree, the weight of its left subtree is less than or equal to the weight of its right subtree, and the weight of any node is less than or equal to the weight of its parent.
    - To update the code tree, find the node with the highest number (the most recent node) that has the same weight as the node that was encoded or decoded. If this node is not the same as the node that was encoded or decoded, swap them. Then, increment the weight of the node and all its ancestors, and repeat the process until reaching the root of the tree.

The following diagram shows an example of adaptive Huffman coding for the string "abracadabra", using Vitter's algorithm:

![Adaptive Huffman coding example](https://i.imgur.com/8lZl1tZ.png)

The code tree is initialized with a single NYT node with weight 0. The first symbol, "a", is encoded as the code for the NYT node (empty), followed by the ASCII code for "a" (01100001). Then, a new node for "a" is added as the left child of the NYT node, with weight 1, and a new NYT node is created as the right child of the old NYT node, with weight 0. The second symbol, "b", is encoded as the code for the new NYT node (1), followed by the ASCII code for "b" (01100010). Then, a new node for "b" is added as the left child of the new NYT node, with weight 1, and a new NYT node is created as the right child of the new NYT node, with weight 0. The third symbol, "r", is encoded as the code for the new NYT node (11), followed by the ASCII code for "r" (01110010). Then, a new node for "r" is added as the left child of the new NYT node, with