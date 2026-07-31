### Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence.
- The code with the lowest probability gets the longest code and the code with the highest probability gets the shortest code.
- The expected code length is the weighted average of the code lengths, where the weights are the symbol probabilities.
- The variance of the code length is the weighted average of the squared deviations of the code lengths from the expected code length, where the weights are the symbol probabilities.
- The minimum variance Huffman code is a variant of Huffman coding that minimizes not only the expected code length but also the variance of the code length .
- The minimum variance Huffman code has the property that the code lengths are as close as possible to each other, and the difference between the maximum and minimum code lengths is at most one.
- The minimum variance Huffman code can be constructed by modifying the standard Huffman algorithm as follows:
  - Sort the symbols in nonincreasing order of probability and assign them to the leaves of a binary tree.
  - Repeat until there is only one node left:
    - Select the two nodes with the smallest probabilities and merge them into a new node with the probability equal to the sum of their probabilities.
    - If the two nodes have different depths in the tree, increase the depth of the shallower node by one.
    - Insert the new node into the sorted list of nodes.
  - Assign a bit (0 or 1) to each edge of the tree and concatenate the bits along the path from the root to each leaf to obtain the code for each symbol.
- The minimum variance Huffman code can be useful for applications where the variance of the code length is important, such as real-time communication or encryption.