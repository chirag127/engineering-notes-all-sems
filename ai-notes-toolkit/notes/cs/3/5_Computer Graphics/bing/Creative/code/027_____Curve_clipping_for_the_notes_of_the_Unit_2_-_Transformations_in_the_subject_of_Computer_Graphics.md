# Curve clipping

- Curve clipping is a method to selectively enable or disable rendering operations within a defined region of interest, called a clip window.
- Curve clipping involves complex procedures as compared to line clipping or polygon clipping, because curves are not linear and may have multiple intersections with the clip window .
- Curve clipping requires more processing than for objects with linear boundaries, and may result in new curves or segments after clipping.
- There are different algorithms for curve clipping, depending on the type of curve and the shape of the clip window. Some examples are:
  - Cohen-Sutherland algorithm for line clipping
  - Sutherland-Hodgman algorithm for polygon clipping
  - Liang-Barsky algorithm for parametric line clipping
  - Cyrus-Beck algorithm for convex polygon clipping
  - Midpoint subdivision algorithm for Bezier curve clipping
  - Nicholl-Lee-Nicholl algorithm for circular arc clipping
- The general steps for curve clipping are:
  - Divide the curve into small segments or sub-curves
  - Test each segment or sub-curve against the clip window
  - Discard the segments or sub-curves that are completely outside the clip window
  - Clip the segments or sub-curves that are partially inside and partially outside the clip window
  - Join the remaining segments or sub-curves that are completely inside the clip window
- The following figure shows an example of curve clipping, where a Bezier curve is clipped against a rectangular clip window:

![Curve clipping example](https://media.geeksforgeeks.org/wp-content/uploads/20190712122302/Bezier-Curve-Clipping.png)