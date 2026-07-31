### Order Statistics

Order statistics are a type of non-linear filter used in image restoration. They are particularly useful for removing noise from an image while preserving edges and other important details.

Some common types of order statistics filters include:

1. **Median filter:** This filter replaces each pixel in the image with the median value of its neighboring pixels. It is effective at removing salt-and-pepper noise from an image.

2. **Minimum and maximum filters:** These filters replace each pixel in the image with the minimum or maximum value of its neighboring pixels, respectively. They can be used to remove bright or dark outliers from an image.

3. **Midpoint filter:** This filter replaces each pixel in the image with the average of the minimum and maximum values of its neighboring pixels. It can be used to reduce noise while preserving edges.

4. **Alpha-trimmed mean filter:** This filter removes the highest and lowest alpha percent of pixel values from the neighborhood before computing the mean. It can be used to reduce the influence of outliers on the filter output.

Order statistics filters can be applied to an image using a sliding window approach, where the filter is applied to each pixel in the image using a neighborhood of pixels defined by the window size. The choice of window size and shape can affect the performance of the filter. Larger window sizes can provide more noise reduction, but may also result in more blurring of edges and details in the image. A square or circular window shape is commonly used, but other shapes may be more appropriate for certain types of images or noise patterns.