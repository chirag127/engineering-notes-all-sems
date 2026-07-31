### Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence.
- The code with the minimum expected codeword length is called the minimum redundancy code or the optimal prefix code.
- The minimum variance Huffman code is a variant of the minimum redundancy code that also minimizes the variance of the codeword length.
- The variance of the codeword length is the difference between the maximum and minimum lengths of the codewords.
- A lower variance means that the codewords have more uniform lengths and are less likely to cause buffer overflow or underflow.
- The minimum variance Huffman code can be constructed by modifying the Huffman algorithm to use a priority queue that sorts the symbols by their probabilities and then by their lengths.
- The algorithm merges the two symbols with the lowest probabilities and assigns them a common prefix, then inserts the merged symbol back into the queue with the sum of their probabilities and the length incremented by one.
- The algorithm repeats this process until there is only one symbol left in the queue, which is the root of the Huffman tree.
- The minimum variance Huffman code can be obtained by traversing the Huffman tree and assigning 0 or 1 to each branch.
- The minimum variance Huffman code has the property that the codewords with the same length are lexicographically ordered according to their probabilities.
- The minimum variance Huffman code is useful for applications that require a bounded codeword length or a low variance of the codeword length.
- An example of a minimum variance Huffman code for a source with six symbols and their probabilities is shown below:

| Symbol | Probability | Codeword | Length |
|--------|-------------|----------|--------|
| a1     | 0.2         | 00       | 2      |
| a2     | 0.2         | 01       | 2      |
| a3     | 0.25        | 10       | 2      |
| a4     | 0.05        | 1100     | 4      |
| a5     | 0.15        | 1101     | 4      |
| a6     | 0.15        | 111      | 3      |

- The Huffman tree for this code is shown below:

```
       1.0
      /   \
    0.5   0.5
   /   \ /   \
 0.25 0.2 0.2 0.15
 /  \       /  \
0.15 0.1   0.05 0.1
```

- The entropy of the source is 2.405 bits/symbol.
- The average length of the code is 2.55 bits/symbol.
- The efficiency of the code is 94.32%.
- The variance of the code is 2 bits/symbol.