### Order Statistics for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Image restoration is the process of recovering an image that has been degraded by a degradation phenomenon, such as noise, blur, or distortion.
- Order statistics are the values obtained by sorting a set of data in ascending or descending order. For example, the minimum, maximum, and median are order statistics.
- Order statistic filters are non-linear spatial filters that operate on the order statistics of the pixels in a neighborhood of the image. They can be used to remove noise, enhance edges, or smooth regions in an image.
- Some common order statistic filters are:

  - The linear average filter, which replaces the center pixel with the mean of the pixels in the neighborhood. This filter is good for reducing random noise, but also blurs edges and details.
  - The median filter, which replaces the center pixel with the median of the pixels in the neighborhood. This filter is good for removing salt-and-pepper noise, but also reduces contrast and sharpness.
  - The min and max filters, which replace the center pixel with the minimum or maximum of the pixels in the neighborhood. These filters are good for enhancing edges and contrast, but also amplify noise and create artifacts.
  - The alpha-trimmed mean filter, which replaces the center pixel with the mean of the pixels in the neighborhood after discarding the alpha highest and lowest values. This filter is a compromise between the linear average and the median filters, as it can reduce noise and preserve edges to some extent.
  - The mid-point filter, which replaces the center pixel with the average of the minimum and maximum of the pixels in the neighborhood. This filter is good for reducing noise and preserving edges in images with constant or slowly varying intensities.
  - The rank-order filter, which replaces the center pixel with the k-th smallest or largest value in the neighborhood. This filter is a generalization of the min, max, and median filters, and can be used to achieve different effects depending on the choice of k.

- Order statistic filters can also be applied to color images, either by processing each color channel separately or by using higher order statistics that measure the similarity or dissimilarity of the pixels in the neighborhood. For example, blind deconvolution is a technique that uses higher order statistics to restore color images that have been blurred by an unknown point spread function.