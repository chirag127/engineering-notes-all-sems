### Models for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

Compression Techniques are widely used to reduce the size of data without significant loss of information. Various models have been developed to achieve this objective. In this unit, we will study different models that are commonly used in Data Compression.

Here are the models we will cover:

1. Lossless Compression Model:
   - In this model, the compressed data can be restored to its original form exactly as it was before compression.
   - This model is used when it is important to retain all the information in the original data.
   - Examples of lossless compression techniques include Huffman Coding, Arithmetic Coding, and Lempel-Ziv-Welch (LZW) Compression.

2. Lossy Compression Model:
   - In this model, some information is lost during compression, and the compressed data cannot be restored to its original form exactly as it was before compression.
   - This model is used when it is acceptable to lose some information in the original data.
   - Examples of lossy compression techniques include JPEG Compression, MPEG Compression, and MP3 Compression.

3. Hybrid Compression Model:
   - This model combines both lossless and lossy compression techniques.
   - The data is first compressed using lossless compression techniques, and then the compressed data is further compressed using lossy compression techniques.
   - This model is used when it is important to retain most of the information in the original data, but some loss of information is acceptable.
   - Examples of hybrid compression techniques include JPEG2000 and PNG.

4. Dictionary-Based Compression Model:
   - In this model, a dictionary is used to map frequently occurring patterns in the data to shorter codes.
   - The compressed data consists of these shorter codes, which can be used to reconstruct the original data.
   - Examples of dictionary-based compression techniques include Lempel-Ziv (LZ) Compression and its variants, such as LZ77 and LZ78.

5. Transform-Based Compression Model:
   - In this model, the data is transformed into a different domain, where it can be compressed more efficiently.
   - The compressed data is then transformed back to its original domain to reconstruct the original data.
   - Examples of transform-based compression techniques include Discrete Cosine Transform (DCT) used in JPEG Compression and Discrete Wavelet Transform (DWT) used in JPEG2000 and MPEG Compression.

These models are essential to understand for anyone interested in the field of Data Compression. By studying these models, we can gain insights into how compression techniques work and how we can use them to efficiently store and transmit data.