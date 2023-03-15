# Diagram Coding for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- Diagram coding is a method of data compression that encodes a sequence of symbols using a variable-length code based on a tree structure.
- The tree structure is built from the bottom up, starting with the most frequent symbols as leaves and assigning them shorter codes, and then combining them into higher-level nodes with longer codes.
- The tree structure is also known as a Huffman tree, after its inventor David Huffman, who proposed the algorithm in 1952.
- The algorithm works as follows:
  - Given a sequence of symbols and their frequencies, create a leaf node for each symbol and add it to a priority queue based on its frequency.
  - While there is more than one node in the queue, do the following:
    - Remove the two nodes with the lowest frequency from the queue and create a new internal node with these two nodes as children. The frequency of the new node is the sum of the frequencies of the children.
    - Assign a bit (0 or 1) to each edge of the tree, such that the left edge is 0 and the right edge is 1. The bit assigned to an edge is also the bit appended to the code of the child node.
    - Add the new node to the queue.
  - The remaining node in the queue is the root of the tree and has no code.
  - To encode a symbol, traverse the tree from the root to the leaf corresponding to the symbol and concatenate the bits along the path. The code for each symbol is the reverse of the concatenation.
  - To decode a code, traverse the tree from the root to a leaf, using the bits of the code to determine the direction of the traversal. The symbol corresponding to the leaf is the decoded symbol.

- An example of diagram coding is shown below:

| Symbol | Frequency |
|--------|-----------|
| A      | 0.4       |
| B      | 0.3       |
| C      | 0.2       |
| D      | 0.1       |

- The Huffman tree for this sequence is:

```
    1.0
   /   \
  /     \
 0.6     0.4
/  \      |
A   0.2   B
   /  \
  C    D
```

- The codes for each symbol are:

| Symbol | Code |
|--------|------|
| A      | 0    |
| B      | 11   |
| C      | 100  |
| D      | 101  |

- The average code length for this sequence is:

```
0.4 * 1 + 0.3 * 2 + 0.2 * 3 + 0.1 * 3 = 1.9 bits/symbol
```

- The compression ratio for this sequence is:

```
Original size / Compressed size = 2 bits/symbol / 1.9 bits/symbol = 1.05
```

- Diagram coding is optimal in the sense that it minimizes the average code length for a given sequence of symbols and their frequencies.
- Diagram coding is also prefix-free, meaning that no code is a prefix of another code, which makes decoding unambiguous and efficient.