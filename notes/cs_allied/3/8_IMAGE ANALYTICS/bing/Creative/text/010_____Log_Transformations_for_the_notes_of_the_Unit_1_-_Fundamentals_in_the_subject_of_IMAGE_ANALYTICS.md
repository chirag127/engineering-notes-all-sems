### Log Transformations

- Log transformations are a type of point operations that are used to enhance the contrast of an image, especially in the dark regions.
- Log transformations map a narrow range of low intensity values in the input image to a wider range of output values, while compressing the high intensity values.
- Log transformations are useful for images with large dynamic range, such as astronomical images, medical images, or images captured in low-light conditions.
- The general formula for log transformations is:

$$s = c \log(1 + r)$$

where $s$ is the output pixel value, $r$ is the input pixel value, and $c$ is a constant that controls the slope of the transformation curve.

- The constant $c$ can be determined by the desired output range, such as $[0, L-1]$, where $L$ is the number of gray levels in the image. In that case, $c = \frac{L-1}{\log(1 + r_{\max})}$, where $r_{\max}$ is the maximum input pixel value.
- Log transformations have the following properties:
  - They are monotonic, meaning that they preserve the order of pixel values in the image.
  - They are invertible, meaning that they can be reversed by applying the inverse transformation, which is:

  $$r = \exp(\frac{s}{c}) - 1$$

  - They are nonlinear, meaning that they change the relative brightness of different regions in the image.