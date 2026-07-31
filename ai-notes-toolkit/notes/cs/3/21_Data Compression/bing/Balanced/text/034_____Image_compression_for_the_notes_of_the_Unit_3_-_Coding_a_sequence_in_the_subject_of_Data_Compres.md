### Image compression

Image compression is the process of reducing the size of an image file without compromising its quality or resolution. Image compression is useful for saving storage space, bandwidth, and transmission time. Image compression can be classified into two types: lossless and lossy.

- Lossless compression: Lossless compression is a technique that preserves the original data exactly, meaning that the decompressed image is identical to the original image. Lossless compression is suitable for images that require high fidelity, such as medical images, text documents, or icons. Lossless compression algorithms include:

  - Deflate: Deflate is a popular lossless image compression algorithm that uses a combination of the LZ77 compression algorithm and Huffman coding. LZ77 replaces repeated sequences of pixels with shorter references, while Huffman coding assigns variable-length codes to the most frequent pixels. Deflate is used in formats such as PNG, GIF, and ZIP.

  - Run-length encoding: Run-length encoding is a simple lossless image compression technique that reduces the size of an image by encoding sequences of repeated pixels with a single value and a count. For example, a sequence of 10 white pixels can be encoded as (10, 255), where 10 is the count and 255 is the value. Run-length encoding is effective for images with large areas of uniform color, such as cartoons or logos.

  - Arithmetic coding: Arithmetic coding is a lossless image compression technique that assigns variable-length codes to the pixels based on their probabilities. Arithmetic coding is more efficient than Huffman coding, as it can use fractional bits to encode the pixels. Arithmetic coding is used in formats such as JPEG 2000 and JPEG-LS.

- Lossy compression: Lossy compression is a technique that discards some of the original data, meaning that the decompressed image is an approximation of the original image. Lossy compression is suitable for images that can tolerate some degradation, such as photographs, videos, or web graphics. Lossy compression algorithms include:

  - Transform coding: Transform coding is the most commonly used method of lossy compression. It converts the image data into a different representation that is more compact and easier to compress. The most widely used form of transform coding is the Discrete Cosine Transform (DCT), which decomposes the image into a sum of cosine functions of different frequencies. DCT is used in formats such as JPEG, MPEG, and MP3 .

  - Quantization: Quantization is the process of reducing the number of possible values for each pixel or coefficient. Quantization reduces the precision and the dynamic range of the image data, resulting in some loss of quality. Quantization is usually applied after transform coding, as the transformed coefficients have different levels of importance and can be quantized differently. Quantization is the main source of compression and distortion in lossy compression.

  - Entropy coding: Entropy coding is the process of assigning variable-length codes to the pixels or coefficients based on their frequencies. Entropy coding removes the redundancy and the statistical correlation in the image data, resulting in a smaller file size. Entropy coding is usually applied after quantization, as the quantized values have a non-uniform distribution and can be encoded more efficiently. Entropy coding algorithms include Huffman coding and arithmetic coding.