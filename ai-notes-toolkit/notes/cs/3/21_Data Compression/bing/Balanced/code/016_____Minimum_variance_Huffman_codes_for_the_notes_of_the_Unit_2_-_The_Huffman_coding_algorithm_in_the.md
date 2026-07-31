### Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence.
- The code with the minimum expected codeword length is called the minimum redundancy code or the optimal prefix code.
- The expected codeword length is the weighted average of the codeword lengths, where the weights are the probabilities of the symbols.
- The variance of the codeword length is the weighted average of the squared deviations of the codeword lengths from the expected codeword length, where the weights are the probabilities of the symbols.
- The variance of the codeword length measures the variability or dispersion of the codeword lengths around the mean.
- A minimum variance Huffman code is a Huffman code that minimizes the variance of the codeword length, subject to the constraint that the code is optimal (minimum redundancy).
- A minimum variance Huffman code can be constructed by modifying the standard Huffman algorithm as follows:
  - Sort the symbols in nonincreasing order of probability.
  - If there are more than two symbols, merge the two symbols with the smallest probabilities into a new symbol with the sum of their probabilities, and repeat until there are only two symbols left.
  - Assign the codeword 0 to the symbol with the larger probability and the codeword 1 to the symbol with the smaller probability.
  - For each merged symbol, split it into its original symbols and append 0 to the codeword of the symbol with the larger probability and 1 to the codeword of the symbol with the smaller probability, and repeat until all the symbols are restored.
- A minimum variance Huffman code has the property that the codeword lengths are as close as possible to the entropy of the source, which is the lower bound on the expected codeword length.
- A minimum variance Huffman code can also be seen as a length-limited Huffman code, where the length of each codeword is restricted to be less than or equal to a given constant.
- A length-limited Huffman code can be constructed by using the package-merge algorithm, which is a generalization of the standard Huffman algorithm that allows merging more than two symbols at a time.