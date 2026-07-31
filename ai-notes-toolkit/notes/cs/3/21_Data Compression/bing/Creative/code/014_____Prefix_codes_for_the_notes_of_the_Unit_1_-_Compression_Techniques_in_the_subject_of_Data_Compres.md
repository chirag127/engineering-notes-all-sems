# Prefix codes for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- A prefix code is a type of code that assigns binary codewords to symbols such that no codeword is a prefix of another codeword.
- Prefix codes are also known as prefix-free codes, prefix condition codes and instantaneous codes.
- Prefix codes have the property of unique decodability, which means that any encoded message can be unambiguously decoded without any ambiguity or error.
- Prefix codes are widely used in data compression, because they can achieve optimal or near-optimal compression ratios for various probability distributions of symbols .
- Some examples of prefix codes are Huffman codes, arithmetic codes, Elias codes, Golomb codes and universal codes .
- A universal code is a special kind of prefix code that can compress any monotonic probability distribution of integers (i.e., p(i) ≥ p(i + 1) for all positive i) within a constant factor of the optimal code.
- A prefix code can be represented by a binary tree, where each leaf node corresponds to a symbol and its codeword, and each internal node corresponds to a common prefix of its children.
- To encode a message using a prefix code, one can traverse the binary tree from the root to the leaf that matches each symbol, and output the bits along the path.
- To decode a message using a prefix code, one can traverse the binary tree from the root to the leaf that matches each bit sequence, and output the symbol at the leaf.
- The expected length of a prefix code for a given probability distribution of symbols is the sum of the products of the codeword lengths and the symbol probabilities.
- The optimal prefix code for a given probability distribution of symbols is the one that minimizes the expected length.
- Huffman coding is a popular algorithm for constructing the optimal prefix code for a given probability distribution of symbols.
- Huffman coding works by creating a binary tree from the bottom up, by merging the two least probable symbols at each step, until only one node remains as the root.
- The codeword for each symbol is obtained by reading the bits along the path from the root to the leaf that corresponds to the symbol.
- Huffman coding can achieve the optimal compression ratio for any discrete memoryless source, which is a source that produces symbols independently and with fixed probabilities.
- Huffman coding can also be generalized to adaptive Huffman coding, which can adjust the codewords dynamically based on the changing probabilities of symbols in the input stream.