# Coding for the notes of the Unit 1 - Compression Techniques in the subject of Data Compression

- Data compression is the process of encoding information using fewer bits than the original representation.
- Data compression can reduce the storage space or transmission bandwidth required for a given piece of information.
- Data compression can be either lossless or lossy.
  - Lossless compression preserves the exact information of the original data, and can be reversed by decompression.
  - Lossy compression discards some information of the original data, and cannot be reversed by decompression.
- Data compression can be performed by using various techniques, such as :
  - Replacing repeated characters or patterns with shorter sequences or tokens (e.g., Lempel–Ziv algorithm).
  - Introducing pointers or references to a string of bits that the compression program has become familiar with (e.g., Huffman coding).
  - Removing redundant characters or information that are not essential for the data quality (e.g., JPEG compression).
  - Applying mathematical transformations to the data to reduce its complexity or dimensionality (e.g., Fourier transform).
- Data compression can be influenced by several factors, such as:
  - The compression level, which determines how much the data is reduced in size.
  - The compression type, which determines whether the data is lossless or lossy.
  - The coprocessor, which can speed up the compression or decompression process by offloading the workload from the main processor.
  - The data deduplication, which can eliminate duplicate data blocks or files before compression.
  - The multi-stage compression, which can apply different compression techniques in sequence to achieve higher compression ratios.