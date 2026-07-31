### Tunstall codes for the notes of the Unit 2 - The Huffman coding algorithm in the subject of Data Compression

- Tunstall codes are a form of entropy coding used for lossless data compression.
- Tunstall codes are based on the idea of parsing a stochastic source with codewords of variable length and encoding them with codewords of fixed length.
- Tunstall codes are similar to Lempel-Ziv codes, but they use a predefined dictionary instead of building it dynamically from the input data.
- Tunstall codes have the advantage of being simpler and faster than Lempel-Ziv codes, but they have the disadvantage of requiring more memory and being less adaptive to the source statistics.
- Tunstall codes can be constructed by using a Huffman tree and pruning it to a desired depth, such that each leaf node corresponds to a fixed-length codeword.
- Tunstall codes can achieve the entropy of the source as the codeword length approaches infinity, but they are suboptimal for finite codeword lengths.
- Tunstall codes are suitable for sources with low entropy and high correlation, such as run-length encoded data.