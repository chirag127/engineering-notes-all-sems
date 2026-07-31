# Curve clipping

- Curve clipping is a method to selectively enable or disable rendering operations within a defined region of interest.
- Curve clipping involves complex procedures as compared to line clipping or polygon clipping .
- Curve clipping requires more processing than for objects with linear boundaries.
- The region of interest, also called the clip window, can be curved or rectangular in shape.
- There are different algorithms for curve clipping, such as the Bezier clipping algorithm, the B-spline clipping algorithm, and the convex hull clipping algorithm.
- The Bezier clipping algorithm uses the convex hull property of Bezier curves to clip them against a rectangular window.
- The B-spline clipping algorithm uses the convex hull property of B-splines to clip them against a rectangular window.
- The convex hull clipping algorithm uses the convex hull of a set of points to clip them against a convex polygonal window .
- Curve clipping can be used for various applications, such as text clipping, font rendering, vector graphics, and computer-aided design  .