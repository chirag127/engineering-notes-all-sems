 Here are the notes on Sutherland Hodgeman polygon clipping for Unit 2 - Transformations in Computer Graphics:

### Sutherland Hodgeman Polygon Clipping

1. Polygon clipping is a technique of cutting a polygon into one or more polygons when it lies partially inside and partially outside the clipping region.
2. Sutherland Hodgeman algorithm is a efficient algorithm to clip a polygon against a rectangle. It uses the outcodes (inside, outside, intersection) to clip the polygon.
3. Steps:

- Calculate outcode for each vertex of the polygon using the clipping rectangle.
- Set current vertex to first vertex and mark it as inside.
- Calculate outcode of next vertex.
- If outcode is 0000, keep processing the vertices.
- Else if outcode is not 0000, it means the edge intersects the rectangle. Find the intersection point and split the edge. Update the current vertex to intersection point.
- Repeat step #4 till the last vertex.
- The remaining vertices form the clipped polygon.

4. The time complexity of Sutherland Hodgeman algorithm is O(n) where n is the number of vertices in the input polygon.
5. Applications: Viewport clipping, Window clipping etc.

### Additional Notes:

- The algorithm can be easily extended to polygon clipping against other convex/non-convex shapes.
- The efficiency can be improved by using scan line algorithm for clipping.
- This algorithm only clips the polygon and does not consider the holes inside the polygon. Separate algorithm is required for hole clipping.