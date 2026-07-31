### Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies or probabilities of occurrence.
- The goal of Huffman coding is to minimize the expected value of the code length, or the average number of bits per symbol.
- The code length of a symbol is the number of bits in its corresponding code word. For example, if a symbol has a code word of 101, its code length is 3 bits.
- The code variance of a Huffman code is the difference between the maximum and minimum code lengths. For example, if the code lengths range from 2 to 4 bits, the code variance is 2.
- A minimum variance Huffman code is a Huffman code that has the smallest possible code variance among all Huffman codes with the same expected code length.
- A minimum variance Huffman code can be constructed by modifying the standard Huffman algorithm as follows:
  - Sort the symbols in non-increasing order of their frequencies or probabilities.
  - Create a binary tree with a leaf node for each symbol.
  - While there are more than two nodes in the tree, do the following:
    - Find the two nodes with the smallest frequencies or probabilities and merge them into a new node with their sum as its frequency or probability.
    - If there are more than two nodes with the same smallest frequency or probability, choose the two nodes that are farthest to the right in the sorted list.
    - Insert the new node into the sorted list in the appropriate position.
  - Assign a bit (0 or 1) to each edge of the tree, starting from the root and going down to the leaves.
  - The code word for each symbol is the sequence of bits along the path from the root to its leaf node.
- A minimum variance Huffman code has the following properties:
  - It is a prefix code, meaning that no code word is a prefix of another code word.
  - It is optimal, meaning that it minimizes the expected code length among all prefix codes.
  - It is unique, meaning that there is only one minimum variance Huffman code for a given set of symbol frequencies or probabilities.
  - It is balanced, meaning that the difference between the depths of any two leaf nodes is at most one.
- An example of a minimum variance Huffman code is shown below:

| Symbol | Probability | Code word | Code length |
|--------|-------------|-----------|-------------|
| a1     | 0.2         | 00        | 2           |
| a2     | 0.2         | 01        | 2           |
| a3     | 0.25        | 10        | 2           |
| a4     | 0.05        | 1100      | 4           |
| a5     | 0.15        | 1101      | 4           |
| a6     | 0.15        | 111       | 3           |

- The expected code length for this code is 2.45 bits per symbol.
- The code variance for this code is 2 bits.
- The entropy of the source is 2.405 bits per symbol.
- The efficiency of the code is 98.16%.