# Adaptive Huffman coding

Adaptive Huffman coding is a technique for compressing data without prior knowledge of the source distribution. It is based on Huffman coding, which assigns variable-length codes to symbols based on their frequencies. However, unlike Huffman coding, which requires two passes over the data (one to build the code and one to encode the data), adaptive Huffman coding builds the code dynamically as the symbols are being transmitted. This allows one-pass encoding and adaptation to changing conditions in data.

## Basic idea

The basic idea of adaptive Huffman coding is to maintain a binary tree that represents the code for each symbol. The tree is initialized with a single node, called the NYT (Not Yet Transmitted) node, which represents all the symbols that have not been seen yet. As each symbol is encountered, the tree is updated as follows:

- If the symbol is new, it is added as a child of the NYT node, and the NYT node is split into two nodes: a new NYT node and a node for the new symbol. The new symbol node is assigned a weight of 1, and the new NYT node inherits the weight of the old NYT node. The code for the new symbol is the code for the old NYT node followed by a binary representation of the symbol (e.g., using a fixed-length code or an escape code).
- If the symbol is already in the tree, its weight is incremented by 1, and the tree is restructured to preserve the Huffman property: the weight of any node is equal to the sum of the weights of its children, and the nodes with lower weights are closer to the root than the nodes with higher weights. This may involve swapping nodes or rotating subtrees.

The code for any symbol is the path from the root to the symbol node, where a left branch is 0 and a right branch is 1. The code is transmitted or stored along with the symbol.

## Example

Suppose we want to encode the string "ABRACADABRA" using adaptive Huffman coding. We start with an empty tree with only the NYT node:

```
  NYT
```

The first symbol is A, which is new, so we add it as a child of the NYT node and split the NYT node. We also assign a weight of 1 to the A node and the new NYT node. The code for A is the code for the old NYT node (empty) followed by a binary representation of A (e.g., 00001).

```
     1
   /   \
NYT     A
 1       1
```

The second symbol is B, which is also new, so we add it as a child of the NYT node and split the NYT node. We also assign a weight of 1 to the B node and the new NYT node. The code for B is the code for the old NYT node (0) followed by a binary representation of B (e.g., 00010).

```
     2
   /   \
  1     A
 / \     1
NYT B
 1  1
```

The third symbol is R, which is also new, so we add it as a child of the NYT node and split the NYT node. We also assign a weight of 1 to the R node and the new NYT node. The code for R is the code for the old NYT node (00) followed by a binary representation of R (e.g., 01010).

```
       3
     /   \
    2     A
   / \     1
  1   R
 / \   1
NYT B
 1  1
```

The fourth symbol is A, which is already in the tree, so we increment its weight by 1 and restructure the tree to preserve the Huffman property. This involves swapping the A node with the R node, since they have the same weight and A is more recent. The code for A is the path from the root to the A node (10).

```
       4
     /   \
    2     A
   / \     2
  1   A
 / \   1
NYT B
 1  1
```

The fifth symbol is C, which is new, so we add it as a child of the NYT node and split the NYT node. We also assign a weight of 1 to the C node and the new NYT node. The code for C is the code for the old NYT node (000) followed by a binary representation of