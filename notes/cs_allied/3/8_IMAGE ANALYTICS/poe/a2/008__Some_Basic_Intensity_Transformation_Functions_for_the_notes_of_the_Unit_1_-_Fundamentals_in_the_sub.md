 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Some Basic Intensity Transformation Functions

1. Log Transformation: Applies logarithmic transformation to the intensity values. It stretches the lower intensity values and compresses the higher intensity values. This increases the contrast in the darker regions of the image.
Formula: c = log(1 + r)
where c is the transformed intensity and r is the original intensity.

2. Power Law Transformation: Raises each intensity value to a power alpha. It can either stretch or compress the range of intensity values depending on the value of alpha.
Formula: c = r^alpha
where alpha is a constant. If alpha > 1, it stretches the intensities. If 0 < alpha < 1, it compresses the intensities.

3. Piecewise Linear Transformation: Divides the intensity range into several segments and applies different linear transformations to different segments. This offers more flexibility to modify the intensity range as compared to logarithmic and power law transformations.
Formula: c = m1r + c1 for r1 <= r < r2
       c = m2r + c2 for r2 <= r < r3
       .
       .
       .
where m1, c1, m2, c2, etc. are constants that determine the linear transformations for different segments.

The functions can be used to improve the contrast in an image and bring out more details. The choice of function and parameters depend on the characteristics of the input image and the desired output.