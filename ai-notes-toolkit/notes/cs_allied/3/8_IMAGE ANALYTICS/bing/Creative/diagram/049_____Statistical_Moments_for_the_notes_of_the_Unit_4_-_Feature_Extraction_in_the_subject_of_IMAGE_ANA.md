### Statistical Moments for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Statistical moments are a set of numerical values that describe the shape and characteristics of a probability distribution or an image .
- Statistical moments can be calculated from the pixel intensities of an image or from the histogram of an image.
- Statistical moments are useful for image analysis, such as segmentation, classification, compression, and denoising .
- The four commonly used statistical moments are: the mean, the variance, the skewness, and the kurtosis.
- The mean is the first moment and it measures the average value of the pixel intensities or the histogram. It is calculated as:

$$
M_{00} = \sum_{x,y} I(x,y)
$$

where $I(x,y)$ is the pixel intensity at $(x,y)$ .

- The variance is the second moment and it measures the spread or dispersion of the pixel intensities or the histogram. It is calculated as:

$$
M_{20} = \sum_{x,y} (x - \bar{x})^2 I(x,y)
$$

where $\bar{x}$ is the mean of the pixel intensities or the histogram .

- The skewness is the third moment and it measures the asymmetry or deviation from the normal distribution of the pixel intensities or the histogram. It is calculated as:

$$
M_{30} = \sum_{x,y} (x - \bar{x})^3 I(x,y)
$$

where $\bar{x}$ is the mean of the pixel intensities or the histogram .

- The kurtosis is the fourth moment and it measures the peakedness or flatness of the pixel intensities or the histogram. It is calculated as:

$$
M_{40} = \sum_{x,y} (x - \bar{x})^4 I(x,y)
$$

where $\bar{x}$ is the mean of the pixel intensities or the histogram .

- Higher-order moments can also be calculated, but they are less commonly used and more difficult to interpret.
- Statistical moments can also be normalized, centralized, or invariant to translation, rotation, or scaling, depending on the application and the desired properties.
- Statistical moments are a simple and effective way of extracting features from images, but they may not capture the complex and nonlinear structures of natural images. Therefore, other methods such as wavelets, deep learning, or manifold learning may be more suitable for some tasks.