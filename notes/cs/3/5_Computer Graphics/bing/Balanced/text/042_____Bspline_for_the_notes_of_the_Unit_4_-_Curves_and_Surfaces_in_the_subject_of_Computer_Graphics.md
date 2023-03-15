### Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A B-spline or basis spline is a piecewise polynomial function with specific properties that determine the polynomial degree/order .
- The idea behind using a B-spline curve is to determine a unique polynomial representation of a set of data, whether that data be structural points in 3D space or a set of data on a graph.
- A B-spline function is a combination of flexible bands that is controlled by a number of points that are called control points, creating smooth curves .
- These functions are used to create and manage complex shapes and surfaces using a number of points.
- A B-spline curve is defined by the following parameters:
  - A set of control points P0, P1, ..., Pn that define the shape of the curve.
  - A degree p that determines the order of the polynomial segments.
  - A knot vector U = {u0, u1, ..., um} that determines the domain and continuity of the curve.
- A B-spline curve has the following properties :
  - It is a linear combination of B-spline basis functions of degree p, which are defined recursively using the Cox-de Boor formula.
  - It is invariant under affine transformations, such as translation, rotation, scaling, and shearing.
  - It has local control, meaning that changing one control point only affects the curve in a local region.
  - It has variation diminishing, meaning that the curve does not oscillate more than the control polygon.
  - It has convex hull property, meaning that the curve lies within the convex hull of the control points.
  - It has minimal support, meaning that each basis function has the smallest possible domain for a given degree and knot vector.
  - It has smoothness, meaning that the curve is continuous and has continuous derivatives up to order p - 1, where p is the degree of the curve. The smoothness can be reduced by repeating knots in the knot vector.
  - It has approximation and interpolation capabilities, meaning that the curve can approximate or interpolate a given set of data points by choosing appropriate control points and knot vector.