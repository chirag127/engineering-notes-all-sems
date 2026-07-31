# Models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

1. **Lossless Compression**: This technique compresses data without losing any information. The original data can be perfectly reconstructed from the compressed data. Examples of lossless compression algorithms include Huffman coding, arithmetic coding, and Lempel-Ziv-Welch (LZW) coding.

2. **Lossy Compression**: This technique compresses data by discarding some information. The original data cannot be perfectly reconstructed from the compressed data. However, the loss of information is usually not noticeable to the human eye or ear. Examples of lossy compression algorithms include JPEG for images and MP3 for audio.

3. **Run-Length Encoding (RLE)**: This technique compresses data by replacing consecutive repeated characters with a single character and a count of the number of repetitions. For example, the string "AAAAABBBBCCCC" would be compressed to "A5B4C4" using RLE.

4. **Dictionary-based Compression**: This technique compresses data by replacing common substrings with shorter codes. A dictionary of common substrings and their corresponding codes is maintained and used for compression and decompression. Examples of dictionary-based compression algorithms include LZW and DEFLATE.

5. **Transform-based Compression**: This technique compresses data by transforming it into a different representation that is more easily compressible. Examples of transform-based compression algorithms include the Discrete Cosine Transform (DCT) used in JPEG and the Discrete Wavelet Transform (DWT) used in JPEG 2000.

6. **Hybrid Compression**: This technique combines two or more of the above techniques to achieve better compression. For example, the DEFLATE algorithm combines dictionary-based compression with Huffman coding.
