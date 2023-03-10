 Here is the content in markdown format for the given topic:

### Lossless Image Compression using Huffman Coding

- Huffman Coding is a lossless data compression algorithm. It assigns variable-length codes to input characters based on their frequencies. Characters that occur more frequently are assigned shorter codes and characters that occur less frequently are assigned longer codes.
- For image compression, the image is first converted into a 1D array by reading pixel values row-wise. These pixel values are then encoded using Huffman Coding. The Huffman Tree is built from the frequency of occurrence of each pixel value in the image. More frequent pixel values are assigned shorter codes and less frequent pixel values are assigned longer codes.
- The compressed image contains the Huffman coding for each pixel value and the Huffman Tree is not stored as it can be reconstructed from the encoded pixel values. This provides high compression as the Huffman Tree contains redundancy.
- The decompression is done by decoding the Huffman codes to reconstruct the original pixel values and then reshaping the 1D array into a 2D image array. This decompression is lossless as no data is lost during compression.
- Advantages: High compression ratio, lossless.
- Disadvantages: Slow encoding and decoding process as the Huffman Tree for the image has to be constructed and traversed for each pixel.
- Applications: Used for archiving lossless copies of images. Medical imaging, Satellite imaging, etc.

[Detailed diagrams and examples can be included here for more clarity.]