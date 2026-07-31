### Erosion and Dilation for the notes of the Unit 2 - Morphological Image Processing in the subject of IMAGE ANALYTICS

- Morphological image processing is a technique that modifies the shape and structure of objects in an image, using mathematical operations based on a predefined structuring element.
- The most basic morphological operations are erosion and dilation, which produce contrasting results when applied to either gray-scale or binary images.
- Erosion involves the removal of pixels at the edges of the region, making the objects smaller and smoother. Dilation involves the addition of pixels to the boundaries of the region, making the objects larger and coarser.
- The number of pixels added or removed from the objects in an image depends on the size and shape of the structuring element used to process the image. The structuring element is a small binary image that defines the neighborhood of a pixel.
- Erosion and dilation are often used in combination to implement image processing operations such as noise removal, edge detection, opening, closing, skeletonization, etc.
- The following are some examples of erosion and dilation applied to a binary image using a 3x3 square structuring element:

![Original image](https://www.mathworks.com/help/examples/images/win64/OriginalImageExample_01.png)

![Eroded image](https://www.mathworks.com/help/examples/images/win64/ErodedImageExample_01.png)

![Dilated image](https://www.mathworks.com/help/examples/images/win64/DilatedImageExample_01.png)

- References:
  -  https://www.geeksforgeeks.org/difference-between-dilation-and-erosion/
  -  https://itexpertly.com/what-is-erosion-and-dilation-in-image-processing/
  -  https://www.mathworks.com/help/images/morphological-dilation-and-erosion.html
  -  https://docs.opencv.org/3.4/db/df6/tutorial_erosion_dilatation.html