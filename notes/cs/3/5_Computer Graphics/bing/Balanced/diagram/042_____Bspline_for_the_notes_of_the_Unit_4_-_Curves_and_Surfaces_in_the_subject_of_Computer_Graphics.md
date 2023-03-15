### Bspline

- A Bspline is a **piecewise polynomial function** that can represent a smooth curve or surface .
- A Bspline is defined by a set of **control points** and a **knot vector** .
- A Bspline has the following properties  :
  - **Local control**: The shape of the Bspline is influenced by only a few control points near a given point.
  - **Affine invariance**: The Bspline is invariant under affine transformations, such as translation, rotation, scaling, and shearing.
  - **Variation diminishing**: The Bspline does not oscillate more than the control polygon.
  - **Convex hull**: The Bspline lies within the convex hull of its control points.
  - **Smoothness**: The Bspline has continuous derivatives up to a certain order, depending on its degree.
  - **Interpolation**: The Bspline can interpolate the first and last control points, if the knot vector is chosen appropriately.
- A Bspline can be evaluated using the **de Boor algorithm**, which is a recursive scheme that computes the value of the Bspline at a given parameter value.
- A Bspline can be modified by changing the control points, the knot vector, or the degree .
- A Bspline can be converted to a **Bezier curve** or a **NURBS (Non-Uniform Rational B-Spline)** by applying suitable transformations .