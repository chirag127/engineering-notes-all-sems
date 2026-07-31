# JPEG standard

- JPEG stands for Joint Photographic Experts Group, which was a group of image processing experts that devised a standard for compressing images (ISO) .
- JPEG is not really a file format but rather an image compression standard . The JPEG standard specifies the codec, which defines how an image is compressed into a stream of bytes and decompressed back into an image.
- JPEG is a lossy image compression method, which means that some information is discarded during the compression process, resulting in a loss of quality .
- JPEG compression works by averaging color variation and blocking together groups of pixels with a more uniform color, so that it doesn’t have to store as many different ones .
- JPEG compression involves the following steps :
  - Convert the image from RGB to YCbCr color space, which separates the luminance (Y) from the chrominance (Cb and Cr) components.
  - Subsample the chrominance components to reduce their resolution, since the human eye is less sensitive to color details than brightness details.
  - Divide the image into 8x8 blocks of pixels and apply a discrete cosine transform (DCT) to each block, which converts the spatial domain into the frequency domain.
  - Quantize the DCT coefficients using a quantization matrix, which assigns smaller values to higher frequencies and larger values to lower frequencies. This reduces the number of bits needed to represent the coefficients, but also introduces errors due to rounding.
  - Encode the quantized coefficients using a variable-length coding scheme, such as Huffman coding or arithmetic coding, which assigns shorter codes to more frequent coefficients and longer codes to less frequent coefficients. This further reduces the file size, but also adds some overhead for the code table.
  - Optionally, add some metadata to the compressed file, such as the Exif or JFIF standards, which define the file format and contain information about the image, such as the resolution, orientation, date, etc.

- JPEG compression allows the user to adjust the level of compression and quality by changing the quantization matrix or the subsampling ratio . Higher compression leads to smaller file size but lower quality, and vice versa.
- JPEG compression is suitable for natural images, such as photographs, that have smooth variations of color and brightness . However, it is not suitable for images that have sharp edges, text, or graphics, as it may introduce artifacts, such as blocking, ringing, or blurring .