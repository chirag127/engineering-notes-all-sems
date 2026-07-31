### Adaptive Huffman coding

Adaptive Huffman coding is a technique for compressing data without prior knowledge of the source distribution. It is based on the Huffman coding algorithm, which assigns variable-length codes to symbols based on their frequencies. However, unlike Huffman coding, which requires two passes over the data (one to build the code and one to encode the data), adaptive Huffman coding builds the code dynamically as the symbols are being transmitted, and adapts to changing conditions in the data. 

Some advantages of adaptive Huffman coding are:

- It can handle any source distribution, even if it is unknown or non-stationary (i.e., changing over time).
- It can achieve near-optimal compression, since the code is always updated to reflect the current frequencies of the symbols.
- It can encode and decode the data in one pass, without requiring any extra storage or communication for the code.

Some disadvantages of adaptive Huffman coding are:

- It requires more computation than Huffman coding, since the code tree has to be modified frequently.
- It may not perform well for small or sparse data sets, since the code may not have enough time to converge to the optimal one.
- It may be vulnerable to noise or errors in the transmission, since a single corrupted bit can affect the decoding of the entire data.

There are different algorithms for implementing adaptive Huffman coding, such as the FGK algorithm and the Vitter algorithm. They differ in how they update the code tree and how they handle the special case of new symbols that have not been seen before.  

The basic steps of adaptive Huffman coding are:

- Initialize the code tree with a single node, called the NYT (Not Yet Transmitted) node, which represents all the symbols that have not been seen yet.
- For each symbol in the data:
  - If the symbol is new, output the code for the NYT node, followed by a fixed-length code for the symbol (e.g., its ASCII code). Then, split the NYT node into two nodes: a new NYT node and a leaf node for the symbol, with a frequency of 1. The new nodes become the children of the old NYT node, and the old NYT node becomes an internal node.
  - If the symbol is not new, output the code for its leaf node in the code tree. Then, increment the frequency of the node by 1, and update the code tree to maintain the Huffman property (i.e., the nodes with lower frequencies are farther from the root than the nodes with higher frequencies). This may involve swapping the node with another node in the same level or higher, and updating the frequencies of the nodes along the path from the node to the root.
- Repeat until all the symbols are processed.

The following diagram shows an example of adaptive Huffman coding for the string "ABRACADABRA". The code tree is updated after each symbol, and the codes for the symbols are shown below the tree. 

![Adaptive Huffman coding example](https://i.imgur.com/0w0Za6x.png)

The total length of the encoded data is 40 bits, compared to 88 bits for the original data (assuming 8 bits per symbol). The compression ratio is 0.45.