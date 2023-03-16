### Optimum Global Thresholding using Otsu’s Method

- Otsu’s method is a technique of performing global thresholding on a digital image. It is optimum in the sense that it maximizes the between-class variance .
- Global thresholding is a process of converting a grayscale image into a binary image by using a single intensity value as a threshold .
- Otsu’s method assumes that the image histogram has two peaks, one for the foreground pixels and one for the background pixels, and tries to find the optimal threshold that separates them .
- Otsu’s method can be formulated as an optimization problem, where the objective function is the weighted sum of the variances of the two classes of pixels, and the goal is to minimize it  .
- Otsu’s method can be implemented as follows  :
  - Compute the normalized histogram of the image, which is the probability distribution of the pixel intensities.
  - Initialize the threshold value to zero and the minimum variance to infinity.
  - For each possible threshold value from 0 to 255, do the following:
    - Compute the probabilities and the means of the foreground and background classes, using the histogram values.
    - Compute the between-class variance, which is the product of the probabilities and the squared difference of the means.
    - If the between-class variance is larger than the current maximum, update the threshold value and the maximum variance.
  - Return the threshold value that maximizes the between-class variance.
- Otsu’s method is a simple and effective way of finding the optimal threshold for image segmentation, but it has some limitations :
  - It assumes that the image histogram has a bimodal distribution, which may not be true for some images.
  - It is sensitive to noise and outliers, which may affect the histogram shape and the threshold value.
  - It does not consider the spatial information or the local characteristics of the image, which may lead to over-segmentation or under-segmentation.