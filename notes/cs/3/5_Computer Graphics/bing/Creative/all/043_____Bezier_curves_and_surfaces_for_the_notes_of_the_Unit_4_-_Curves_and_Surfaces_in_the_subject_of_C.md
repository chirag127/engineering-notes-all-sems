# Bezier curves and surfaces

- Bezier curves and surfaces are a way of representing smooth curves and surfaces using polynomial functions and a set of control points .
- Bezier curves and surfaces are widely used in computer graphics, computer-aided design, animation, and font design.
- Bezier curves and surfaces have some desirable properties, such as:
  - They are invariant under affine transformations, such as translation, rotation, scaling, and shearing .
  - They can be easily subdivided into smaller curves or surfaces that are also Bezier .
  - They can be evaluated efficiently using recursive algorithms, such as de Casteljau's algorithm and Bernstein polynomials .
  - They can be intuitively manipulated by adjusting the positions of the control points .

## Bezier curves

- A Bezier curve of degree n is defined by n+1 control points P0, P1, ..., Pn.
- The curve passes through the first and last control points, P0 and Pn, but not necessarily through the others.
- The curve is a weighted sum of the control points, where the weights are given by the Bernstein polynomials of degree n.
- The curve can be written as:

  B(t) = sum_{i=0}^n B_i^n(t) P_i, 0 <= t <= 1

  where B_i^n(t) = C(n,i) t^i (1-t)^(n-i) are the Bernstein polynomials, and C(n,i) = n! / (i! (n-i)!) are the binomial coefficients.

- The curve can also be computed recursively using de Casteljau's algorithm, which splits the curve into two subcurves at any parameter value t.
- The algorithm can be described as:

  B(t) = P0, if n = 0
  B(t) = (1-t) B0(t) + t B1(t), if n = 1
  B(t) = (1-t) B(t)_{0..n-1} + t B(t)_{1..n}, if n > 1

  where B(t)_{i..j} is the Bezier curve defined by the control points P_i, P_i+1, ..., P_j.

- The curve can be subdivided into two smaller curves at any parameter value t by applying de Casteljau's algorithm and taking the first and last points of each iteration as the new control points.
- The curve can be approximated by a polygonal chain by sampling the curve at regular intervals of t and connecting the points with straight lines.

## Bezier surfaces

- A Bezier surface of degree (m,n) is defined by (m+1)(n+1) control points P_{i,j}, where 0 <= i <= m and 0 <= j <= n.
- The surface is a weighted sum of the control points, where the weights are given by the tensor product of the Bernstein polynomials of degree m and n.
- The surface can be written as:

  S(u,v) = sum_{i=0}^m sum_{j=0}^n B_i^m(u) B_j^n(v) P_{i,j}, 0 <= u,v <= 1

  where B_i^m(u) and B_j^n(v) are the Bernstein polynomials of degree m and n, respectively.

- The surface can also be computed recursively using a generalization of de Casteljau's algorithm, which splits the surface into four subsurfaces at any parameter values (u,v).
- The algorithm can be described as:

  S(u,v) = P_{0,0}, if m = n = 0
  S(u,v) = (1-u) S0(u,v) + u S1(u,v), if m = 1 and n = 0
  S(u,v) = (1-v) S0(u,v) + v S1(u,v), if m = 0 and n = 1
  S(u,v) = (1-u) (1-v) S(u,v)_{0..m-1,0..n-1}