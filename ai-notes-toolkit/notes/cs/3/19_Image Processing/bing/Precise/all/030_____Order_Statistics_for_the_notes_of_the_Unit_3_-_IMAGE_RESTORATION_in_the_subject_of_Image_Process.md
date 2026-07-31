### Order Statistics

Order statistics are a type of non-linear filter used in image restoration. They are particularly useful for removing noise from an image while preserving edges and other important features. Some common types of order statistics filters include:

1. **Median filter:** This filter replaces each pixel in the image with the median value of its neighboring pixels. It is effective at removing salt-and-pepper noise from an image.

2. **Min filter:** This filter replaces each pixel in the image with the minimum value of its neighboring pixels. It is useful for removing bright outliers from an image.

3. **Max filter:** This filter replaces each pixel in the image with the maximum value of its neighboring pixels. It is useful for removing dark outliers from an image.

4. **Midpoint filter:** This filter replaces each pixel in the image with the average of the minimum and maximum values of its neighboring pixels. It is effective at removing both bright and dark outliers from an image.

5. **Alpha-trimmed mean filter:** This filter replaces each pixel in the image with the mean of its neighboring pixels, after discarding the highest and lowest alpha percent of the values. It is useful for removing multiple types of noise from an image.

These filters can be applied to an image using a sliding window approach, where the filter is applied to each pixel in the image, one at a time. The size of the window determines the number of neighboring pixels that are considered when calculating the new value for each pixel. A larger window size will result in more smoothing, while a smaller window size will preserve more detail in the image.

Order statistics filters are a powerful tool for image restoration, and can be used to effectively remove noise and other unwanted artifacts from an image while preserving important features. They are widely used in image processing and computer vision applications.