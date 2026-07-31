### Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformations are the mappings of coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformations are part of the viewing pipeline, which consists of the following steps :
  - Define the world coordinate system (WCS), which is the right-handed Cartesian coordinate system where the picture is defined.
  - Define the viewing coordinate system (VCS), which is the coordinate system relative to the viewer's position and orientation.
  - Define the projection type, which can be parallel or perspective, and the projection plane, which is the plane where the picture is projected.
  - Define the window, which is the rectangular region of the projection plane that contains the part of the picture to be displayed.
  - Define the viewport, which is the rectangular region of the display device where the window is mapped.
  - Apply the window-to-viewport transformation, which is the mapping of the window coordinates to the viewport coordinates.
  - Apply the clipping, which is the removal of objects, lines, or line segments that are outside the window or behind the viewer.
- Viewing transformations can be represented by matrices, which can be composed by multiplying them in the correct order.
- Viewing transformations can be implemented by using various methods and algorithms, such as homogeneous coordinates, Cohen-Sutherland algorithm, Liang-Barsky algorithm, Sutherland-Hodgman algorithm, etc .