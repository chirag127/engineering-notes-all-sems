### Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformations are the mappings of coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformations are part of the viewing pipeline, which consists of the following steps :
  - Define the world coordinate system (WCS), which is the right-handed Cartesian coordinate system where the picture is defined.
  - Define the viewing coordinate system (VCS), which is the coordinate system relative to the viewer's position and orientation.
  - Apply the viewing transformation, which converts the WCS to the VCS.
  - Define the clipping window, which is the rectangular region in the VCS that defines the portion of the picture to be displayed.
  - Apply the clipping algorithm, which removes the objects, lines, or line segments that are outside the clipping window.
  - Define the viewport, which is the subregion of the display device where the picture is to be displayed .
  - Apply the window-to-viewport transformation, which maps the coordinates of the clipping window to the coordinates of the viewport.
- Viewing transformations can be implemented using matrix operations, such as translation, rotation, scaling, and projection .
- Viewing transformations can be classified into two types: parallel and perspective.
  - Parallel viewing transformation preserves the parallelism of lines and the relative sizes of objects in the picture.
  - Perspective viewing transformation simulates the effect of distance and depth on the appearance of objects in the picture.