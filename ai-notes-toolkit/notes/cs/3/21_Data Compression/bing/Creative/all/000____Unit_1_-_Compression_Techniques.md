## Unit 1 - Compression Techniques

- Compression techniques are methods of reducing the size of data without losing information or quality.
- Compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the exact original data after decompression. They are suitable for text, audio, and some images that require high fidelity.
- Lossy compression techniques discard some data that is deemed less important or perceptible. They are suitable for images, video, and some audio that can tolerate some degradation.
- Compression techniques can be further divided into two types: symmetric and asymmetric.
- Symmetric compression techniques use the same algorithm for both compression and decompression. They are faster and simpler, but require the same software or hardware at both ends.
- Asymmetric compression techniques use different algorithms for compression and decompression. They are slower and more complex, but allow more flexibility and compatibility.
- Some examples of compression techniques are:

  - Huffman coding: a lossless symmetric technique that assigns variable-length codes to symbols based on their frequency of occurrence.
  - Run-length encoding: a lossless symmetric technique that replaces repeated symbols with a count and a symbol.
  - Lempel-Ziv-Welch (LZW): a lossless symmetric technique that builds a dictionary of common patterns and replaces them with codes.
  - JPEG: a lossy symmetric technique that applies discrete cosine transform (DCT) and quantization to reduce the size of images.
  - MPEG: a lossy symmetric technique that applies DCT, quantization, and motion estimation to reduce the size of video and audio.
  - MP3: a lossy symmetric technique that applies psychoacoustic modeling and Huffman coding to reduce the size of audio.
  - ZIP: a lossless asymmetric technique that combines different algorithms such as LZW, Huffman coding, and deflate to compress files.
  - GZIP: a lossless asymmetric technique that uses deflate algorithm to compress files.
  - BZIP2: a lossless asymmetric technique that uses Burrows-Wheeler transform and Huffman coding to compress files.