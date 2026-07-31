# Power-Law Transformations

- Power-law transformations are a type of intensity transformation that can be used for image enhancement    .
- The general form of a power-law transformation is given by  :

$$
s = cr^\gamma
$$

where $s$ and $r$ are the output and input pixel values, respectively, $c$ is a constant, and $\gamma$ is a parameter that controls the shape of the transformation curve.

- Power-law transformations can be used to adjust the contrast and brightness of an image, as well as to correct for the gamma of different display devices  .
- The effect of power-law transformations depends on the value of $\gamma$ :
  - If $\gamma < 1$, the transformation curve is concave and maps a narrow range of dark input values to a wider range of output values, while compressing the range of bright input values. This results in an image with increased contrast in the dark regions and decreased contrast in the bright regions.
  - If $\gamma > 1$, the transformation curve is convex and maps a narrow range of bright input values to a wider range of output values, while compressing the range of dark input values. This results in an image with increased contrast in the bright regions and decreased contrast in the dark regions.
  - If $\gamma = 1$, the transformation curve is a straight line and the output image is identical to the input image.

- The following figure shows some examples of power-law transformations with different values of $\gamma$:

![Power-law transformations with different values of gamma](https://theailearner.files.wordpress.com/2019/01/power-law.png?w=1024)

- Power-law transformations can be implemented in Python using the following code:

```python
import cv2
import numpy as np

# Read the input image
img = cv2.imread('input.jpg', 0)

# Define the power-law transformation function
def power_law(img, gamma):
  # Normalize the input image
  norm_img = img / 255.0
  # Apply the power-law transformation
  transformed_img = np.power(norm_img, gamma)
  # Convert the image back to 8-bit format
  transformed_img = np.uint8(transformed_img * 255)
  return transformed_img

# Apply the power-law transformation with gamma = 0.5
img_05 = power_law(img, 0.5)

# Apply the power-law transformation with gamma = 2.0
img_20 = power_law(img, 2.0)

# Display the input and output images
cv2.imshow('Input', img)
cv2.imshow('Output (gamma = 0.5)', img_05)
cv2.imshow('Output (gamma = 2.0)', img_20)
cv2.waitKey(0)
cv2.destroyAllWindows()
```