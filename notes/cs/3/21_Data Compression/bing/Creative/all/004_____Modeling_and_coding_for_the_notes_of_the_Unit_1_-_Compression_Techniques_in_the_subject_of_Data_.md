# Modeling and Coding for Data Compression

Data compression is the process of reducing the size of data without losing any essential information. Data compression can be classified into two types: lossless and lossy. Lossless compression preserves the exact original data, while lossy compression discards some information that is deemed less important.

Modeling and coding are the two levels to compress data :

- In the first level, the data will be analyzed for any redundant information and extract it to develop a model. A model is a representation of the data that captures its structure and statistics. For example, a model can be a probability distribution of the symbols in the data, or a dictionary of common patterns in the data.
- In the second level, the difference between the modeled and actual data called residual is computed and is coded by an encoding technique. An encoding technique is a method of assigning binary codes to the symbols or patterns in the data, such that the codes are shorter for more frequent or important symbols or patterns, and longer for less frequent or less important ones. For example, an encoding technique can be a Huffman code, an arithmetic code, or a run-length code.

The goal of modeling and coding is to minimize the size of the encoded data, while maintaining the desired quality or fidelity of the original data.

Some examples of modeling and coding techniques for data compression are:

- Statistical modeling and coding: This technique uses the probability of each symbol in the data to assign codes. The symbols with higher probability are assigned shorter codes, and the symbols with lower probability are assigned longer codes. This technique is lossless and can be applied to any type of data. Examples of statistical modeling and coding are Huffman coding, arithmetic coding, and Golomb coding.
- Dictionary-based modeling and coding: This technique uses a dictionary of common patterns or strings in the data to assign codes. The patterns or strings that are in the dictionary are replaced by a single code, and the patterns or strings that are not in the dictionary are encoded as literals. This technique can be lossless or lossy, depending on the size and quality of the dictionary. Examples of dictionary-based modeling and coding are Lempel-Ziv coding, Burrows-Wheeler transform, and JPEG.
- Transform-based modeling and coding: This technique uses a mathematical transform to change the representation of the data from the spatial or temporal domain to the frequency or spectral domain. The transformed data is then quantized and coded. This technique is usually lossy, as some information is lost during the transformation and quantization. Examples of transform-based modeling and coding are discrete cosine transform, wavelet transform, and MPEG.