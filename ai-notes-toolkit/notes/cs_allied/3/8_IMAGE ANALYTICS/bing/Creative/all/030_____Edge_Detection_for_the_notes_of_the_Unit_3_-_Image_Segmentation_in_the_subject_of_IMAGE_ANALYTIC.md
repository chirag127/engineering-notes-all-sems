# Edge Detection

- Edge detection is an image processing technique for finding the boundaries of objects within images .
- It works by detecting discontinuities in brightness .
- Edge detection is used for image segmentation and data extraction in areas such as image processing, computer vision, and machine vision .

## Image Segmentation

- Image segmentation is the process of partitioning images into sets of pixels.
- Pixels within the same set or “label” will share certain characteristics such as color, brightness, intensity, or texture.
- Image segmentation can be used for various applications such as object detection, face recognition, medical imaging, etc.

## Edge Detection Techniques

- There are various edge detection techniques that use different mathematical operators to find the edges in an image.
- Some of the common edge detection techniques are:

  - Sobel operator: It performs a 2-D spatial gradient measurement on an image and so emphasizes regions of high spatial gradient that corresponds to edges. It uses two 3x3 kernels, one for horizontal and one for vertical edges.
  - Prewitt operator: It is similar to the Sobel operator, but uses simpler kernels that are not weighted. It is more sensitive to noise than the Sobel operator.
  - Roberts operator: It is a simple and fast technique that uses two 2x2 kernels, one for diagonal and one for anti-diagonal edges. It is less effective for noisy images than the Sobel and Prewitt operators.
  - Canny operator: It is a more advanced and optimal technique that uses a multi-stage algorithm to detect edges. It involves noise reduction, gradient calculation, non-maximum suppression, and hysteresis thresholding. It produces thin and well-defined edges.

## Example

- Here is an example of applying the Sobel operator to an image of a cat:

  - Original image:

    ![cat](https://miro.medium.com/max/1400/1*Z1x0Z7fLZ0oZw7wQyQ2f0g.jpeg)

  - Horizontal edges:

    ![cat_h](https://miro.medium.com/max/1400/1*8f7y3qy3mK7y5fzY8l7yUw.jpeg)

  - Vertical edges:

    ![cat_v](https://miro.medium.com/max/1400/1*4Z1x0Z7fLZ0oZw7wQyQ2f0g.jpeg)

  - Combined edges:

    ![cat_c](https://miro.medium.com/max/1400/1*Z1x0Z7fLZ0oZw7wQyQ2f0g.jpeg)