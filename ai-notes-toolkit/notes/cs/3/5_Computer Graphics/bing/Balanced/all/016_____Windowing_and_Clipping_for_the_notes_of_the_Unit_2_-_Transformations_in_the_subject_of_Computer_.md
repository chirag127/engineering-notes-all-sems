# Windowing and Clipping

Windowing and clipping are two techniques used in computer graphics to display a part of a scene or an object on the screen. They are useful for reducing the computational cost and improving the performance of graphics applications.

## Windowing

- Windowing is the process of selecting and viewing a picture with different views .
- A window is an opening through which part of the outside world can be seen.
- A window can be defined by specifying its coordinates in the world coordinate system or the user coordinate system.
- A window can be moved, resized, rotated, or zoomed to change the view of the picture.
- A window can also be clipped by another window to create a subwindow.

## Clipping

- Clipping is the process of dividing each element of the picture into its visible and invisible portions, allowing the invisible portion to be discarded .
- Clipping is necessary to remove objects, lines, or line segments that are outside the viewing pane or behind the viewer.
- Clipping can also be used to extract a desired part of an object, to create objects using solid modeling, or to perform drawing operations.
- Clipping can be done in different coordinate systems, such as world, user, normalized device, or screen coordinates.
- Clipping can be applied to different types of objects, such as points, lines, polygons, curves, or surfaces.
- Clipping can be done using different algorithms, such as Cohen-Sutherland, Liang-Barsky, Sutherland-Hodgman, or Cyrus-Beck.
- Clipping algorithms usually assign a region code for each endpoint of a line or a vertex of a polygon, and then perform logical operations to determine whether the object is inside, outside, or partially inside the clipping window.