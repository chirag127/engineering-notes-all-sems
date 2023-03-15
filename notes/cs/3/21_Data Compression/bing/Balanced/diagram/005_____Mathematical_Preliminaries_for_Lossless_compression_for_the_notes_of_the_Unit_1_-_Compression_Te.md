### Mathematical Preliminaries for Lossless Compression

- Lossless compression is a technique that reduces the size of data without losing any information. The original data can be exactly reconstructed from the compressed data .
- Lossless compression is useful for applications that require high fidelity and accuracy, such as text, audio, images, and executable files.
- Lossless compression is based on the concept of entropy, which measures the average amount of information per symbol in a data source .
- Entropy is defined as:

$$
H(X) = -\sum_{x \in X} p(x) \log_2 p(x)
$$

where $X$ is the set of possible symbols, and $p(x)$ is the probability of symbol $x$ occurring in the data source .
- Entropy is a lower bound for the average number of bits per symbol needed to encode the data source. The closer the entropy is to the average number of bits per symbol, the more efficient the compression scheme is .
- Lossless compression schemes can be classified into two categories: statistical and dictionary-based .
- Statistical compression schemes assign variable-length codes to symbols based on their probabilities. The more frequent symbols are assigned shorter codes, and the less frequent symbols are assigned longer codes. This reduces the average number of bits per symbol .
- Examples of statistical compression schemes are Huffman coding, arithmetic coding, and Golomb coding .
- Dictionary-based compression schemes use a predefined or dynamically generated dictionary of strings to replace repeated occurrences of the same string with a shorter code. This reduces the redundancy in the data .
- Examples of dictionary-based compression schemes are Lempel-Ziv (LZ) coding, Lempel-Ziv-Welch (LZW) coding, and Burrows-Wheeler transform (BWT) coding .