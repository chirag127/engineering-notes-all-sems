 Here is the content in markdown format for the topic ### Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics:

### Bspline

- Bspline stands for Basis Spline. They are a type of spline curve with the following properties:
- They are piecewise polynomial curves.
- They are constructed using a set of control points.
- The shape of the curve is determined by a set of knots.
- The curve passes through the first and last control points.
- The curve is continuous and exhibits a high degree of smoothness at the joints between polynomial pieces.

*Control Points*: The shape of a Bspline curve is controlled by a set of control points (P0, P1, P2...Pn). The curve passes through the first and last control points. The positions of the intermediate control points determine the shape of the curve.

*Knots*: Knots are parameters that determine the rate of change of the spline curve. A knot vector is a non-decreasing sequence of parameter values used to construct a Bspline basis. The curve is defined over the interval spanned by the first and last knots. The number of knots must be equal to the number of control points plus the degree of the curve plus 1. The degree of the curve is one less than the number of control points that influence a given point on the curve.

*Degree of curve*: The degree of a Bspline curve is one less than the number of control points that influence a given point on the curve. A curve of degree n has n+1 control points that influence a given point on the curve. Higher-degree curves are more flexible than lower-degree curves of the same number of control points.

* Advantages:
- Bspline curves are smooth and exhibit good shape control.
- They can model a wide variety of shapes with relative ease.
- The curve passes through the first and last control points.
- The shape can be edited by changing the positions of the control points.
- They are computationally efficient to evaluate and manipulate.

* Applications:
- Curve and surface modeling in CAD/CAM systems.
- Motion control and robotics.
- Shape editing and free-form deformation.
- Data interpolation and approximation.
- etc.