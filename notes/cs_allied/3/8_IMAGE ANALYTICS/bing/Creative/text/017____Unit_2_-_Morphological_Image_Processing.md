## Unit 2 - Morphological Image Processing

- Morphological image processing is a technique that deals with the shape and structure of objects in an image.
- It is based on the mathematical theory of sets and the concept of structuring elements, which are small shapes that are used to probe the image.
- The basic operations of morphological image processing are erosion and dilation, which can be combined to form more complex operations such as opening, closing, boundary extraction, and skeletonization.
- Erosion is the operation that shrinks an object by removing pixels from its boundary, while dilation is the operation that expands an object by adding pixels to its boundary.
- Opening is the operation that smooths the contour of an object and removes small protrusions, while closing is the operation that fills small gaps and holes in an object.
- Boundary extraction is the operation that extracts the edge of an object by subtracting the eroded image from the original image, while skeletonization is the operation that reduces an object to a thin line that preserves its topology and shape.
- Morphological image processing can be applied to binary images, which have only two pixel values (0 and 1), or to grayscale images, which have a range of pixel values (0 to 255).
- For binary images, the structuring element is also binary, and the operations are defined by set operations such as intersection, union, and complement.
- For grayscale images, the structuring element is also grayscale, and the operations are defined by the minimum and maximum values of the pixels under the structuring element.