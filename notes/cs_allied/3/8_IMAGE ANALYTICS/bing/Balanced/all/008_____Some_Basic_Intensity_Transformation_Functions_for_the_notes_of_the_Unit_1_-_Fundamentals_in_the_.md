# Some Basic Intensity Transformation Functions

Intensity transformation functions are mathematical operations that map the pixel values of an input image to new values for the output image. They are also called point processing techniques or intensity transformation techniques, because they depend only on the intensity at a point and not on the neighborhood of the point  .

Some of the basic intensity transformation functions are:

- **Negative transformation**: This function reverses the intensity levels of an image, such that the dark pixels become light and vice versa. It is useful for enhancing white or gray detail embedded in dark regions of an image. The negative transformation function is given by:

  `s = L - 1 - r`

  where `s` and `r` are the output and input pixel values, respectively, and `L` is the number of gray levels in the image.

- **Logarithmic transformation**: This function maps a narrow range of low-intensity values to a wider range of output values, and vice versa. It is useful for expanding the values of dark pixels and compressing the values of bright pixels in an image. The logarithmic transformation function is given by:

  `s = c log(1 + r)`

  where `s` and `r` are the output and input pixel values, respectively, and `c` is a constant.

- **Power-law (gamma) transformation**: This function maps a narrow range of low-intensity values to a wider range of output values, and vice versa, depending on the value of a parameter called gamma. It is useful for correcting the brightness or contrast of an image. The power-law transformation function is given by:

  `s = c r^γ`

  where `s` and `r` are the output and input pixel values, respectively, `c` is a constant, and `γ` is the gamma value. If `γ < 1`, the transformation is similar to the logarithmic function. If `γ > 1`, the transformation is similar to the inverse logarithmic function.

- **Contrast stretching**: This function increases the dynamic range of the gray levels in an image, such that the output image has a higher contrast than the input image. It is useful for enhancing the details of an image that has poor contrast. The contrast stretching function is given by:

  `s = (r - r_min) * (L - 1) / (r_max - r_min)`

  where `s` and `r` are the output and input pixel values, respectively, `L` is the number of gray levels in the image, and `r_min` and `r_max` are the minimum and maximum pixel values in the input image, respectively.

- **Histogram equalization**: This function modifies the histogram of an image, such that the output image has approximately the same number of pixels at each gray level, i.e., the histogram of the output is uniformly distributed. It is useful for enhancing the contrast of an image that has a narrow or skewed histogram . The histogram equalization function is given by:

  `s = (L - 1) * ∑_(i=0)^r P_r(i)`

  where `s` and `r` are the output and input pixel values, respectively, `L` is the number of gray levels in the image, and `P_r(i)` is the probability of occurrence of pixel value `i` in the input image.