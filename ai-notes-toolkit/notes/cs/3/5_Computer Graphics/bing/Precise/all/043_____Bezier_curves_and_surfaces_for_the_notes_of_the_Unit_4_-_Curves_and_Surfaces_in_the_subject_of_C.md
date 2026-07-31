# Bezier Curves and Surfaces

Bezier curves and surfaces are mathematical representations used in computer graphics to model smooth curves and surfaces. They are named after Pierre Bezier, who used them in the design of automobile bodies.

## Bezier Curves

A Bezier curve is defined by a set of control points and a set of basis functions. The curve is a weighted sum of the control points, where the weights are given by the basis functions. The most commonly used basis functions are the Bernstein polynomials.

The degree of a Bezier curve is determined by the number of control points. A curve with n+1 control points has degree n. The curve starts at the first control point and ends at the last control point. The other control points determine the shape of the curve.

Bezier curves have several useful properties. They are invariant under affine transformations, which means that the shape of the curve does not change when it is translated, rotated, or scaled. They also have the convex hull property, which means that the curve lies entirely within the convex hull of its control points.

## Bezier Surfaces

A Bezier surface is defined in a similar way to a Bezier curve, but with two sets of control points and two sets of basis functions. The surface is a weighted sum of the control points, where the weights are given by the product of the basis functions in the two parameter directions.

Bezier surfaces have many of the same properties as Bezier curves. They are invariant under affine transformations and have the convex hull property. They can also be split into smaller Bezier surfaces, which is useful for rendering and collision detection.

Bezier curves and surfaces are widely used in computer graphics and other fields. They provide a flexible and intuitive way to model smooth shapes, and their mathematical properties make them well-suited for computer-based manipulation and rendering. They are an important tool in the study of curves and surfaces in computer graphics.