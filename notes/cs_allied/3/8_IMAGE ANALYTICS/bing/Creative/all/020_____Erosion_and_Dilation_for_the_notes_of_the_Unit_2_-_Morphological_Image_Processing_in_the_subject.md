# Erosion and Dilation for the notes of the Unit 2 - Morphological Image Processing in the subject of IMAGE ANALYTICS

- Erosion and dilation are two basic operations in morphological image processing, which is a branch of image processing that deals with the shape and structure of objects in an image.
- Erosion and dilation are applied to binary images, which are images that have only two pixel values: 0 (black) and 1 (white).
- Erosion and dilation are defined by using a structuring element, which is a small binary image that specifies the neighborhood of a pixel.
- Erosion and dilation are also called as hit-or-miss and fit-or-split operations, respectively.

## Erosion

- Erosion is an operation that shrinks or thins the foreground (white) regions in a binary image.
- Erosion works by sliding the structuring element over the image and checking if it fits completely within the foreground region at each pixel location.
- If the structuring element fits, the output pixel is set to 1 (white); otherwise, it is set to 0 (black).
- Erosion can be mathematically expressed as:

  - A ⊖ B = {z | (B)z ⊆ A}

  - where A is the input image, B is the structuring element, (B)z is the translation of B by the vector z, and ⊆ is the subset relation.
- Erosion can be used for:

  - Removing noise or small objects from an image.
  - Separating connected components or thinning the boundaries of objects.
  - Finding the skeleton or medial axis of an object.

## Dilation

- Dilation is an operation that expands or thickens the foreground (white) regions in a binary image.
- Dilation works by sliding the structuring element over the image and checking if it hits any foreground pixel at each pixel location.
- If the structuring element hits, the output pixel is set to 1 (white); otherwise, it is set to 0 (black).
- Dilation can be mathematically expressed as:

  - A ⊕ B = {z | (B̂)z ∩ A ≠ ∅}

  - where A is the input image, B is the structuring element, B̂ is the reflection of B, (B̂)z is the translation of B̂ by the vector z, and ∩ is the intersection operation.
- Dilation can be used for:

  - Filling holes or gaps in an image.
  - Merging or enlarging the boundaries of objects.
  - Finding the convex hull or envelope of an object.