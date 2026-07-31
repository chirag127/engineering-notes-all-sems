### Weiler and Atherton polygon clipping

Weiler and Atherton polygon clipping is an algorithm used in computer graphics to clip a polygon against a rectangular clipping window. This algorithm is used in the subject of Computer Graphics, specifically in Unit 2 - Transformations.

The algorithm works by dividing the polygon into two parts: the part inside the clipping window and the part outside the clipping window. The part inside the clipping window is then drawn, while the part outside the clipping window is discarded.

The algorithm uses the following steps:
1. Identify the intersection points between the polygon and the clipping window.
2. Divide the polygon into sub-polygons using the intersection points.
3. Discard the sub-polygons that are outside the clipping window.
4. Draw the sub-polygons that are inside the clipping window.

This algorithm is efficient and can handle concave and convex polygons. It is widely used in computer graphics applications.