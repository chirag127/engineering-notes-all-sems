# Unit 2 - Morphological Image Processing

- Morphological image processing is a collection of non-linear operations that process images based on shapes or morphology of features in an image  .
- Morphological operations apply a structuring element to an input image, creating an output image of the same size  .
- The structuring element defines the region of interest or neighborhood around a pixel. By choosing the size and shape of the structuring element, we can construct a morphological operation that is sensitive to specific shapes in the input image.
- Morphological operations can be used for various purposes, such as noise removal, edge detection, image enhancement, image segmentation, skeletonization, etc  .
- Some common morphological operations are:
  - Erosion: It shrinks or thins the foreground (white) pixels in the input image, by eroding away the boundaries of regions of foreground pixels  . It can be used to remove small noises, detach two connected objects, etc .
  - Dilation: It expands or thickens the foreground pixels in the input image, by adding pixels to the boundaries of regions of foreground pixels  . It can be used to fill small holes, join two separated objects, etc .
  - Opening: It is a combination of erosion followed by dilation. It removes small objects or thin protrusions from the foreground  . It can be used to smooth the contour of an object, break thin connections, etc .
  - Closing: It is a combination of dilation followed by erosion. It fills small holes or gaps in the foreground  . It can be used to smooth the contour of an object, fuse thin breaks, etc .
  - Morphological Gradient: It is the difference between dilation and erosion of an image. It highlights the boundaries of the foreground objects  . It can be used for edge detection, image enhancement, etc .
  - Top Hat: It is the difference between the input image and its opening. It extracts small bright spots from the background  . It can be used for background subtraction, image enhancement, etc .
  - Black Hat: It is the difference between the closing of the input image and the input image. It extracts small dark spots from the foreground  . It can be used for background subtraction, image enhancement, etc .