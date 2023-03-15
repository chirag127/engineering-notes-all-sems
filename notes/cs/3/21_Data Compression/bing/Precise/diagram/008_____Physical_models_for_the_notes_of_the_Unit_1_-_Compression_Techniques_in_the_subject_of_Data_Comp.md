### Physical models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

1. **Lossless Compression**: This technique compresses data without losing any information. The original data can be perfectly reconstructed from the compressed data. Examples include Huffman coding and arithmetic coding.

2. **Lossy Compression**: This technique compresses data by discarding some information. The original data cannot be perfectly reconstructed from the compressed data. However, the loss of information is usually not noticeable to the human eye or ear. Examples include JPEG and MP3.

3. **Run-Length Encoding**: This technique compresses data by replacing consecutive occurrences of the same symbol with a single occurrence of the symbol followed by the number of occurrences. For example, the string "AAAABBBCC" would be compressed to "A4B3C2".

4. **Dictionary-based Compression**: This technique compresses data by replacing common substrings with shorter codes. The codes and their corresponding substrings are stored in a dictionary. Examples include LZW and LZ77.

5. **Transform-based Compression**: This technique compresses data by transforming it into a different representation that is more easily compressible. Examples include the Discrete Cosine Transform (DCT) used in JPEG and the Discrete Wavelet Transform (DWT) used in JPEG 2000.

6. **Hybrid Compression**: This technique combines two or more of the above techniques to achieve better compression. Examples include the use of Huffman coding with DCT in JPEG and the use of arithmetic coding with DWT in JPEG 2000.