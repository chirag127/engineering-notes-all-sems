## Unit 4 - Distortion criteria

Distortion is a crucial factor in signal processing, and it refers to the changes or alterations that occur in a signal during its processing. Therefore, it is essential to have criteria that can evaluate the distortion of a signal accurately. In this unit, we will explore the different distortion criteria used in signal processing.

### Types of Distortion Criteria

There are several distortion criteria used in signal processing, including:

1. Mean Square Error (MSE) - This criterion evaluates the difference between the original signal and the reconstructed signal. It is calculated by taking the average of the squared differences between the two signals.

2. Peak Signal-to-Noise Ratio (PSNR) - This criterion measures the ratio of the maximum power of a signal to the power of noise that affects the fidelity of its representation. It is calculated by taking the logarithm of the ratio of the maximum pixel value to the mean square error.

3. Structural Similarity Index (SSIM) - This criterion evaluates the structural similarity between two images. It is calculated by comparing the luminance, contrast, and structure of the original and reconstructed images.

4. Visual Information Fidelity (VIF) - This criterion evaluates the quality of an image by measuring the amount of visual information that is lost during compression or transmission.

### Advantages and Disadvantages

Each distortion criterion has its advantages and disadvantages, which are important to consider when selecting a criterion for a particular application. Some of the advantages and disadvantages of the most commonly used criteria are:

1. MSE - This criterion is simple to calculate, and its value correlates well with the subjective quality of the reconstructed signal. However, it is sensitive to outliers and does not consider the perceptual differences between the original and reconstructed signals.

2. PSNR - This criterion is widely used in image and video processing, and its value is easy to interpret. However, it does not account for the human visual system's non-linear response to changes in image quality.

3. SSIM - This criterion is more robust to changes in image content and illumination, and it considers the perceptual differences between the original and reconstructed images. However, it is more complex to calculate than other criteria.

4. VIF - This criterion is designed to evaluate the quality of an image in terms of the amount of visual information that is lost. However, it is computationally intensive and may not be suitable for real-time applications.

### Applications

Distortion criteria are used in various signal processing applications, including:

1. Image and video compression - Distortion criteria are used to evaluate the quality of compressed images and videos and to optimize the compression algorithms.

2. Image and video restoration - Distortion criteria are used to evaluate the quality of restored images and videos and to optimize the restoration algorithms.

3. Speech and audio processing - Distortion criteria are used to evaluate the quality of speech and audio signals after processing, such as noise reduction or compression.

### Conclusion

Distortion criteria are essential tools in signal processing for evaluating the accuracy and fidelity of processed signals. The selection of a distortion criterion depends on the specific application and the trade-off between computational complexity and accuracy. Understanding the advantages and disadvantages of different distortion criteria is crucial in selecting the most appropriate criterion for a particular application.