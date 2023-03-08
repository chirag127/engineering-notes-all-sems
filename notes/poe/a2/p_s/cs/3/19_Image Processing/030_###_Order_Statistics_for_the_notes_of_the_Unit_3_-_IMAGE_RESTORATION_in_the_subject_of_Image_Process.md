 Here is the content in markdown format for the topic ### Order Statistics for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing:

### Order Statistics

- Order Statistics refers to the arrangement of data points from lowest to highest value (or highest to lowest).
- When a set of data points are arranged in ascending (or descending) order, each data point gets an rank corresponding to its position in the ordered list. The data point with lowest value gets rank 1, the next higher gets rank 2 and so on. These ranks are known as order statistics.
- Order statistics are important in image processing as they are used to filter out noise (outliers) and perform various restoration tasks like:

1. Median Filter: Uses the median of all neighborhood pixel values as the output. Very effective in removing salt-and-pepper noise.
2. Alpha-Trimmed Mean: Calculates the mean after discarding a fixed percentage (alpha) of the extreme pixel values. Useful for Gaussian noise removal.
3. Order Statistic Filters: Utilizes a range of order statistics like minimum, maximum, median, etc. to filter the image. Flexible and can be used for various restoration tasks.

- The main advantage of order statistics is their robustness to outliers. The median and trimmed mean are not affected by extreme deviations from the norm.
- However, order statistic filters have the disadvantage of being computationally expensive as the pixels in the neighborhood need to be sorted to determine the order statistics.
- Order statistics find applications in smoothing, noise removal, image enhancement, etc. They are a useful tool in the arsenal of image restoration methods.

[Include any diagrams/images/codes/tables here if required]