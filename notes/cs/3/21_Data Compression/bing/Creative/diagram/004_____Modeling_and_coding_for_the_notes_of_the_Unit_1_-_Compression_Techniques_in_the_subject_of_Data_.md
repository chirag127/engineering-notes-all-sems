### Modeling and coding for data compression

- Data compression is the process of reducing the size of data without losing essential information or quality.
- Data compression can be divided into two levels: modeling and coding .
- Modeling is the process of analyzing the data and finding patterns, redundancies, or correlations that can be used to represent the data more efficiently.
- Coding is the process of encoding the data using a set of symbols or codes that can be decoded by the receiver.
- There are two types of data compression: lossless and lossy.
- Lossless data compression preserves the exact information of the original data and allows perfect reconstruction after decompression.
- Lossy data compression discards some information of the original data and allows only approximate reconstruction after decompression.
- Lossless data compression is generally implemented using one of two different types of modeling: statistical or dictionary-based.
- Statistical modeling reads in and encodes a single symbol at a time using the probability of that character’s appearance. Examples of statistical modeling are Huffman coding, arithmetic coding, and Golomb coding.
- Dictionary-based modeling uses a single code to replace strings of symbols that are stored in a dictionary. Examples of dictionary-based modeling are Lempel-Ziv (LZ) coding, Lempel-Ziv-Welch (LZW) coding, and Burrows-Wheeler transform (BWT) coding.
- Lossy data compression is generally implemented using transform-based modeling, which converts the data into a different domain that allows better compression of the relevant information. Examples of transform-based modeling are discrete cosine transform (DCT), wavelet transform, and Fourier transform.
- A recent approach to data compression is based on deep learning, which uses neural networks to learn the optimal representation of the data and the optimal coding scheme. An example of deep learning-based compression is Bit-Swap, which uses latent variable models and bits-back coding.