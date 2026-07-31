### Statistical Moments for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Statistical moments are a set of numerical values that describe the shape and distribution of pixel intensities in an image or a region of an image .
- Statistical moments can be used for various purposes in image analysis, such as pattern recognition, object identification, texture analysis, image compression, and image denoising  .
- The most common types of statistical moments are the raw moments, the central moments, and the normalized central moments .
- The raw moments of order (i,j) for a greyscale image with pixel intensities I(x,y) are defined as:

$$M_{ij} = \sum_{x}\sum_{y} x^i y^j I(x,y)$$

- The raw moments can be used to calculate the centroid (x̄,ȳ) of the image, which is the center of mass of the pixel intensities:

$$\bar{x} = \frac{M_{10}}{M_{00}}$$

$$\bar{y} = \frac{M_{01}}{M_{00}}$$

- The central moments of order (i,j) are obtained by shifting the origin to the centroid of the image:

$$\mu_{ij} = \sum_{x}\sum_{y} (x-\bar{x})^i (y-\bar{y})^j I(x,y)$$

- The central moments are invariant to translation, meaning that they do not change if the image is moved to a different location.
- The normalized central moments of order (i,j) are obtained by dividing the central moments by a scaling factor:

$$\eta_{ij} = \frac{\mu_{ij}}{\mu_{00}^{(1+\frac{i+j}{2})}}$$

- The normalized central moments are invariant to both translation and scaling, meaning that they do not change if the image is moved or resized.
- The normalized central moments can be used to calculate the Hu moments, which are a set of seven values that are invariant to translation, scaling, and rotation, meaning that they do not change if the image is moved, resized, or rotated.
- The Hu moments are defined as:

$$
\begin{aligned}
&H_1 = \eta_{20} + \eta_{02} \\
&H_2 = (\eta_{20} - \eta_{02})^2 + 4\eta_{11}^2 \\
&H_3 = (\eta_{30} - 3\eta_{12})^2 + (3\eta_{21} - \eta_{03})^2 \\
&H_4 = (\eta_{30} + \eta_{12})^2 + (\eta_{21} + \eta_{03})^2 \\
&H_5 = (\eta_{30} - 3\eta_{12})(\eta_{30} + \eta_{12})[(\eta_{30} + \eta_{12})^2 - 3(\eta_{21} + \eta_{03})^2] + (3\eta_{21} - \eta_{03})(\eta_{21} + \eta_{03})[3(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2] \\
&H_6 = (\eta_{20} - \eta_{02})[(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2] + 4\eta_{11}(\eta_{30} + \eta_{12})(\eta_{21} + \eta_{03}) \\
&H_7 = (3\eta_{21} - \eta_{03})(\eta_{30} + \eta_{12})[(\eta_{30} + \eta_{12})^2 - 3(\eta_{21} + \eta_{03})^2] - (\eta_{30} - 3\eta_{12})(\eta_{21} + \eta_{03})[3(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2]
\end{aligned}
$$

- The Hu moments can be used