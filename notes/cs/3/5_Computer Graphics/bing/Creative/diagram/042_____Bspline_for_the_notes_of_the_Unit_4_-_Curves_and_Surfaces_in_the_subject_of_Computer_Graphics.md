### Bspline

A Bspline is a type of curve that is defined by a set of control points and a degree. A Bspline curve is a piecewise polynomial function that has the following properties :

- It is smooth and continuous, meaning that there are no sharp corners or breaks in the curve.
- It is invariant under affine transformations, meaning that scaling, rotating, or translating the control points will not change the shape of the curve.
- It has local control, meaning that moving one control point will only affect a small portion of the curve near that point.
- It has minimal support, meaning that the curve is contained within the convex hull of the control points.
- It has a variable degree, meaning that the curve can be more or less smooth depending on the chosen degree.

The Bspline curve is defined by a linear combination of basis functions, which are also called Bsplines. The basis functions are determined by the degree of the curve and a knot vector, which is a sequence of non-decreasing numbers that specify the domain of each polynomial segment. The basis functions have the following properties :

- They are non-negative, meaning that they are always greater than or equal to zero.
- They are normalized, meaning that they sum up to one at any point in the domain.
- They are linearly independent, meaning that they cannot be expressed as a linear combination of each other.
- They have compact support, meaning that they are zero outside a certain interval.

The Bspline curve can be evaluated at any point in the domain by using the de Boor algorithm, which is a recursive procedure that computes the weighted average of the control points using the basis functions. The Bspline curve can also be modified by changing the control points, the degree, or the knot vector. Some common operations on Bspline curves are :

- Inserting a knot, which increases the number of control points and the degree of smoothness of the curve.
- Removing a knot, which decreases the number of control points and the degree of smoothness of the curve.
- Refining the knot vector, which increases the number of knots and the resolution of the curve.
- Degree elevation, which increases the degree of the curve and the smoothness of the curve.
- Degree reduction, which decreases the degree of the curve and the smoothness of the curve.

Bspline curves are widely used in computer graphics and computer-aided design, as they offer a flexible and efficient way of representing and manipulating complex shapes and surfaces. Bspline curves can also be generalized to higher dimensions, such as Bspline surfaces and Bspline volumes, which are defined by a grid of control points and two or three knot vectors, respectively.