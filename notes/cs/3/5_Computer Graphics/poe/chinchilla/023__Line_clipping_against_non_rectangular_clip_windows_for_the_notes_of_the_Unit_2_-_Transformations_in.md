### Line clipping against non rectangular clip windows

In computer graphics, it is often necessary to clip lines against non-rectangular clip windows, such as polygons or circles. Clipping algorithms are used to remove portions of lines that are outside the designated clip window, and retain only the portion that is visible within the clip window. Here are some common algorithms for line clipping against non-rectangular clip windows:

1. Cohen-Sutherland algorithm:
This algorithm uses a four-bit code to represent the position of a point relative to the clip window. The code is generated for both end points of the line. If both codes are 0000, the line lies entirely within the clip window and is retained. If both codes have at least one 1-bit in common, the line lies entirely outside the clip window and is discarded. Otherwise, the line is partially visible and is clipped against the clip window.

2. Cyrus-Beck algorithm:
This algorithm uses vector arithmetic to determine the intersection of the line with the edges of the clip window. The intersection points are used to determine the portion of the line that lies within the clip window. This algorithm is more efficient than Cohen-Sutherland algorithm when clipping against convex polygons.

3. Liang-Barsky algorithm:
This algorithm uses parameterization of the line to determine the intersection points with the edges of the clip window. The parameter values are used to determine the portion of the line that lies within the clip window. This algorithm is also more efficient than Cohen-Sutherland algorithm when clipping against convex polygons.

4. Sutherland-Hodgman algorithm:
This algorithm clips a polygon against a clip window by iteratively clipping each edge of the polygon against the clip window. The resulting clipped polygon is the portion of the original polygon that lies within the clip window. This algorithm can be used to clip lines against non-convex clip windows by first converting the clip window into a polygon.

In summary, there are many algorithms for line clipping against non-rectangular clip windows. The choice of algorithm depends on the type of clip window and the efficiency requirements of the application.