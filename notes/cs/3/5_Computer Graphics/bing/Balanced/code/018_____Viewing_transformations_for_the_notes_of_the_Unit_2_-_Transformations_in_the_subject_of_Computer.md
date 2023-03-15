### Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformations are the mappings of coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformations are part of the viewing pipeline, which consists of the following steps :
  - Define the world coordinate system (WCS), which is the right-handed Cartesian coordinate system where the picture is defined.
  - Define the viewing coordinate system (VCS), which is the coordinate system relative to the viewer's position and orientation .
  - Apply the viewing transformation, which converts the WCS to the VCS .
  - Define the clipping window, which is the rectangular region in the VCS that defines the portion of the picture to be displayed .
  - Apply the clipping algorithm, which removes the objects, lines, or line segments that are outside the clipping window.
  - Define the viewport, which is the subregion of the display device where the clipped picture is mapped  .
  - Apply the window-to-viewport transformation, which scales and translates the clipped picture from the VCS to the device coordinates  .
- Viewing transformations can be implemented using matrices and homogeneous coordinates, which allow for the representation of translation, scaling, rotation, and perspective transformations using matrix multiplication .
- Viewing transformations can be classified into two types: parallel and perspective .
  - Parallel viewing transformations preserve the parallelism of lines and the relative sizes of objects, and are suitable for engineering and architectural drawings .
  - Perspective viewing transformations introduce the effects of distance and depth, and are suitable for realistic and natural scenes .
- Viewing transformations can be further customized by changing the parameters of the viewing volume, such as the field of view, the aspect ratio, the near and far clipping planes, and the projection reference point .