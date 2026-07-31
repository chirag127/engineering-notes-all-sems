### Log Transformations

- Log transformations are a type of point operations that are used to enhance the contrast of an image, especially in the dark regions.
- Log transformations map a narrow range of low intensity values in the input image to a wider range of output values, while compressing the high intensity values.
- Log transformations are useful for images with large dynamic range, such as astronomical images, medical images, or images captured in low-light conditions.
- The general formula for log transformations is:

  `s = c log(1 + r)`

  where `s` is the output pixel value, `r` is the input pixel value, `c` is a constant, and `log` is the natural logarithm function.
- The constant `c` controls the slope of the transformation curve and can be determined by:

  `c = (L - 1) / log(1 + max(r))`

  where `L` is the number of gray levels in the image and `max(r)` is the maximum pixel value in the input image.
- Log transformations are invertible, meaning that the original image can be recovered from the transformed image by applying the inverse function:

  `r = exp((s / c) - 1)`

  where `exp` is the exponential function.
- Log transformations can also be applied to color images by transforming each color channel separately. However, this may result in color distortion or loss of saturation. A better alternative is to convert the color image to a different color space, such as HSV or LAB, and apply the log transformation to the intensity or luminance component only.