### Need for data compression

- Data compression is the process of reducing the number of bits needed to represent data by using encoding techniques.
- Data compression can be either lossless or lossy. Lossless compression preserves the original information without any distortion, while lossy compression discards some information to achieve higher compression ratios.
- Data compression is needed for various reasons, such as:
  - Saving storage space and cost: Compressing data can reduce the amount of memory or disk space required to store the data, which can lower the hardware expenses and maintenance costs.
  - Improving transmission speed and efficiency: Compressing data can reduce the amount of bandwidth or time needed to transmit the data over a network or a communication channel, which can improve the performance and reliability of the system.
  - Enhancing security and privacy: Compressing data can make the data more difficult to access or interpret by unauthorized parties, which can protect the confidentiality and integrity of the data.
- Data compression is especially important for image processing, because images typically contain a large amount of data that can be redundant or irrelevant for certain applications. Some examples of image compression techniques are:
  - Run-length encoding: A simple lossless compression method that replaces consecutive identical pixels with a single value and a count of how many times it occurs.
  - Huffman coding: A lossless compression method that assigns variable-length codes to pixels based on their frequencies, such that more common pixels have shorter codes and less common pixels have longer codes.
  - JPEG: A lossy compression standard that divides an image into blocks and applies discrete cosine transform (DCT) and quantization to each block, followed by Huffman coding or arithmetic coding to the resulting coefficients.
  - PNG: A lossless compression standard that applies a filter to each row of pixels to reduce the correlation between adjacent pixels, followed by Huffman coding or deflate algorithm to the filtered data.
  - GIF: A lossy compression standard that reduces the number of colors in an image to a maximum of 256, followed by Lempel-Ziv-Welch (LZW) algorithm to the indexed data.