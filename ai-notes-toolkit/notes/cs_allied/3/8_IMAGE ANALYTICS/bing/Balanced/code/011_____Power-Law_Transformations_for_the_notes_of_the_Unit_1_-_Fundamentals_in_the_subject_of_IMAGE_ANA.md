Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Power-Law Transformations for the notes of the Unit 1 - Fundamentals in the subject of IMAGE ANALYTICS:

### Power-Law Transformations

- Power-law transformations are a class of image enhancement techniques that can be used to adjust the contrast and brightness of an image.
- Power-law transformations are also known as gamma corrections, because they are based on the gamma function, which is defined as:

$$
\gamma(x) = \int_0^\infty t^{x-1} e^{-t} dt
$$

- The basic form of a power-law transformation is:

$$
s = cr^\gamma
$$

where s and r are the output and input pixel values, respectively, c is a positive constant, and $\gamma$ is the exponent that controls the shape of the transformation.

- Power-law transformations can be applied to grayscale or color images, by applying the same transformation to each pixel or color channel.
- Power-law transformations can be used for different purposes, depending on the value of $\gamma$:

  - If $\gamma < 1$, the transformation is called a power-law compression, and it can be used to increase the contrast of dark regions and decrease the contrast of bright regions in an image. This can be useful for enhancing images that are too bright or have low dynamic range.
  - If $\gamma > 1$, the transformation is called a power-law expansion, and it can be used to increase the contrast of bright regions and decrease the contrast of dark regions in an image. This can be useful for enhancing images that are too dark or have high dynamic range.
  - If $\gamma = 1$, the transformation is a linear transformation, and it does not change the contrast or brightness of the image.

- The following figure shows an example of applying different power-law transformations to an image:

![Power-law transformations](https://i.imgur.com/4w4pZ1O.png)

- The following code shows how to implement power-law transformations in Python using OpenCV:

```python
import cv2
import numpy as np

# Read the image as grayscale
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Define the constants c and gamma
c = 1
gamma = 0.5 # Change this value to see different results

# Apply the power-law transformation
img_transformed = c * np.power(img, gamma)

# Convert the image to uint8 format
img_transformed = np.uint8(img_transformed)

# Display the original and transformed images
cv2.imshow('Original', img)
cv2.imshow('Transformed', img_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
```