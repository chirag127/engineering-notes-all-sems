# Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A spline is a smooth curve that passes through a series of given points.
- Splines are useful for modeling arbitrary functions and are used extensively in computer graphics.
- Splines can be classified into different types based on their degree, basis functions, and continuity conditions.
- Some common types of splines are:
  - Linear splines: Splines of degree one that connect the given points with straight line segments.
  - Quadratic splines: Splines of degree two that consist of parabolic segments joined at the given points.
  - Cubic splines: Splines of degree three that consist of cubic polynomial segments joined at the given points.
  - Bezier curves: Splines that are defined by a set of control points that influence the shape of the curve, but do not necessarily lie on the curve.
  - B-splines: Splines that are defined by a set of control points and a knot vector that determines the degree and continuity of the curve.
  - NURBS: Non-uniform rational B-splines that are a generalization of B-splines that allow for rational (non-polynomial) curves and surfaces.
- Splines have several properties that make them suitable for computer graphics, such as:
  - Affine invariance: Splines are invariant under affine transformations, such as rotation, translation, scaling, and shearing.
  - Local control: Splines are controlled by local parameters, such as control points and knots, that affect only a small portion of the curve or surface.
  - Smoothness: Splines can have different levels of smoothness, such as continuity of position, tangent, curvature, etc., depending on the choice of basis functions and knots.
  - Interpolation or approximation: Splines can either interpolate (pass through) or approximate (fit) the given points, depending on the design criteria.