# Power-Law Transformations

- Power-law transformations are a type of image enhancement technique that can be used to adjust the contrast and brightness of an image  .
- The general form of power-law transformation function is: `s = c*r^γ`   , where:
  - `s` is the output pixel value
  - `r` is the input pixel value
  - `c` and `γ` are positive constants
- The value of `γ` determines the type and degree of enhancement. For different values of `γ`, different levels of enhancement can be obtained.
  - If `γ` is less than 1, the transformation is called a gamma correction and it increases the brightness of the image .
  - If `γ` is equal to 1, the transformation is an identity function and it does not change the image .
  - If `γ` is greater than 1, the transformation is called a contrast stretching and it decreases the brightness of the image .
- The value of `c` is usually chosen to normalize the output pixel values to the range [0, 255].
- Power-law transformations can be applied to grayscale or color images .
- Power-law transformations can be useful for enhancing images that have poor contrast due to illumination or sensor limitations .
- Power-law transformations can also be used to correct the gamma distortion caused by some display devices .

: https://www.camomienoteca.com/research-paper-help/what-is-power-law-transformation-in-image-processing/
: https://benchpartner.com/power-law-transformations-gamma-correction-in-image-processing
: https://theailearner.com/2019/01/26/power-law-gamma-transformations/
: https://link.springer.com/article/10.1007/s12046-012-0110-4