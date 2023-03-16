### Statistical Moments for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Statistical moments are a set of numerical values that describe the shape and distribution of pixel intensities in an image or a region of an image .
- Statistical moments can be used for various purposes in image analysis, such as texture classification, object recognition, shape description, image segmentation, and image compression .
- Statistical moments can be computed for different types of images, such as grayscale, binary, color, or multispectral images.
- Statistical moments can be classified into different types, such as geometric moments, central moments, normalized central moments, Hu moments, Zernike moments, Legendre moments, etc.
- Statistical moments can be calculated for different orders, such as zeroth, first, second, third, etc. The order of a moment indicates the degree of the polynomial function that is used to weight the pixel intensities .
- Statistical moments can be calculated for different axes, such as x, y, xy, etc. The axis of a moment indicates the direction of the pixel coordinates that are used to weight the pixel intensities.
- Statistical moments can be calculated for different regions, such as the whole image, a sub-image, a contour, a mask, etc. The region of a moment indicates the spatial extent of the pixel intensities that are used to weight the pixel intensities.
- Statistical moments can be calculated using different formulas, depending on the type, order, axis, and region of the moment. The general formula for a moment of order (i,j) for a grayscale image with pixel intensities I(x,y) is given by :

M_ij = sum_x sum_y x^i y^j I(x,y)

- Statistical moments can be transformed into different forms, such as invariant moments, orthogonal moments, complex moments, etc. The transformed moments have some desirable properties, such as rotation invariance, scale invariance, translation invariance, etc .
- Statistical moments can be used to derive different features, such as mean, variance, skewness, kurtosis, entropy, etc. The features can be used to characterize the image or the region of the image in terms of its intensity distribution, contrast, smoothness, symmetry, etc .