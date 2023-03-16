# Optimum Global Thresholding using Otsu’s Method

- Otsu’s method is a technique of performing global thresholding on a digital image. It is optimum in the sense that it maximizes the between-class variance.
- Global thresholding is a process of dividing an image into two regions: foreground and background, based on a single intensity value called the threshold.
- Otsu’s method assumes that the image histogram has two peaks, one for each region, and tries to find the optimal threshold that separates them.
- The optimal threshold is the one that minimizes the within-class variance, or equivalently, maximizes the inter-class variance.
- The within-class variance is the weighted sum of the variances of the foreground and background pixels, and the inter-class variance is the variance of the means of the foreground and background pixels.
- Otsu’s method can be formulated as an optimization problem: find the threshold T that maximizes the inter-class variance σ^2_B(T), given by:

    ```math
    \sigma^2_B(T) = \omega_0(T)\omega_1(T)(\mu_0(T) - \mu_1(T))^2
    ```

    where

    - ω_0(T) and ω_1(T) are the probabilities of the foreground and background pixels, respectively, computed from the normalized histogram
    - μ_0(T) and μ_1(T) are the means of the foreground and background pixels, respectively, computed from the normalized histogram
    - T is the threshold value, ranging from 0 to L-1, where L is the number of intensity levels

- Otsu’s method can be implemented by iterating over all possible values of T and computing the inter-class variance for each one, then choosing the maximum value.
- Alternatively, Otsu’s method can be implemented more efficiently by using the cumulative sums and means of the histogram, and updating them recursively for each value of T.
- Otsu’s method is a one-dimensional discrete analogue of Fisher’s Discriminant Analysis, is related to Jenks optimization method, and is equivalent to a globally optimal k-means performed on the intensity histogram.
- Otsu’s method is simple, fast, and robust, but it has some limitations, such as:

    - It assumes that the image has a bimodal histogram, which may not be true for some images
    - It does not consider the spatial information or the correlation between pixels, which may affect the segmentation quality
    - It may not work well for images with uneven illumination or noise
    - It may not be suitable for images with more than two regions or classes