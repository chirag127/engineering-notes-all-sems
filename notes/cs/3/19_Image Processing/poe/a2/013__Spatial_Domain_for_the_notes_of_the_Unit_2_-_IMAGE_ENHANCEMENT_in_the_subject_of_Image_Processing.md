 Here are the notes for Spatial Domain for the Unit 2 - IMAGE ENHANCEMENT in Image Processing:

### Spatial Domain

- In spatial domain methods, the image is directly manipulated by changing the values of pixels.
- These methods do not convert the image to another domain (like frequency domain) for processing. The pixels are processed directly.
- Some common spatial domain methods are:

1. Histogram Equalization: It improves the contrast in an image by stretching the range of intensity values it contains. This enhances the brightness and detail in the image.
2. Thresholding: It converts the gray level image into a binary image by setting a threshold value. Pixels with intensities greater than the threshold are set to white and pixels with intensities less than the threshold are set to black. This is useful for image segmentation.
3. Image Negation: It inverts the pixels of an image. Bright pixels become dark and vice versa. This can enhance some features in an image like defects, etc.
4. Smoothing and Sharpening: These are used to reduce noise and enhance edges respectively. This is done by modifying the pixels in the neighborhood of each pixel. Various filters like average, median, etc. are used for smoothing and Laplacian, Sobel, etc. are used for sharpening.

- The advantage of spatial domain methods is that they are relatively simple and fast. However, they can be noisy and not very effective at times. Frequency domain methods are more powerful but complex to implement. A combination of both spatial and frequency domain methods is often used to get the best results.