### Bezier curves and surfaces

- Bezier curves and surfaces are a type of mathematical spline used in computer graphics, computer-aided design, and finite element modeling .
- They are defined by a set of control points that influence the shape of the curve or surface, but do not necessarily pass through them .
- They have the properties of continuity, smoothness, and local control, which make them highly useful and convenient for curve and surface design.
- Bezier curves and surfaces are named after Pierre Bezier, a French engineer who patented and popularized them in the 1960s and 1970s.

#### Bezier curves

- A Bezier curve is a parametric curve that can be of any degree n, where n is the number of control points minus one.
- The curve is defined by the following formula, where B(t) is the point on the curve at parameter t, P_i are the control points, and b_i,n(t) are the Bernstein polynomials:

  B(t) = sum_{i=0}^n b_i,n(t) P_i, 0 <= t <= 1

- The Bernstein polynomials are given by the following formula, where C(n,i) is the binomial coefficient:

  b_i,n(t) = C(n,i) t^i (1-t)^(n-i), 0 <= i <= n

- The degree of the curve determines its shape and flexibility. The most common types of Bezier curves are:

  - Linear: A straight line between two control points (n=1).
  - Quadratic: A parabolic curve with three control points (n=2).
  - Cubic: A smooth curve with four control points (n=3).

- The curve always starts at the first control point and ends at the last control point. The curve is tangent to the line joining the first two and the last two control points.
- The curve is contained within the convex hull of the control points, which is the smallest polygon that encloses all the control points.
- The curve can be subdivided into smaller Bezier curves at any parameter value t, using a technique called de Casteljau's algorithm.

#### Bezier surfaces

- A Bezier surface is a parametric surface that can be of any degree m and n in the u and v directions, where m and n are the number of control points in each direction minus one.
- The surface is defined by the following formula, where S(u,v) is the point on the surface at parameters u and v, P_i,j are the control points, and b_i,m(u) and b_j,n(v) are the Bernstein polynomials:

  S(u,v) = sum_{i=0}^m sum_{j=0}^n b_i,m(u) b_j,n(v) P_i,j, 0 <= u,v <= 1

- The degree of the surface determines its shape and flexibility. The most common type of Bezier surface is:

  - Bicubic: A smooth surface with 16 control points (m=n=3).

- The surface always passes through the four corner control points. The surface is tangent to the lines joining the adjacent control points along the edges.
- The surface is contained within the convex hull of the control points, which is the smallest polyhedron that encloses all the control points.
- The surface can be subdivided into smaller Bezier surfaces at any parameter values u and v, using a technique similar to de Casteljau's algorithm.

#### Examples

- The following image shows a cubic Bezier curve with four control points. The curve is drawn in blue, the control points are marked with red dots, and the control polygon is drawn in dashed black. The curve is tangent to the control polygon at the endpoints, and is contained within the convex hull of the control points.

  ![Cubic Bezier curve](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/B%C3%A9zier_3_big.gif/220px-B%C3%A9zier_3_big.gif)

- The following image shows a bicubic Bezier surface with 16 control points. The surface is drawn in gray, the control points are marked with red dots, and the control net is drawn in dashed black. The surface passes through the corner control points