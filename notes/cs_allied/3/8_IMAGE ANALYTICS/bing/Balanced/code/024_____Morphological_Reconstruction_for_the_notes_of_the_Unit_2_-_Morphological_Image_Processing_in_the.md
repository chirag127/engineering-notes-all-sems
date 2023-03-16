### Morphological Reconstruction

- Morphological reconstruction is a technique to extract or enhance marked objects from an image without changing their size or shape .
- It uses two images: a marker image and a mask image. The marker image specifies the regions of interest, while the mask image defines the boundaries of the objects .
- The process starts from the peaks or high points of the marker image and spreads out or dilates to fill in the mask image, while being constrained by the mask image  .
- Morphological reconstruction can be performed by repeated geodesic dilation or erosion, depending on whether the marker image is brighter or darker than the mask image .
- Morphological reconstruction can be used for various applications, such as image segmentation, filtering, contrast enhancement, skeletonization, and watershed transformation .
- Morphological reconstruction is based on pixel connectivity, rather than a structuring element with a specific shape and size, so it preserves the shape and size of the objects from the mask image .