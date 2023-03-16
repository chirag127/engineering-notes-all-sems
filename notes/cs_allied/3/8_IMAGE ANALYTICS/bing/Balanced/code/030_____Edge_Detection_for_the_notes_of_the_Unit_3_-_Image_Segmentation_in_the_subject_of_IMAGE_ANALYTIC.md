### Edge Detection

- Edge detection is an image processing technique for finding the boundaries of objects within images .
- It works by detecting discontinuities in brightness .
- Edge detection is used for image segmentation and data extraction in areas such as image processing, computer vision, and machine vision .
- Image segmentation is the process of partitioning images into sets of pixels.
- Pixels within the same set or “label” will share certain characteristics such as color, brightness, intensity, or texture.
- Edge detection allows users to observe the features of an image for a significant change in the gray level.
- There are various edge detection operators in digital image processing, such as Sobel, Prewitt, Roberts, Canny, Laplacian, etc  .
- Each operator has its own advantages and disadvantages, such as sensitivity to noise, accuracy, speed, etc  .
- Edge detection techniques can be classified into two categories: gradient-based and laplacian-based .
- Gradient-based techniques use the first-order derivative of the image intensity function to find the edges, such as Sobel, Prewitt, Roberts, and Canny .
- Laplacian-based techniques use the second-order derivative of the image intensity function to find the edges, such as Laplacian, Laplacian of Gaussian, and Difference of Gaussian .
- The following diagram illustrates the basic steps of edge detection:

![Edge detection steps](https://miro.medium.com/max/700/1*ZQ6w3yf0w0wQ0zQx8y7f9w.png)

- The steps are:
  - Convert the image to grayscale
  - Apply a smoothing filter to reduce noise
  - Apply an edge detection operator to find the edge pixels
  - Apply a thresholding technique to remove weak edges
  - Apply a non-maximum suppression technique to thin the edges
  - Apply a hysteresis technique to connect the edge segments