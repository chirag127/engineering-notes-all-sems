# Modeling and coding for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Modeling and coding are two fundamental steps in data compression.
- Modeling is the process of finding a suitable representation of the data that captures its essential features and reduces its redundancy.
- Coding is the process of assigning binary codes to the symbols or units of the model, such that the length of the code reflects the probability or frequency of the symbol.
- There are two main types of models: statistical and dictionary-based.
- Statistical models use the probability distribution of the data to assign codes to the symbols. The most common statistical models are Huffman coding and arithmetic coding.
- Dictionary-based models use a predefined or adaptive set of strings to represent the data. The most common dictionary-based models are LZ77, LZ78, and LZW.
- The choice of the model and the coding scheme depends on the characteristics of the data and the compression objectives. Some factors that affect the choice are:
  - The size and complexity of the data
  - The type and amount of redundancy in the data
  - The desired compression ratio and quality
  - The computational and memory resources available
  - The encoding and decoding speed and complexity
- Modeling and coding are often combined or integrated to achieve better compression performance and efficiency. Some examples of integrated methods are:
  - Adaptive Huffman coding, which updates the model and the code dynamically based on the data
  - Run-length encoding, which uses a simple model of repeated symbols and a fixed-length code
  - Burrows-Wheeler transform, which transforms the data into a more compressible form and then applies a statistical or dictionary-based coding
  - JPEG, which uses a discrete cosine transform to model the image blocks and a Huffman or arithmetic coding to encode the coefficients