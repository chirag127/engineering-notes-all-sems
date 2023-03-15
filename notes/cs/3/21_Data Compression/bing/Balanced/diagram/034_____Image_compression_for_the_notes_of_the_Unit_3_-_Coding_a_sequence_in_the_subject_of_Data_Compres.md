### Image compression

Image compression is the process of reducing the size of an image file without compromising its quality or resolution. Image compression is useful for saving storage space, bandwidth, and transmission time. Image compression can be classified into two types: lossless and lossy.

- Lossless compression: Lossless compression is a technique that preserves the original data exactly, without any loss of information. Lossless compression is suitable for images that require high fidelity, such as medical images, text, and graphics. Lossless compression algorithms include:

  - Deflate: Deflate is a popular lossless image compression algorithm that uses a combination of the LZ77 compression algorithm and Huffman coding. Deflate is used in formats such as PNG, ZIP, and GZIP.
  - Run-length encoding: Run-length encoding is a lossless image compression technique that is used to reduce the size of an image by encoding sequences of repeated pixels. Run-length encoding is effective for images that have large areas of uniform color, such as icons and logos.
  - Arithmetic coding: Arithmetic coding is a lossless image compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence. Arithmetic coding is more efficient than Huffman coding, but also more complex and slower.

- Lossy compression: Lossy compression is a technique that discards some of the original data, resulting in some loss of quality. Lossy compression is suitable for images that can tolerate some degradation, such as photographs and videos. Lossy compression algorithms include:

  - Transform coding: Transform coding is a lossy image compression technique that uses mathematical transformations to reduce the size of an image. The idea behind transform coding is to convert the image data into a different representation that is more compact, making it easier to compress. Transform coding is commonly used for JPEGs.
  - Discrete cosine transform: Discrete cosine transform (DCT) is the most widely used form of transform coding. DCT is a type of Fourier-related transform, and was originally developed by Nasir Ahmed, T. Natarajan and K. R. Rao in 1974. DCT converts an image into a sum of cosine functions of different frequencies, and then discards the high-frequency components that are less visible to the human eye.
  - JPEG: JPEG is the most popular image format that uses lossy compression. JPEG stands for Joint Photographic Experts Group, which is the name of the committee that created the standard in 1992. JPEG uses DCT to compress an image into blocks of 8x8 pixels, and then applies a quantization matrix to reduce the number of bits per block. JPEG allows the user to adjust the compression level and the quality of the image.