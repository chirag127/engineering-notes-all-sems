### Mathematical Preliminaries for Lossless Compression

- Lossless compression is a technique that reduces the size of data without losing any information. The original data can be exactly reconstructed from the compressed data.
- Lossless compression is useful for applications that require high fidelity and accuracy, such as text, audio, images, and executable files.
- Lossless compression is based on the concept of entropy, which measures the amount of information or uncertainty in a data source. The lower the entropy, the more predictable and compressible the data is.
- Entropy can be calculated using different models, such as the zero-order model, the first-order model, the k-th order model, and the Markov model. These models capture the statistical properties and dependencies of the data symbols.
- The entropy of a data source is the lower bound for the average number of bits per symbol needed to encode the data. No lossless compression scheme can achieve a compression ratio lower than the entropy of the data source.
- The compression ratio is the ratio of the size of the compressed data to the size of the original data. The higher the compression ratio, the more efficient the compression scheme is.
- The compression efficiency is the ratio of the entropy of the data source to the average number of bits per symbol used by the compression scheme. The higher the compression efficiency, the closer the compression scheme is to the optimal encoding.
- Some common lossless compression techniques are Huffman coding, arithmetic coding, run-length encoding, dictionary-based encoding, and Lempel-Ziv encoding. These techniques use different methods to assign variable-length codes to the data symbols based on their probabilities or frequencies.