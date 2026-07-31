### Models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

1. **Lossless Compression**: This technique compresses data without losing any information. The original data can be perfectly reconstructed from the compressed data. Examples of lossless compression algorithms include Huffman coding, arithmetic coding, and Lempel-Ziv-Welch (LZW) coding.

2. **Lossy Compression**: This technique compresses data by discarding some information. The original data cannot be perfectly reconstructed from the compressed data. However, the loss of information is usually not noticeable to the human eye or ear. Examples of lossy compression algorithms include JPEG for images and MP3 for audio.

3. **Run-Length Encoding (RLE)**: This is a simple form of lossless data compression in which runs of data (sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run.

4. **Dictionary-based Compression**: This is a lossless data compression technique that uses a dictionary to encode data. The dictionary is built based on the data being compressed and is used to encode the data in a more compact form. Examples of dictionary-based compression algorithms include LZW and DEFLATE.

5. **Transform-based Compression**: This is a lossy data compression technique that transforms the data into a different representation, making it easier to compress. Examples of transform-based compression algorithms include the Discrete Cosine Transform (DCT) used in JPEG and the Modified Discrete Cosine Transform (MDCT) used in MP3.

6. **Hybrid Compression**: This is a combination of lossless and lossy compression techniques. The data is first compressed using a lossless technique, and then further compressed using a lossy technique. This can result in higher compression ratios than using either technique alone.