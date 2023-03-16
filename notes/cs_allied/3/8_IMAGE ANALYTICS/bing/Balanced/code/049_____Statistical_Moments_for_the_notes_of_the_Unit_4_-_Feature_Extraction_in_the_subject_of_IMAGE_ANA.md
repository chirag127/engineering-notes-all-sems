### Statistical Moments for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Feature extraction is the process of transforming raw image data into a more compact and meaningful representation that can be used for further analysis or classification.
- Statistical moments are numerical values that describe the shape and distribution of an image or a region of interest in an image.
- Statistical moments can be calculated from the pixel intensity values, the frequency coefficients of a transform domain (such as Fourier or wavelet), or the probability density function of an image.
- Statistical moments can be classified into two types: ordinary moments and central moments.
- Ordinary moments are calculated with respect to the origin of the coordinate system, while central moments are calculated with respect to the mean or centroid of the image or region.
- Ordinary moments can be defined as:

$$
M_{pq} = \sum_{x=0}^{N-1} \sum_{y=0}^{M-1} x^p y^q f(x,y)
$$

where $p$ and $q$ are non-negative integers, $N$ and $M$ are the image dimensions, and $f(x,y)$ is the pixel intensity value at $(x,y)$.
- Central moments can be defined as:

$$
\mu_{pq} = \sum_{x=0}^{N-1} \sum_{y=0}^{M-1} (x-\bar{x})^p (y-\bar{y})^q f(x,y)
$$

where $\bar{x}$ and $\bar{y}$ are the mean or centroid coordinates, given by:

$$
\bar{x} = \frac{M_{10}}{M_{00}}, \quad \bar{y} = \frac{M_{01}}{M_{00}}
$$

- Statistical moments can be used to extract various features from an image or region, such as area, perimeter, orientation, eccentricity, compactness, skewness, kurtosis, etc.
- Statistical moments can also be normalized or invariant to certain transformations, such as scaling, rotation, translation, or affine transformations, by applying appropriate formulas or transformations.
- Statistical moments can be extended to higher dimensions, such as 3D or 4D, to deal with volumetric or temporal data, such as ground penetrating radar scans or video sequences.
- Statistical moments can be combined with other feature extraction methods, such as spectral or texture analysis, to improve the performance of image classification or recognition .