### 2-D Clipping algorithms

Clipping is the process of removing or hiding the parts of a graphical object that lie outside a specified region of interest, such as the viewport or the window. Clipping is useful for improving the efficiency and the aesthetics of computer graphics applications.

There are different types of clipping algorithms depending on the type of graphical object and the shape of the clipping region. Some of the common 2-D clipping algorithms are:

- Point clipping: This algorithm determines whether a given point lies inside or outside the clipping region, and discards the point if it is outside. The clipping region can be a rectangle, a circle, or a polygon. A simple way to perform point clipping is to compare the coordinates of the point with the boundaries of the clipping region and check if they satisfy the inclusion criteria. For example, for a rectangular clipping region with coordinates (Xmin, Ymin) and (Xmax, Ymax), a point (X, Y) is inside if and only if Xmin <= X <= Xmax and Ymin <= Y <= Ymax.

- Line clipping: This algorithm determines whether a given line segment intersects with the clipping region, and clips the line segment to the portion that lies inside the region. The clipping region can be a convex or a concave polygon, but the most common case is a rectangle. There are several line clipping algorithms, such as Cohen-Sutherland, Liang-Barsky, Cyrus-Beck, and Nicholl-Lee-Nicholl. These algorithms use different techniques to reduce the number of calculations and to handle special cases, such as horizontal or vertical lines, or lines that are completely inside or outside the region  .

- Polygon clipping: This algorithm determines whether a given polygon overlaps with the clipping region, and clips the polygon to the sub-polygon that lies inside the region. The clipping region can be any polygon, but the most common case is a convex polygon. There are several polygon clipping algorithms, such as Sutherland-Hodgman, Weiler-Atherton, Greiner-Hormann, and Vatti. These algorithms use different techniques to find the intersection points between the polygon edges and the clipping boundaries, and to construct the output polygon from the input polygon and the intersection points.

Some of the advantages of clipping algorithms are:

- They reduce the amount of data that needs to be processed and displayed, which improves the performance and the quality of the graphics output.
- They allow the user to focus on a specific region of interest, which enhances the user experience and the interactivity of the graphics applications.
- They prevent the graphical objects from overlapping or obscuring each other, which improves the clarity and the realism of the graphics output.