### Adaptive Huffman coding

Adaptive Huffman coding is a technique for compressing data without prior knowledge of the source distribution. It is based on Huffman coding, which assigns variable-length codes to symbols based on their frequencies. However, unlike Huffman coding, which requires two passes over the data (one to build the code and one to encode the data), adaptive Huffman coding builds the code dynamically as the symbols are being transmitted, and adapts to changing conditions in the data.  

Some advantages of adaptive Huffman coding are:

- It can handle any source distribution, even if it is unknown or changing over time.
- It can achieve near-optimal compression, since the code is always updated to reflect the current frequencies of the symbols.
- It can encode and decode the data in one pass, without requiring any extra storage or communication.

Some disadvantages of adaptive Huffman coding are:

- It requires more computation than static Huffman coding, since the code tree has to be modified frequently.
- It may not perform well for very small or very large data sets, since the code may not have enough time to adapt or may become too complex.
- It may introduce some overhead in the encoded data, since the code tree has to be transmitted along with the symbols.

There are different algorithms for implementing adaptive Huffman coding, such as FGK algorithm and Vitter algorithm. They differ in how they update the code tree and how they handle the special case of new symbols that have not been seen before.  

A general procedure for adaptive Huffman coding is:

- Initialize the code tree with a single node, called the NYT (Not Yet Transmitted) node, which represents all the symbols that have not been seen yet.
- For each symbol in the input data:
  - If the symbol has been seen before, encode it using the current code tree and update the frequencies of the nodes along the path from the symbol to the root.
  - If the symbol is new, encode the NYT node using the current code tree, then encode the symbol using a fixed-length code (such as ASCII), and add a new node for the symbol as a child of the NYT node. Update the frequencies of the nodes along the path from the new node to the root.
  - If the code tree violates the sibling property (which states that the nodes with the same frequency should be ordered by increasing symbol value), swap the nodes to restore the property and update the codes accordingly.

A general procedure for adaptive Huffman decoding is:

- Initialize the code tree with a single node, called the NYT node, which represents all the symbols that have not been seen yet.
- For each code in the encoded data:
  - If the code corresponds to an existing node in the code tree, decode it as the symbol represented by that node and update the frequencies of the nodes along the path from the node to the root.
  - If the code corresponds to the NYT node, decode the next fixed-length code as a new symbol, add a new node for the symbol as a child of the NYT node, and update the frequencies of the nodes along the path from the new node to the root.
  - If the code tree violates the sibling property, swap the nodes to restore the property and update the codes accordingly.