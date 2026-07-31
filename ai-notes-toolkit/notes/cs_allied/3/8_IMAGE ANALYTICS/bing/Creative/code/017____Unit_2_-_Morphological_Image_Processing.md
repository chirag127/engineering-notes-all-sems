## Unit 2 - Morphological Image Processing

Morphological image processing is a technique that deals with the shape and structure of objects in an image. It is based on the mathematical theory of sets and the concept of structuring elements. Morphological operations can be used for various purposes, such as:

- Noise removal
- Edge detection
- Segmentation
- Thinning
- Skeletonization
- Reconstruction
- Granulometry
- Morphological filtering
- Morphological gradients
- Morphological feature extraction

Some of the basic morphological operations are:

- Dilation: It expands the foreground pixels by adding pixels to the boundaries of the objects. It can be used to fill small holes, connect gaps, and increase the size of the objects.
- Erosion: It shrinks the foreground pixels by removing pixels from the boundaries of the objects. It can be used to eliminate small objects, separate connected objects, and reduce the size of the objects.
- Opening: It is a combination of erosion followed by dilation. It can be used to remove small objects or noise from the foreground, while preserving the shape and size of the larger objects.
- Closing: It is a combination of dilation followed by erosion. It can be used to fill small holes or gaps in the foreground, while preserving the shape and size of the larger objects.

The structuring element is a small binary image that defines the neighborhood of a pixel. It can have different shapes and sizes, such as a square, a circle, a cross, etc. The structuring element is placed over the input image and the output pixel is determined by the relation between the structuring element and the input image. For example, in dilation, the output pixel is set to 1 if at least one pixel in the structuring element overlaps with a 1 pixel in the input image. In erosion, the output pixel is set to 1 only if all the pixels in the structuring element overlap with 1 pixels in the input image.

Morphological operations can be extended to gray-scale images by using the concepts of maxima and minima. For example, in gray-scale dilation, the output pixel is the maximum value of the input pixels covered by the structuring element. In gray-scale erosion, the output pixel is the minimum value of the input pixels covered by the structuring element.

Morphological operations can also be applied to color images by using the vector ordering of the color components. For example, in color dilation, the output pixel is the vector maximum of the input pixels covered by the structuring element. In color erosion, the output pixel is the vector minimum of the input pixels covered by the structuring element.

Morphological image processing can be implemented using various algorithms, such as:

- Sequential algorithm: It applies the structuring element to each pixel of the input image in a sequential order, such as row-wise or column-wise.
- Parallel algorithm: It applies the structuring element to all the pixels of the input image simultaneously, using parallel processing techniques.
- Hierarchical algorithm: It applies the structuring element to the input image at different levels of resolution, using a pyramid or a tree structure.
- Fast algorithm: It applies the structuring element to the input image using fast Fourier transform (FFT) or other methods that reduce the computational complexity.