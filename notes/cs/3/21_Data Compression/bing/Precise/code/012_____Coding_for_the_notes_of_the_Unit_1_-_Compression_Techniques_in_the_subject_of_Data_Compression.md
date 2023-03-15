### Unit 1 - Compression Techniques in Data Compression

Data compression is the process of encoding information using fewer bits than the original representation. Compression can be lossy or lossless. Lossless compression reduces bits by identifying and eliminating statistical redundancy. Lossy compression reduces bits by removing less important information.

There are several techniques used for data compression, including:

1. **Run-length encoding (RLE)**: This technique replaces sequences of the same data values within a file by a count number and a single value. It is useful for compressing data with many runs of repeated values.

2. **Huffman coding**: This technique uses a variable-length code table for encoding a source symbol where the variable-length code table has been derived in a particular way based on the estimated probability of occurrence for each possible value of the source symbol.

3. **Arithmetic coding**: This technique represents a long sequence of symbols as a single floating-point number. It is more efficient than Huffman coding for compressing data with high entropy.

4. **Dictionary-based compression**: This technique replaces strings of characters with single codes. It is useful for compressing text data.

5. **Transform coding**: This technique transforms the data into a different representation that is more compressible. It is commonly used for compressing image, audio, and video data.

These are some of the common compression techniques used in data compression. Each technique has its own advantages and disadvantages and is suitable for different types of data. It is important to choose the right technique for the data being compressed to achieve the best compression ratio.