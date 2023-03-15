# Bspline for the notes of the Unit 4 - Curves and Surfaces in the subject of Computer Graphics

- A B-spline or basis spline is a piecewise polynomial function with specific properties that determine the polynomial degree/order .
- The idea behind using a B-spline curve is to determine a unique polynomial representation of a set of data, whether that data be structural points in 3D space or a set of data on a graph.
- A B-spline function is a combination of flexible bands that is controlled by a number of points that are called control points, creating smooth curves .
- These functions are used to create and manage complex shapes and surfaces using a number of points.
- A B-spline curve is defined by the following parameters:
  - A set of control points P0, P1, ..., Pn that define the shape of the curve.
  - A degree p that determines the order of the polynomial segments.
  - A knot vector U = {u0, u1, ..., um} that determines the domain and continuity of the curve.
- A B-spline curve can be expressed as a linear combination of B-spline basis functions of degree p as follows:

  ![B-spline curve equation](https://latex.codecogs.com/png.latex?C%28u%29%20%3D%20%5Csum_%7Bi%3D0%7D%5E%7Bn%7D%20N_%7Bi%2Cp%7D%28u%29P_i%2C%20%5Cquad%20u_0%20%5Cleq%20u%20%5Cleq%20u_m)

  where N<sub>i,p</sub>(u) are the B-spline basis functions of degree p defined recursively by the Cox-de Boor formula:

  ![B-spline basis functions](https://latex.codecogs.com/png.latex?N_%7Bi%2C0%7D%28u%29%20%3D%20%5Cbegin%7Bcases%7D%201%2C%20%26%20%5Ctext%7Bif%20%7D%20u_i%20%5Cleq%20u%20%3C%20u_%7Bi&plus;1%7D%20%5C%5C%200%2C%20%26%20%5Ctext%7Botherwise%7D%20%5Cend%7Bcases%7D%20%5Cquad%20N_%7Bi%2Cp%7D%28u%29%20%3D%20%5Cfrac%7Bu-u_i%7D%7Bu_%7Bi&plus;p%7D-u_i%7DN_%7Bi%2Cp-1%7D%28u%29&plus;%5Cfrac%7Bu_%7Bi&plus;p&plus;1%7D-u%7D%7Bu_%7Bi&plus;p&plus;1%7D-u_%7Bi&plus;1%7D%7DN_%7Bi&plus;1%2Cp-1%7D%28u%29)

- Some properties of B-spline curves are :
  - They are invariant under affine transformations, such as translation, rotation, scaling, and shearing.
  - They have local control, meaning that changing one control point only affects the curve in a local region.
  - They have variation diminishing property, meaning that the curve does not oscillate more than the control polygon.
  - They have convex hull property, meaning that the curve lies within the convex hull of the control points.
  - They have C<sup>p-k</sup> continuity at the k-th multiple knot, where k is the multiplicity of the knot and p is the degree of the curve.
  - They can approximate any smooth curve arbitrarily well by increasing the number of control points and adjusting their positions.