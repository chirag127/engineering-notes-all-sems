### 2-D Clipping algorithms for the notes of the Unit 2 - Transformations in the subject of Computer Graphics

In computer graphics, clipping is the process of removing those parts of a picture that are outside the viewing area. Clipping algorithms are used to clip lines, polygons, and other geometrical shapes.

Some of the commonly used 2-D clipping algorithms are:

1. Cohen-Sutherland Algorithm:
   - It is a line clipping algorithm that uses a four-bit code to represent the location of a point with respect to the viewport.
   - The viewport is divided into nine regions, and each point is assigned a code based on its location.
   - The algorithm checks if the line is entirely inside, outside, or partially inside the viewport and clips accordingly.

2. Liang-Barsky Algorithm:
   - It is a line clipping algorithm that is more efficient than the Cohen-Sutherland algorithm.
   - The algorithm first determines the intersection points of the line with the viewport edges.
   - It then clips the line by using these intersection points to define the new endpoints of the clipped line.

3. Sutherland-Hodgman Algorithm:
   - It is a polygon clipping algorithm that clips a polygon against one edge of the viewport at a time.
   - The algorithm first clips the polygon against the left edge of the viewport and then clips the resulting polygon against the top edge, and so on.
   - This process is repeated until the polygon is completely clipped.

4. Weiler-Atherton Algorithm:
   - It is a polygon clipping algorithm that uses a linked list data structure to store the vertices of the polygon.
   - The algorithm first finds the intersection points between the polygon edges and the viewport edges.
   - It then uses these intersection points to create a new polygon that is completely inside the viewport.

5. Nicholl-Lee-Nicholl Algorithm:
   - It is a polygon clipping algorithm that is based on the Sutherland-Hodgman algorithm.
   - The algorithm uses a binary space partitioning tree to divide the viewport into smaller regions.
   - The polygon is then clipped against each region of the tree to determine the final clipped polygon.

These 2-D clipping algorithms are essential for rendering images in computer graphics. By using these algorithms, we can remove those parts of an image that are outside the viewing area and improve the overall rendering performance.