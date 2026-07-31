### 2-D Clipping algorithms

Clipping is the process of removing or hiding the portions of an object that are outside the viewing area. In computer graphics, 2-D clipping algorithms are used to clip lines, polygons, and other graphical objects against a rectangular clipping window.

Some common 2-D clipping algorithms include:

1. **Cohen-Sutherland Line Clipping Algorithm**: This algorithm divides the clipping window into nine regions and uses a 4-bit code to determine the position of the line endpoints relative to the clipping window. The algorithm then uses this information to clip the line.

2. **Liang-Barsky Line Clipping Algorithm**: This algorithm uses parametric equations to clip lines against the clipping window. It is more efficient than the Cohen-Sutherland algorithm.

3. **Sutherland-Hodgman Polygon Clipping Algorithm**: This algorithm clips a polygon against the clipping window by successively clipping it against each edge of the clipping window. The resulting clipped polygon is then used as the input for the next clipping operation.

4. **Weiler-Atherton Polygon Clipping Algorithm**: This algorithm is similar to the Sutherland-Hodgman algorithm, but it is more efficient for complex polygons. It uses a data structure called a vertex list to keep track of the vertices of the clipped polygon.

These are some of the most commonly used 2-D clipping algorithms in computer graphics. They are used to ensure that only the visible portions of graphical objects are displayed, which can improve the efficiency and performance of graphical applications.