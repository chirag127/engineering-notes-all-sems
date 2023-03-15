### Polygon clipping for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

- Polygon clipping is the process of removing the portions of a polygon that lie outside a given clipping window or region.
- Polygon clipping is used for various purposes in computer graphics, such as:
  - To prevent undesirable effects when displaying polygons on the output device.
  - To render 3D images through hidden surface removal techniques.
  - To produce high-quality surface details using techniques such as beam tracing.
  - To distribute the objects of a scene to appropriate processors in multiprocessor raytracing systems to improve rendering speeds.
- Polygon clipping can be performed by different algorithms, such as:
  - Sutherland-Hodgman algorithm: This algorithm clips a polygon against a convex clipping window by processing each polygon edge against each window edge in a sequential manner. The output is a sequence of vertices that define the clipped polygon boundaries .
  - Weiler-Atherton algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersections of the polygon edges and the window edges, and then tracing the boundary of the clipped polygon using a winding number rule.
  - Greiner-Hormann algorithm: This algorithm clips a polygon against a convex or concave clipping window by finding the intersections of the polygon edges and the window edges, and then using a parity test to determine the inside and outside regions of the clipped polygon.
- Polygon clipping can be illustrated by the following diagrams:

![Polygon clipping example](https://www.tutorialandexample.com/wp-content/uploads/2019/09/Polygon-Clipping-in-Computer-Graphics-1.png)

Figure 1: A polygon and a clipping window

![Polygon clipping result](https://www.tutorialandexample.com/wp-content/uploads/2019/09/Polygon-Clipping-in-Computer-Graphics-2.png)

Figure 2: The result of polygon clipping