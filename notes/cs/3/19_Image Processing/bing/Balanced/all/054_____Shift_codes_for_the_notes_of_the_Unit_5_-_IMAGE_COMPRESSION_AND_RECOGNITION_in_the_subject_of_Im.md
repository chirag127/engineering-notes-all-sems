# Shift codes for the notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing

- Image compression is the process of reducing the amount of data required to represent an image, without compromising its quality or information content.
- Image compression can be classified into two types: lossless and lossy.
- Lossless image compression preserves the exact pixel values of the original image, and allows perfect reconstruction of the image after decompression.
- Lossy image compression discards some of the pixel values of the original image, and introduces some distortion or error in the reconstructed image after decompression.
- Lossy image compression can achieve higher compression ratios than lossless image compression, but at the cost of image quality.
- Shift coding is a technique for lossless image compression, based on the idea of shifting the pixel values of an image by a certain amount, and then encoding the shifted values using a variable-length code, such as Huffman coding.
- Shift coding can exploit the spatial correlation and redundancy in an image, and reduce the entropy or average number of bits per pixel of the image.
- Shift coding can be applied in two ways: using a leading short word (LSW) or using a lead bit (LB).
- LSW shift coding shifts the pixel values of an image by the minimum value in the image, and then encodes the shifted values using a variable-length code that assigns shorter codes to smaller values.
- LB shift coding shifts the pixel values of an image by the most significant bit (MSB) of the maximum value in the image, and then encodes the shifted values using a variable-length code that assigns shorter codes to values with fewer bits.
- Shift coding can achieve better compression performance than other lossless image compression techniques, such as run-length encoding (RLE) or Lempel-Ziv-Welch (LZW) coding, for images with low dynamic range or high spatial correlation.