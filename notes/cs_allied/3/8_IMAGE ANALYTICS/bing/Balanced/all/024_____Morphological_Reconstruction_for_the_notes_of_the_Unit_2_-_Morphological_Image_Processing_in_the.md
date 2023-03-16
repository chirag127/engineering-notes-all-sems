# Morphological Reconstruction

- Morphological reconstruction is a technique for extracting or enhancing marked objects from an image without changing their size or shape .
- Morphological reconstruction uses two images: a marker image and a mask image. The marker image specifies where the processing begins, and the mask image limits the processing region  .
- The basic operations of morphological reconstruction are geodesic dilation and geodesic erosion. Geodesic dilation spreads the peaks of the marker image until they reach the boundary of the mask image or meet another peak. Geodesic erosion shrinks the valleys of the marker image until they reach the boundary of the mask image or meet another valley  .
- Morphological reconstruction can be used for various applications, such as filling holes, extracting the largest connected component, smoothing boundaries, removing noise, and separating objects  .
- Morphological reconstruction is different from other morphological operations because it uses pixel connectivity rather than a structuring element with a specific shape and size. This preserves the shape and size of the objects from the mask image .