### Viewing transformations for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Viewing transformations are the mappings of coordinates of points and lines that form the picture into appropriate coordinates on the display device .
- Viewing transformations are necessary to display the picture in a desired way, such as perspective, parallel, or orthographic projection.
- Viewing transformations can be divided into two steps: window-to-viewport transformation and projection transformation .
- Window-to-viewport transformation is the mapping of the window, which is a rectangular region in the world coordinate system (WCS), onto a subregion of the display device called the viewport  .
- Projection transformation is the mapping of the window onto a projection plane, which is a plane perpendicular to the viewing direction .
- The projection plane can be either at a finite distance from the window, which results in a perspective projection, or at infinity, which results in a parallel projection.
- The viewing direction can be specified by a viewing reference point (VRP), a view plane normal (VPN), and a view up vector (VUP) .
- The viewing transformation can be represented by a 4x4 matrix that transforms the world coordinates to the eye coordinates, which are the coordinates on the projection plane.
- The viewing transformation can be composed of translation, rotation, and scaling operations .
- The viewing transformation is insensitive to the position of points relative to the viewing volume, especially those points behind the viewer, and it is necessary to remove these points before generating the view.
- The process of removing the points or lines that are outside the viewing volume is called clipping.
- Clipping can be done in different ways, such as Cohen-Sutherland algorithm, Liang-Barsky algorithm, Sutherland-Hodgman algorithm, etc.