### Modeling and coding for compression techniques

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the exact information of the original data, while lossy compression techniques discard some information that is considered less important or perceptible.
- Modeling and coding are the two levels to compress data :
  - In the first level, the data will be analyzed for any redundant information and extract it to develop a model. The model captures the probability distribution or the structure of the data.
  - In the second level, the difference between the modeled and actual data called residual is computed and is coded by an encoding technique. The encoding technique assigns shorter codes to more frequent or probable symbols and longer codes to less frequent or probable symbols.
- Some examples of modeling techniques are:
  - Markov models: These models assume that the probability of a symbol depends only on a fixed number of previous symbols. They can capture the statistical dependencies and patterns in the data.
  - Dictionary-based models: These models use a predefined or dynamically constructed dictionary of symbols or phrases to represent the data. They can exploit the repetitions and commonalities in the data.
  - Transform-based models: These models apply a mathematical transform to the data to change its representation from one domain to another. They can reduce the correlation and redundancy among the data elements.
- Some examples of coding techniques are:
  - Huffman coding: This is a lossless coding technique that assigns variable-length codes to the symbols based on their frequencies. It guarantees the optimal code length for a given source distribution.
  - Arithmetic coding: This is a lossless coding technique that assigns a single code to the entire data sequence based on its cumulative probability. It can achieve higher compression ratios than Huffman coding by avoiding the rounding errors.
  - Run-length encoding: This is a lossless coding technique that encodes the runs of identical symbols by their length and value. It is effective for compressing data with long runs of repeated symbols.
  - Lempel-Ziv coding: This is a lossless coding technique that uses a sliding window to store the previous symbols and encodes the current symbol by its position and length in the window. It is adaptive and can handle unknown or varying source distributions.
  - JPEG coding: This is a lossy coding technique that compresses images by applying a discrete cosine transform (DCT) to the image blocks, quantizing the DCT coefficients, and encoding them using Huffman or arithmetic coding. It can achieve high compression ratios by discarding the high-frequency components that are less visible to the human eye.
  - MP3 coding: This is a lossy coding technique that compresses audio by applying a modified discrete cosine transform (MDCT) to the audio frames, quantizing the MDCT coefficients, and encoding them using Huffman or arithmetic coding. It can achieve high compression ratios by discarding the components that are less audible to the human ear.