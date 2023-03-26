### 3-D Clipping

In computer graphics, 3-D clipping is the process of removing or discarding those parts of a 3-D object that lie outside of the view volume or the clipping volume. The clipping volume is the region defined by the visible portion of the 3-D object. 3-D clipping is an important step in the rendering pipeline as it helps to reduce the computational overhead and increase the efficiency of the graphics rendering.

The following are the techniques used for 3-D clipping in computer graphics:

1. **Cohen-Sutherland Algorithm:** This algorithm is used to clip line segments and is based on dividing the 3-D space into six regions using three mutually perpendicular planes. The algorithm checks whether a line segment intersects with the planes and clips the line segment accordingly.

2. **Liang-Barsky Algorithm:** This algorithm is also used to clip line segments and provides better performance than the Cohen-Sutherland algorithm. It works by finding the intersection points of the line segment with the clipping planes and then determining the parameter values for the line segment that lie within the clipping volume.

3. **Sutherland-Hodgman Algorithm:** This algorithm is used to clip polygons and works by iterating over each vertex of the polygon and checking whether it lies inside or outside of the clipping volume. The algorithm then clips the polygon accordingly by adding new vertices or removing existing ones.

4. **Weiler-Atherton Algorithm:** This algorithm is used to clip complex polygons and works by splitting the polygon into two parts, one inside the clipping volume and one outside. The algorithm then clips both parts separately and combines them to form the final clipped polygon.

In summary, 3-D clipping is an important process in computer graphics that helps to optimize the rendering pipeline by discarding those parts of a 3-D object that are not visible to the viewer. The above techniques are widely used for 3-D clipping in computer graphics and are essential for creating realistic 3-D scenes and animations.