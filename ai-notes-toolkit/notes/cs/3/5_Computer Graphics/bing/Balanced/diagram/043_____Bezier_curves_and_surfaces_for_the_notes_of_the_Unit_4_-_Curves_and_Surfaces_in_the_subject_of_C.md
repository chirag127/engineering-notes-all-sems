# Bezier curves and surfaces

## Introduction

- Bezier curves and surfaces are a type of mathematical spline used in computer graphics, computer-aided design, and finite element modeling.
- They are defined by a set of control points that influence the shape of the curve or surface, but do not necessarily pass through them.
- They have properties that make them highly useful and convenient for curve and surface design, such as smoothness, continuity, and local control.

## Bezier curves

- A Bezier curve is a parametric curve that can be expressed as a linear combination of Bernstein polynomials.
- The degree of the curve is equal to the number of control points minus one.
- The curve starts at the first control point and ends at the last control point, and is tangent to the first and last segments of the control polygon.
- The curve is contained within the convex hull of the control points, which means it does not have any loops or self-intersections.
- The curve can be subdivided at any parameter value into two smaller Bezier curves of the same degree.

## Bezier surfaces

- A Bezier surface is a parametric surface that can be expressed as a tensor product of Bernstein polynomials in two variables.
- The degree of the surface is equal to the number of control points in each direction minus one.
- The surface is defined by a rectangular grid of control points, also called a control net.
- The surface passes through the four corner control points, and is tangent to the boundary curves of the control net.
- The surface is contained within the convex hull of the control points, which means it does not have any holes or self-intersections.
- The surface can be subdivided at any parameter value in either direction into four smaller Bezier surfaces of the same degree.

## References

: Bézier surface - Wikipedia
: Pierre Bézier - Wikipedia
: Computer Graphics Curve in Computer Graphics - GeeksforGeeks
: Bézier curve - Wikipedia