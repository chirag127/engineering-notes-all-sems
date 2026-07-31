### Fundamentals for the notes of the Unit 2 - Morphological Image Processing in the subject of IMAGE ANALYTICS

1. Morphological image processing is a collection of non-linear operations related to the shape or morphology of features in an image.
2. It is used to extract image components that are useful in the representation and description of region shape, such as boundaries, skeletons, and the convex hull.
3. The basic morphological operations are erosion and dilation. These operations are defined for binary images, but can be extended to grayscale images.
4. Erosion is an operation that shrinks or thins objects in a binary image. It is defined as the set of all points for which the structuring element, when placed with its origin at that point, fits entirely within the foreground of the image.
5. Dilation is an operation that grows or thickens objects in a binary image. It is defined as the set of all points for which the structuring element, when placed with its origin at that point, overlaps at least one foreground pixel of the image.
6. Other morphological operations include opening, closing, hit-or-miss transform, thinning, thickening, skeletonization, and pruning.
7. Morphological operations can be applied to grayscale images by defining the structuring element as a grayscale image and using a comparison operator other than set inclusion.
8. Morphological image processing has applications in various fields, including computer vision, image analysis, and pattern recognition.
