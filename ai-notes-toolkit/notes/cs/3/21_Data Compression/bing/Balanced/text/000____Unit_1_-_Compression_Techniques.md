## Unit 1 - Compression Techniques

- Compression techniques are methods of reducing the size of data without losing essential information.
- Compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the exact original data after decompression. They are suitable for applications that require high fidelity, such as text, audio, and images.
- Lossy compression techniques discard some data that is deemed less important or perceptible. They are suitable for applications that can tolerate some degradation, such as video, speech, and music.
- Some common lossless compression techniques are:
  - Run-length encoding (RLE): Replaces consecutive identical symbols with a symbol and a count.
  - Huffman coding: Assigns variable-length codes to symbols based on their frequencies.
  - Lempel-Ziv-Welch (LZW): Builds a dictionary of common patterns and encodes them with fixed-length codes.
- Some common lossy compression techniques are:
  - Transform coding: Applies a mathematical transform to the data and quantizes the coefficients.
  - Vector quantization: Divides the data into blocks and maps them to a set of representative vectors.
  - Differential coding: Encodes the difference between successive samples or frames.