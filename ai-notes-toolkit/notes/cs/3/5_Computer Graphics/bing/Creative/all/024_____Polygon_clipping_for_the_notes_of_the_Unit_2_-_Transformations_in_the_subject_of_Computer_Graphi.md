# Polygon clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Polygon clipping is the process of removing the portions of a polygon that lie outside a given clipping window or region.
- Polygon clipping is used for various purposes in computer graphics, such as:
  - To prevent undesirable effects when displaying polygons on the output device.
  - To render 3D images through hidden surface removal.
  - To produce high-quality surface details using techniques such as beam tracing.
  - To distribute the objects of a scene to appropriate processors in multiprocessor raytracing systems to improve rendering speeds.
- Polygon clipping can be performed by different algorithms, such as:
  - Sutherland-Hodgman algorithm: This algorithm clips a polygon against a convex clipping window by processing each edge of the polygon against each edge of the window in a clockwise order .
  - Weiler-Atherton algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersection points of the polygon and the window edges and then tracing the clipped polygon boundaries.
  - Greiner-Hormann algorithm: This algorithm clips a polygon against a convex or concave clipping window by using a doubly-connected edge list data structure and a boolean operation to determine the clipped polygon boundaries.
- Polygon clipping can be illustrated by the following example:

![Polygon clipping example](https://www.tutorialandexample.com/wp-content/uploads/2019/11/Polygon-Clipping-in-Computer-Graphics-1.png)

In this example, the blue polygon is clipped against the red clipping window using the Sutherland-Hodgman algorithm. The resulting clipped polygon is shown in green.