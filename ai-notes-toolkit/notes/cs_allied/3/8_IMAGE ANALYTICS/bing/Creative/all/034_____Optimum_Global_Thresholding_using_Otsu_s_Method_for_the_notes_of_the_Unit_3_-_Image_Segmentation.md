# Optimum Global Thresholding using Otsu’s Method

- Otsu’s method is a technique of performing global thresholding on a digital image. It is optimum in the sense that it maximizes the between-class variance.
- Global thresholding is a process of converting a grayscale image into a binary image by using a single intensity value as a threshold.
- Otsu’s method assumes that the image contains two classes of pixels: foreground and background, and that the histogram of the image is bimodal.
- Otsu’s method finds the optimal threshold value that minimizes the within-class variance or maximizes the inter-class variance of the two classes  .
- Otsu’s method can be formulated as follows  :
  - Let p(i) be the probability of a pixel having intensity i, where i ranges from 0 to L-1, and L is the number of possible intensity levels.
  - Let w0 and w1 be the probabilities of the background and foreground classes, respectively, defined as:

    w0 = sum(p(i)) for i = 0 to t-1

    w1 = sum(p(i)) for i = t to L-1

  - Let m0 and m1 be the means of the background and foreground classes, respectively, defined as:

    m0 = sum(i*p(i)) / w0 for i = 0 to t-1

    m1 = sum(i*p(i)) / w1 for i = t to L-1

  - Let mT be the global mean of the image, defined as:

    mT = sum(i*p(i)) for i = 0 to L-1

  - Then, the between-class variance is given by:

    sigmaB^2 = w0 * (m0 - mT)^2 + w1 * (m1 - mT)^2

  - And the within-class variance is given by:

    sigmaW^2 = w0 * sigma0^2 + w1 * sigma1^2

    where sigma0^2 and sigma1^2 are the variances of the background and foreground classes, respectively, defined as:

    sigma0^2 = sum((i - m0)^2 * p(i)) / w0 for i = 0 to t-1

    sigma1^2 = sum((i - m1)^2 * p(i)) / w1 for i = t to L-1

  - Otsu’s method finds the optimal threshold value t* that maximizes sigmaB^2 or minimizes sigmaW^2, by iterating over all possible values of t and computing the corresponding variances.
- Otsu’s method can be implemented using various libraries and tools, such as OpenCV, MATLAB, Python, etc .
- Otsu’s method is a simple and effective way of performing global thresholding, but it has some limitations, such as:
  - It assumes that the image histogram is bimodal, which may not be true for some images.
  - It does not consider the spatial information of the pixels, which may affect the visual quality of the thresholded image.
  - It may not be robust to noise, illumination changes, or uneven background.