### Some Basic Intensity Transformation Functions

- Intensity transformation is a process of modifying the pixel values of an image to enhance its appearance or to highlight some features.
- It is also known as point operation or gray level mapping, as it maps each pixel value to a new value based on a transformation function.
- The general form of an intensity transformation function is `s = T(r)`, where `r` is the input pixel value, `s` is the output pixel value, and `T` is the transformation function.
- Some basic types of intensity transformation functions are:

  - **Linear transformation**: This is a simple and fast transformation that preserves the relative order of pixel values. It can be used for negative and identity transformation.
    - **Negative transformation**: This is a linear transformation that reverses the pixel values, such that `s = L - 1 - r`, where `L` is the maximum pixel value. It can be used to invert the image or to enhance white or gray detail embedded in dark regions.
    - **Identity transformation**: This is a linear transformation that does not change the pixel values, such that `s = r`. It can be used to keep the image unchanged or to copy it.
  - **Logarithmic transformation**: This is a non-linear transformation that compresses the dynamic range of pixel values. It can be used for log and inverse-log transformation.
    - **Log transformation**: This is a logarithmic transformation that maps low pixel values to higher values, and high pixel values to lower values, such that `s = c log (1 + r)`, where `c` is a constant. It can be used to expand the dark pixels and compress the bright pixels, or to enhance the details in dark regions.
    - **Inverse-log transformation**: This is a logarithmic transformation that maps high pixel values to lower values, and low pixel values to higher values, such that `s = c exp (r) - 1`, where `c` is a constant. It can be used to expand the bright pixels and compress the dark pixels, or to enhance the details in bright regions.
  - **Power-law transformation**: This is a non-linear transformation that has the form of `s = c r^γ`, where `c` and `γ` are constants. It can be used for gamma correction or contrast stretching.
    - **Gamma correction**: This is a power-law transformation that adjusts the brightness and contrast of an image according to the display device. It can be used to correct the non-linear response of the human eye or the monitor.
    - **Contrast stretching**: This is a power-law transformation that increases the contrast of an image by spreading out the pixel values. It can be used to enhance the details in low-contrast images or to improve the visibility of features.
  - **Histogram equalization**: This is a non-linear transformation that produces an output image with a uniform histogram. It can be used to enhance the contrast of an image by utilizing the full range of pixel values.