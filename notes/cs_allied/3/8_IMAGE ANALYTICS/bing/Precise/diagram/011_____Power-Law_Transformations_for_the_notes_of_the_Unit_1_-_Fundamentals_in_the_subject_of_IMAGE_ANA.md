### Power-Law Transformations

Power-law transformations are a family of transformations that are used to enhance the contrast of an image. These transformations are also known as gamma corrections. The basic form of the power-law transformation is given by the expression:

s = c * r^γ

where s and r are the pixel values of the output and input image, respectively, c is a constant, and γ is the exponent that determines the nature of the transformation.

- When γ = 1, the transformation is a linear transformation and the output image is the same as the input image.
- When γ < 1, the transformation is a compression transformation and the output image has higher contrast in the dark regions and lower contrast in the bright regions.
- When γ > 1, the transformation is an expansion transformation and the output image has higher contrast in the bright regions and lower contrast in the dark regions.

Power-law transformations are useful for correcting the brightness and contrast of an image that has been captured in non-ideal lighting conditions. They can also be used to correct the non-linear response of display devices such as CRT monitors.