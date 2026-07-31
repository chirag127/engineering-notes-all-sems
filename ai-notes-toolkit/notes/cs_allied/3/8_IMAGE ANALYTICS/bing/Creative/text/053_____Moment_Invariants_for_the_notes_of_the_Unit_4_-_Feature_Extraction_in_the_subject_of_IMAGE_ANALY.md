### Moment Invariants for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Moment invariants are numerical values that are derived from the moments of an image and are invariant to certain geometric transformations, such as translation, scaling and rotation .
- Moments are scalar quantities that describe the distribution of pixel intensities in an image. They can be computed for the whole image or for a region of interest.
- Moments can be classified into different types, such as geometric moments, central moments, normalized central moments, Zernike moments, Legendre moments, etc.
- Moment invariants are useful for image analysis and pattern recognition, as they can capture the shape and appearance of an object regardless of its position, size and orientation .
- One of the most widely used sets of moment invariants was proposed by Hu in 1962, which consists of seven invariant values derived from the second and third order central moments .
- Hu's moment invariants are defined as follows :

$$
\begin{aligned}
I_1 &= \eta_{20} + \eta_{02} \\
I_2 &= (\eta_{20} - \eta_{02})^2 + 4\eta_{11}^2 \\
I_3 &= (\eta_{30} - 3\eta_{12})^2 + (3\eta_{21} - \eta_{03})^2 \\
I_4 &= (\eta_{30} + \eta_{12})^2 + (\eta_{21} + \eta_{03})^2 \\
I_5 &= (\eta_{30} - 3\eta_{12})(\eta_{30} + \eta_{12})[(\eta_{30} + \eta_{12})^2 - 3(\eta_{21} + \eta_{03})^2] + (3\eta_{21} - \eta_{03})(\eta_{21} + \eta_{03})[3(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2] \\
I_6 &= (\eta_{20} - \eta_{02})[(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2] + 4\eta_{11}(\eta_{30} + \eta_{12})(\eta_{21} + \eta_{03}) \\
I_7 &= (3\eta_{21} - \eta_{03})(\eta_{30} + \eta_{12})[(\eta_{30} + \eta_{12})^2 - 3(\eta_{21} + \eta_{03})^2] - (\eta_{30} - 3\eta_{12})(\eta_{21} + \eta_{03})[3(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2]
\end{aligned}
$$

where $\eta_{pq}$ are the normalized central moments of order $(p+q)$, defined as:

$$
\eta_{pq} = \frac{\mu_{pq}}{\mu_{00}^{(1 + (p+q)/2)}}
$$

and $\mu_{pq}$ are the central moments of order $(p+q)$, defined as:

$$
\mu_{pq} = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} (x - \bar{x})^p (y - \bar{y})^q f(x,y)
$$

where $f(x,y)$ is the pixel intensity at $(x,y)$, $\bar{x}$ and $\bar{y}$ are the coordinates of the centroid of the image, and $M$ and $N$ are the dimensions of the image.

- Hu's moment invariants are not strictly invariant for discrete images, as they may change over image geometric transformations due to discretization errors . Therefore, some methods have been proposed to improve the accuracy and robustness of moment invariants, such as using higher order moments, applying normalization or weighting schemes, or combining different types of moments  .