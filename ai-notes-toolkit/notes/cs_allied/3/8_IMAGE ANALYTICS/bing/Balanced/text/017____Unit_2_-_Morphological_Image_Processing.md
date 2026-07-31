## Unit 2 - Morphological Image Processing

- Morphological image processing is a technique that deals with the shape and structure of objects in an image.
- It is based on the mathematical theory of sets and the concept of structuring elements, which are small shapes or patterns that are used to probe the image.
- The basic operations of morphological image processing are erosion and dilation, which can be used to modify the boundaries, holes, and connectivity of objects in an image.
- Erosion shrinks an object by removing pixels that do not fit the structuring element, while dilation expands an object by adding pixels that fit the structuring element.
- Erosion and dilation can be combined to form more complex operations, such as opening, closing, boundary extraction, hole filling, and skeletonization.
- Opening is the erosion of an object followed by the dilation of the eroded object, which can be used to remove small noise or protrusions from the object boundary.
- Closing is the dilation of an object followed by the erosion of the dilated object, which can be used to fill small gaps or holes in the object boundary.
- Boundary extraction is the subtraction of the eroded object from the original object, which can be used to highlight the contour of the object.
- Hole filling is the complement of the dilation of the complement of the object, which can be used to fill the interior holes of the object.
- Skeletonization is the iterative erosion of the object until only a thin line remains, which can be used to represent the shape and topology of the object.