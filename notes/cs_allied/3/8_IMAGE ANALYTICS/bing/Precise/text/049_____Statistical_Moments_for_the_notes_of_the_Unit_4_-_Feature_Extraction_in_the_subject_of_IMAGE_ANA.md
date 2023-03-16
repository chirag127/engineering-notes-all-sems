### Statistical Moments

Statistical moments are quantitative measures that describe the shape of a probability distribution. They are used in feature extraction to provide a compact representation of the distribution of pixel values in an image. The first four statistical moments are commonly used in image analysis:

1. **Mean**: The mean is the first moment and is a measure of central tendency. It is calculated as the average value of all the pixels in the image.

2. **Variance**: The variance is the second moment and is a measure of dispersion. It is calculated as the average of the squared differences between each pixel value and the mean.

3. **Skewness**: The skewness is the third moment and is a measure of asymmetry. It is calculated as the average of the cubed differences between each pixel value and the mean, divided by the standard deviation cubed.

4. **Kurtosis**: The kurtosis is the fourth moment and is a measure of peakedness. It is calculated as the average of the fourth power of the differences between each pixel value and the mean, divided by the standard deviation to the fourth power.

These statistical moments can be used to extract features from an image that can be used in image analysis and classification. For example, the mean can be used to determine the overall brightness of an image, while the variance can be used to determine the level of detail in the image. Skewness and kurtosis can provide additional information about the shape of the distribution of pixel values in the image.