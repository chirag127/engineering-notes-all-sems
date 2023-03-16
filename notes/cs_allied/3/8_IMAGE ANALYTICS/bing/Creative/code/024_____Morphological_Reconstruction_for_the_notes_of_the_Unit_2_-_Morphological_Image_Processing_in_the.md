### Morphological Reconstruction

- Morphological reconstruction is a method for extracting meaningful information about shapes in an image.
- Morphological reconstruction is based on morphological dilation, but uses two images, a marker and a mask, rather than one image and a structuring element.
- The marker image specifies the starting points for the dilation process, and the mask image constrains the dilation to the regions of interest.
- Morphological reconstruction can be used to extract or enhance marked objects from an image without changing their size or shape .
- Morphological reconstruction can also be used to fill holes, extract the image skeleton, or perform watershed segmentation.
- Morphological reconstruction can be performed in binary or grayscale images.
- Morphological reconstruction can be implemented using geodesic dilation and erosion operations, which are repeated until stability is reached .
- Geodesic dilation and erosion are defined as follows:

  - Geodesic dilation: D<sub>G</sub>(f,g) = (f ⊕ B) ∧ g, where f is the marker image, g is the mask image, B is a structuring element, ⊕ is the dilation operator, and ∧ is the pixel-wise minimum operator.
  - Geodesic erosion: E<sub>G</sub>(f,g) = (f ⊖ B) ∨ g, where f is the marker image, g is the mask image, B is a structuring element, ⊖ is the erosion operator, and ∨ is the pixel-wise maximum operator.

- Morphological reconstruction by dilation is defined as the repeated application of geodesic dilation until stability:

  - R<sub>D</sub>(f,g) = D<sub>G</sub><sup>k</sup>(f,g), where k is the smallest integer such that D<sub>G</sub><sup>k+1</sup>(f,g) = D<sub>G</sub><sup>k</sup>(f,g).

- Morphological reconstruction by erosion is defined as the repeated application of geodesic erosion until stability:

  - R<sub>E</sub>(f,g) = E<sub>G</sub><sup>k</sup>(f,g), where k is the smallest integer such that E<sub>G</sub><sup>k+1</sup>(f,g) = E<sub>G</sub><sup>k</sup>(f,g).

- An example of morphological reconstruction by dilation is shown below:

  - The marker image is a binary image with white pixels at the center of each object of interest.
  - The mask image is the original binary image with the objects of interest.
  - The result image is the morphological reconstruction by dilation, which fills the holes in the objects and preserves their shape and size.

![marker image](https://www.mathworks.com/help/examples/images/win64/MarkerImageExample_01.png)
![mask image](https://www.mathworks.com/help/examples/images/win64/MaskImageExample_01.png)
![result image](https://www.mathworks.com/help/examples/images/win64/ReconstructionByDilationExample_01.png)

- An example of morphological reconstruction by erosion is shown below:

  - The marker image is a grayscale image with the intensity values of the local minima of the original image.
  - The mask image is the original grayscale image.
  - The result image is the morphological reconstruction by erosion, which separates the objects based on the watershed lines.

![marker image](https://www.mathworks.com/help/examples/images/win64/MarkerImageExample_02.png)
![mask image](https://www.mathworks.com/help/examples/images/win64/MaskImageExample_02.png)
![result image](https://www.mathworks.com/help/examples/images/win64/ReconstructionByErosionExample_01.png)