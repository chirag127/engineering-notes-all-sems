### Statistical Moments for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Statistical moments are a set of numerical values that describe the shape and distribution of pixel intensities in an image or a region of an image .
- Statistical moments can be used for various purposes in image analysis, such as texture characterization, pattern recognition, object identification, image segmentation, image compression, and image denoising  .
- Statistical moments can be computed for different types of images, such as grayscale, binary, color, or multispectral images. They can also be computed for different types of regions, such as rectangular, circular, elliptical, or arbitrary shapes .
- Statistical moments can be classified into different types, such as geometric moments, central moments, normalized central moments, Hu moments, Zernike moments, Legendre moments, and complex moments. Each type of moment has its own advantages and disadvantages in terms of computational complexity, invariance properties, and descriptive power .
- The most basic type of statistical moment is the geometric moment, which is defined as the weighted sum of the pixel intensities in an image or a region, where the weights are the coordinates of the pixels raised to some powers. Mathematically, the geometric moment of order (p,q) for a grayscale image with pixel intensities I(x,y) is given by :

```math
M_{pq} = \sum_{x}\sum_{y} x^p y^q I(x,y)
```

- The geometric moments can be used to compute some basic features of an image or a region, such as the area, the centroid, the orientation, and the eccentricity .
- The geometric moments are not invariant to translation, rotation, scaling, or other geometric transformations. To achieve invariance, other types of moments can be derived from the geometric moments, such as the central moments, the normalized central moments, and the Hu moments .
- The central moments are defined as the geometric moments computed with respect to the centroid of the image or the region, rather than the origin of the coordinate system. Mathematically, the central moment of order (p,q) for a grayscale image with pixel intensities I(x,y) and centroid (x̅,y̅) is given by :

```math
\mu_{pq} = \sum_{x}\sum_{y} (x-x̅)^p (y-y̅)^q I(x,y)
```

- The central moments are invariant to translation, but not to rotation or scaling. The normalized central moments are obtained by dividing the central moments by a suitable normalization factor, which is usually the zeroth-order central moment raised to some power. Mathematically, the normalized central moment of order (p,q) for a grayscale image with pixel intensities I(x,y) and centroid (x̅,y̅) is given by :

```math
\eta_{pq} = \frac{\mu_{pq}}{\mu_{00}^{(p+q)/2+1}}
```

- The normalized central moments are invariant to translation and scaling, but not to rotation. The Hu moments are a set of seven invariant moments derived from the normalized central moments, which are invariant to translation, scaling, and rotation. They are also invariant to reflection, up to a sign change. Mathematically, the Hu moments for a grayscale image with pixel intensities I(x,y) and centroid (x̅,y̅) are given by :

```math
\begin{aligned}
h_1 &= \eta_{20} + \eta_{02} \\
h_2 &= (\eta_{20} - \eta_{02})^2 + 4\eta_{11}^2 \\
h_3 &= (\eta_{30} - 3\eta_{12})^2 + (3\eta_{21} - \eta_{03})^2 \\
h_4 &= (\eta_{30} + \eta_{12})^2 + (\eta_{21} + \eta_{03})^2 \\
h_5 &= (\eta_{30} - 3\eta_{12})(\eta_{30} + \eta_{12