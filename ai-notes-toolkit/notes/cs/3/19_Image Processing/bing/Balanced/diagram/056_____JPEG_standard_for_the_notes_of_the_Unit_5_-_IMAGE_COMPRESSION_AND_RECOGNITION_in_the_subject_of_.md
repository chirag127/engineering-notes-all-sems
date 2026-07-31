### JPEG standard

- JPEG stands for Joint Photographic Experts Group, which was a group of image processing experts that devised a standard for compressing images (ISO).
- JPEG is not really a file format but rather an image compression standard that works by averaging color variation and discarding what the human eye cannot see, a process known as “lossy” compression.
- JPEG compression reduces file size by changing the color values and blocking together groups of pixels with a more uniform color, so that it doesn’t have to store as many different ones.
- JPEG compression consists of the following steps:
  - Color space transformation: The image is converted from RGB to YCbCr color space, which separates luminance (Y) from chrominance (Cb and Cr).
  - Subsampling: The chrominance components are subsampled by a factor of 2 or 4, since the human eye is less sensitive to color details than brightness details.
  - Block splitting: The image is divided into 8x8 blocks of pixels, which are processed independently.
  - Discrete cosine transform (DCT): Each block is transformed into a frequency domain representation, using a mathematical function called DCT.
  - Quantization: The DCT coefficients are divided by a quantization matrix, which specifies how much each frequency component can be compressed. The higher the compression, the more information is lost.
  - Entropy encoding: The quantized coefficients are encoded using a variable-length code, such as Huffman coding or arithmetic coding, which assigns shorter codes to more frequent values.
- JPEG decompression is the reverse process of compression, which involves entropy decoding, dequantization, inverse DCT, block merging, upsampling, and color space conversion.
- JPEG standard specifies the codec, which defines how an image is compressed into a stream of bytes and decompressed back into an image, but not the file format used to contain that stream. The Exif and JFIF standards define the commonly used file formats for interchange of JPEG-compressed images.
- JPEG compression has some advantages and disadvantages:
  - Advantages: JPEG compression can achieve high compression ratios, reducing the file size and storage space. JPEG compression is widely supported by various devices and applications. JPEG compression can be adjusted to trade off quality and file size according to the user's preference.
  - Disadvantages: JPEG compression is lossy, meaning that some image quality is sacrificed during the compression process. JPEG compression can introduce artifacts, such as blockiness, blurring, ringing, or color distortion, especially at high compression levels. JPEG compression is not suitable for images that contain sharp edges, text, or graphics, as these features can be degraded by the compression.