 Here is the content in markdown format for the topic ### Introductory concepts of Spline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics:

## Splines

- Splines are flexible curves used in Computer Graphics to create smooth curves and surfaces.
- They are constructed as a combination of polynomial segments.
- Each segment is defined locally by a polynomial function and is connected together into a single continuous curve by shared constraints or control points.
- The curve passes through or near the given control points.
- The shape of the spline can be controlled by changing the positions of the control points.
- The change in the shape of the spline is smooth as the control points are moved.
- The degree of the spline determines the smoothness of the curve. Higher the degree, smoother is the curve.
- Commonly used splines are:
    - Bezier splines (Quadratic and Cubic) - defined by Bernstein polynomials
    - B-splines - defined using basis functions and control points
    - NURBS (Non-uniform rational B-splines) - more flexible and powerful splines that can represent conic sections and cylinders.

Advantages:
- Smooth curves and surfaces can be created.
- Flexible and versatile. Various shapes can be created by changing control points.
- C1 or higher continuity can be achieved.
- Efficient algorithms exist to evaluate, render and manipulate splines.

Disadvantages:
- Can be computationally expensive for high degree splines or those with many control points.
- May introduce unwanted oscillations or wiggles if not designed properly.

Applications:
- Creating curves and surfaces for CAGD (Computer Aided Geometric Design).
- Animation and modelling.
- Curve and surface editing.
- Vehicle design.
- Architectural design.
- Robotics, etc.