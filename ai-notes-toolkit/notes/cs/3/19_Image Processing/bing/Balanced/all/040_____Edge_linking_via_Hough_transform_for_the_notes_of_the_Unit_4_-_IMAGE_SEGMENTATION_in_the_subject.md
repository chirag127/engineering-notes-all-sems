# Edge linking via Hough transform

- Edge linking is the process of connecting edge pixels in an image to form continuous edge contours.
- Edge linking can be done by local or global methods.
- Local methods analyze the characteristics of pixels in a small neighborhood around each edge pixel and link them based on criteria such as gradient direction, intensity, or continuity.
- Global methods use a parameter space to represent all possible curves that can pass through the edge pixels and find the optimal ones that maximize some objective function.
- Hough transform is a global method that can detect lines, circles, ellipses, or other shapes in an image.
- Hough transform works by mapping each edge pixel in the image space to a set of curves in the parameter space, where each curve corresponds to a possible shape that passes through the pixel.
- The parameter space is discretized into cells, called accumulator cells, and each cell counts the number of curves that pass through it.
- The cells with high counts indicate the presence of a shape in the image space, and the parameters of the shape can be obtained from the coordinates of the cell.
- For example, to detect lines in an image, the parameter space is defined by the slope and intercept of the line, and each edge pixel is mapped to a sinusoidal curve in the parameter space.
- The accumulator cells that lie on the peaks of the sinusoids indicate the lines in the image, and the slope and intercept of the line can be obtained from the cell coordinates.
- Hough transform can be used to link edge pixels that belong to the same shape, by finding the accumulator cells that correspond to the shape and tracing back the edge pixels that map to those cells.
- Hough transform can handle noisy, incomplete, or broken edges, and can detect multiple shapes in an image.
- However, Hough transform also has some limitations, such as requiring a priori knowledge of the shape to be detected, being sensitive to the choice of parameter space and accumulator resolution, and being computationally expensive.