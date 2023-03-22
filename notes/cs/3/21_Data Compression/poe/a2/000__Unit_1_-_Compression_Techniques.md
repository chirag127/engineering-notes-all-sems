 Here is the content in markdown format without any emojis or external links, written in a formal tone with points inside the given header:

## Unit 1 - Compression Techniques

1. Lossless Compression:
- Entropy coding: Huffman coding, arithmetic coding
- Dictionary techniques: LZ77, LZ78
- Run-length encoding

Advantages: Original data can be perfectly reconstructed from the compressed data.

2. Lossy Compression:
- Quantization: Reduction in the number of bits used to represent a signal
- Audio compression: MP3, AAC, Vorbis
- Image compression: JPEG, PNG

Advantages: Much higher compression ratios than lossless compression.
Disadvantages: Original data cannot be perfectly reconstructed from the compressed data.

3. JPEG Image Compression:
- Divide image into 8x8 blocks
- Apply Discrete Cosine Transform (DCT) on each block
- Quantize the DCT coefficients
- Entropy encode the quantized DCT coefficients

Advantages: High compression ratio, minimal loss of perceptual quality.
Disadvantages: Lossy compression, visible compression artifacts may appear at high compression ratios.