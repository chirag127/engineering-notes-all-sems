### Morphological Reconstruction

- Morphological reconstruction is a technique to extract or enhance marked objects from an image without changing their size or shape .
- Morphological reconstruction uses two images: a marker image and a mask image. The marker image specifies the regions of interest, while the mask image defines the boundaries of the objects.
- The marker image must be equal to or smaller than the mask image in a pointwise sense, i.e., each pixel value in the marker image must be less than or equal to the corresponding pixel value in the mask image.
- The basic operation of morphological reconstruction is geodesic dilation, which dilates the marker image under the constraints of the mask image. Geodesic dilation can be iterated until the image values stop changing, resulting in the reconstructed image.
- Morphological reconstruction can be used for various applications, such as filling holes, extracting the largest connected component, removing small objects, smoothing boundaries, and separating touching objects .
- Morphological reconstruction can be performed in binary or grayscale images, and can be extended to use erosion instead of dilation .