# 3-D Clipping

- Clipping is the process of removing parts of objects that are outside the viewing volume or the region of interest.
- Clipping is important for efficiency and accuracy in computer graphics.
- Clipping can be done in different stages of the graphics pipeline, such as object space, eye space, clip space or screen space.
- Clipping can be applied to different types of primitives, such as points, lines, polygons, curves or surfaces.
- Clipping can be done using different methods, such as parametric, geometric, Cohen-Sutherland, Liang-Barsky, Sutherland-Hodgman or Weiler-Atherton.
- Clipping can be done using different shapes of clipping regions, such as rectangles, circles, polygons or polyhedra.
- Clipping can be done using different types of clipping planes, such as near, far, left, right, top or bottom.

## Object Space Clipping

- Object space clipping is done before the transformation of objects from their local coordinate systems to the world coordinate system.
- Object space clipping is useful for culling objects that are completely outside the viewing volume or the region of interest.
- Object space clipping can be done using bounding boxes or bounding spheres that enclose the objects and test their intersection with the clipping region.
- Object space clipping can be done using hierarchical data structures, such as octrees or BSP trees, that partition the objects and the space into smaller regions and test their inclusion or exclusion with the clipping region.

## Eye Space Clipping

- Eye space clipping is done after the transformation of objects from the world coordinate system to the eye coordinate system, where the eye is at the origin and the viewing direction is along the negative z-axis.
- Eye space clipping is useful for culling objects that are behind the eye or outside the field of view.
- Eye space clipping can be done using outcodes, which are binary codes that indicate the position of a point relative to the six clipping planes of the view frustum.
- Eye space clipping can be done using the Cohen-Sutherland algorithm for line clipping, which uses the outcodes to determine the trivial accept, trivial reject or subdivision cases.
- Eye space clipping can be done using the Liang-Barsky algorithm for line clipping, which uses the parametric equation of the line and the inequalities of the clipping planes to compute the intersection points.
- Eye space clipping can be done using the Sutherland-Hodgman algorithm for polygon clipping, which uses the clipping planes as boundaries and clips the polygon against each boundary in turn, generating a new polygon at each step.
- Eye space clipping can be done using the Weiler-Atherton algorithm for polygon clipping, which uses the intersection points of the polygon edges and the clipping planes as vertices and constructs a list of entry and exit points for each polygon and each clipping region.

## Clip Space Clipping

- Clip space clipping is done after the transformation of objects from the eye coordinate system to the clip coordinate system, where the coordinates are normalized by the homogeneous component w.
- Clip space clipping is useful for perspective projection, where the view frustum is a truncated pyramid and the clipping region is a unit cube.
- Clip space clipping can be done using the homogeneous clipping algorithm, which uses the sign and magnitude of the homogeneous coordinates to determine the trivial accept, trivial reject or subdivision cases.
- Clip space clipping can be done using the perspective divide, which divides the homogeneous coordinates by w and maps the clip space coordinates to the normalized device coordinates, which range from -1 to 1 in each axis.
- Clip space clipping can be done using the guard-band clipping algorithm, which extends the clipping region slightly beyond the unit cube and allows some tolerance for numerical errors.

## Screen Space Clipping

- Screen space clipping is done after the transformation of objects from the clip coordinate system to the screen coordinate system, where the coordinates are mapped to the pixel coordinates of the display device.
- Screen space clipping is useful for rasterization, where the primitives are converted to pixels and drawn on the screen.
- Screen space clipping can be done using the 2D clipping algorithm, which clips the primitives against the screen boundaries and prevents drawing outside the screen.
- Screen space clipping can be done using the scan-line algorithm, which clips the primitives against the horizontal scan-lines and fills the pixels inside the primitives.