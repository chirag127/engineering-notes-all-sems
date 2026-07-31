# Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A B-spline or basis spline is a piecewise polynomial function with specific properties that determine the polynomial degree/order .
- The idea behind using a B-spline curve is to determine a unique polynomial representation of a set of data, whether that data be structural points in 3D space or a set of data on a graph.
- A B-spline function is a combination of flexible bands that is controlled by a number of points that are called control points, creating smooth curves .
- These functions are used to create and manage complex shapes and surfaces using a number of points.
- A B-spline curve can be defined by the following equation:

![B-spline curve equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a)

where *n* is the number of control points, *p* is the degree of the curve, *N* is the basis function, and *P* is the control point.

- The basis function *N* is defined by the following recursive formula:

![B-spline basis function](https://wikimedia.org/api/rest_v1/media/math/render/svg/0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a)

where *t* is the parameter, and *u* is the knot vector.

- The knot vector *u* is a non-decreasing sequence of real numbers that determines the domain and the shape of the curve.
- The degree *p* of the curve determines the smoothness and the number of segments of the curve.
- The control points *P* determine the position and the direction of the curve.

- Some properties of B-spline curves are:

  - They are invariant under affine transformations, such as translation, rotation, scaling, and shearing.
  - They have local control, meaning that changing one control point affects only a local part of the curve.
  - They have variation diminishing, meaning that the curve does not oscillate more than the control polygon.
  - They have convex hull property, meaning that the curve lies within the convex hull of the control points.
  - They have minimal support, meaning that each basis function has the smallest possible support for a given degree and smoothness.