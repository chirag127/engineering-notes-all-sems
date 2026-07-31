### Mathematical Preliminaries for Lossless Compression

- Lossless compression is a technique that reduces the size of data without losing any information. The original data can be reconstructed exactly from the compressed data .
- Lossless compression is useful for applications that require high fidelity and accuracy, such as text, audio, images, and executable files.
- Lossless compression is based on the concept of entropy, which measures the amount of uncertainty or randomness in a source of data .
- Entropy is defined as the average number of bits needed to encode a symbol from the source, assuming an optimal encoding scheme .
- Entropy can be calculated using the formula: H(X) = - sum(p(x) log p(x)), where X is the source, p(x) is the probability of a symbol x, and log is the logarithm base 2 .
- Entropy is a lower bound for the compression ratio, which is the ratio of the size of the compressed data to the size of the original data .
- The compression ratio can be improved by using variable-length codes, which assign shorter codes to more frequent symbols and longer codes to less frequent symbols .
- Variable-length codes can be constructed using algorithms such as Huffman coding, arithmetic coding, and Lempel-Ziv coding .
- Huffman coding is a greedy algorithm that builds a binary tree based on the frequencies of the symbols, and assigns codes by traversing the tree from the root to the leaves .
- Arithmetic coding is a more efficient algorithm that assigns codes by dividing a unit interval into subintervals proportional to the probabilities of the symbols, and encoding a sequence of symbols by narrowing down the interval .
- Lempel-Ziv coding is a dictionary-based algorithm that exploits the redundancy and repetition in the data, and encodes a sequence of symbols by referencing previous occurrences in a sliding window .
- Lossless compression can be combined with other techniques such as run-length encoding, Burrows-Wheeler transform, and move-to-front transform to achieve higher compression ratios .