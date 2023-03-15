# Shift codes for the notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing

- Image compression is the process of reducing the amount of data required to store or transmit an image.
- Image compression can be either lossless or lossy, depending on whether the original image can be perfectly reconstructed from the compressed data or not.
- Lossless image compression techniques preserve the exact pixel values of the original image, while lossy image compression techniques introduce some distortion or error in the reconstructed image.
- Shift coding is a lossless image compression technique that exploits the correlation between adjacent pixels in an image.
- Shift coding works by shifting the pixel values of an image by a certain amount, such that the resulting values have a smaller range and can be represented by fewer bits.
- Shift coding can be applied in two ways: using leading short word (LSW) or using lead bit (LB).
- LSW shift coding works by finding the minimum and maximum pixel values in the image, and shifting all the pixel values by the minimum value. Then, the shifted values are encoded using a variable-length code, such that the most frequent values have the shortest codes.
- LB shift coding works by finding the most significant bit (MSB) position of the pixel values in the image, and shifting all the pixel values by the MSB position. Then, the shifted values are encoded using a fixed-length code, such that all the values have the same number of bits.
- Shift coding can reduce the number of bits required to store or transmit an image, without losing any information or quality. However, shift coding is not very effective for images with high dynamic range or complex textures, as the shifted values may still have a large range and require many bits to encode.