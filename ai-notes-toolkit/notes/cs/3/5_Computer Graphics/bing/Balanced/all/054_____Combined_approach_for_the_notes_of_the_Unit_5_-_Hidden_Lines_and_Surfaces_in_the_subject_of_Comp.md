# Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges that are not visible from a given viewpoint in a 3D scene.
- Hidden line and surface removal algorithms are used to improve the realism and clarity of the rendered images by eliminating the hidden parts.
- Hidden line and surface removal algorithms can be classified into two categories: object space methods and image space methods .
- Object space methods compare the objects and parts of objects to each other within the scene definition to determine which surfaces, as a whole or in part, are hidden .
- Image space methods compare each projected pixel position on the view plane against a depth value stored in the refresh buffer to determine visibility .
- Some of the common object space methods are back-face removal, depth sorting, binary space partitioning, and area subdivision .
- Some of the common image space methods are z-buffer, scan-line, and ray tracing .
- A combined approach can use both object space and image space methods to achieve a balance between efficiency and accuracy.
- A possible combined approach is to use back-face removal and depth sorting as object space methods, and then use z-buffer as an image space method.
- Back-face removal eliminates the polygons that are facing away from the viewer, reducing the number of polygons to be processed.
- Depth sorting orders the polygons from back to front, so that the closer polygons can overwrite the farther ones in the image buffer.
- Z-buffer assigns a depth value to each pixel in the image buffer, and compares it with the depth value of the incoming polygon at that pixel. If the incoming polygon is closer, it replaces the pixel value and depth value; otherwise, it is discarded.
- This combined approach can handle concave and intersecting polygons, as well as transparency effects.