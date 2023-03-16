# Morphological Reconstruction

Morphological reconstruction is a technique for image processing that uses two images, a marker and a mask, to extract or enhance marked objects from an image without changing their size or shape  . The marker image specifies the regions of interest, while the mask image defines the boundaries of the objects. The process involves spreading the marker image values to the neighboring pixels that are not lower than the mask image values, until the image values stop changing.

Some applications of morphological reconstruction are:

- Filling holes and gaps in objects 
- Removing small objects or noise 
- Smoothing object contours 
- Extracting the skeleton or medial axis of objects 
- Segmenting touching or overlapping objects 

Morphological reconstruction can be performed by two basic operations: geodesic dilation and geodesic erosion  . Geodesic dilation spreads the marker image values to the neighboring pixels that are lower than the mask image values, while geodesic erosion shrinks the marker image values to the neighboring pixels that are higher than the mask image values. Both operations can be iterated until the image values stop changing, or until a certain number of iterations is reached. The result of the geodesic dilation is called the reconstruction by dilation, while the result of the geodesic erosion is called the reconstruction by erosion  .

The following figure shows an example of morphological reconstruction by dilation. The marker image is a binary image that marks the regions of interest, while the mask image is a grayscale image that defines the object boundaries. The reconstruction by dilation fills the holes and gaps in the objects, while preserving their shape and size.

![Morphological reconstruction by dilation](https://www.mathworks.com/company/newsletters/articles/morphological-reconstruction/_jcr_content/mainParsys/image_0.adapt.full.high.jpg/1629285904878.jpg)

: Morphological Reconstruction - MATLAB & Simulink. (n.d.). Retrieved March 16, 2023, from https://www.mathworks.com/company/newsletters/articles/morphological-reconstruction.html

: Morphological Operations (Image Processing Toolbox). (n.d.). Retrieved March 16, 2023, from http://www.ece.northwestern.edu/local-apps/matlabhelp/toolbox/images/morph11.html

: Understanding Morphological Reconstruction - MATLAB & Simulink. (n.d.). Retrieved March 16, 2023, from https://www.mathworks.com/help/images/understanding-morphological-reconstruction.html