### Optimum Global Thresholding using Otsu’s Method

- Otsu’s method is a technique of performing global thresholding on a digital image. It is optimum in the sense that it maximizes the between-class variance .
- Global thresholding is a process of converting a grayscale image into a binary image by using a single intensity value as a threshold .
- Otsu’s method assumes that the image contains two classes of pixels: foreground and background, and that the histogram of the image is bimodal .
- Otsu’s method aims to find the optimal threshold value that minimizes the within-class variance or maximizes the inter-class variance of the two classes  .
- Otsu’s method can be formulated as an optimization problem as follows  :

  - Let p(i) be the probability of pixel intensity i in the image, where i ranges from 0 to L-1, and L is the number of possible intensity levels.
  - Let T be the threshold value that separates the foreground and background classes, where 0 <= T <= L-1.
  - Let w0 and w1 be the probabilities of the foreground and background classes, respectively, defined as:

    - w0 = sum(p(i)) for i = 0 to T
    - w1 = sum(p(i)) for i = T+1 to L-1

  - Let u0 and u1 be the mean intensities of the foreground and background classes, respectively, defined as:

    - u0 = sum(i * p(i)) / w0 for i = 0 to T
    - u1 = sum(i * p(i)) / w1 for i = T+1 to L-1

  - Let u be the overall mean intensity of the image, defined as:

    - u = sum(i * p(i)) for i = 0 to L-1

  - Then, the within-class variance is given by:

    - sigma^2 = w0 * (u0 - u)^2 + w1 * (u1 - u)^2

  - And the inter-class variance is given by:

    - eta^2 = w0 * w1 * (u0 - u1)^2

  - The optimal threshold value T* is the one that minimizes sigma^2 or maximizes eta^2.

- Otsu’s method can be implemented by iterating over all possible threshold values and computing the within-class variance or inter-class variance for each value, and then selecting the value that gives the minimum or maximum result  .
- Otsu’s method can also be implemented by using the cumulative histogram of the image and applying some algebraic manipulations to simplify the computation of the within-class variance or inter-class variance .
- Otsu’s method is a one-dimensional discrete analogue of Fisher's Discriminant Analysis, is related to Jenks optimization method, and is equivalent to a globally optimal k-means performed on the intensity histogram.
- Otsu’s method is simple, fast, and effective for images with bimodal histograms, but it may not work well for images with multimodal histograms or non-uniform illumination  .
- Otsu’s method can be extended to multilevel thresholding by using a recursive approach or a dynamic programming approach .