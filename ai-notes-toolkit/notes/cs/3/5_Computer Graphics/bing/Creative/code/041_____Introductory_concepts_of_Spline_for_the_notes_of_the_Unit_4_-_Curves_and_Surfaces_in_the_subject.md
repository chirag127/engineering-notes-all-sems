# Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A spline is a smooth curve that passes through a series of given points .
- Splines are useful for modeling arbitrary functions and are used extensively in computer graphics .
- Splines can be classified into different types based on their degree, continuity, and basis functions.
- Some common types of splines are:
  - Linear splines: splines of degree one that connect the given points with straight line segments.
  - Quadratic splines: splines of degree two that consist of parabolic segments that join at the given points.
  - Cubic splines: splines of degree three that have smooth transitions at the given points and can approximate any smooth curve.
  - Bezier curves: splines that are defined by a set of control points that influence the shape of the curve .
  - B-splines: splines that are defined by a set of basis functions that have local support and can be modified by changing the knot vector .
  - NURBS: non-uniform rational B-splines that are generalizations of B-splines that can represent conic sections and rational curves .
- Splines have many properties and applications in computer graphics, such as:
  - Affine invariance: splines are invariant under affine transformations, such as rotation, translation, scaling, and shearing.
  - Interpolation: splines can pass through the given points exactly or approximate them with some error.
  - Approximation: splines can approximate any smooth curve or surface with arbitrary precision by increasing the number of control points or knots.
  - Subdivision: splines can be subdivided into smaller splines without changing the shape of the curve or surface.
  - Rendering: splines can be rendered efficiently by using algorithms such as de Casteljau's algorithm, de Boor's algorithm, or Cox-de Boor's algorithm.