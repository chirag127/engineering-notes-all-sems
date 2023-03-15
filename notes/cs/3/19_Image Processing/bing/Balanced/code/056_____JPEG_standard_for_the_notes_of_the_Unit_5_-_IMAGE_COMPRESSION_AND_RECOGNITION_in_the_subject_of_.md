### JPEG standard

- JPEG stands for Joint Photographic Experts Group, which was a group of image processing experts that devised a standard for compressing images (ISO).
- JPEG is not really a file format but rather an image compression standard that works by averaging color variation and discarding what the human eye cannot see, a process known as “lossy” compression.
- JPEG compression reduces file size by changing the color values and blocking together groups of pixels with a more uniform color, so that it doesn’t have to store as many different ones. While this does decrease the file size, it also alters the true image by changing the colors.
- The JPEG standard specifies the codec, which defines how an image is compressed into a stream of bytes and decompressed back into an image, but not the file format used to contain that stream. The Exif and JFIF standards define the commonly used file formats for interchange of JPEG-compressed images.
- The JPEG standard is complicated with many different options and color space regulations. The basic steps of JPEG compression are :
  - Convert the image from RGB to YCbCr color space, which separates the luminance (Y) from the chrominance (Cb and Cr) components.
  - Subsample the chrominance components to reduce their resolution, since the human eye is less sensitive to color details than brightness details.
  - Divide the image into 8x8 pixel blocks and apply a discrete cosine transform (DCT) to each block, which transforms the spatial domain into the frequency domain.
  - Quantize the DCT coefficients according to a predefined quantization table, which assigns more bits to the low-frequency coefficients (which contain more information) and less bits to the high-frequency coefficients (which contain more noise).
  - Encode the quantized coefficients using a variable-length coding scheme, such as Huffman coding or arithmetic coding, which assigns shorter codes to more frequent symbols and longer codes to less frequent symbols.
  - Optionally, apply a lossless compression algorithm, such as run-length encoding or Lempel-Ziv-Welch (LZW) algorithm, to further reduce the file size.
- The JPEG standard also supports progressive encoding, which allows the image to be displayed in multiple passes with increasing quality, and hierarchical encoding, which allows the image to be stored in multiple resolutions.