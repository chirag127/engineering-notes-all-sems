# Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence.
- The code with the lowest expected codeword length is called the minimum redundancy code or the optimal prefix code.
- The expected codeword length is the weighted average of the codeword lengths, where the weights are the probabilities of the symbols.
- The variance of the codeword length is the weighted average of the squared deviations of the codeword lengths from the expected codeword length, where the weights are the probabilities of the symbols.
- The variance of the codeword length measures the variability or dispersion of the codeword lengths around the expected codeword length.
- A lower variance implies a more uniform distribution of the codeword lengths, which may be desirable for some applications.
- A minimum variance Huffman code is a Huffman code that minimizes the variance of the codeword length, subject to the constraint that the expected codeword length is also minimized.
- A minimum variance Huffman code may not be unique, and it may not exist for some probability distributions.
- A minimum variance Huffman code can be constructed by modifying the standard Huffman algorithm as follows:
  - Start with a set of nodes, each representing a symbol and its probability.
  - Sort the nodes in ascending order of their probabilities.
  - While there are more than two nodes in the set:
    - Select the two nodes with the lowest probabilities and merge them into a new node, whose probability is the sum of the probabilities of the two nodes.
    - Assign a 0 bit to the edge connecting the new node and the node with the lower probability, and a 1 bit to the edge connecting the new node and the node with the higher probability.
    - Insert the new node into the set, maintaining the ascending order of probabilities.
  - Assign a 0 bit to the edge connecting the root node and the node with the lower probability, and a 1 bit to the edge connecting the root node and the node with the higher probability.
  - Traverse the tree from the root to the leaves, and concatenate the bits along the path to form the codeword for each symbol.
- An example of a minimum variance Huffman code is shown below for the following probability distribution:

| Symbol | Probability |
|--------|-------------|
| a      | 0.2         |
| b      | 0.2         |
| c      | 0.25        |
| d      | 0.05        |
| e      | 0.15        |
| f      | 0.15        |

- The Huffman tree and the corresponding codewords are:

```
     1.00
    /    \
  0.45    0.55
 /   \    /  \
0.2  0.25 0.3 0.25
a    c   / \  f
       0.15 0.15
       e    b
```

| Symbol | Codeword |
|--------|----------|
| a      | 00       |
| b      | 111      |
| c      | 01       |
| d      | 1100     |
| e      | 100      |
| f      | 101      |

- The expected codeword length is:

```
0.2 * 2 + 0.2 * 3 + 0.25 * 2 + 0.05 * 4 + 0.15 * 3 + 0.15 * 3 = 2.55 bits/symbol
```

- The variance of the codeword length is:

```
0.2 * (2 - 2.55)^2 + 0.2 * (3 - 2.55)^2 + 0.25 * (2 - 2.55)^2 + 0.05 * (4 - 2.55)^2 + 0.15 * (3 - 2.55)^2 + 0.15 * (3 - 2.55)^2 = 0.3475 bits^2/symbol
```

- The entropy of the source is:

```
-0.2 * log2(0.2) - 0.2 * log2(0.2) - 0.25 * log2(0.25) - 0.05 * log2(0.05) - 0.15 * log2(0.15) - 0

```
