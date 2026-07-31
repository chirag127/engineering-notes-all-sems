# Order Statistics for Image Restoration

- Order statistics are statistical measures that depend on the ordering or ranking of the data values, such as the minimum, maximum, median, and percentiles.
- Order statistic filters are non-linear spatial filters that operate on the ranked pixels in a local neighborhood of an image, and replace the center pixel with a value determined by the ranking result.
- Order statistic filters are useful for image restoration when the image is corrupted by noise or other degradation phenomena that affect the pixel values in a random or unpredictable way.
- Some common order statistic filters are:
  - The linear average filter, which computes the arithmetic mean of the pixels in the neighborhood.
  - The median filter, which selects the middle value of the pixels in the neighborhood.
  - The minimum filter, which selects the smallest value of the pixels in the neighborhood.
  - The maximum filter, which selects the largest value of the pixels in the neighborhood.
  - The alpha-trimmed mean filter, which discards the highest and lowest alpha percent of the pixels in the neighborhood, and computes the mean of the remaining pixels.
  - The mid-point filter, which computes the average of the minimum and maximum values of the pixels in the neighborhood.
- Order statistic filters have different properties and effects on the image, such as smoothing, sharpening, edge preservation, noise reduction, and outlier removal .
- Order statistic filters can be designed and optimized for specific types of noise or degradation, such as Gaussian noise, salt-and-pepper noise, speckle noise, impulse noise, etc .
- Order statistic filters can also be extended to higher order statistics, which involve moments or cumulants of higher than second order, such as skewness and kurtosis.
- Higher order statistics are less affected by the background than the second order measures, and can be used to identify the noise pixels or the edges in the image.
- Higher order statistics can also be used for blind deconvolution, which is a technique to restore an image that has been blurred by an unknown point spread function.
- Higher order statistics can be combined with other image restoration techniques, such as nonlocal image averaging, to achieve better results.