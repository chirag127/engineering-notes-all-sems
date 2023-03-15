### Edge linking via Hough transform

- Edge linking is the process of connecting edge pixels that belong to the same edge in an image.
- Edge linking can be done by local or global processing methods.
- Local processing methods analyze the characteristics of pixels in a small neighborhood around each edge pixel and link them based on criteria such as continuity, smoothness, and similarity of edge direction.
- Global processing methods use a parameter space to represent all possible curves that can pass through the edge pixels and find the optimal ones that maximize some objective function.
- Hough transform is a global processing method that can detect lines, circles, ellipses, and other shapes in an edge image.
- Hough transform works by mapping each edge pixel in the image space to a set of curves in the parameter space that represent all possible lines that can pass through that pixel.
- The parameter space is usually discretized into a two-dimensional array called the accumulator or Hough space, where each cell corresponds to a line with a specific slope and intercept.
- The Hough transform accumulates the votes for each cell in the Hough space by incrementing the cell value by one for each edge pixel that maps to it.
- The peaks in the Hough space indicate the most likely lines that exist in the image space.
- The Hough transform can be used for edge linking by finding the peaks in the Hough space and then visiting the pixels along the corresponding lines in the image space and linking them if they are edge pixels.
- The Hough transform can handle noisy, incomplete, and broken edges, as well as multiple edges that intersect or overlap.
- The Hough transform can also be extended to detect other shapes such as circles, ellipses, and arbitrary curves by using different parameterizations and accumulator arrays.
- The Hough transform has some limitations, such as the computational complexity, the sensitivity to the choice of parameters, and the difficulty of distinguishing between multiple shapes that have similar parameter values.