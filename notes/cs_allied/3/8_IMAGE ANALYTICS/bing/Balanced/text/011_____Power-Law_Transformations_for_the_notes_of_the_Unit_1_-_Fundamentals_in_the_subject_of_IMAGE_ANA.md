### Power-Law Transformations

- Power-law transformations are a type of image enhancement technique that can be used to adjust the contrast and brightness of an image.
- The general form of power-law transformation function is  :

$$
s = c*r^\gamma
$$

where, $s$ and $r$ are the output and input pixel values, respectively and $c$ and $\gamma$ are the positive constants.

- The value of $\gamma$ determines the type and degree of enhancement. For various values of $\gamma$, different levels of enhancement can be obtained.
- If $\gamma < 1$, the transformation is called gamma correction and it increases the brightness of the image by mapping dark pixels to lighter ones.
- If $\gamma > 1$, the transformation is called gamma encoding and it decreases the brightness of the image by mapping light pixels to darker ones.
- If $\gamma = 1$, the transformation is an identity function and it does not change the image.
- The value of $c$ is usually chosen to normalize the output pixel values to the range [0, 255].
- Power-law transformations can be applied to grayscale or color images, but they may affect the color balance of the image if applied to each channel separately.
- Power-law transformations can be used to correct the effects of different types of illumination or sensors on the image, such as the nonlinearity of CRT monitors or the sensitivity of CCD cameras .
- Power-law transformations can also be used to enhance the details or edges of the image by changing the local contrast.