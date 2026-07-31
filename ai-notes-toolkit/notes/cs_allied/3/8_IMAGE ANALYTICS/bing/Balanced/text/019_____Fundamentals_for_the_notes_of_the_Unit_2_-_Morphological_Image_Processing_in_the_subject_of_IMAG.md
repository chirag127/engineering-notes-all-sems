### Fundamentals for the notes of the Unit 2 - Morphological Image Processing in the subject of IMAGE ANALYTICS

- Morphological image processing is a technique that deals with the shape and structure of objects in an image.
- It is based on the mathematical theory of sets and the concept of structuring elements, which are small shapes that are used to probe the image.
- The basic operations of morphological image processing are erosion and dilation, which can be combined to form more complex operations such as opening, closing, thinning, thickening, skeletonization, etc.
- Erosion is an operation that shrinks the foreground objects in an image by removing pixels from their boundaries. It is defined as the intersection of the image and the translated structuring element.
- Dilation is an operation that expands the foreground objects in an image by adding pixels to their boundaries. It is defined as the union of the image and the translated structuring element.
- Opening is an operation that smooths the contours of the foreground objects and removes small protrusions. It is defined as the erosion followed by the dilation of the image by the same structuring element.
- Closing is an operation that smooths the contours of the foreground objects and fills small holes. It is defined as the dilation followed by the erosion of the image by the same structuring element.
- Thinning is an operation that reduces the foreground objects to one-pixel wide skeletons. It is defined as the repeated erosion of the image until no further change occurs, while preserving the connectivity and end-points of the objects.
- Thickening is an operation that increases the thickness of the foreground objects by one pixel. It is defined as the repeated dilation of the image until no further change occurs, while preserving the connectivity and end-points of the objects.
- Skeletonization is an operation that extracts the skeleton of the foreground objects, which is the set of pixels that are equidistant from the object boundaries. It is defined as the repeated application of thinning and thickening until the skeleton is obtained.
- Morphological image processing can be applied to binary or grayscale images, depending on the type of structuring element and the definition of the operations.
- Morphological image processing can be used for various purposes, such as noise removal, edge detection, segmentation, feature extraction, shape analysis, etc.