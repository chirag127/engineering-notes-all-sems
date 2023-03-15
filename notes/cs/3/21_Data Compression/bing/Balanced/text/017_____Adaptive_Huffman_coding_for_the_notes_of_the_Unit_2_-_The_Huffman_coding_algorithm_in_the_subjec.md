### Adaptive Huffman coding

- Adaptive Huffman coding (also called Dynamic Huffman coding) is an adaptive coding technique based on Huffman coding.
- It permits building the code as the symbols are being transmitted, having no initial knowledge of source distribution, that allows one-pass encoding and adaptation to changing conditions in data.
- It uses a binary tree to represent the codes and frequencies of the symbols, and updates the tree as new symbols are encountered.
- The tree is maintained such that the most frequent symbols are near the root and the least frequent symbols are near the leaves.
- The tree is also kept in a sibling property order, which means that nodes with lower weights are higher in the tree and nodes with equal weights are ordered by the time of their creation.
- There are two main algorithms for adaptive Huffman coding: FGK algorithm and Vitter algorithm.
- FGK algorithm was proposed by Faller, Gallager and Knuth in 1979. It uses a special node called NYT (Not Yet Transmitted) to represent new symbols that have not been seen before. It also uses a procedure called node swapping to maintain the sibling property order of the tree.
- Vitter algorithm was proposed by Jeffrey Vitter in 1987. It improves the FGK algorithm by using a different node swapping procedure that reduces the number of swaps and the size of the tree. It also uses two parameters, e and r, to control the creation and deletion of nodes.
- Adaptive Huffman coding has some advantages over static Huffman coding, such as:
  - It does not require a priori knowledge of the source distribution or a separate transmission of the code table.
  - It can adapt to changing source statistics and achieve near-optimal compression ratios.
  - It can handle infinite or unknown input streams.
- Adaptive Huffman coding also has some disadvantages, such as:
  - It requires more computation and memory than static Huffman coding.
  - It may perform poorly for sources with highly skewed or non-stationary distributions.
  - It may introduce some overhead for transmitting the NYT symbol and the initial tree structure.