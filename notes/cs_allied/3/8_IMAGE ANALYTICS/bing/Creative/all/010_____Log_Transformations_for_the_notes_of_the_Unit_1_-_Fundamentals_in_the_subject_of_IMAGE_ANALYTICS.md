# Log Transformations

- Log transformations are a type of point operations that are used to enhance the contrast of an image, especially in the dark regions.
- Log transformations map a narrow range of low intensity values in the input image to a wider range of output values, while compressing the high intensity values.
- Log transformations are useful for images with large dynamic range, such as astronomical images, medical images, or images captured in low-light conditions.
- The general formula for log transformations is:

  `s = c log(1 + r)`

  where `s` is the output pixel value, `r` is the input pixel value, `c` is a constant, and `log` is the natural logarithm function.
- The constant `c` controls the slope of the log curve and can be chosen to scale the output values to a desired range.
- The term `1` inside the logarithm function is added to avoid taking the logarithm of zero, which is undefined.
- Log transformations are invertible, meaning that the original image can be recovered from the transformed image by applying the inverse log function:

  `r = exp((s / c) - 1)`

  where `exp` is the natural exponential function.
- Log transformations have the following properties:

  - They are monotonic, meaning that they preserve the order of pixel values in the image.
  - They are non-linear, meaning that they change the relative brightness of different regions in the image.
  - They are contrast-stretching, meaning that they increase the contrast of low intensity values and decrease the contrast of high intensity values.
  - They are illumination-invariant, meaning that they are not affected by changes in the overall brightness of the image.