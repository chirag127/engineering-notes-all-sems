### Physical models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

1. **Lossless Compression**: This technique involves compressing data without losing any information. The original data can be perfectly reconstructed from the compressed data. Examples of lossless compression techniques include Huffman coding, arithmetic coding, and Lempel-Ziv-Welch (LZW) coding.

2. **Lossy Compression**: This technique involves compressing data by discarding some information. The original data cannot be perfectly reconstructed from the compressed data. However, the loss of information is usually not noticeable to the human eye or ear. Examples of lossy compression techniques include JPEG for images and MP3 for audio.

3. **Entropy Encoding**: This technique involves encoding data based on the probability of occurrence of each symbol in the data. Symbols that occur more frequently are assigned shorter codes, while symbols that occur less frequently are assigned longer codes. This results in a more efficient encoding of the data. Examples of entropy encoding techniques include Huffman coding and arithmetic coding.

4. **Dictionary-based Compression**: This technique involves replacing common substrings in the data with shorter codes. A dictionary of common substrings and their corresponding codes is maintained. Examples of dictionary-based compression techniques include Lempel-Ziv-Welch (LZW) coding and DEFLATE.

5. **Transform Coding**: This technique involves transforming the data into a different domain, where it can be more efficiently compressed. Examples of transform coding techniques include the Discrete Cosine Transform (DCT) used in JPEG and the Modified Discrete Cosine Transform (MDCT) used in MP3.

6. **Run-length Encoding**: This technique involves replacing consecutive occurrences of the same symbol with a single occurrence of the symbol followed by the number of occurrences. This can result in significant compression for data with long runs of the same symbol. Run-length encoding is commonly used in fax machines and in the BMP image format.

7. **Predictive Coding**: This technique involves predicting the value of a symbol based on the values of previous symbols. The difference between the predicted value and the actual value is then encoded. Predictive coding can result in significant compression for data with strong correlations between adjacent symbols. Examples of predictive coding techniques include delta encoding and linear predictive coding.