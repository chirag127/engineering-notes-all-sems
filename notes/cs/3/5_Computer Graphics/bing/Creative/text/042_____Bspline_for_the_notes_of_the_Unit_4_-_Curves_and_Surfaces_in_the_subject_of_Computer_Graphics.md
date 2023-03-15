### Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A B-spline or basis spline is a piecewise polynomial function with specific properties that determine the polynomial degree/order .
- The idea behind using a B-spline curve is to determine a unique polynomial representation of a set of data, whether that data be structural points in 3D space or a set of data on a graph.
- A B-spline function is a combination of flexible bands that is controlled by a number of points that are called control points, creating smooth curves .
- These functions are used to create and manage complex shapes and surfaces using a number of points.
- A B-spline curve can be defined as follows:

  - Let P0, P1, ..., Pn be a set of control points in a d-dimensional space, where d is usually 2 or 3.
  - Let t0, t1, ..., tm be a non-decreasing sequence of real numbers, called the knot vector, where m = n + k + 1 and k is the degree of the B-spline curve.
  - The B-spline curve of degree k with control points P0, P1, ..., Pn and knot vector t0, t1, ..., tm is given by:

    - C(t) = sum_{i=0}^n N_{i,k}(t) P_i, for t_k <= t <= t_{m-k}

  - where N_{i,k}(t) are the B-spline basis functions of degree k, defined recursively as follows:

    - N_{i,0}(t) = 1, if t_i <= t < t_{i+1}, and 0 otherwise
    - N_{i,k}(t) = (t - t_i) / (t_{i+k} - t_i) N_{i,k-1}(t) + (t_{i+k+1} - t) / (t_{i+k+1} - t_{i+1}) N_{i+1,k-1}(t), for k > 0

- Some properties of B-spline curves are:

  - They are invariant under affine transformations, such as translation, rotation, scaling, and shearing.
  - They have local control, meaning that changing one control point only affects the curve in a local neighborhood.
  - They have variation diminishing, meaning that the curve does not oscillate more than the control polygon.
  - They have convex hull property, meaning that the curve lies within the convex hull of the control points.
  - They have smoothness, meaning that the curve is continuous and has continuous derivatives up to degree k - 1.