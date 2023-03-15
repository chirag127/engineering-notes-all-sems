### Minimum variance Huffman codes

- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies or probabilities of occurrence.
- The code with the lowest frequency is assigned the longest code, and the code with the highest frequency is assigned the shortest code.
- The average code length is minimized by Huffman coding, which is equivalent to minimizing the expected value of the code length.
- However, Huffman coding does not necessarily minimize the variance of the code length, which is the measure of how much the code length deviates from the average.
- The variance of the code length is given by the formula:

![variance formula](https://latex.codecogs.com/png.latex?V%28L%29%20%3D%20%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%20p_i%28l_i-%5Cbar%7BL%7D%29%5E2)

where ![p_i](https://latex.codecogs.com/png.latex?p_i) is the probability of the i-th symbol, ![l_i](https://latex.codecogs.com/png.latex?l_i) is the code length of the i-th symbol, and ![L bar](https://latex.codecogs.com/png.latex?%5Cbar%7BL%7D) is the average code length.

- A minimum variance Huffman code is a Huffman code that minimizes the variance of the code length, subject to the constraint that the code is prefix-free.
- A prefix-free code is a code in which no codeword is a prefix of another codeword, which ensures that the code can be uniquely decoded.
- A minimum variance Huffman code can be constructed by modifying the standard Huffman algorithm, which is as follows:

  - Sort the symbols in descending order of their probabilities.
  - Create a binary tree with n leaves, where each leaf corresponds to a symbol and its probability.
  - Repeat until there is only one node left in the tree:
    - Select the two nodes with the lowest probabilities and merge them into a new node, whose probability is the sum of the two nodes' probabilities.
    - Assign the new node a code bit of 0 or 1, and append it to the code bits of its children.
    - Insert the new node into the tree and remove the two nodes that were merged.
  - The code for each symbol is obtained by traversing the tree from the root to the leaf and concatenating the code bits along the path.

- The modification for the minimum variance Huffman code is to assign the code bit of 0 to the node with the higher probability and the code bit of 1 to the node with the lower probability, when merging two nodes.
- This ensures that the symbols with higher probabilities have shorter codes and lower variances, and the symbols with lower probabilities have longer codes and higher variances.
- The minimum variance Huffman code is not unique, as there may be more than one way to assign the code bits when merging two nodes with equal probabilities.
- An example of constructing a minimum variance Huffman code is given below:

  - Suppose the source alphabet is A = {a1, a2, a3, a4, a5, a6}, with probabilities P(a1) = P(a2) = 0.2, P(a3) = 0.25, P(a4) = 0.05, P(a5) = P(a6) = 0.15.
  - The initial tree is:

![initial tree](https://i.imgur.com/5a9Q5Qo.png)

  - The first step is to merge a4 and a6, which have the lowest probabilities, into a new node with probability 0.2. Assign the code bit of 0 to a4 and the code bit of 1 to a6. The tree becomes:

![first step](https://i.imgur.com/7Q0c0Xy.png)

  - The second step is to merge a1 and a2, which have the lowest probabilities, into a new node with probability 0.4. Assign the code bit of 0 to a1 and the code bit of 1 to a2. The tree becomes:

![second step](https://i.imgur.com/0QZ8f0Z.png)

  - The third step is to merge the two nodes with probability