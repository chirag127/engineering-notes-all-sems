 Here is the formal content in Markdown format without any emojis or external links for the topic "Image compression for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression":

### Image compression for the notes of the Unit 3 - Coding a sequence in the subject of Data Compression

1. Introduction
- Images contain a large amount of data which needs to be compressed for efficient storage and transmission.
- Image compression techniques remove redundancy from the image data and represent it in a more compact form.

2. Lossless compression
- The compressed image is an exact replica of the original image.
- Used for medical images, satellite images, etc. where no loss of information is acceptable.
- Examples: PNG, GIF, TIFF.

3. Lossy compression
- The compressed image is an approximation of the original image with some amount of distortion.
- Used for photographs, videos where some loss of information is tolerable.
- Examples: JPEG, JPEG 2000.

4. JPEG compression
- Removes spatial redundancy.
- Divides image into 8x8 blocks and applies DCT.
- Quantizes the DCT coefficients and encodes them.
- Configurable trade-off between compression ratio and image quality.
- Artifacts may appear at high compression ratios.

5. Conclusion
- Choose an appropriate image compression technique based on the application requirements of lossless vs lossy, compression ratio, complexity, etc.
- Lossy techniques achieve higher compression ratios but at the cost of some loss in image quality.
- JPEG is one of the most popular image compression standards suitable for photographs and images.