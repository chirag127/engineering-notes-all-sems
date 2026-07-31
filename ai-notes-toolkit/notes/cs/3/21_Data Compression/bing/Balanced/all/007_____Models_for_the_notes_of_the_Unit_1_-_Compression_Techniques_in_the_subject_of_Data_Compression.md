# Models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Data compression is the process of reducing the size of data without losing information or degrading its quality.
- Data compression can be classified into two types: lossless and lossy.
- Lossless compression techniques preserve the exact original data after decompression, while lossy compression techniques discard some information and produce an approximation of the original data after decompression.
- Lossless compression techniques are suitable for applications that require exact reproduction of the original data, such as text, audio, or executable files.
- Lossy compression techniques are suitable for applications that can tolerate some degradation of the original data, such as images, video, or speech.
- Some common lossless compression techniques are:
  - Run-length encoding (RLE): replaces consecutive identical symbols with a symbol and a count.
  - Huffman coding: assigns variable-length codes to symbols based on their frequencies of occurrence.
  - Lempel-Ziv coding: exploits the repetition of patterns in the data by using pointers to previous occurrences.
  - Arithmetic coding: assigns codes to symbols based on their probabilities of occurrence and the context of the data.
- Some common lossy compression techniques are:
  - Transform coding: transforms the data into a different domain, such as frequency or wavelet, and discards the less significant components.
  - Quantization: reduces the number of bits used to represent each symbol by grouping them into levels or bins.
  - Vector quantization: represents blocks of data as vectors and assigns them to clusters or codebooks.
  - Differential coding: encodes the difference between successive symbols rather than the symbols themselves.
  - Predictive coding: predicts the next symbol based on the previous symbols and encodes the error or residual.