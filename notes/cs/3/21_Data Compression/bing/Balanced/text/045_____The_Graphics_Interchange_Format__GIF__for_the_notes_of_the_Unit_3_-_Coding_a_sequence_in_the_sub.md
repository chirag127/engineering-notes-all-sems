### The Graphics Interchange Format (GIF) for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

- GIF is a graphical image format that uses a variant of LZW (Lempel-Ziv-Welch) lossless data compression technique to reduce the file size without degrading the visual quality .
- GIF was introduced by CompuServe in 1987 to provide a color image format for their file downloading areas .
- GIF supports up to 8 bits per pixel for each image, allowing a single image to reference its own palette of up to 256 different colors chosen from the 24-bit RGB color space.
- GIF also supports animations and allows a separate palette of up to 256 colors for each frame. The color limitation makes the GIF format unsuitable for reproducing color photographs and other images with color gradients, but it is well-suited for simpler images such as graphics or logos with solid areas of color.
- GIF images are compressed using the following steps:
  - The image is divided into blocks of 8x8 pixels, each block having its own color palette.
  - Each block is encoded using a variable-length code based on the LZW algorithm, which replaces repeated sequences of pixels with shorter codes.
  - The codes are stored in a data stream, preceded by a header that contains information such as the image size, the number of colors, and the compression method.
  - The data stream is optionally further compressed using a run-length encoding scheme, which replaces consecutive identical codes with a code and a count.
- GIF is a popular format for transmitting images and animations over the Internet, especially for web pages, because of its small file size and wide compatibility.
- However, GIF has some drawbacks, such as the limited color range, the patent issues with the LZW algorithm, and the lack of transparency and alpha channel support.
- PNG (Portable Network Graphics) is a newer image format that was designed to overcome some of the limitations of GIF, such as offering a larger color depth, a lossless compression method that does not use LZW, and support for transparency and alpha channel.