## Unit 1 - Compression Techniques

- Compression is the process of reducing the size of data without losing information or quality.
- Compression techniques can be classified into two categories: lossless and lossy.
- Lossless compression techniques preserve the exact original data after decompression. They are suitable for text, audio, and some images that require high fidelity.
- Lossy compression techniques discard some data that is deemed less important or perceptible. They are suitable for images, video, and some audio that can tolerate some quality degradation.
- Some common lossless compression techniques are:
  - Run-length encoding (RLE): replaces consecutive identical symbols with a count and a symbol.
  - Huffman coding: assigns variable-length codes to symbols based on their frequency of occurrence.
  - Lempel-Ziv-Welch (LZW): builds a dictionary of common patterns and encodes them with fixed-length codes.
- Some common lossy compression techniques are:
  - JPEG: uses discrete cosine transform (DCT) and quantization to compress images.
  - MPEG: uses DCT, quantization, and motion estimation to compress video.
  - MP3: uses psychoacoustic model and bit allocation to compress audio.