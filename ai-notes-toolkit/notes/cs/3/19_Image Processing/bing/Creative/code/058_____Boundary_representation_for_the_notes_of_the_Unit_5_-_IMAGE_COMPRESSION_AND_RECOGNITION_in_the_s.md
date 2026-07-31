### Boundary representation

- Boundary representation (B-rep) is a method for representing a 3D shape by defining the limits of its volume.
- A boundary representation of a model comprises topological components (faces, edges and vertices) and the connections between them, along with geometric definitions for those components (surfaces, curves and points, respectively).
- A face is a bounded portion of a surface; an edge is a bounded piece of a curve and a vertex lies at a point.
- Boundary representation is useful for image compression and recognition because it reduces the amount of data needed to describe a shape and allows for efficient operations on the shape such as intersection, union, difference, etc.
- Boundary representation can be obtained from a binary image by using morphological image processing techniques such as erosion, dilation, opening, closing, etc .
- Morphological image processing is a set of operations that modify the shape and structure of objects in an image based on their connectivity and geometry.
- Thresholding is a technique for converting a grey-scale image into a binary image by assigning a pixel value of 0 or 1 depending on whether it is below or above a certain threshold.
- Thresholding is the main technique used to extract the foreground from the background in a binary image.
- Boundary extraction is the process of finding the boundary pixels of an object in a binary image.
- Boundary extraction can be done by subtracting the eroded image from the original image.
- Erosion is a morphological operation that shrinks the foreground pixels by removing the pixels at the boundaries of the objects.
- Dilation is a morphological operation that expands the foreground pixels by adding pixels to the boundaries of the objects.
- Opening is a morphological operation that smooths the contour of an object by applying erosion followed by dilation.
- Closing is a morphological operation that fills the gaps and holes in an object by applying dilation followed by erosion.
- Boundary representation can also be obtained from a grey-scale image by using edge detection techniques such as gradient, Laplacian, Canny, etc.
- Edge detection is the process of finding the pixels where the intensity of an image changes abruptly.
- Edge detection is based on the concept of the polynomial transform, which is an image representation model that mimics some properties of the human visual system.
- The polynomial transform models edges in terms of their characteristic parameters such as orientation, curvature, contrast, etc.