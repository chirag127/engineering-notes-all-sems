### Mathematical Preliminaries for Lossless Compression

- Lossless compression is a technique that reduces the size of a data file without losing any information or distorting the original data.
- Lossless compression is based on the concept of **entropy**, which measures the average amount of information per symbol in a data source.
- Entropy is defined as `H(X) = -sum(p(x)log(p(x)))`, where `X` is a discrete random variable, `p(x)` is the probability of occurrence of symbol `x`, and `log` is the logarithm base 2.
- Entropy is a lower bound for the average number of bits per symbol required to encode a data source without loss of information.
- Lossless compression algorithms try to achieve an encoding that is close to the entropy of the data source, or in other words, to minimize the **redundancy** of the data.
- Redundancy is the difference between the actual average number of bits per symbol and the entropy of the data source. It can be expressed as `R(X) = L(X) - H(X)`, where `L(X)` is the actual average number of bits per symbol.
- Redundancy can be reduced by exploiting the **statistical properties** of the data source, such as the frequency of occurrence of symbols, the correlation between symbols, and the patterns or regularities in the data.
- Some common lossless compression techniques are **Huffman coding**, **arithmetic coding**, **run-length encoding**, **dictionary-based encoding**, and **Lempel-Ziv encoding**. Each technique has its own advantages and disadvantages, depending on the characteristics of the data source and the compression requirements.