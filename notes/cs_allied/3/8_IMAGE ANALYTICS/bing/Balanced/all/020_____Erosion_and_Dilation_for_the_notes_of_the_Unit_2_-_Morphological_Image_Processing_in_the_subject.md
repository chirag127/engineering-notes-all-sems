# Erosion and Dilation for the notes of the Unit 2 - Morphological Image Processing in the subject of IMAGE ANALYTICS

- Erosion and dilation are two basic operations in morphological image processing, which is a branch of image processing that deals with the shape and structure of objects in an image.
- Erosion and dilation are applied to binary images, which are images that have only two pixel values: 0 (black) and 1 (white).
- Erosion and dilation use a small shape or pattern called a structuring element, which is moved over the image to perform the operation.
- Erosion and dilation can be used for various purposes, such as noise removal, edge detection, boundary extraction, image enhancement, and image segmentation.

## Erosion

- Erosion is an operation that shrinks or thins the foreground (white) regions in a binary image.
- Erosion works by placing the structuring element on each pixel of the image and checking if it fits completely within the foreground region. If yes, the pixel is kept as 1; otherwise, it is set to 0.
- Erosion can be mathematically defined as:

  - A ⊖ B = {x | (B)x ⊆ A}

  - where A is the input image, B is the structuring element, (B)x is the translation of B by x, and ⊆ is the subset relation.
- Erosion has the following properties:

  - It is idempotent, meaning that applying erosion multiple times does not change the result after the first application.
  - It is anti-extensive, meaning that the output image is always a subset of the input image.
  - It is increasing, meaning that if A ⊆ B, then A ⊖ C ⊆ B ⊖ C for any C.
  - It is translation invariant, meaning that A ⊖ B = (A − x) ⊖ (B − x) for any x.
- Erosion can be used to:

  - Remove small noise or isolated pixels in the foreground.
  - Separate connected or touching objects in the foreground.
  - Smooth the boundaries of the foreground objects.
  - Reduce the size of the foreground objects.

## Dilation

- Dilation is an operation that expands or thickens the foreground regions in a binary image.
- Dilation works by placing the structuring element on each pixel of the image and checking if it overlaps with any foreground pixel. If yes, the pixel is set to 1; otherwise, it is kept as 0.
- Dilation can be mathematically defined as:

  - A ⊕ B = {x + b | x ∈ A, b ∈ B}

  - where A is the input image, B is the structuring element, and ⊕ is the dilation operator.
- Dilation has the following properties:

  - It is not idempotent, meaning that applying dilation multiple times changes the result.
  - It is extensive, meaning that the output image is always a superset of the input image.
  - It is increasing, meaning that if A ⊆ B, then A ⊕ C ⊆ B ⊕ C for any C.
  - It is translation invariant, meaning that A ⊕ B = (A + x) ⊕ (B + x) for any x.
- Dilation can be used to:

  - Fill small holes or gaps in the foreground.
  - Connect disjoint or broken objects in the foreground.
  - Smooth the boundaries of the foreground objects.
  - Increase the size of the foreground objects.