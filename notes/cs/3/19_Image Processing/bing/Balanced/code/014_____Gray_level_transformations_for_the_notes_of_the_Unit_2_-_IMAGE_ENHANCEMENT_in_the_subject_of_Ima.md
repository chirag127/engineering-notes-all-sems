### Gray level transformations

- Gray level transformations are methods of image enhancement that modify the pixel values of an image based on a mathematical function.
- The general form of a gray level transformation is s = T(r), where r is the input pixel value, s is the output pixel value, and T is the transformation function.
- The transformation function T can be linear or nonlinear, depending on the desired effect on the image contrast, brightness, or dynamic range.
- Some common types of gray level transformations are:

  - Identity transformation: s = T(r) = r. This transformation does not change the image at all.
  - Negative transformation: s = T(r) = L - 1 - r, where L is the number of gray levels in the image. This transformation produces a negative image, where dark and light regions are reversed.
  - Logarithmic transformation: s = T(r) = c log(1 + r), where c is a constant. This transformation compresses the dynamic range of the image, making dark regions brighter and bright regions darker. It is useful for enhancing details in low-light images or images with high contrast.
  - Power-law transformation: s = T(r) = c r^γ, where c and γ are constants. This transformation can either increase or decrease the contrast of the image, depending on the value of γ. If γ < 1, the transformation is called gamma correction, and it brightens the image. If γ > 1, the transformation is called contrast stretching, and it darkens the image.
  - Piecewise-linear transformation: s = T(r) = a r + b, where a and b are constants that vary for different ranges of r. This transformation allows for more flexibility and control over the image enhancement, as different linear functions can be applied to different regions of the image. Some examples of piecewise-linear transformations are:

    - Contrast stretching: s = T(r) = a r + b, where a > 1 and b < 0. This transformation increases the contrast of the image by expanding the range of pixel values.
    - Thresholding: s = T(r) = 0, if r < T; s = T(r) = L - 1, if r >= T, where T is a threshold value. This transformation converts a gray level image into a binary image, where pixels are either black or white, depending on whether they are below or above the threshold.
    - Clipping: s = T(r) = 0, if r < T1; s = T(r) = L - 1, if r > T2; s = T(r) = r, otherwise, where T1 and T2 are lower and upper limits. This transformation removes the pixel values that are outside a specified range, and preserves the ones that are inside.
    - Gray level slicing: s = T(r) = A, if T1 <= r <= T2; s = T(r) = r, otherwise, where A is a constant value and T1 and T2 are lower and upper limits. This transformation highlights a specific range of pixel values by assigning them a constant value, and leaves the rest of the image unchanged.