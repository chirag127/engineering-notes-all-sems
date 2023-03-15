### Curve clipping

- Curve clipping is a method to selectively enable or disable rendering operations within a defined region of interest.
- Curve clipping involves complex procedures as compared to line clipping or polygon clipping .
- Curve clipping requires more processing than for objects with linear boundaries.
- The region of interest, also called the clip window, can be curved or rectangular in shape.
- There are different algorithms for curve clipping, such as the Bezier clipping algorithm, the B-spline clipping algorithm, and the rational B-spline clipping algorithm.
- The Bezier clipping algorithm is based on the convex hull property of Bezier curves, which states that the curve lies entirely within the convex hull of its control points.
- The B-spline clipping algorithm is based on the convex hull property of B-splines, which states that the curve lies entirely within the convex hull of its control points and knots.
- The rational B-spline clipping algorithm is based on the convex hull property of rational B-splines, which states that the curve lies entirely within the convex hull of its weighted control points and knots.
- The general steps of curve clipping algorithms are:
  - Divide the curve into segments using the control points and knots.
  - Test each segment against the clip window boundaries.
  - If the segment is entirely inside the clip window, accept it.
  - If the segment is entirely outside the clip window, reject it.
  - If the segment intersects the clip window boundaries, subdivide it and repeat the process.
- An example of curve clipping is shown below:

![Curve clipping example](https://media.geeksforgeeks.org/wp-content/uploads/20190702111135/clip.png)

: https://www.javatpoint.com/computer-graphics-text-clipping
: https://www.javatpoint.com/computer-graphics-clipping
: https://en.wikipedia.org/wiki/Clipping_(computer_graphics)
: https://www.geeksforgeeks.org/computer-graphics-curve-in-computer-graphics/
: https://www.geeksforgeeks.org/polygon-clipping-sutherland-hodgman-algorithm/