## Unit 2 - Morphological Image Processing

- Morphological image processing is a technique that deals with the shape and structure of objects in an image.
- It is based on the mathematical theory of sets and the concept of structuring elements, which are small shapes that are used to probe the image.
- The basic operations of morphological image processing are erosion and dilation, which can be used to perform various tasks such as noise removal, edge detection, boundary extraction, thinning, skeletonization, etc.
- Erosion is an operation that shrinks the foreground objects in an image by removing pixels from their boundaries. It is defined as the intersection of the image and the translated structuring element.
- Dilation is an operation that expands the foreground objects in an image by adding pixels to their boundaries. It is defined as the union of the image and the translated structuring element.
- The combination of erosion and dilation can produce more complex operations such as opening and closing, which can be used to smooth the contours of objects, eliminate small holes or gaps, fill small breaks or cracks, etc.
- Opening is an operation that first erodes an image and then dilates it with the same structuring element. It can remove small objects or noise from the image while preserving the shape and size of the larger objects.
- Closing is an operation that first dilates an image and then erodes it with the same structuring element. It can fill small holes or gaps in the image while preserving the shape and size of the larger objects.
- Morphological image processing can also be extended to grayscale images by using the concepts of set order, rank, and supremum and infimum. The grayscale erosion and dilation are defined as the minimum and maximum of the image and the translated structuring element, respectively.
- The grayscale opening and closing are defined as the erosion followed by the dilation and the dilation followed by the erosion, respectively, with the same structuring element. They can be used to smooth the grayscale image, enhance the contrast, or remove the background.