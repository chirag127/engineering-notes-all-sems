### Adaptive Huffman coding

- Adaptive Huffman coding (also called Dynamic Huffman coding) is an adaptive coding technique based on Huffman coding.
- It permits building the code as the symbols are being transmitted, having no initial knowledge of source distribution, that allows one-pass encoding and adaptation to changing conditions in data.
- It uses a binary tree to store the symbols and their frequencies, and updates the tree as new symbols are encountered.
- The tree is constructed such that the most frequent symbols are near the root and have shorter codes, while the less frequent symbols are near the leaves and have longer codes.
- The tree is maintained using two rules:
  - Sibling property: The nodes in the tree are ordered by decreasing weight, and the sibling of a node is the node to its right. The weight of a node is the sum of the weights of its children, or the frequency of the symbol if it is a leaf node.
  - Swap property: Whenever a new symbol is added or an existing symbol is updated, the tree is rearranged to preserve the sibling property. This may involve swapping nodes that are not siblings or ancestors.
- The encoding process is as follows:
  - Initialize the tree with a special node called NYT (Not Yet Transmitted), which has a weight of zero and no symbol.
  - For each symbol in the input:
    - If the symbol is already in the tree, output its code and increment its weight and the weights of its ancestors. Then, apply the swap property to the tree.
    - If the symbol is not in the tree, output the code of NYT followed by the fixed-length code of the symbol. Then, add the symbol as a leaf node to the right of NYT, and create a new NYT node as its left sibling. Increment the weights of the new symbol and its ancestors, and apply the swap property to the tree.
- The decoding process is as follows:
  - Initialize the tree with a special node called NYT, which has a weight of zero and no symbol.
  - For each bit in the input:
    - Traverse the tree from the root according to the bit. If the bit is 0, go to the left child; if the bit is 1, go to the right child.
    - If the node reached is a leaf node, output its symbol and increment its weight and the weights of its ancestors. Then, apply the swap property to the tree.
    - If the node reached is NYT, read the next fixed-length bits and output the corresponding symbol. Then, add the symbol as a leaf node to the right of NYT, and create a new NYT node as its left sibling. Increment the weights of the new symbol and its ancestors, and apply the swap property to the tree.
- The advantage of adaptive Huffman coding is that it can handle any source distribution without prior knowledge, and can adjust to changing frequencies dynamically.
- The disadvantage of adaptive Huffman coding is that it requires more computation and memory to update and rearrange the tree, and it may not achieve optimal compression if the source distribution is not stationary.
- An example of adaptive Huffman coding is shown below:

![Adaptive Huffman coding example](http://ben-tanen.com/adaptive-huffman/img/adaptive-huffman-example.png)

: https://en.wikipedia.org/wiki/Adaptive_Huffman_coding
: https://xlinux.nist.gov/dads/HTML/adaptiveHuffman.html
: https://www.geeksforgeeks.org/adaptive-huffman-coding-and-decoding/
: http://ben-tanen.com/adaptive-huffman/