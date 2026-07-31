# Some Basic Intensity Transformation Functions for the notes of the Unit 1 - Fundamentals in the subject of IMAGE ANALYTICS

- Intensity transformation is a basic digital image processing technique, where the pixel intensity levels of an image are transformed to new values using a mathematical transformation function, so as to get a new output image.
- Intensity transformations are in the spatial domain, i.e. they are performed directly on the pixels of the image at hand, as opposed to being performed on the Fourier transform of the image.
- Intensity transformations are applied on images for contrast manipulation or image thresholding.
- The following are some commonly used intensity transformation functions  :

  - **Negative transformation**: This function reverses the intensity levels of an image, i.e. the output image is the negative of the input image. It is useful for enhancing white or gray detail embedded in dark regions of an image. The transformation function is given by:

    `s = L - 1 - r`

    where `s` and `r` are the output and input pixel values, respectively, and `L` is the number of gray levels in the image.

  - **Log transformation**: This function maps a narrow range of low intensity values in the input image to a wider range of output levels. It is useful for expanding the values of dark pixels in an image while compressing the higher-level values. The transformation function is given by:

    `s = c log(1 + r)`

    where `s` and `r` are the output and input pixel values, respectively, and `c` is a constant.

  - **Power-law (gamma) transformation**: This function maps a narrow range of high intensity values in the input image to a wider range of output levels. It is useful for expanding the values of bright pixels in an image while compressing the lower-level values. The transformation function is given by:

    `s = c r^γ`

    where `s` and `r` are the output and input pixel values, respectively, `c` and `γ` are constants, and `^` denotes exponentiation.

  - **Contrast stretching**: This function increases the dynamic range of the gray levels in the image. It is useful for improving the contrast of an image that has low contrast. The transformation function is given by:

    `s = (r - r_min) / (r_max - r_min) * (L - 1)`

    where `s` and `r` are the output and input pixel values, respectively, `r_min` and `r_max` are the minimum and maximum pixel values in the input image, and `L` is the number of gray levels in the image.

  - **Histogram equalization**: This function transforms the input image such that the output image has approximately the same number of pixels at each gray level, i.e. the histogram of the output is uniformly distributed. It is useful for enhancing the contrast of an image that has a skewed histogram. The transformation function is given by:

    `s = (L - 1) / MN * ∑_(v=0)^r h(v)`

    where `s` and `r` are the output and input pixel values, respectively, `L` is the number of gray levels in the image, `M` and `N` are the dimensions of the image, `h(v)` is the histogram of the input image at gray level `v`, and `∑` denotes summation.