### Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A spline is a smooth curve that passes through a series of given points.
- Splines are useful for modeling arbitrary functions and are used extensively in computer graphics.
- Splines can be classified into different types based on their degree, basis functions, and continuity conditions.
- Some common types of splines are:
  - Linear splines: Splines of degree one that connect the given points with straight line segments.
  - Quadratic splines: Splines of degree two that consist of parabolic segments joined at the given points.
  - Cubic splines: Splines of degree three that have smooth transitions between the given points.
  - Bezier curves: Splines that are defined by a set of control points that influence the shape of the curve. They can have any degree, but are usually cubic.
  - B-splines: Splines that are defined by a set of control points and a knot vector that determines the domain and continuity of the curve. They can have any degree, but are usually cubic.
  - NURBS: Non-uniform rational B-splines that are a generalization of B-splines that allow for rational weights on the control points. They can represent conic sections and other curves that are not possible with B-splines.
- Splines can be transformed by affine transformations, such as rotation, translation, scaling, and shearing, without changing their shape.
- Splines can be used to create complex curves and surfaces by combining multiple splines or by using higher-dimensional splines.