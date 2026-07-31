### Warn model for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the lines and surfaces that are not visible from a particular viewpoint or projection direction in a 3D scene.
- Hidden line and surface elimination is the problem of determining which lines or edges, vertices, surfaces or volumes are visible or invisible to the observer at a specified point.
- Hidden line and surface elimination can be classified into two categories: object space methods and image space methods.
- Object space methods operate on the object definitions and apply geometric or spatial coherence to eliminate hidden parts. Examples of object space methods are back-face detection, depth sorting, BSP trees, octrees, etc.
- Image space methods operate on the projection image and apply pixel or area coherence to eliminate hidden parts. Examples of image space methods are Z-buffer, A-buffer, scan-line, ray tracing, etc.
- Warn model is an image space method that uses area subdivision algorithm to compute the visible surface in the scene. It was proposed by John Warnock in 1969.
- Warn model divides the projection window into smaller subareas recursively until each subarea is either fully visible, fully invisible, or contains a single object.
- Warn model uses four rules to determine the visibility of a subarea:
  - Rule 1: If the subarea contains only one object, then the object is visible and the subarea is painted with the object color.
  - Rule 2: If the subarea is empty, then the subarea is invisible and the subarea is painted with the background color.
  - Rule 3: If the subarea contains more than one object, and all the objects are at the same depth, then the subarea is visible and the subarea is painted with the color of the nearest object.
  - Rule 4: If the subarea contains more than one object, and the objects are at different depths, then the subarea is divided into four equal subareas and the algorithm is applied recursively to each subarea.
- Warn model can handle transparency, shadows, and reflections by using the A-buffer technique, which stores the depth and color information of all the objects in a subarea in a linked list.
- Warn model can also simulate studio lighting effects by controlling the light intensity in different directions, using the Phong model for the surface points.