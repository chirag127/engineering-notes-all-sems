# Curve clipping

- Curve clipping is a method to selectively enable or disable rendering operations within a defined region of interest.
- Curve clipping involves complex procedures as compared to line clipping or polygon clipping .
- Curve clipping requires more processing than for objects with linear boundaries.
- The region of interest, also called the clip window, can be curved or rectangular in shape.
- There are different algorithms for curve clipping, such as the Bezier clipping algorithm, the B-spline clipping algorithm, and the rational Bezier clipping algorithm.
- The Bezier clipping algorithm is based on the convex hull property of Bezier curves, which states that the curve lies entirely within the convex hull of its control points.
- The B-spline clipping algorithm is based on the convex hull property of B-spline curves, which states that the curve lies entirely within the convex hull of its control polygon.
- The rational Bezier clipping algorithm is based on the perspective projection of rational Bezier curves, which preserves the convex hull property.
- The general steps of curve clipping algorithms are:
  - Divide the curve into segments using the control points or the control polygon.
  - Test each segment against the clip window boundaries.
  - If the segment is entirely inside the clip window, accept it.
  - If the segment is entirely outside the clip window, reject it.
  - If the segment intersects the clip window boundaries, subdivide it and repeat the process.