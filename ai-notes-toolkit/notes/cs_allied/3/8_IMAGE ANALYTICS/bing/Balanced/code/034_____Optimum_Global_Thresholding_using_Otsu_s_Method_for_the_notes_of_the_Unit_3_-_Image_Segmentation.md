### Optimum Global Thresholding using Otsu’s Method

- Otsu’s method is a technique of performing global thresholding on a digital image. It is optimum in the sense that it maximizes the between-class variance.
- Global thresholding is a process of converting a grayscale image into a binary image by using a single intensity value as a threshold.
- Otsu’s method assumes that the image histogram has two peaks, one for the foreground pixels and one for the background pixels, and tries to find the optimal threshold that separates them.
- The optimal threshold is the one that minimizes the within-class variance, or equivalently, maximizes the inter-class variance.
- The within-class variance is the weighted sum of the variances of the foreground and background pixels, and the inter-class variance is the product of the probabilities and the mean difference of the foreground and background pixels.
- Otsu’s method can be formulated as an optimization problem as follows:

  - Let p(i) be the probability of pixel intensity i in the image, where i ranges from 0 to L-1, and L is the number of possible intensity levels.
  - Let t be the threshold that divides the image into foreground and background pixels, where 0 <= t <= L-1.
  - Let w0(t) and w1(t) be the probabilities of the foreground and background pixels, respectively, given by:

    - w0(t) = sum(p(i)) for i = 0 to t
    - w1(t) = sum(p(i)) for i = t+1 to L-1

  - Let m0(t) and m1(t) be the mean intensities of the foreground and background pixels, respectively, given by:

    - m0(t) = sum(i*p(i)) / w0(t) for i = 0 to t
    - m1(t) = sum(i*p(i)) / w1(t) for i = t+1 to L-1

  - Let m(t) be the mean intensity of the whole image, given by:

    - m(t) = w0(t) * m0(t) + w1(t) * m1(t)

  - Then, the within-class variance is given by:

    - sigma^2_w(t) = w0(t) * (m0(t) - m(t))^2 + w1(t) * (m1(t) - m(t))^2

  - And the inter-class variance is given by:

    - sigma^2_b(t) = w0(t) * w1(t) * (m0(t) - m1(t))^2

  - The optimal threshold is the one that minimizes sigma^2_w(t) or maximizes sigma^2_b(t), i.e.:

    - t_opt = argmin(sigma^2_w(t)) or argmax(sigma^2_b(t)) for t = 0 to L-1

- Otsu’s method can be implemented using a simple algorithm that iterates over all possible thresholds and computes the variances for each one, and then selects the one that gives the minimum or maximum value.
- Otsu’s method can also be implemented using built-in functions in some libraries or frameworks, such as OpenCV, MATLAB, scikit-image, etc .
- Otsu’s method is a simple and effective technique for global thresholding, but it has some limitations, such as:

  - It assumes that the image histogram has a bimodal distribution, which may not be true for some images.
  - It does not consider the spatial information or the local variations of the image pixels.
  - It may not be robust to noise or outliers in the image.

- Therefore, some extensions or modifications of Otsu’s method have been proposed to overcome these limitations, such as adaptive thresholding, multi-level thresholding, fuzzy thresholding, etc.