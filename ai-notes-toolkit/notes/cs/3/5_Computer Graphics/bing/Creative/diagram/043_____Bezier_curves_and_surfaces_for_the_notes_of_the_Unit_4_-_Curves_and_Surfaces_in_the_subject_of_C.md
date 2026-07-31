# Bezier curves and surfaces

## Introduction

- Bezier curves and surfaces are a type of mathematical spline used in computer graphics, computer-aided design, and finite element modeling.
- They are defined by a set of control points that influence the shape of the curve or surface, but do not necessarily pass through them.
- They have properties that make them highly useful and convenient for curve and surface design, such as:
  - Affine invariance: the shape of the curve or surface does not change under affine transformations (such as translation, rotation, scaling, and shearing).
  - Convex hull property: the curve or surface lies entirely within the convex hull of its control points, which provides a simple way of bounding and clipping the curve or surface.
  - Variation diminishing property: the curve or surface does not oscillate more than its control polygon, which means it does not have unnecessary wiggles or loops.
  - Local control: moving a control point only affects a local region of the curve or surface, which allows for easy editing and manipulation.
  - Smoothness: the curve or surface has continuous derivatives up to a certain order, depending on the degree of the curve or surface.

## Bezier curves

- A Bezier curve is a parametric curve of the form:

  $$\mathbf{B}(t) = \sum_{i=0}^n \binom{n}{i} (1-t)^{n-i} t^i \mathbf{P}_i, \quad 0 \leq t \leq 1$$

  where $\mathbf{P}_0, \mathbf{P}_1, \ldots, \mathbf{P}_n$ are the control points, and $\binom{n}{i}$ are the binomial coefficients.
- The degree of the Bezier curve is equal to the number of control points minus one, i.e. $n$.
- The curve starts at $\mathbf{P}_0$ and ends at $\mathbf{P}_n$, and is tangent to the first and last segments of the control polygon.
- The curve can be evaluated efficiently using the de Casteljau algorithm, which recursively subdivides the control polygon into smaller polygons until a single point is obtained.
- The curve can also be represented using a matrix form, such as the Bernstein basis or the power basis.
- The curve can be subdivided into two smaller curves of the same degree at any parameter value $t$, using the de Casteljau algorithm.
- The curve can be converted into a different basis, such as the B-spline basis, using a change of basis matrix.

## Bezier surfaces

- A Bezier surface is a parametric surface of the form:

  $$\mathbf{S}(u,v) = \sum_{i=0}^m \sum_{j=0}^n \binom{m}{i} \binom{n}{j} (1-u)^{m-i} u^i (1-v)^{n-j} v^j \mathbf{P}_{ij}, \quad 0 \leq u,v \leq 1$$

  where $\mathbf{P}_{ij}$ are the control points, arranged in a rectangular grid of size $(m+1) \times (n+1)$, and $\binom{m}{i}$ and $\binom{n}{j}$ are the binomial coefficients.
- The degree of the Bezier surface is equal to the number of control points in each direction minus one, i.e. $m$ and $n$.
- The surface passes through the four corner control points, and is tangent to the boundary control polygons.
- The surface can be evaluated efficiently using a tensor product extension of the de Casteljau algorithm, which recursively subdivides the control grid into smaller grids until a single point is obtained.
- The surface can also be represented using a matrix form, such as the tensor product Bernstein basis or the tensor product power basis.
- The surface can be subdivided into four smaller surfaces of the same degree at any parameter values $u$ and $v$, using the tensor product extension of the de Casteljau algorithm.
- The surface can be converted into a different basis,