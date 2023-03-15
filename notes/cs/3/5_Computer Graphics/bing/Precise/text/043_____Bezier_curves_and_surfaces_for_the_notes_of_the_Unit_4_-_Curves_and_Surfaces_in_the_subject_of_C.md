### Bezier Curves and Surfaces

Bezier curves and surfaces are mathematical representations used in computer graphics to model smooth curves and surfaces. They are named after Pierre Bezier, who used them in the design of automobile bodies.

#### Bezier Curves

A Bezier curve is defined by a set of control points and a set of basis functions. The curve is a weighted sum of the control points, where the weights are given by the basis functions. The most commonly used basis functions are the Bernstein polynomials.

The degree of a Bezier curve is determined by the number of control points. A curve with n+1 control points is of degree n. The curve passes through the first and last control points and is tangent to the line connecting the first two and the last two control points.

Bezier curves have several useful properties, including:

- They are invariant under affine transformations.
- The curve lies entirely within the convex hull of its control points.
- The curve can be subdivided into two Bezier curves of the same degree.

#### Bezier Surfaces

A Bezier surface is defined in a similar way to a Bezier curve, but with two sets of control points and two sets of basis functions. The surface is a weighted sum of the control points, where the weights are given by the product of the basis functions in the two parameter directions.

Bezier surfaces have many of the same properties as Bezier curves, including invariance under affine transformations and the ability to subdivide the surface into smaller Bezier surfaces.

Bezier surfaces are commonly used in computer graphics to model smooth, curved surfaces. They are often used in conjunction with other techniques, such as subdivision surfaces and NURBS, to create complex models.