### Edge linking via Hough transform

- Edge linking is the process of connecting the edge pixels in an image to form continuous contours or boundaries of objects.
- Hough transform is a global technique for edge linking that can detect the presence of regular curves such as lines, circles, ellipses, etc. in an image.
- The basic idea of Hough transform is to map each edge pixel in the image space to a set of parameters in the parameter space that define the curve passing through that pixel.
- For example, for a line, the parameter space can be the slope-intercept form (y = mx + b) or the normal form (x cos θ + y sin θ = ρ), where m, b, θ and ρ are the parameters.
- Each edge pixel in the image space corresponds to a curve in the parameter space, and the intersection of the curves indicates a possible line in the image space.
- The parameter space is discretized into a grid of cells called accumulator array, and each cell accumulates the votes from the edge pixels that map to it.
- The cells with high votes indicate the presence of a curve in the image space, and the parameters of the curve can be obtained from the cell coordinates.
- The Hough transform can be applied to the edge map obtained from any edge detection method, such as Sobel, Prewitt, Roberts, Canny, etc.
- The Hough transform has some advantages and disadvantages for edge linking:
  - Advantages:
    - It is robust to noise and occlusion, as it can detect curves even if they are partially visible or broken.
    - It can handle multiple curves in the image, as each curve has a distinct peak in the accumulator array.
    - It can deal with curves that are not well defined by local information, such as straight lines or circles.
  - Disadvantages:
    - It is computationally expensive, as it requires a large accumulator array and a lot of voting operations.
    - It is sensitive to the choice of parameters, such as the resolution of the accumulator array, the threshold for peak detection, and the curve model.
    - It may produce false positives or miss some curves, as the voting scheme may not reflect the true shape or strength of the curves.