### Some Basic Intensity Transformation Functions

- Intensity transformation functions are used to modify the pixel values of an image to enhance its appearance or highlight certain features.
- The general form of an intensity transformation function is `s = T(r)`, where `r` is the input pixel value and `s` is the output pixel value.
- Some basic intensity transformation functions are:

  - **Image negative**: `s = L - 1 - r`, where `L` is the maximum intensity value. This function reverses the intensity values of an image, making dark areas bright and vice versa. It is useful for enhancing white or gray detail embedded in dark regions of an image.
  - **Log transformation**: `s = c log(1 + r)`, where `c` is a constant. This function maps a narrow range of low-intensity values to a wider range of output values. It is useful for expanding the values of dark pixels in images with large dynamic ranges, such as medical or astronomical images.
  - **Power-law (gamma) transformation**: `s = c r^γ`, where `c` and `γ` are constants. This function can perform either contrast stretching or compression, depending on the value of `γ`. If `γ < 1`, the output image is brighter than the input image, and vice versa. It is useful for correcting the brightness or contrast of an image.
  - **Piecewise-linear transformation**: This function consists of several linear segments with different slopes and intercepts. It can be used to perform various operations, such as contrast stretching, clipping, thresholding, or gray-level slicing. It is useful for enhancing specific ranges of intensities in an image.