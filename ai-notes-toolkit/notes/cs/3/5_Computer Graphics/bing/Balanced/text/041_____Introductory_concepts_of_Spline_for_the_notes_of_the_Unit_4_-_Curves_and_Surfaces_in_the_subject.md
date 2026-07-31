### Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A spline is a smooth curve that passes through a series of given points.
- Splines are useful for modeling arbitrary functions and are used extensively in computer graphics.
- Splines can be classified into different types based on their degree, continuity, and basis functions.
- Some common types of splines are:
  - Linear splines: Splines of degree one that connect the given points with straight line segments.
  - Quadratic splines: Splines of degree two that have continuous first derivatives at the given points.
  - Cubic splines: Splines of degree three that have continuous first and second derivatives at the given points.
  - Bezier curves: Splines that are defined by a set of control points that influence the shape of the curve, but do not necessarily lie on the curve.
  - B-splines: Splines that are defined by a set of control points and a knot vector that determines the degree and continuity of the curve.
  - NURBS: Non-uniform rational B-splines that are a generalization of B-splines that can represent conic sections and other rational curves.
- Splines have many properties and applications in computer graphics, such as:
  - Affine invariance: Splines are invariant under affine transformations, such as rotation, translation, scaling, and shearing.
  - Local control: Splines can be modified locally by changing only a few control points or knots, without affecting the rest of the curve.
  - Interpolation or approximation: Splines can either pass through the given points (interpolation) or lie close to them (approximation), depending on the choice of control points and knots.
  - Smoothness and continuity: Splines can have different levels of smoothness and continuity at the given points, which affect the appearance and behavior of the curve.
  - Subdivision and refinement: Splines can be subdivided or refined into smaller segments or higher degrees, without changing the shape of the curve.