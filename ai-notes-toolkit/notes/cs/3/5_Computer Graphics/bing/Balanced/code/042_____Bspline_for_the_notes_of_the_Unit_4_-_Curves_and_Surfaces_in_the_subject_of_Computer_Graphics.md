### Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A B-spline is a type of spline function that is defined by a set of control points and a degree.
- A spline function is a piecewise polynomial function that is smooth and continuous.
- B-splines have some advantages over other types of splines, such as Bezier curves, such as:
  - They have local control, meaning that changing a control point affects only a small part of the curve.
  - They have a variable degree, meaning that they can represent curves of different smoothness and complexity.
  - They have a compact support, meaning that each basis function is nonzero only in a finite interval.
  - They have a partition of unity, meaning that the sum of the basis functions is always one.
- B-splines are widely used in computer graphics, computer-aided design, and shape optimization, because they can create and manipulate complex shapes and surfaces with a few parameters.
- B-splines are constructed as linear combinations of B-spline basis functions, which are defined recursively using the Cox-de Boor formula .
- B-spline basis functions depend on a knot vector, which is a sequence of non-decreasing parameter values that determine the shape and continuity of the curve.
- B-splines can be evaluated efficiently using the de Boor algorithm , which is a generalization of the de Casteljau algorithm for Bezier curves.
- B-splines can be rendered using OpenGL/GLU by approximating them with piecewise linear curves, using a small step size for the parameter.
- B-splines can be modified by changing the control points, the degree, the knot vector, or the weights (in the case of rational B-splines).
- B-splines can be converted to other types of splines, such as Bezier curves, NURBS, or Catmull-Rom splines, using appropriate transformations .