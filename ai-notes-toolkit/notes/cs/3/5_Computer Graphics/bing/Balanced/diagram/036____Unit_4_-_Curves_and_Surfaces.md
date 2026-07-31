## Unit 4 - Curves and Surfaces

This unit covers the following topics:

- Parametric curves and surfaces
- Bezier curves and surfaces
- B-spline curves and surfaces
- NURBS curves and surfaces
- Subdivision curves and surfaces

### Parametric curves and surfaces

- A parametric curve is a curve that is defined by a function that maps a parameter domain to a set of points in a coordinate space.
- A parametric surface is a surface that is defined by a function that maps a parameter domain to a set of points in a coordinate space.
- The parameter domain is usually a subset of the real numbers or a rectangular region in the plane.
- The coordinate space is usually the Euclidean space of two or three dimensions.
- Examples of parametric curves are circles, ellipses, parabolas, hyperbolas, spirals, etc.
- Examples of parametric surfaces are spheres, cylinders, cones, tori, etc.

### Bezier curves and surfaces

- A Bezier curve is a parametric curve that is defined by a set of control points and a polynomial basis function.
- A Bezier surface is a parametric surface that is defined by a set of control points and a polynomial basis function.
- The control points are the vertices of a polygon or a polyhedron that influence the shape of the curve or surface.
- The polynomial basis function is a linear combination of Bernstein polynomials that determine the weights of the control points.
- The degree of the Bezier curve or surface is equal to the number of control points minus one.
- The Bezier curve or surface passes through the first and last control points, but not necessarily through the others.
- The Bezier curve or surface is invariant under affine transformations, such as translation, rotation, scaling, and shearing.
- The Bezier curve or surface can be subdivided into smaller Bezier curves or surfaces using the de Casteljau algorithm.

### B-spline curves and surfaces

- A B-spline curve is a parametric curve that is defined by a set of control points and a knot vector.
- A B-spline surface is a parametric surface that is defined by a set of control points and two knot vectors.
- The control points are the vertices of a polygon or a polyhedron that influence the shape of the curve or surface.
- The knot vector is a sequence of non-decreasing real numbers that determine the domain and continuity of the curve or surface.
- The degree of the B-spline curve or surface is equal to the number of knots minus the number of control points.
- The B-spline curve or surface does not necessarily pass through any of the control points, except for the endpoints if the knot vector is clamped.
- The B-spline curve or surface is invariant under affine transformations, such as translation, rotation, scaling, and shearing.
- The B-spline curve or surface can be subdivided into smaller B-spline curves or surfaces using the Cox-de Boor algorithm.

### NURBS curves and surfaces

- A NURBS curve is a parametric curve that is defined by a set of control points, a knot vector, and a weight vector.
- A NURBS surface is a parametric surface that is defined by a set of control points, two knot vectors, and a weight matrix.
- The control points, the knot vector, and the weight vector or matrix are the same as in the B-spline case, except that the weights are positive real numbers that affect the shape of the curve or surface.
- The NURBS curve or surface is a generalization of the B-spline curve or surface that allows for rational functions and conic sections, such as circles, ellipses, parabolas, and hyperbolas.
- The NURBS curve or surface is invariant under projective transformations, such as perspective projection and homography.
- The NURBS curve or surface can be subdivided into smaller NURBS curves or surfaces using the same algorithms as in the B-spline case.

### Subdivision curves and surfaces

- A subdivision curve is a parametric curve that is defined by a set of control points and a subdivision scheme.
- A subdivision surface is a parametric surface that is defined by a set of control points and a subdivision scheme.
- The control points are the vertices of a polygon or a polyhedron that influence the shape of the curve or surface.
- The subdivision scheme is a recursive procedure that generates new control points and new curves or surfaces from the old ones.
- The subdivision curve or surface is the limit of the sequence of curves or surfaces obtained by applying the subdivision scheme repeatedly.
- The subdivision curve or surface can have arbitrary topology and can approximate any smooth curve or surface.
-