# Bezier curves and surfaces

- Bezier curves and surfaces are a type of mathematical spline used in computer graphics, computer-aided design, and finite element modeling.
- They are defined by a set of control points that influence the shape of the curve or surface, but do not necessarily pass through them.
- They have the properties of continuity, smoothness, and local control, which make them highly useful and convenient for curve and surface design.
- Bezier curves and surfaces are named after Pierre Bezier, a French engineer who patented and popularized them in the 1960s and 1970s.

## Bezier curves

- A Bezier curve of degree n is defined by n+1 control points P0, P1, ..., Pn.
- The curve starts at P0 and ends at Pn, and the intermediate control points influence the shape of the curve.
- The curve can be expressed as a linear combination of Bernstein polynomials, which are a special type of basis functions that have the properties of non-negativity, partition of unity, and symmetry.
- The curve can also be constructed using the de Casteljau algorithm, which is a recursive method that subdivides the control polygon into smaller ones and computes the point on the curve corresponding to a given parameter value.
- The degree of the curve determines the smoothness and flexibility of the curve. A higher degree curve can approximate more complex shapes, but also requires more control points and computations.
- Some common types of Bezier curves are:

  - Linear Bezier curve: A straight line between two control points P0 and P1. It has degree 1 and can be expressed as B(t) = (1-t)P0 + tP1, where t is the parameter value between 0 and 1.
  - Quadratic Bezier curve: A parabolic curve defined by three control points P0, P1, and P2. It has degree 2 and can be expressed as B(t) = (1-t)^2 P0 + 2(1-t)tP1 + t^2 P2.
  - Cubic Bezier curve: A cubic curve defined by four control points P0, P1, P2, and P3. It has degree 3 and can be expressed as B(t) = (1-t)^3 P0 + 3(1-t)^2 tP1 + 3(1-t)t^2 P2 + t^3 P3.

## Bezier surfaces

- A Bezier surface of degree (m, n) is defined by (m+1)(n+1) control points arranged in a rectangular grid.
- The surface can be expressed as a tensor product of two Bezier curves, one in the u direction and one in the v direction, where u and v are the parameter values between 0 and 1.
- The surface can also be constructed using the de Casteljau algorithm, which is applied twice, once for each parameter direction.
- The degree of the surface determines the smoothness and flexibility of the surface. A higher degree surface can approximate more complex shapes, but also requires more control points and computations.
- A common type of Bezier surface is:

  - Bicubic Bezier surface: A surface of degree (3, 3) defined by 16 control points in a 4x4 grid. It can be expressed as S(u, v) = sum_{i=0}^3 sum_{j=0}^3 B_i^3 (u) B_j^3 (v) P_ij, where B_i^3 and B_j^3 are the Bernstein polynomials of degree 3 for u and v, respectively, and P_ij are the control points.

## References

: Bézier surface - Wikipedia
: Pierre Bézier - Wikipedia
: Computer Graphics Curve in Computer Graphics - GeeksforGeeks
: Bezier Curves and Splines - MIT OpenCourseWare