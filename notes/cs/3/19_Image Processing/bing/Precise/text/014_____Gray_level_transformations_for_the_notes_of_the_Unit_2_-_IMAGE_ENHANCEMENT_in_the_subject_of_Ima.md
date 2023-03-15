### Gray Level Transformations

Gray level transformations, also known as point processing or pixel processing, are image enhancement techniques that operate on individual pixels of an image. These techniques are used to adjust the brightness, contrast, and overall appearance of an image.

Some common gray level transformations include:

1. **Identity transformation:** This transformation leaves the image unchanged. The output pixel value is the same as the input pixel value.

2. **Negative transformation:** This transformation produces a negative image by inverting the pixel values. The output pixel value is calculated by subtracting the input pixel value from the maximum pixel value.

3. **Log transformation:** This transformation compresses the dynamic range of the image by taking the logarithm of the pixel values. The output pixel value is calculated by taking the logarithm of the input pixel value and scaling it to the desired range.

4. **Power-law transformation:** This transformation, also known as gamma correction, is used to adjust the contrast of an image. The output pixel value is calculated by raising the input pixel value to a power and scaling it to the desired range.

5. **Contrast stretching:** This transformation increases the contrast of an image by stretching the range of pixel values. The output pixel value is calculated by linearly scaling the input pixel value to the desired range.

6. **Histogram equalization:** This transformation enhances the contrast of an image by redistributing the pixel values so that the histogram of the output image is approximately flat. The output pixel value is calculated by mapping the input pixel value to a new value based on the cumulative distribution function of the input image.

These are some of the common gray level transformations used in image enhancement. They can be applied individually or in combination to achieve the desired result.