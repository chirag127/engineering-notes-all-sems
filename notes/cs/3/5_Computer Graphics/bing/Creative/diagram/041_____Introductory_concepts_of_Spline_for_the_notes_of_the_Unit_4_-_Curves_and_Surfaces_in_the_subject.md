### Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A spline is a smooth curve that passes through a series of given points.
- Splines are useful for modeling arbitrary functions and are used extensively in computer graphics.
- Splines can be classified into different types based on their degree, continuity, and basis functions.
- Some common types of splines are:
  - Linear splines: splines of degree one that connect the given points with straight line segments.
  - Quadratic splines: splines of degree two that have continuous first derivatives at the given points.
  - Cubic splines: splines of degree three that have continuous first and second derivatives at the given points.
  - Bezier curves: splines that are defined by a set of control points that influence the shape of the curve, but do not necessarily lie on the curve .
  - B-splines: splines that are defined by a set of control points and a knot vector that determines the degree and continuity of the curve .
  - NURBS (Non-uniform rational B-splines): splines that are defined by a set of control points, a knot vector, and a weight vector that allows for rational and non-uniform curves.
- Splines can be transformed by affine transformations (such as rotation, translation, scaling, etc.) without changing their shape.
- Splines can be used to represent curves and surfaces in computer graphics by using parametric equations .