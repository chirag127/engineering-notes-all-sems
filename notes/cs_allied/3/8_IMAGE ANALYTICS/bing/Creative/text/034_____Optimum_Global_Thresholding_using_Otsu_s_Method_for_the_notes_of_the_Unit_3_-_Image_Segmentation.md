### Optimum Global Thresholding using Otsu’s Method

- Otsu’s method is a technique of performing global thresholding on a digital image. It is optimum in the sense that it maximizes the between-class variance .
- Global thresholding is a process of converting a grayscale image into a binary image by using a single intensity value as a threshold .
- Otsu’s method assumes that the image contains two classes of pixels: foreground and background, and that the intensity histogram of the image is bimodal  .
- Otsu’s method finds the optimal threshold value that minimizes the within-class variance or maximizes the inter-class variance of the two classes   .
- Otsu’s method can be formulated as an optimization problem as follows :

  - Let $p_i$ be the probability of pixel intensity $i$ in the image, where $i = 0, 1, ..., L-1$ and $L$ is the number of possible intensity levels.
  - Let $T$ be the threshold value that separates the foreground and background classes, where $0 \leq T \leq L-1$.
  - Let $w_0$ and $w_1$ be the probabilities of the foreground and background classes, respectively, defined as:

    $$w_0 = \sum_{i=0}^{T-1} p_i$$

    $$w_1 = \sum_{i=T}^{L-1} p_i$$

  - Let $\mu_0$ and $\mu_1$ be the mean intensities of the foreground and background classes, respectively, defined as:

    $$\mu_0 = \frac{1}{w_0} \sum_{i=0}^{T-1} i p_i$$

    $$\mu_1 = \frac{1}{w_1} \sum_{i=T}^{L-1} i p_i$$

  - Let $\mu_T$ be the mean intensity of the entire image, defined as:

    $$\mu_T = \sum_{i=0}^{L-1} i p_i$$

  - Then, the within-class variance $\sigma_W^2$ and the inter-class variance $\sigma_B^2$ are given by:

    $$\sigma_W^2 = w_0 (\mu_0 - \mu_T)^2 + w_1 (\mu_1 - \mu_T)^2$$

    $$\sigma_B^2 = w_0 w_1 (\mu_0 - \mu_1)^2$$

  - Otsu’s method aims to find the optimal threshold value $T^*$ that minimizes $\sigma_W^2$ or maximizes $\sigma_B^2$, which are equivalent objectives. This can be done by iterating over all possible values of $T$ and computing the corresponding variances, and then choosing the value that gives the minimum or maximum variance.

- Otsu’s method has some advantages and disadvantages  :

  - Advantages:

    - It is simple and fast to implement and does not require any prior knowledge of the image characteristics.
    - It is robust to noise and illumination variations in the image.
    - It can handle images with complex and non-uniform backgrounds.

  - Disadvantages:

    - It assumes that the image histogram is bimodal, which may not be true for some images.
    - It may not perform well for images with overlapping intensity distributions of the foreground and background classes.
    - It may not be suitable for images with multiple objects or regions of interest that require different threshold values.