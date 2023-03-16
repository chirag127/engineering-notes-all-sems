## Unit 2 - Morphological Image Processing

- Morphological image processing is a collection of non-linear operations that process images based on shapes or morphology of features in an image  .
- Morphological operations apply a structuring element to an input image, creating an output image of the same size . The structuring element defines the region of interest or neighborhood around a pixel.
- Morphological operations can be used for various purposes, such as noise removal, edge detection, image enhancement, image segmentation, skeletonization, etc.
- Some common morphological operations are:
  - Erosion: It shrinks or thins the foreground (white) pixels in the image, by eroding the boundaries of regions of foreground pixels  . It can be used to remove small noises or detach two connected objects.
  - Dilation: It expands or thickens the foreground pixels in the image, by adding pixels to the boundaries of regions of foreground pixels  . It can be used to fill small holes or gaps or connect two separated objects.
  - Opening: It is a combination of erosion followed by dilation. It removes small objects or thin protrusions from the image  .
  - Closing: It is a combination of dilation followed by erosion. It fills small holes or gaps in the image  .
  - Morphological Gradient: It is the difference between dilation and erosion of an image. It highlights the boundaries or edges of the image  .
  - Top Hat: It is the difference between the input image and its opening. It extracts small bright spots from the image  .
  - Black Hat: It is the difference between the input image and its closing. It extracts small dark spots from the image  .
- Morphological operations can be implemented using various libraries or tools, such as MATLAB, scikit-image, OpenCV, etc.