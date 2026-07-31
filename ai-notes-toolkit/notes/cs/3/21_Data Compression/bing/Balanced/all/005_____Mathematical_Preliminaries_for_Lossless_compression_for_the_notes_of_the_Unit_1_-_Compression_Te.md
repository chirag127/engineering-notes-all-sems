# Mathematical Preliminaries for Lossless Compression

- Lossless compression is a technique that reduces the size of data without losing any information. The original data can be exactly reconstructed from the compressed data .
- Lossless compression is useful for applications that require high fidelity and accuracy, such as text, audio, images, and executable files .
- Lossless compression is based on the concept of entropy, which measures the amount of uncertainty or randomness in a data source .
- Entropy is defined as the average number of bits needed to encode a symbol from the source, assuming an optimal encoding scheme .
- Entropy can be calculated using the formula: H(X) = - sum(p(x) log p(x)), where X is the source, p(x) is the probability of a symbol x, and log is the logarithm base 2 .
- Entropy is a lower bound for the compression ratio, which is the ratio of the compressed size to the original size. The compression ratio cannot be lower than the entropy of the source .
- Lossless compression techniques can be classified into two categories: statistical and dictionary-based .
- Statistical techniques use the probability distribution of the source symbols to assign variable-length codes to each symbol. The more frequent symbols are assigned shorter codes, and the less frequent symbols are assigned longer codes .
- Dictionary-based techniques use a predefined or dynamically generated dictionary of strings to replace repeated occurrences of the same string with a shorter code. The dictionary can be shared or transmitted along with the compressed data .
- Some examples of lossless compression algorithms are Huffman coding, arithmetic coding, Lempel-Ziv-Welch (LZW) algorithm, and run-length encoding (RLE) .